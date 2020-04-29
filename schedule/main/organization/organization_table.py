import json

from sqlalchemy import create_engine
from sqlalchemy.types import Integer, Text

from schedule.config import SQLAlchemyConfig
from schedule.main.utils.db_utils import assemble_sqlalchemy_url
from schedule.main.organization.search import get_path_to_node

def create_organization_table(df, org_chart, tree_depth=7):
    '''
    Creates the organization table in the database.
    '''
    engine = create_engine(assemble_sqlalchemy_url(SQLAlchemyConfig))
    org_df = df[["org_id", "org_name", "dept_id", "org_structure"]].drop_duplicates()
    # Get the paths to each org unit and store them in a table column
    org_df = generate_org_paths(org_df, org_chart)
    # Write org_df to the database
    org_df[["org_id", "org_name", "dept_id", "org_chart_path"]].to_sql(
        "organizations",
        engine,
        if_exists="replace",
        chunksize=1000,
        dtype={
            "org_id": Integer,
            "org_name": Text,
            "dept_id": Integer,
            "org_chart_path": Text,
        }
    )

def generate_org_paths(df, org_chart):
    '''
    Generates the path to each business unit in the org chart.
    '''
    # Serialize the path to the node as a string
    df["org_chart_path"] = df["org_name"].str.lower().apply(
        lambda x: json.dumps(get_path_to_node(x, org_chart)))
    return df