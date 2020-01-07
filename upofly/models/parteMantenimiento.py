# -*- coding: utf-8 -*-

from odoo import models, fields, api

class parteMantenimiento(models.Model):
    _name = 'upofly.parte_mantenimiento'
    _rec_name = 'state'
    
    fecha = fields.Date("Fecha", required=True)
    descripcion = fields.Text("Descripcion")
    #estado = fields.Selection([('espera', 'En espera'), ('reparacion', 'En reparacion'), ('reparado', 'Reparado')], 'Estado del mantenimiento')
    tiempoEstimado = fields.Integer("Tiempo Estimado de reparación (Horas)", required = True)
    aeronave_id = fields.Many2one("upofly.aeronave", "Aeronave")
    state = fields.Selection([('espera','En espera'),
                          ('reparacion', 'En reparacion'),
                          ('reparado', 'Reparado'),],
                          'Estado del mantenimiento',
                          default='espera')

    @api.one
    def btn_submit_to_reparacion(self):
        self.write({'state':'reparacion'})
        
    @api.one
    def btn_submit_to_reparado(self):
        self.write({'state':'reparado'})
        
    #@api.onchange('gymclass_ids')
    #def onchange_gymclass(self):
        #if self.state != 'reparado':
            #raise models.ValidationError('El usuario debe estar admitido para apuntarlo a una clase')