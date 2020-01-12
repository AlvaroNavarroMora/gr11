# -*- coding: utf-8 -*-

from odoo import models, fields, api
from openerp.exceptions import ValidationError

class Cliente(models.Model):
    _name = 'upofly.cliente'
    _inherits = {'res.partner' : 'partner_id'}
    partner_id = fields.Many2one ('res.partner', ondelete='cascade')
    identificacion = fields.Char('DNI/CIF', size=9, required=True)
    ventas_ids = fields.One2many("upofly.venta", "cliente_id", string="Compras realizadas")
    
    _sql_constraints = [('cliente_identificacion_unique','UNIQUE (identificacion)','El identificador debe ser único')]
    
    @api.one
    @api.constrains('identificacion')
    def _validaId(self):
        if len(self.identificacion) < 9:
            raise ValidationError('El DNI/NIF debe tener 9 caracteres')