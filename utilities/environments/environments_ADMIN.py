class Environments_ADMIN(dict):

    def return_environments(environment):

        # Data Dictionary of Environments
        environments={
            'DEV': 'https://bicladmindev.wedbush.com',
            'UAT': 'https://bicladminuat.wedbush.com',
            'PROD': 'https://bicladmin.wedbush.com'
            }
        return environments[environment]