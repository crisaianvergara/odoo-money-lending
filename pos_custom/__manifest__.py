{
    'name': 'POS Order Receipt Customization',
    'version': '1.0.0',
    'category': 'Point of Sale',
    'author': 'Cris-aian Vergara',
    'sequence': -99,
    'summary': 'POS Order Receipt Customization',
    'description': """POS Order Receipt Customization""",
    'depends': ['product'],
    'data': [
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_custom/static/src/js/**/*',
            'pos_custom/static/src/xml/**/*',
        ],
    },
    'demo': [],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}