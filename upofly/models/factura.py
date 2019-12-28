# -*- coding: utf-8 -*-

from odoo import models, fields, api

class factura(models.Model):
     _name = 'upofly.factura'
     _rec_name = 'identificador'

     identificador = fields.Integer("ID", required=True)
     iva = fields.Float("IVA%", required=True)     
     concepto = fields.Char("Concepto", required=True)
     descripcion = fields.Text("Descripcion")
     fecha = fields.Date("Fecha")
     venta_id = fields.Many2one("upofly.venta", "Venta")
     subtotal = fields.Float("Subtotal", related='venta_id.total')
     importeTotal = fields.Float("Importe total", compute="_importe_total")
         
     @api.depends('subtotal', 'iva')
     def _importe_total(self):
         self.importeTotal = float(self.subtotal) + (float(self.subtotal) * (float(self.iva))/100)