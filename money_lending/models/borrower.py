import re
from datetime import date, timedelta
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Borrower(models.Model):
    _name = "borrower"
    _description = "Borrower"
    # Delegation Inheritance
    _inherits = {"res.partner": "partner_id"}

    # Modifying fields (Delegation Inheritance)
    partner_id = fields.Many2one(
        "res.partner",
        delegate=True,
        ondelete="cascade",
        required=True,
    )
    email = fields.Char(related="partner_id.email", readonly=False)
    mobile = fields.Char(related="partner_id.mobile", required=True, readonly=False)
    title = fields.Many2one(related="partner_id.title", required=True, readonly=False)

    address = fields.Char(string="Address", required=True, size=250)
    birth_date = fields.Date(string="Birth Date", required=True)
    age = fields.Integer(string="Age", readonly=True, compute="_compute_age", required=True)
    gender = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
        ],
        string="Gender",
        required=True,
    )

    # Other fields
    # Gcash Account
    gcash_account_name = fields.Char(string="Gcash Account Name")
    gcash_account_number = fields.Char(string="Gcash Account Number")

    # Bank Account
    bank_account_name = fields.Char(string="Bank Account Name")
    bank_account_number = fields.Char(string="Bank Account Number")
    bank_branch = fields.Char(string="Bank Branch")

    # Relations
    borrow_money_ids = fields.One2many(
        'borrow.money',
        'borrower_id',
        string="Borrows"
    )
    


    @api.onchange('email')
    def _validate_email(self):
        """Validate email address"""
        try:
            if self.email:
                match = re.match(
                    '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
                    self.email
                )
            if match == None:
                raise ValidationError('Please enter a valid email address!')
        except UnboundLocalError:
            print("UnboundLocalError triggered!")
            


    @api.depends('birth_date')
    def _compute_age(self):
        """Compute age"""
        for rec in self:
            if rec.birth_date:
                rec.age = (date.today() - rec.birth_date) // timedelta(days=365.2425)
            else:
                rec.age = 0














