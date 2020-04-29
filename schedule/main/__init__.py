from schedule.main.prepare_data import prepare_data
from schedule.main.prepare_org_chart import prepare_org_chart

from schedule.main.employee.employee_table import create_employee_table
from schedule.main.department.department_table import create_department_table
from schedule.main.organization.organization_table import create_organization_table

def main():
    '''
    The main function to be run in the scheduled job. Everything required in
    the workflow should be called from here.
    '''
    # Fetch GEDS data and write to csv 
    df = prepare_data()
    # # Create the employees table
    create_employee_table(df)
    # # Load the org chart
    # org_chart = prepare_org_chart(df)
    # # Create departments table
    # create_department_table(df, org_chart)
    # # Create organizations table
    # create_organization_table(df, org_chart)

if __name__ == "__main__":
    main()