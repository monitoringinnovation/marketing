from odoo import fields, models


class leadsClients(models.Model):
    _name = 'motion.leads'
    _description = 'Landing data'

    name = fields.Char(string='Nombre')
    email = fields.Char(string='Email')
    phone_number = fields.Char(string='Numero de telefono')
    city = fields.Char(string='Ciudad')
    message = fields.Text(string='Mensaje')
    origin = fields.Char(string='Donde nos encontro')
    curr_time = fields.Datetime(string="Fecha del mensaje", default=fields.Datetime.now())
    _order = 'curr_time desc'
