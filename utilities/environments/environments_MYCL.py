class Environments_MYCL(dict):

    def return_environments(environment):

        # Data Dictionary of Environments
        environments={
            'DEV': 'https://fiscldev.wedbush.com/',
            'UAT': 'https://uat.myclientlink.com',
            'PROD': 'https://prod.myclientlink.com/',
            'PROD-LIVE': 'https://myclientlink.com/'
            }
        return environments[environment]