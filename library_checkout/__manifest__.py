{
    "name": "Library Checkout",
    "description": """Members can borrow books from the library""",
    "author": "Cris-aian Vergara",
    "depends": ["library_member"],
    "data": [
        "security/ir.model.access.csv",
        "views/library_menu.xml",
        "views/checkout_view.xml",
        "data/library_checkout_stage.xml",
    ],
    "demo": [
        # "data/library_checkout_stage.xml",
    ],
    "license": "LGPL-3",
    "application": False
}