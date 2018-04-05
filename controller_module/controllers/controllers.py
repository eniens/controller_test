# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class ControllerModule(http.Controller):
    @http.route('/empresas/', auth='none')
    def index(self, **kw):
        page = open('/odoo11/custom/controller_module/static/src/html/index.html').read()
        partners = request.env['res.partner'].sudo().search([('customer','=',True)])
        for partner in partners:
            page += '''
            <h1>%s  -  %s</h1>
            ''' % (partner.name, partner.id)

        return page
        # print(partners)
        # values = {
        #     'name':'Diogo',
        #     'partners':partners
        # }
        # response = request.render("controller_module.template_testing", values)
        # return response


    @http.route('/controller_module/controller_module/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('controller_module.listing', {
            'root': '/controller_module/controller_module',
            'objects': http.request.env['controller_module.controller_module'].search([]),
        })

    @http.route('/controller_module/controller_module/objects/<model("controller_module.controller_module"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('controller_module.object', {
            'object': obj
        })

    @http.route(["/qqrcoisa/save"], type='http', auth="none", website=True)
    def expense_save(self, redirect=None, **post):
        print('Cheguei aqui!')
        if post:

            print(post)

