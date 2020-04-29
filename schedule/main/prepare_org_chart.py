from schedule.main.department.flat_to_hierarchical import get_org_chart

def prepare_org_chart(df, tree_depth=7):
    '''
    Creates hierarchical data of the organizational structure using the csv.
    Args:
        df: a pandas dataframe
        tree_depth: an int specifying how deep the org chart tree should go.
    Returns:
        org_chart: a python dict-like object containing the org chart.
    '''
    org_table = df[["org_name"]].drop_duplicates()
    org_struc = df["org_structure"].drop_duplicates()
    org_struc = org_struc.str.split(":", n=-1, expand=True)
    columns = [i for i in range(0, min(tree_depth + 1, len(org_struc.columns)), 1)]
    org_struc = org_struc[columns]
    return get_org_chart(org_struc)