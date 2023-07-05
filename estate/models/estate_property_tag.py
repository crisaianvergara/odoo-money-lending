from odoo import api, fields, models

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Estate Property Tag'
    _order = 'name'
    _sql_constraints = [
        ('check_unique_name', 'UNIQUE(name)', 'The name must be unique.')
    ]

    name = fields.Char(string="Name", required=True)
    color = fields.Integer(string="Color")
    