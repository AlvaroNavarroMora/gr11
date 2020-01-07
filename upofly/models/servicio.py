# -*- coding: utf-8 -*-

from odoo import models, fields, api

class servicio(models.Model):
    _name = 'upofly.servicio'
    _rec_name = 'nombre'
    
    nombre = fields.Char("Nombre", required=True)
    descripcion = fields.Char("Descripción", required=True)
    precio_hora = fields.Float("Precio por Hora", required=True)
    precio_base = fields.Float("Precio base", required=True)
    lineas_de_venta_ids = fields.One2many("upofly.linea_de_venta", "servicio_ids", string="Líneas de Venta")
