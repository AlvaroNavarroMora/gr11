# -*- coding: utf-8 -*-

from odoo import models, fields, api

class linea_de_venta(models.Model):
    _name = 'upofly.linea_de_venta'
    _rec_name = 'num_horas'
    
    num_horas = fields.Float("Número de horas", required=True)
    venta_id = fields.Many2one("upofly.venta", "Venta")
    servicio_ids = fields.Many2one("upofly.servicio", "Servicio", required=True)
    vuelo_id = fields.Many2one("upofly.vuelo", "Vuelo", required=True)
    
    
    subtotal = fields.Float("Subtotal", store=True, compute="_calcular_subtotal")
    precio_base_id = fields.Float("Precio Base", related='servicio_ids.precio_base')
    precio_hora_id = fields.Float("Precio por Hora", related='servicio_ids.precio_hora')
    
    @api.depends('num_horas', 'precio_base_id', 'precio_hora_id')
    def _calcular_subtotal(self):
        for record in self:
            record.subtotal = float(record.precio_base_id) + (float(record.precio_hora_id) * float(record.num_horas))
    

