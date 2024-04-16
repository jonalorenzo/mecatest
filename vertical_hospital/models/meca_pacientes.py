from odoo import models, fields, api, _
from odoo.exceptions import UserError

class MecaPacientes(models.Model):
    _name = "meca.pacientes"
    _description = "Pacientes"

    name = fields.Char('Nombre y apellido', required=True, tracking=True)
    sequence = fields.Char(string='Secuencia', readonly=True, required=True, copy=False, default=lambda self: _('New'))
    dni = fields.Char('DNI', required=True)
    treatment_ids = fields.Many2many('meca.tratamientos', string='Tratamientos')
    admission_date = fields.Datetime('Fecha de alta', default=fields.Datetime.now)
    update_date = fields.Datetime('Hora de actualización', readonly=True)
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('active', 'Alta'),
        ('inactive', 'Baja')
    ], default='draft', tracking=True)
    
    