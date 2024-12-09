from odoo import  models,api,fields



class Bedroom (models.Model):

    _name = 'bedroom'


    number = fields.Char(required=True)

    description = fields.Text()
    property_id = fields.Many2one('properity')
    # departmet= fields
    # item_ids= fields