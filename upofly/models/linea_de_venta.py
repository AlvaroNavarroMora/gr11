# -*- coding: utf-8 -*-

from odoo import models, fields, api

class linea_de_venta(models.Model):
    _name = 'upofly.linea_de_venta'
    _rec_name = 'precio'
    
    precio = fields.Float("Precio")
    venta_id = fields.Many2one("upofly.venta", "Venta")
    servicio_ids = fields.Many2one("upofly.servicio", "Servicios")

