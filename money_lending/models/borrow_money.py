from datetime import date
from dateutil.relativedelta import relativedelta
from odoo import api, fields, models


DEFAULT_INTEREST_RATE = 5


class BorrowMoney(models.Model):
    _name = "borrow.money"
    _description = "Borrow money"
    _rec_name = "borrower_id"

    # Constraints
    _sql_constraints = [
        (
            "borrow_money_check_amount",
            "CHECK(amount >= 1000)",
            "Amount must be greater than or equal to 1000 pesos."
        ),
        (
            "borrow_money_check_borrowed_date",
            "CHECK(borrowed_date <= current_date)",
            "Borrowed date must not be in the future."
        ),
        (
            "borrow_money_check_payment_date",
            "CHECK(payment_date >= current_date)",
            "Payment date must not be in the past."
        )
    ]

    # Relational Fields
    borrower_id = fields.Many2one(
        comodel_name="borrower",
        string="Name",
        required=True
    )
    user_id = fields.Many2one(
        "res.users", string="Lender",
        default=lambda self: self.env.user,
        readonly=True,
    )

    # Date Fields
    borrowed_date = fields.Date(
        string="Borrowed Date",
        required=True,
        default=fields.Date.context_today,
    )
    payment_date = fields.Date(
        string="Payment Date",
        required=True
    )

    amount = fields.Float(string="Amount", required=True)
    interest_rate = fields.Float(
        string="Interest Rate (%)",
        required=True,
    )
    interest_value = fields.Float(
        string="Interest Value",
        compute="_compute_interest_value",
        readonly=True
    )
    transfer_method = fields.Selection(
        [
            ("cash", "Cash"),
            ("cebuana", "Cebuana"),
            ("gcash", "Gcash"),
            ("bank", "Bank"),
        ],
        string="Transfer Method",
        required=True,
    )
    monthly_interest = fields.Float(string="Monthly Interest", readonly=True)


    @api.depends('amount', 'interest_rate')
    def _compute_interest_value(self):
        for rec in self:
            if rec.amount:
                rec.interest_value = rec.amount * (rec.interest_rate / 100)
                rec.monthly_interest = rec.interest_value
            else:
                rec.interest_value = 0

    
    @api.onchange("payment_date")
    def onchange_interest_rate_by_date(self):
        date_today = date.today()
        payment_date_in_a_month = date_today + relativedelta(months=1)
        number_of_days_in_month = (payment_date_in_a_month - date_today).days
        if self.payment_date:
            days_to_pay = (self.payment_date - date_today).days
            if days_to_pay > number_of_days_in_month:
                self.interest_rate = DEFAULT_INTEREST_RATE
            else:
                self.interest_rate = 0