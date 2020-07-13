
# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Website(models.Model):

    _inherit = "website"
    def get_first_level_categories(self):
        return self.env['product.public.category'].search([('parent_id','=',False)])