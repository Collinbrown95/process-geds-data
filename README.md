# pandas-sqlalchemy-integration
> A repository to showcase how Python's pandas library can be used to interact with a SQL database via SQLAlchemy. The primary use case for this type of integration is when a "data science" workflow needs to integrate with a software development workflow. This repository in particular is organized around a scheduled job that involves fetching, preprocessing, and writing data to a SQL database.

## Folder Organization

### data
For illustrative purposes, a small csv with fake data is included to simulate what raw data on employees of an organization might look like.

### schedule

#### config

#### main
All code that will run as part of the scheduled job goes in here.

There is a ```main``` function which, in this example, is run as a scheduled job using Python's ```apscheduler``` library.

```main``` should call all functions that are required to perform the workflow. Beyond this, there is no restriction on how modules should be structured inside of the main folder.
__Dev call graph__
<!-- ![call graph](https://g.gravizo.com/svg?digraph%20G%20%7B%0A%20%20main%20-%3E%20prepare_data%20%5Blabel%3D%221%22%5D%3B%0A%20%20prepare_data%20-%3E%20%7Bload_as_dataframe%3B%20preprocess_columns%3B%20create_table_keys%7D%3B%0A%20%20prepare_data%20-%3E%20main%20%5Bcolor%3D%22red%22%20label%3D%22df%22%5D%3B%0A%20%20main%20-%3E%20create_employees_table%20%5Blabel%3D%222%22%5D%3B%0A%20%20main%20-%3E%20prepare_org_chart%20%5Blabel%3D%223%22%5D%3B%0A%20%20prepare_org_chart%20-%3E%20main%20%5Bcolor%3D%22red%22%20label%3D%22org%20chart%22%5D%3B%0A%20%20prepare_org_chart%20-%3E%20get_org_chart%3B%0A%20%20get_org_chart%20-%3E%20flat_to_hierarchical%3B%0A%20%20flat_to_hierarchical%20-%3E%20%7Bbuild_leaf%3B%20ctree%7D%3B%0A%20%20main%20-%3E%20create_department_table%20%5Blabel%3D%224%22%5D%3B%0A%20%20create_department_table%20-%3E%20%7Bget_department_org_chart%7D%3B%0A%20%20main%20-%3E%20create_organization_table%20%5Blabel%3D%225%22%5D%3B%0A%20%20create_organization_table%20-%3E%20generate_org_paths%3B%0A%7D) -->
<!-- <!-- This is the original graph -->
<img src='https://g.gravizo.com/svg?
digraph G {
  main -> prepare_data [label="1"];
  prepare_data -> "csv on disk?" [color="blue"];
  "csv on disk?" -> load_df_from_csv [label="yes"];
  "csv on disk?" -> fetch_geds [label="no"];
  "csv on disk?" -> prepare_data [color="red" label="df"];
  prepare_data -> {preprocess_columns; create_table_keys};
  prepare_data -> main [color="red" label="df"];
  main -> create_employees_table [label="2"];
  main -> prepare_org_chart [label="3"];
  prepare_org_chart -> main [color="red" label="org chart"];
  prepare_org_chart -> get_org_chart;
  get_org_chart -> flat_to_hierarchical;
  flat_to_hierarchical -> {build_leaf; ctree};
  main -> create_department_table [label="4"];
  create_department_table -> {get_department_org_chart};
  main -> create_organization_table [label="5"];
  create_organization_table -> generate_org_paths;
}'/>


<!-- Github's flavour of markdown doesn't support url encoding. A temporary workaround to this is given below.
In a python terminal (tested with python 3.8), do
raw='''digraph G {
  main -> prepare_data [label="1"];
  prepare_data -> {load_as_dataframe; preprocess_columns; create_table_keys};
  prepare_data -> main [color="red" label="df"];
  main -> create_contacts_table [label="2"];
  main -> create_organizations_table [label="3"];
  main -> create_departments_table [label="4"];
}'''
import urllib.parse
urllib.parse.quote(raw)
Then copy + paste the encoded url into the image tag
-->

__Production call graph__
![call graph](https://g.gravizo.com/svg?digraph%20G%20%7B%0A%20%20main%20-%3E%20prepare_data%20%5Blabel%3D%221%22%5D%3B%0A%20%20prepare_data%20-%3E%20%7Bload_as_dataframe%3B%20preprocess_columns%3B%20create_table_keys%7D%3B%0A%20%20prepare_data%20-%3E%20main%20%5Bcolor%3D%22red%22%20label%3D%22df%22%5D%3B%0A%20%20main%20-%3E%20create_employees_table%20%5Blabel%3D%222%22%5D%3B%0A%20%20main%20-%3E%20prepare_org_chart%20%5Blabel%3D%223%22%5D%3B%0A%20%20prepare_org_chart%20-%3E%20main%20%5Bcolor%3D%22red%22%20label%3D%22org%20chart%22%5D%3B%0A%20%20prepare_org_chart%20-%3E%20get_org_chart%3B%0A%20%20get_org_chart%20-%3E%20flat_to_hierarchical%3B%0A%20%20flat_to_hierarchical%20-%3E%20%7Bbuild_leaf%3B%20ctree%7D%3B%0A%20%20main%20-%3E%20create_department_table%20%5Blabel%3D%224%22%5D%3B%0A%20%20create_department_table%20-%3E%20%7Bget_department_org_chart%7D%3B%0A%20%20main%20-%3E%20create_organization_table%20%5Blabel%3D%225%22%5D%3B%0A%20%20create_organization_table%20-%3E%20generate_org_paths%3B%0A%7D)
<!-- This is the original graph
<img src='https://g.gravizo.com/svg?
digraph G {
  main -> prepare_data [label="1"];
  prepare_data -> {load_as_dataframe; preprocess_columns; create_table_keys};
  prepare_data -> main [color="red" label="df"];
  main -> create_employees_table [label="2"];
  main -> prepare_org_chart [label="3"];
  prepare_org_chart -> main [color="red" label="org chart"];
  prepare_org_chart -> get_org_chart;
  get_org_chart -> flat_to_hierarchical;
  flat_to_hierarchical -> {build_leaf; ctree};
  main -> create_department_table [label="4"];
  create_department_table -> {get_department_org_chart};
  main -> create_organization_table [label="5"];
  create_organization_table -> generate_org_paths;
}
'/>
-->

#### test

#### playground


## Resources
1. [SQLalchemy guide ch 1](https://www.oreilly.com/library/view/essential-sqlalchemy-2nd/9781491916544/ch01.html)
2. [sqlalchemy schema](https://overiq.com/sqlalchemy-101/defining-schema-in-sqlalchemy-orm/)
3. [pandas with sqlalchemy](https://hackersandslackers.com/connecting-pandas-to-a-sql-database-with-sqlalchemy/)