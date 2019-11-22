# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ruta(models.Model):
    _name = 'upofly.ruta'
    
    nombre = fields.Char('Nombre', size=64, required=True)
    descripcion = fields.Char("Descripcion", size=64,required=True)
    lista_coordenadas = fields.Char("Coordenadas",size=64)