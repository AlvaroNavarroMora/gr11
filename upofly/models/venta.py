# -*- coding: utf-8 -*-

from odoo import models, fields, api

class venta(models.Model):
    _name = 'upofly.venta'
    _rec_name = 'total'
    
    #total = fields.Float("Total")
    factura_id = fields.Many2one("upofly.factura", "Factura")
    cliente_id = fields.Many2one("upofly.cliente", "Cliente")
    lineas_de_venta_ids = fields.One2many("upofly.linea_de_venta", "venta_id", string="Líneas de Venta")
    
    total = fields.Float("Total sin IVA", compute="_calcular_precio")

    #@api.multi
    #@api.depends('lineas_de_venta_ids', 'lineas_de_venta_ids.subtotal')
    def _calcular_precio(self):
        
        '''tot = 0
        for record in self:
            for ldv in record.lineas_de_venta_ids:
                
                tot += sum(ven.subtotal for ven in ldv)
            
            record.update({'total' : tot})'''

        
        tot = 0
        for record in self:
            if record.lineas_de_venta_ids:
                for ldv in record.lineas_de_venta_ids:
                    
                    for ven in ldv:
                        if ven:
                            tot = tot + ven.subtotal
                #record.total = tot
                record.update({'total' : tot})