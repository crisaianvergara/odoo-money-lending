from odoo import api, fields, models


class Occupation(models.Model):
    _name = "occupation"
    _description = "Borrower occupation"

    name = fields.Char(string="Title", size=250, required=True)
