from odoo import fields, models, api


class HospitalParent(models.Model):
    _name = 'hospital.parent'
    _description = "this is the patient's parents"
    _rec_name = 'parent_name'
    parent_name = fields.Char(
        string='Parent_name',
        required=False)

    mobile = fields.Char(
        string='Mobile',
        required=False)
