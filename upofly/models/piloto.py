# -*- coding: utf-8 -*-

from odoo import models, fields, api

class piloto(models.Model):
    _name = 'upofly.piloto'
    _rec_name = 'nombre'
    nombre = fields.Char('Nombre', size=60, required=True)
    dni = fields.Char('DNI', size=9, required=True)
    num_licencia = fields.Char('Licencia Nº', size=10, required=True)
    imagen = fields.Binary('Foto')