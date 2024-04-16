from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class MecaTratamientos(models.Model):
    _name = "meca.tratamientos"
    _description = "Tratamientos"

    name = fields.Char('Nombre', required=True)
    code = fields.Char('Código', required=True)
    doctor_id = fields.Char('Médico tratante', required=True)

    @api.constrains('code')
    def _check_code(self):
        for record in self:
            if '026' in record.code:
                raise ValidationError(_("El código no debe contener la secuencia '026'."))
