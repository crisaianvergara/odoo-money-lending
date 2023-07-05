from datetime import date, timedelta
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient"

    name = fields.Char(string="Name", tracking=True)
    date_of_birth = fields.Date(string="Date of Birth")
    ref = fields.Char(string="Reference")
    age = fields.Integer(string="Age", compute="_compute_age", tracking=True)
    gender = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
        ],
        string="Gender",
        tracking=True
    )
    active = fields.Boolean(string="Active", default=True)


    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            if rec.date_of_birth:
                rec.age = (date.today() - rec.date_of_birth) // timedelta(days=365.2425)
            else:
                rec.age = 0
            