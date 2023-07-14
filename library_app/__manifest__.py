# -*- coding: utf-8 -*-
{
    'name': "Library Management",
    'summary': """Manage library catalog and book lending.""",
    'description': """Manage library catalog and book lending.""",
    'author': "Cris-aian Vergara",
    'license': "LGPL-3",
    'website': "http://www.crisaianvergara.com",
    'category': 'Services/Library',
    'version': '15.0.1.0.0',
    'depends': ['base'],
    'data': [
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/library_menu.xml",
        "views/book_list_template.xml",
        "reports/library_book_report.xml",
    ],
    "demo": [
        "data/res.partner.csv",
        "data/library.book.csv",
        "data/book_demo.xml"
    ],
    'sequence': -99,
    "application": True,
}
