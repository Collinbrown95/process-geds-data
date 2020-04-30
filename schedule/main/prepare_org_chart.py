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
    # Start by getting a dataframe that contains unique organization structures
    # in both languages
    org_struc_en = df["org_structure_en"].str.replace('\(.*?\)', '').drop_duplicates()
    org_struc_fr = df["org_structure_fr"].str.replace('\(.*?\)', '').drop_duplicates()
    # Split org units into columns and keep a subset of them based on the
    # desired tree depth.
    org_struc_en = org_struc_en.str.split(" :", n=-1, expand=True)
    org_struc_fr = org_struc_fr.str.split(" :", n=-1, expand=True)
    # Column subset is the same in both languages
    columns = [i for i in range(0, min(tree_depth + 1, len(org_struc_en.columns)), 1)]
    org_struc_en = org_struc_en[columns]
    org_struc_fr = org_struc_fr[columns]
    # Get the org charts
    org_chart_en = get_org_chart(org_struc_en)
    org_chart_fr = get_org_chart(org_struc_fr)
    # Remove any instances of None from the list of org charts
    # TODO: check why one of the departments yields None
    org_chart_en = [dept for dept in org_chart_en if dept is not None]
    org_chart_fr = [dept for dept in org_chart_fr if dept is not None]
    return org_chart_en, org_chart_fr