# -*- coding: utf-8 -*-
from odoo import http

# class Upofly(http.Controller):
#     @http.route('/upofly/upofly/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/upofly/upofly/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('upofly.listing', {
#             'root': '/upofly/upofly',
#             'objects': http.request.env['upofly.upofly'].search([]),
#         })

#     @http.route('/upofly/upofly/objects/<model("upofly.upofly"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('upofly.object', {
#             'object': obj
#         })