# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ruta(models.Model):
    _name = 'upofly.ruta'
    _rec_name = 'nombre'
    
    nombre = fields.Char('Nombre', size=64, required=True)
    descripcion = fields.Char("Descripcion", size=64,required=True)
    localizacion_ids = fields.Many2many("upofly.localizacion", string="Localizaciones")
    
    def eliminarLocalizaciones(self):         
        # Eliminamos los registros de la relación many2many 
        self.write({'localizacion_ids':[ (5,  ) ]})  