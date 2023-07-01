from datetime import date, timedelta
from odoo import api, fields, models


class Borrower(models.Model):
    _name = "borrower"
    _description = "Borrower"

    name = fields.Char(string="Borrower Name", required=True, size=250)
    address = fields.Char(string="Address", required=True, size=250)
    birth_date = fields.Date(string="Birth Date", required=True)
    age = fields.Integer(string="Age", readonly=True, compute="_compute_age",)
    gender = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
        ],
        string="Gender",
        required=True,
    )
    occupation_ids = fields.Many2many(comodel_name="occupation", string="Occupation", required=True)
    cellphone_number = fields.Char(string="Cellphone Number", required=True, size=13)

    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            if rec.birth_date:
                rec.age = (date.today() - rec.birth_date) // timedelta(days=365.2425)
            else:
                rec.age = 0














