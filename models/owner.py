from odoo import models ,api,fields
from datetime import datetime


class Owner(models.Model):

    _name = 'owner'


    name = fields.Char(required=True)
    title= fields.Selection([
        ('mr','Mr'),
        ('miss','Miss'),

    ])
    dob = fields.Date()
    age = fields.Integer(compute = '_compute_age', store=1)
    address = fields.Text()
    phone = fields.Char()
    property_ids = fields.One2many(comodel_name='properity',inverse_name='owner_id')

    active = fields.Boolean(default=True)
    @api.depends('dob')
    def _compute_age(self):

        for record in self:
            if record.dob:
                today = datetime.today()
                dob = fields.Date.from_string(record.dob)
                record.age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            else:
                record.age = 0  # If DOB is not set, age will be 0


