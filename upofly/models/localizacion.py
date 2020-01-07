# -*- coding: utf-8 -*-

from odoo import models, fields, api


class localizacion(models.Model):
    _name = 'upofly.localizacion'
    _rec_name = 'ubicacion'
    
    ubicacion = fields.Char("Ubicación", required=True)
    latitud = fields.Float('Latitud', required=True)
    longitud = fields.Float('Longitud', required=True)
    ruta_ids = fields.Many2many("upofly.ruta", string="Rutas")