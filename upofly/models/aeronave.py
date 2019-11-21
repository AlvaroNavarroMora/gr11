# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class upofly(models.Model):
#     _name = 'upofly.upofly'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


class aeronaveclass(models.Model):
    _name = 'upofly.aeronave'
    
    modelo = fields.Char()
    capacidad = fields.Integer()
    suplemento = fields.Float()
    matricula = fields.Char()