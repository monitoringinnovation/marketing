from odoo import fields, models


class leadsClients(models.Model):
    _name = 'motion.leads'
    _description = 'Landing data'

    name = fields.Char(string='Nombre')
    email = fields.Char(string='Email')
    phone_number = fields.Char(string='Numero de telefono')
    department = fields.Char(string='Departamento')
    message = fields.Text(string='Mensaje')
    curr_time = fields.Datetime(string="Fecha del mensaje", default=fields.Datetime.now())
