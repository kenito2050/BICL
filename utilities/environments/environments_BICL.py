class Environments_BICL(dict):

    def return_environments(environment):

        # Data Dictionary of Environments
        environments={
            'DEV': 'https://betabidev.wedbush.com/',
            'UAT': 'https://uatbrokerinsight.wedbush.com/',
            'PROD': 'https://prodbrokerinsight.wedbush.com/',
            'PROD-LIVE': 'https://brokerinsight.wedbush.com/',
            'PROD-LB': 'https://biload.wedbush.com/'
            }
        return environments[environment]