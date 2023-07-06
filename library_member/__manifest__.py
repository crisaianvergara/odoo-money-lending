# -*- coding: utf-8 -*-
{
    'name': "Library Members",
    'license': "LGPL-3",
    'description': """Manage members borrowing books.""",
    'author': "Cris-aian Vergara",
    'depends': ['library_app', "mail"],
    'data': [
        "security/ir.model.access.csv",
        "security/library_security.xml",
        "views/book_view.xml",
        "views/member_view.xml",
        "views/library_menu.xml",
        "views/book_list_template.xml",
    ],
    "application": False,
}
