# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import os
import jinja2

from os import walk
import pathlib

loader = jinja2.FileSystemLoader('/mnt/extra-addons/controller_module/web/views')
env = jinja2.Environment(loader=loader, autoescape=True)
# env = jinja2.Environment(loader=loader, autoescape=True)

class ControllerModule(http.Controller):
    def _render_template(self, **d):
        print("------------------------------------------------------------------------")
        print(os.getcwd())
        d.setdefault('manage', True)
        d['regioes'] = [['R1','Ibirapuera'], ['R2','Mooca'], ('R3','Ana Rosa')]
        # d.setdefault('manage',True)
        # d['insecure'] = odoo.tools.config.verify_admin_password('admin')
        d['list_db'] = ['DB1','DB2']
        # d['langs'] = odoo.service.db.exp_list_lang()
        d['especs'] = [
['acupuntura','acupuntura'],
['alergologista','alergia e imunologia'],
['alergologista_pediatrico','alergia e imunologia pediatrica'],
['cardiologista','cardiologia'],
['cardiologistacongenita','cardiologia congenita'],
['cardiologiainfantil','cardiologia pediatrica'],
['cirurgia-aparelho-digestivo','cirurgia do aparelho digestivo'],
['cirurgiao-geral','cirurgia geral'],
['cirurgiapediatrica','cirurgia pediatrica'],
['cirurgiao-plastico','cirurgia plastica'],
['cirurgiao-vascular','cirurgia vascular'],
['clinico-geral','clinica geral'],
['coloproctologista','coloproctologia'],
['dermatologista','dermatologia'],
['endocrinologista','endocrinologia'],
['endocrinologiainfantil','endocrinologia pediatrica'],
['fisioterapeuta','fisioterapia'],
['gastroenterologista','gastroenterologia'],
['gastroenterologiainfantil','gastroenterologia pediatrica'],
['geriatra','geriatria'],
['ginecologista','ginecologia e obstetricia'],
['hematologista','hematologia'],
['HEMATOLOGISTA_PEDIATRICO','hematologia pediatrica'],
['hepatologista','hepatologia'],
['homeopatia','homeopatia'],
['infectologista','infectologia'],
['mastologista','mastologia'],
['medicina_esportiva','medicina esportiva'],
['nefrologista','nefrologia'],
['nefrologiainfantil','nefrologia pediatrica'],
['neurologista','neurologia'],
['neurologiainfantil','neurologia pediatrica'],
['nutricionista','nutricao'],
['nutrologia','nutrologia'],
['dentista','odontologia (avaliacao odontologica)'],
['oftalmologista','oftalmologia'],
['oftalmologista_ped','oftalmologia pediatrica'],
['ortopedista','ortopedia'],
['otorrinolaringologista','otorrinolaringologia'],
['pediatra','pediatria'],
['pneumologista','pneumologia'],
['pneumoinfantil','pneumologia pediatrica'],
['psicologo','psicologia'],
['psiquiatra','psiquiatria'],
['psiquatriainfantil','psiquiatria pediatrica'],
['reumatologista','reumatologia'],
['reumatologista_pedriatrico','reumatologia pediatrica'],
['urologista','urologia']
]
        # d['countries'] = odoo.service.db.exp_list_countries()
        # d['pattern'] = DBNAME_PATTERN
        # # databases list
        # d['databases'] = []
        # try:
        #     d['databases'] = http.db_list()
        #     d['incompatible_databases'] = odoo.service.db.list_db_incompatible(d['databases'])
        # except odoo.exceptions.AccessDenied:
        #     monodb = db_monodb()
        #     if monodb:
        #         d['databases'] = [monodb]
        return env.get_template("teste.html").render(d)

    @http.route('/dbselector', type='http', auth="none")
    def selector(self, **kw):
        print("------------------------------------------------------------------------")
        current_dir = pathlib.Path(__file__).parent
        print(current_dir)
        print("------------------------------------------------------------------------")
        request._cr = None
        return self._render_template(manage=False)

    @http.route('/empresas/', auth='none')
    def index(self, **kw):
        print("------------------------------------------------------------------------")
        print(os.getcwd())
        # print("Caminho:" & os.path.dirname(__file__))
        # loader = jinja2.PackageLoader('YourCustomAddonPath', "yourcustomhtmlfilepathresidingfolder eg:views")
        # loader = jinja2.PackageLoader('odoo.addons.web', "views")
        # env.get_template("custom_html.html").render(d).



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
