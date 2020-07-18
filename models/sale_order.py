# -*- coding: utf-8 -*-

from odoo import api, models, fields, tools, _
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    shipping_fees = fields.Float('Shipping Fees', compute='_compute_shipping_fees')

    @api.multi
    @api.depends('website_order_line')
    def _compute_shipping_fees(self):
        minimum = self.env['website'].get_minimum_amount_for_free_shipping()
        for rec in self:
            fees = 0.00
            if minimum > 0 and rec.amount_total < minimum:
                for line in rec.website_order_line:
                    if line.product_id.is_shipping_service:
                        fees = line.product_id.website_public_price
                        break
            rec.shipping_fees = fees

    @api.model
    def _get_website_data(self, order):
        res = super(SaleOrder, self)._get_website_data(order)
        # get shiping minimum amount for free shipping
        minimum = self.env['website'].get_minimum_amount_for_free_shipping()
        shipping_fees = False
        # check if shipping fees should apply
        if minimum > 0 and order.amount_total < minimum:
            # check if shipping fees already applied
            shipping_fees_applied = False
            for line in order.website_order_line:
                if line.product_id.is_shipping_service:
                    shipping_fees = line.product_id.website_public_price
                    shipping_fees_applied = True
                    break
            # apply shipping if not already applied
            if not shipping_fees_applied:
                shipping_service_id = self.env['product.template'].search([('is_shipping_service','=',True)], limit=1)
                if shipping_service_id:
                    if shipping_service_id:
                        self.env['sale.order.line'].create({
                            'order_id': order.id,
                            'product_id': shipping_service_id.id,
                        })
                        shipping_fees = shipping_service_id.website_public_price
        res.update({'shipping_fees': shipping_fees})
        #raise ValidationError(shipping_fees)
        return res