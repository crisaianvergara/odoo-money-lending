from odoo import http

# This is the correct way
# from odoo.addons.library_app.controllers.main import Books

# This getting me error
# from custom.library_app.controllers.main import Books

# This is one way but not a good practice
from ...library_app.controllers.main import Books


class BooksExtended(Books):
    @http.route()
    def list(self, **kwargs):
        response = super().list(**kwargs)
        if kwargs.get("available"):
            all_books = response.qcontext["books"]
            available_books = all_books.filtered("is_available")
            response.qcontext["books"] = available_books
        return response
