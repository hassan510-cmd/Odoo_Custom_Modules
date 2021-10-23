# -*- coding: utf-8 -*-
# from odoo import http


# class Hassan(http.Controller):
#     @http.route('/hassan/hassan/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hassan/hassan/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hassan.listing', {
#             'root': '/hassan/hassan',
#             'objects': http.request.env['hassan.hassan'].search([]),
#         })

#     @http.route('/hassan/hassan/objects/<model("hassan.hassan"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hassan.object', {
#             'object': obj
#         })
