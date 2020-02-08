class Screens(dict):

    def return_screens(screen):

        # Data Dictionary of screens
        screens={
            'dashboard': '/mainDash/dashboard',
            'account_positions': '/account/positions',
            'account_activity': '/account/activities',
            'account_cashflow': '/account/cashFlow',
            'gains_loss_unrealized_summary': '/incomeTaxes/taxlNet',
            'gains_loss_unrealized_detail': '/incomeTaxes/performance/taxlOpen',
            'gains_loss_realized': '/incomeTaxes/closed',
            'gains_loss_projected_income': '/incomeTaxes/projectedIncome',
            'gains_loss_pending_income': '/incomeTaxes/pendingIncome',
            'documents_monthly_statements': '/documents/statements',
            'documents_confirms': '/documents/confirms',
            'documents_tax_statements': '/documents/taxStatements',
            'documents_shareholder_materials': '/documents/shareHolderMaterials',
            'tools_wedbush_research': '/tools/wedbushResearch',
            'tools_quotes_charts': '/tools/quotesCharts',
            'tools_calculators': '/tools/calculators',
            'tools_help': '/tools/help',
            'profiles_preferences_user_preferences': '/profilePreferences/userPreferences',
            'profiles_preferences_account_preferences': '/profilePreferences/accountPreferences',
            'logout': 'user/login?logout=1'
            }
        return screens[screen]