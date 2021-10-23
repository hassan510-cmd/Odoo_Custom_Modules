# to extend another modules to our custom module
from openerp import models, fields, api

# start define your classes
import odoo.fields


class DietFacts(models.Model):
    _name="product.template"
    _inherit="product.template"
    calorie=fields.Integer("Calories") # Cal refer to label
    serve_size = fields.Float(
        string='Serve_size',
        required=False)
    last_update = fields.Date(
        string='Last_update',
        required=False)
    is_diet = fields.Boolean(
        string='Is_diet', 
        required=False)

