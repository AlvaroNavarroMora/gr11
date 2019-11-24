# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Cliente(models.Model):
    _name = 'upofly.cliente'
    _inherits = {'res.partner' : 'partner_id'}
    partner_id = fields.Many2one ('res.partner', ondelete='cascade')
    identificacion = fields.Char('DNI/CIF', size=9, required=True)