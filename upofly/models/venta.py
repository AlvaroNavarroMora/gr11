# -*- coding: utf-8 -*-

from odoo import models, fields, api

class venta(models.Model):
    _name = 'upofly.venta'
    _rec_name = 'total'
    
    total = fields.Float("Total")
    factura_id = fields.Many2one("upofly.factura", "Factura")
    cliente_id = fields.Many2one("upofly.cliente", "Cliente")
    lineas_de_venta_ids = fields.One2many("upofly.linea_de_venta", "venta_id", string="Líneas de Venta")
    
    #total = fields.Float("Total sin IVA", compute="_calcular_precio")

    
    #@api.depends()
    #def _calcular_precio(self):
        #self.total = sumar los subtotales de las lineass de venta