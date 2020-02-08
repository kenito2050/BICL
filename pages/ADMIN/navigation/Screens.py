class Screens(dict):

    def return_screens(screen):

        # Data Dictionary of screens
        screens={
            'Users': 'ManageUser.aspx',
            'Role_Templates': 'UserEntitlements.aspx'
            }
        return screens[screen]