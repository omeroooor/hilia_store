
# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Website(models.Model):
    _inherit = "website"

    
    shipping_fees = fields.Float('Shipping fees', default=2.0)
    minimum_for_free_shipping = fields.Float('Minimum amount for free shipping', default=0)

    def get_first_level_categories(self):
        return self.env['product.public.category'].search([('parent_id','=',False)])

    @api.model
    def get_minimum_amount_for_free_shipping(self):
        website_settings = self.env['website.config.settings'].search([], limit=1)
        minimum = 0
        if website_settings:
            minimum = website_settings.minimum_for_free_shipping
            
        #raise ValidationError(minimum)
        return minimum

    @api.model
    def get_shipping_cost(self):
        shipping_service_id = self.env['product.template'].search([('is_shipping_service','=',True)], limit=1)
        if shipping_service_id:
            return shipping_service_id.website_public_price
        else:
            return 0
