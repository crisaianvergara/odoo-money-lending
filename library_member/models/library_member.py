from  odoo import api, fields, models


class Member(models.Model):
    _name = "library.member"
    _description = "Library Member"
    
    # Delegation Inheritance
    _inherits = {"res.partner": "partner_id"}
    # Inheritance
    _inherit = ["mail.thread", "mail.activity.mixin"]

    card_number = fields.Char()

    # Delegation Inheritance
    partner_id = fields.Many2one(
        "res.partner",
        delegate=True,
        ondelete="cascade",
        required=True
    )