# -*- coding: utf-8 -*-

from odoo import models, fields, api
from openerp.exceptions import ValidationError

class piloto(models.Model):
    _name = 'upofly.piloto'
    _rec_name = 'nombre'
    
    nombre = fields.Char('Nombre', size=60, required=True)
    dni = fields.Char('DNI', size=9, required=True)
    num_licencia = fields.Char('Licencia Nº', size=10, required=True)
    imagen = fields.Binary('Foto')
    vuelo_id = fields.Many2many('upofly.vuelo', string="Vuelos")
    
    _sql_constraints = [('piloto_dni_unique','UNIQUE (dni)','El dni debe ser único')]
    _sql_constraints = [('piloto_num_licencia_unique','UNIQUE (num_licencia)','La licencia debe ser única')]
    
    @api.one
    @api.constrains('dni')
    def _validaDni(self):
        if len(self.dni) < 9:
            raise ValidationError('El DNI debe tener 9 caracteres')