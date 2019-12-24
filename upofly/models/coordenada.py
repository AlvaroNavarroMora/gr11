# -*- coding: utf-8 -*-

from odoo import models, fields, api


class coordenada(models.Model):
    _name = 'upofly.coordenada'
    _rec_name = 'coordenada'
    
    coordenada = fields.Integer('Coordenada', required=True)
    ruta_ids = fields.Many2many("upofly.ruta", string="Rutas")