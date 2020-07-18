# -*- coding: utf-8 -*-

from odoo import http, SUPERUSER_ID
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

class WebsiteSaleInherit(WebsiteSale):
    @http.route()
    def cart(self, **post):
        # call the original cart method
        res = super(WebsiteSaleInherit, self).cart(**post)
        # attach packaging ids
        order = res.qcontext.get('website_sale_order') or False
        selected_packaging_ids = []
        if order:
            for line in order.website_order_line:
                if line.product_id.is_packaging_service:
                    selected_packaging_ids.append(line.product_id.id)
                if line.product_id.is_shipping_service:
                    line.unlink()
        packaging_ids = request.env['product.template'].search([('is_packaging_service','=',True),('id','not in', selected_packaging_ids)])
        res.qcontext.update({'packaging_ids': packaging_ids, 'selected_packaging_ids': selected_packaging_ids})
        # return updated response
        return res
