
from odoo import models, fields, api

class PackagingService(models.Model):
    _inherit= 'product.template'

    is_packaging_service = fields.Boolean("Is packaging service?", default=False)