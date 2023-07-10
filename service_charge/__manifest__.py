{
    "name": "Service Charge",
    "version": "1.0",
    "depends": ['point_of_sale'],
    "category": "Point of Sale",
    "assets": {
        'point_of_sale.assets': [
            'service_charge/static/src/js/service_charge_button.js',
        ],
        'web.assets_qweb': [
            'service_charge/static/src/xml/service_charge_button.xml',
        ],
    },
    "application": False,
    "license": "LGPL-3",
}