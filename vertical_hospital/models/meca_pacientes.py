from odoo import models, fields, api, _
from odoo.exceptions import UserError

class MecaPacientes(models.Model):
    _name = "meca.pacientes"
    _description = "Pacientes"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Nombre y apellido', required=True, tracking=True)
    sequence = fields.Char(string='Secuencia', readonly=True, required=True, copy=False, default=lambda self: _('New'))
    dni = fields.Char('DNI', required=True, tracking=True)
    treatment_ids = fields.Many2many('meca.tratamientos', string='Tratamientos', options="{'no_create': True}")
    admission_date = fields.Datetime('Fecha de alta', default=fields.Datetime.now)
    update_date = fields.Datetime('Hora de actualización', readonly=True)
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('active', 'Alta'),
        ('inactive', 'Baja')
    ], default='draft', tracking=True)

    @api.model
    def create(self, vals):
        if vals.get('sequence', _('New')) == _('New'):
            vals['sequence'] = self.env['ir.sequence'].next_by_code('meca.pacientes') or _('New')
        return super(MecaPacientes, self).create(vals)

    @api.constrains('dni')
    def _check_dni(self):
        for record in self:
            if not record.dni.isdigit():
                raise UserError(_('El DNI solo debe contener números.'))

    def set_active(self):
        self.state = 'active'

    def set_inactive(self):
        self.state = 'inactive'

    def reset_to_draft(self):
        self.state = 'draft'
