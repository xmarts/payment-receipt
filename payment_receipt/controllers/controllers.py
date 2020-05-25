# -*- coding: utf-8 -*-
# from odoo import http


# class PaymentReceipt(http.Controller):
#     @http.route('/payment_receipt/payment_receipt/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/payment_receipt/payment_receipt/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('payment_receipt.listing', {
#             'root': '/payment_receipt/payment_receipt',
#             'objects': http.request.env['payment_receipt.payment_receipt'].search([]),
#         })

#     @http.route('/payment_receipt/payment_receipt/objects/<model("payment_receipt.payment_receipt"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('payment_receipt.object', {
#             'object': obj
#         })
