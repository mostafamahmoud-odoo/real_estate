
{
    'name' : 'Real Estate',
    'version' : '1.2',
    'summary': 'Real Estate Customization odoo',
    'sequence': 10,
    'description': """Real Estate Customization odoo """,
    'category': '',


    'depends' : ['base','sale_management','account','mail'],
    'data': [
        'security/property_manager_group.xml',
        'security/ir.model.access.csv',
        'data/property_sequance.xml',
        'views/base_menu.xml',
        'views/properity_view.xml',
        'views/sale_order_view.xml',
        'views/owner_view.xml',
        'wizard/change_state_view.xml',
        'reports/property_report.xml',
        'reports/Invoice_report.xml',
        'reports/templates.xml',





    ],

    'assets':{
        'web.assets_backend':
            [
                'property_module/static/src/css/properity.css',
                'property_module/static/src/css/custom_font.css',
                'property_module/static/src/css/popover.css'

             ],

'web.report_assets_common':
            [
                'property_module/static/src/css/font.css'

             ]
    },
    'installable': True,
    'application': True,



}
