# -*- coding: utf-8 -*-

from odoo import models, fields, api

class venta(models.Model):
    _name = 'upofly.venta'
    _rec_name = 'total'
    
    total = fields.Float("Total")
    factura_id = fields.Many2one("upofly.factura", "Factura")
    cliente_id = fields.Many2one("upofly.cliente", "Cliente")
