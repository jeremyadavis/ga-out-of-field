import yaml
from constants import (
    MIGRATION_DIR,
    TABLE_NAME
)

from helpers import (
    get_data_file,
)

from utils import (
    execute_sql,
    pretty_print,
    get_num_files_in_dir,
    create_directory
)


class DataMaker:
    def __init__(self, engine, filename):
        self.engine = engine
        self.df_data = get_data_file(filename)

    def make_tables(self):

        # DATABASE OUTPUT
        self.df_data.to_sql(TABLE_NAME, self.engine,
                            if_exists="replace",
                            method="multi",
                            chunksize=10000)

    def make_migrations(self):

        self.make_migration_file(
            'track_tables', self.make_tracking_migration_yaml)
        # self.make_migration_file(
        #     'access_roles', self.make_role_access_yaml)

    def make_migration_file(self, file_name, markup_method):
        migration_version = get_num_files_in_dir(MIGRATION_DIR) + 1
        migration_file_name = f"{migration_version}__{file_name}.up.yaml"
        pretty_print(f"Making Migration File {migration_file_name}", True)

        yaml_data = []

        # print(self.df_data.columns)

        # for column in self.df_data.columns:
        #     if(row.is_first_column):
        #         columns = [self.primary_key]

        #     if (row.view_column_name != self.primary_key):
        #         columns.append(row.view_column_name)

        #     if(row.is_last_column):
        migration_data = markup_method({
            "table_name": TABLE_NAME,
        })

        # print('type', type(view_migration_data))
        if(migration_data):
            if(isinstance(migration_data, (list,))):
                for item in migration_data:
                    yaml_data.append(item)
            else:
                yaml_data.append(migration_data)

        with open(MIGRATION_DIR + migration_file_name, 'w') as yaml_file:
            noalias_dumper = yaml.dumper.SafeDumper
            noalias_dumper.ignore_aliases = lambda self, data: True
            yaml.dump(yaml_data, yaml_file, default_flow_style=False,
                      Dumper=noalias_dumper)
            yaml_file.close()

    def make_tracking_migration_yaml(self, args):
        return ({
            "args": {
                "name": args['table_name'],
                "schema": 'public'
            },
            "type": "add_existing_table_or_view"
        })

    # def make_relationship_migration_yaml(self, args):
    #     relationships_config = self.config['relationships']
    #     primary_module = relationships_config['primary_module']
    #     primary_to_secondary_map = relationships_config['primary_to_secondary_map']
    #     secondary_to_primary_field = relationships_config['secondary_to_primary_field']

    #     if((not relationships_config)):
    #         return None

    #     data = []
    #     relationships = []
    #     if(args['module'] == primary_module):
    #         for module, name in primary_to_secondary_map.items():
    #             relationships.append({
    #                 "name": name,
    #                 "remote_view_name": module_to_db_object(
    #                     module, self.config, "")
    #             })
    #     else:
    #         relationships.append({
    #             "name": secondary_to_primary_field,
    #             "remote_view_name": module_to_db_object(
    #                 primary_module, self.config, "")
    #         })

    #     for relationship in relationships:
    #         data.append({
    #             "args": {
    #                 "name": relationship['name'],
    #                 "table": {
    #                     "name": args['view_name'],
    #                     "schema": args['schema']
    #                 },
    #                 "using": {
    #                     "manual_configuration": {
    #                         "column_mapping": {
    #                             self.primary_key: self.primary_key
    #                         },
    #                         "remote_table": {
    #                             "name": relationship['remote_view_name'],
    #                             "schema": args['schema']
    #                         }
    #                     }
    #                 },
    #             },
    #             "type": "create_object_relationship"
    #         })

    #     return data

    # def make_role_access_yaml(self, args):

    #     roles_config = self.config['roles']
    #     data = []

    #     # print('cols', args['columns'])
    #     for role, settings in roles_config.items():

    #         filter_config = settings["filter"]
    #         filter = {}

    #         if(filter_config):
    #             condition = {
    #                 filter_config["source_view_column"]: {
    #                     "_eq": filter_config["hasura_variable"]
    #                 }
    #             }
    #             # Curr Module is Source Module
    #             if(filter_config["source_module"] == args['module']):
    #                 filter = condition
    #             else:
    #                 # Curr Model isn't source module, so have to use relationship field to get to filter column
    #                 relationship_field = self.config['relationships']['secondary_to_primary_field']

    #                 filter = {
    #                     relationship_field: condition
    #                 }

    #         data.append({
    #             "args": {
    #                 "permission": {
    #                     "allow_aggregations": True,
    #                     "columns": args['columns'],
    #                     "filter": filter,
    #                     "limit": settings["limit"] if settings["limit"] else None
    #                 },
    #                 "role": role,
    #                 "table": {
    #                     "name": args['view_name'],
    #                     "schema": self.db_schema,
    #                 },
    #             },
    #             "type": "create_select_permission"
    #         })
    #     return data
