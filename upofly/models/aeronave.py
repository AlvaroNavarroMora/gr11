# -*- coding: utf-8 -*-

from odoo import models, fields, api


class aeronaveclass(models.Model):
    _name = 'upofly.aeronave'
    
    modelo = fields.Char('Nombre modelo', size=64, required=True)
    capacidad = fields.Integer("Capacidad", required=True)
    suplemento = fields.Float("Suplemento")
    matricula = fields.Char("Matricula aeronave", size=6, required=True)