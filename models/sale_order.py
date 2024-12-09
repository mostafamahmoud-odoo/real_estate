from odoo import  models,fields,api



class SaleOrder(models.Model):
    _inherit = ['sale.order']

    properity_ids = fields.One2many(comodel_name='properity',inverse_name='order_id')
