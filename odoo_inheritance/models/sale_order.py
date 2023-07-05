from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Adding new field to existing views - sale.order form
    confirmed_user_id = fields.Many2one("res.users", string="Confirmed User")
    short_note = fields.Char(string="Short Note")

    def action_confirm(self):
        super(SaleOrder, self).action_confirm()
        print("Success...........................")
        # Set Confirmed User to the current user
        self.confirmed_user_id = self.env.user.id