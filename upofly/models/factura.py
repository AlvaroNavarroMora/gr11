# -*- coding: utf-8 -*-

from odoo import models, fields, api

class factura(models.Model):
     _name = 'upofly.factura'

     iva = fields.Float("IVA%", required=True)     
     concepto = fields.Char("Concepto", required=True)
     descripcion = fields.Text("Descripción")
     fecha = fields.Date("Fecha", required=True)
     venta_id = fields.Many2one("upofly.venta", "Venta", required=True)
     subtotal = fields.Float("Subtotal", related='venta_id.total')
     importeTotal = fields.Float("Importe total", compute="_importe_total")
     state = fields.Selection([('borrador','Borrador'),
                      ('pendiente', 'Pendiente de cobro'),
                      ('cobrada', 'Cobrada'),],
                      'Estado',
                      default='borrador')
    

     @api.onchange('subtotal', 'iva')
     def _importe_total(self):
         for record in self:
             record.importeTotal = float(record.subtotal) + (float(record.subtotal) * (float(record.iva))/100)
    
     @api.one
     def btn_submit_to_pendiente(self):
         self.write({'state':'pendiente'})
        
     @api.one
     def btn_submit_to_cobrada(self):
         self.write({'state':'cobrada'})