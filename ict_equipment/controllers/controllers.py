# -*- coding: utf-8 -*-
# from odoo import http


# class IctEquipment(http.Controller):
#     @http.route('/ict_equipment/ict_equipment', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ict_equipment/ict_equipment/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ict_equipment.listing', {
#             'root': '/ict_equipment/ict_equipment',
#             'objects': http.request.env['ict_equipment.ict_equipment'].search([]),
#         })

#     @http.route('/ict_equipment/ict_equipment/objects/<model("ict_equipment.ict_equipment"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ict_equipment.object', {
#             'object': obj
#         })
