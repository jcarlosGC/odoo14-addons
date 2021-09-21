# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale_management'

    payment_mode = fields.Selection(
        string="Payment Mode",
        selection=[
            ('cash', "Cash"),
            ('bank', "Bank"),
            ('bitcoin', "Bitcoin"),
        ]
    )
    