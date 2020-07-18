
from odoo import models, fields, api

class PackagingService(models.Model):
    _inherit= 'product.template'

    is_shipping_service = fields.Boolean("Is shipping service?", default=False)