# -*- coding: utf-8 -*-

from odoo import models, fields, api

class parteMantenimiento(models.Model):
    _name = 'upofly.parte_mantenimiento'
    _rec_name = 'estado'
    
    fecha = fields.Date("Fecha", required=True)
    descripcion = fields.Text("Descripcion")
    estado = fields.Selection([('En espera', 'En espera'), ('En reparacion', 'En reparacion'), ('Reparado', 'Reparado')], 'Estado del mantenimiento')
    tiempoEstimado = fields.Integer("Tiempo Estimado de reparación (Horas)", required = True)
    aeronave_id = fields.Many2one("upofly.aeronave", "Aeronave")