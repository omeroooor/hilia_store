from odoo import api, fields, models

class mega_menu_content(models.Model):
    _inherit='megamenu.content'
    main_content_type=fields.Selection(selection_add=[('category_list_3','Category Listing 3 Levels')])
    category_ids=fields.Many2many("product.public.category",string="Category", domain=['|',('parent_id','=',False),'|',('parent_id.parent_id','=',False),('parent_id.parent_id.parent_id','=',False)])
