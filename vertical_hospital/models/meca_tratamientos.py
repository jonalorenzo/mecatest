from odoo import models, fields, api, _
from odoo.exceptions import UserError

class MecaTratamientos(models.Model):
    _name = "meca.tratamientos"
    _description = "Tratamientos"

    name = fields.Char('Nombre', required=True)
    code = fields.Char('Código', required=True)
    doctor_id = fields.Char('Médito tratante', required=True)
