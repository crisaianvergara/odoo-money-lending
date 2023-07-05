{
    "name": "Real Estate",
    "version": "1.0.0",
    "depends": ["base",],
    "author": "Cris-aian Vergara",
    'sequence': -101,
    "category": "Real Estate/Brokerage",
    "description": """
    Real Estate
    """,
    "data": [
        # "security/security.xml",
        "security/ir.model.access.csv",
        "views/estate_menus.xml",
        "views/estate_property_views.xml",
        "views/estate_property_type_views.xml",
        "views/estate_property_tag_views.xml",
        "views/estate_property_offer_views.xml",
        "views/res_users_views.xml",
    ],
    "demo": [
        "demo/demo_data.xml",
    ],
    "application": True,
    'license': 'LGPL-3'
}