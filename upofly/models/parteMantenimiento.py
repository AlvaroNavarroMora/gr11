# -*- coding: utf-8 -*-

from odoo import models, fields, api

class parteMantenimiento(models.Model):
    _name = 'upofly.parte_mantenimiento'
    
    fecha = fields.Date("Fecha", required=True)
    descripcion = fields.Text("Descripcion")
    estado = fields.Selection([('enEspera', 'En espera'), ('enReparacion', 'En reparacion'), ('reparado', 'Reparado')], 'Estado del mantenimiento')
    tiempoEstimado = fields.Integer("Tiempo Estimado de reparación (Días)", required = True)
    aeronave_id = fields.Many2one("upofly.aeronave", "Aeronave")