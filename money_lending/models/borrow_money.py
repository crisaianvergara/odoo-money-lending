from odoo import api, fields, models


class Borrow(models.Model):
    _name = "borrow.money"
    _description = "Borrow money"
    _rec_name = "borrower_id"

    borrower_id = fields.Many2one(comodel_name="borrower", string="Borrower Name")
    date_borrowed = fields.Date(string="Date Borrowed", required=True, default=fields.Date.context_today)
    amount = fields.Float(string="Amount", required=True)
    interest_rate = fields.Float(string="Interest Rate (%)", default=5.00)
    interest_value = fields.Float(string="Interest Value", compute="_compute_interest_value", readonly=True)


    @api.depends('amount', 'interest_rate')
    def _compute_interest_value(self):
        for rec in self:
            if rec.amount:
                rec.interest_value = rec.amount * (rec.interest_rate / 100)
            else:
                rec.interest_value = 0.00