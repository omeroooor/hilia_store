
# -*- coding: utf-8 -*-

from odoo import api, fields, models


class WebsiteConfigSettings(models.TransientModel):
    _inherit = 'website.config.settings'

    shipping_fees = fields.Float('Shipping fees', related='website_id.shipping_fees', required=True, default=2.0)
    minimum_for_free_shipping = fields.Float('Minimum amount for free shipping', related='website_id.minimum_for_free_shipping', default=0)