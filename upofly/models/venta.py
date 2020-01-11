# -*- coding: utf-8 -*-

from odoo import models, fields, api

class venta(models.Model):
    _name = 'upofly.venta'
    _rec_name = 'total'
    
    factura_id = fields.Many2one("upofly.factura", "Factura")
    cliente_id = fields.Many2one("upofly.cliente", "Cliente")
    lineas_de_venta_ids = fields.One2many("upofly.linea_de_venta", "venta_id", string="Líneas de Venta")
    total = fields.Float("Total sin IVA", compute="_calcular_precio")
    total_aux = fields.Float("Preco total", compute="_calcular_precio_aux", store=True)

    
    
    #@api.multi
    #@api.depends('lineas_de_venta_ids', 'lineas_de_venta_ids.subtotal')
    def _calcular_precio(self):
        tot = 0
        for record in self:
            if record.lineas_de_venta_ids:
                record.total = sum(ldv.subtotal for ldv in record.lineas_de_venta_ids)

    
     #@api.depends('total')
    def _calcular_precio_aux(self):
        for record in self:
            record.total2 = record.total
    
    