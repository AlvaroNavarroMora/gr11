# -*- coding: utf-8 -*-

from odoo import models, fields, api

class linea_de_venta(models.Model):
    _name = 'upofly.linea_de_venta'
    _rec_name = 'num_horas'
    
    num_horas = fields.Float("Número de horas")
    venta_id = fields.Many2one("upofly.venta", "Venta")
    servicio_ids = fields.Many2one("upofly.servicio", "Servicios")
    vuelo_id = fields.Many2one("upofly.vuelo", "Vuelo")
    
    
    subtotal = fields.Float("Subtotal", compute="_calcular_subtotal")
    precio_base_id = fields.Float("Precio Base", related='servicio_ids.precio_base')
    precio_hora_id = fields.Float("Precio por Hora", related='servicio_ids.precio_hora')
    
    @api.depends('num_horas', 'precio_base_id', 'precio_hora_id')
    def _calcular_subtotal(self):
        self.subtotal = float(self.precio_base_id) + (float(self.precio_hora_id) * float(self.num_horas))
    

