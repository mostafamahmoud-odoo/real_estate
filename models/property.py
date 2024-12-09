from datetime import datetime

from odoo import  models,fields,api
from odoo.exceptions import ValidationError


class Properity(models.Model):
    _name = 'properity'
    _inherit = ['mail.thread','mail.activity.mixin']


    name = fields.Char(required=True,tracking=1)
    ref = fields.Char(default='New',readonly=True)
    description = fields.Text()
    postcode = fields.Char(required=True)
    date_availability = fields.Date(tracking=1)
    expected_price = fields.Float()
    selling_price = fields.Float(tracking=1)
    bedrooms = fields.Integer(string="Number of Bedrooms") # u can't use required=1 with fields of type Intger and Float because it's default value is 0 which already value Instead use api decerator
    garage  = fields.Boolean()
    # Each Selection Field is list of tubles / Each Tuble contains 2 values ("the Value that is set in Db","Presented Value")
    garden_orientation = fields.Selection([
        ('north', "North"),
        ('eest', 'West'),
        ('douth', 'South'),
        ('east', 'East')
    ])

    state = fields.Selection([
        ('draft', "Draft"),
        ('pending', 'Pending'),
        ('done', 'Done'),
        ('closed', 'Closed'),

    ],readonly=True)
    owner_id = fields.Many2one('owner')
    _sql_constraints = [
        ('unique_name','unique(name)','Name is exist!')
    ]
    order_id = fields.Many2one('sale.order')
    age = fields.Integer(related='owner_id.age', store=1)
    address = fields.Text(related='owner_id.address',store=1)

    bedrooms_ids = fields.One2many('bedroom',inverse_name='property_id')
    active=fields.Boolean(default=True)
    expected_saling_date = fields.Date(string="Expected Salling Date")
    is_late  = fields.Boolean(default=False)

    #CRUD operations


    @api.constrains('bedrooms')
    def check_bedrooms_greater_zero(self):
        for rec in self:
            if (rec.bedrooms <=0 ):
                raise ValidationError('Please Add Valid Number for Bedrooms')



    def set_state_to_draft(self):
        for rec in self:
            rec.state = 'draft'



    def set_state_to_pending(self):
        for rec in self:
            rec.state = 'pending'


    def set_state_to_done(self):
        for rec in self:
            rec.state = 'done'

    def set_state_to_closed(self):
        for rec in self:
            rec.state = 'closed'

    def check_late_properties(self):
        properties = self.search([])
        for rec in properties:
            if rec.expected_saling_date  and rec.expected_saling_date < fields.date.today() :
                rec.is_late = True

    def open_related_owner(self):
        #to open view from code u need to call action related to thie view
        #1 action to open form
        action= self.env['ir.actions.actions']._for_xml_id('property_module.owner_action')

        #2 view id of this form
        view_id= self.env.ref('property_module.owner_view_form').id
        action['views'] = [[view_id, 'form']]
        action['res_id'] = self.owner_id.id

        return action



    @api.model
    def create(self,vals):
        res  = super(Properity,self).create(vals)
        if res.ref == 'New':
            res.ref = self.env['ir.sequence'].next_by_code("property_seq")

        return res












    # # Create
    # @api._model_create_multi
    # def create(self, vals):
    #     res = super(Properity,self).create(vals)
    #     print("inside create")
    #     return res
    # # read
    # @api.model
    # def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
    #     res = super(Properity, self)._search(domain, offset=0, limit=None, order=None, access_rights_uid=None)
    #     print("inside search")
    #     return res
    #
    #
    # def write(self, vals):
    #     res = super(Properity, self).write(vals)
    #     print("inside Write")
    #     return res
    #
    #
    #
    # def unlink(self):
    #     res = super(Properity,self).unlink()
    #     print ("inside Delete ")
    #     return res