from sqlalchemy import create_engine
from sqlalchemy.types import Integer, Text

from schedule.config import SQLAlchemyConfig
from schedule.main.utils.db_utils import assemble_sqlalchemy_url


def create_employee_table(df):
    '''
    Creates the employees table in the database.
    '''
    col_en = SQLAlchemyConfig.EMPLOYEES_COLUMNS_EN  # English column names
    col_fr = SQLAlchemyConfig.EMPLOYEES_COLUMNS_FR  # French column names
    engine = create_engine(assemble_sqlalchemy_url(SQLAlchemyConfig))
    # Create employees table (english)
    df[col_en].to_sql(
        "employees_en",
        engine,
        if_exists="replace",
        index=False,
        chunksize=1000,
        dtype={
            col_en[0]: Integer,  # employee ID
            col_en[1]: Text,  # last name
            col_en[2]: Text,  # first name
            col_en[3]: Text,  # job title
            col_en[4]: Text,  # phone number
            col_en[5]: Text,  # email
            col_en[6]: Text,  # address
            col_en[7]: Text,  # province
            col_en[8]: Text,  # city
            col_en[9]: Text,  # postal code
            col_en[5]: Integer,  # organization id
            col_en[5]: Integer,  # department id
        })
    # Create employees table (french)
    df[col_fr].to_sql(
        "employees_fr",
        engine,
        if_exists="replace",
        index=False,
        chunksize=1000,
        dtype={
            col_fr[0]: Integer,  # employee ID
            col_fr[1]: Text,  # last name
            col_fr[2]: Text,  # first name
            col_fr[3]: Text,  # job title
            col_fr[4]: Text,  # phone number
            col_fr[5]: Text,  # email
            col_fr[6]: Text,  # address
            col_fr[7]: Text,  # province
            col_fr[8]: Text,  # city
            col_fr[9]: Text,  # postal code
            col_fr[5]: Integer,  # organization id
            col_fr[5]: Integer,  # department id
        })


