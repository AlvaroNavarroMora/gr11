# -*- coding: utf-8 -*-

from odoo import models, fields, api

class aeronave(models.Model):
    _name = 'upofly.aeronave'
    _rec_name = 'matricula'
    
    modelo = fields.Char('Modelo', size=64, required=True)
    capacidad = fields.Integer("Capacidad", required=True)
    matricula = fields.Char("Matrícula", size=6, required=True)
    parte_mantenimiento_ids = fields.One2many("upofly.parte_mantenimiento", "aeronave_id", string="Partes de Mantenimiento")
