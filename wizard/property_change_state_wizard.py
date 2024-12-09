from odoo import models,api,fields


class ChangeState(models.TransientModel):

    _name = 'change.state'

    reason= fields.Text()
    state= fields.Selection([
        ('draft','Draft'),
        ('pending','Pending')
    ])
    property_id = fields.Many2one('properity')



