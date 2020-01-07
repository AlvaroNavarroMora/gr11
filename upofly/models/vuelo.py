# -*- coding: utf-8 -*-

from odoo import models, fields, api


class vuelo(models.Model):
    _name = 'upofly.vuelo'
    _rec_name = 'fecha'
    
    fecha = fields.Date('Fecha', required=True)
    aeronave_id = fields.Many2one("upofly.aeronave", "Aeronave", required=True)
    ruta_id = fields.Many2one("upofly.ruta", "Ruta", required=True)
    piloto_id = fields.Many2many("upofly.piloto", string="Pilotos", required=True)
    linea_de_venta_id = fields.Many2one('upofly.linea_de_venta', "Líneas de venta")