# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Pliente(models.Model):
    _name = 'upofly.piloto'
    _inherits = {'res.partner' : 'partner_id'}
    #partner_id = fields.Many2one('res.partner', ondelete='cascade')
    name = fields.Char('Nombre', required=True)
    dni = fields.Char('DNI', size=9, required=True)
    num_licencia = fields.Char('Licencia Nº', required=True)