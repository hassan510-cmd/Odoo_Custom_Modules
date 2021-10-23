from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    patient_seq = fields.Char(
        string='Patient_seq',
        required=True,
        copy=False,
        readonly=True,
        default='new')

    patient_name = fields.Char(
        string='Patient Name',
        required=True)

    patient_age = fields.Integer(
        string='Patient Age',
        required=True,
        tracking=True
    )

    gender = fields.Selection(
        string='Gender',
        selection=[
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other')
        ],
        required=True, default='other')

    notes = fields.Text(
        string="Notes",
        required=False,
        tracking=True)

    state = fields.Selection(
        [
            ('urgent', 'Urgent'),
            ('normal', 'Normal'),
            ('naction', 'Need Action')
        ],
        string='Status',
        required=True,
        tracking=True
        # default='normal'
    )

    related_parent = fields.Many2one(
        comodel_name='hospital.parent',
        string='parent name',
        required=False)

    def to_urgent(self):
        self.state = 'urgent'

    def to_normal(self):
        self.state = 'normal'

    def to_action(self):
        self.state = 'naction'

    @api.model
    def create(self, vals_list):
        # print(vals_list)
        vals_list['patient_seq'] = self.env['ir.sequence'].next_by_code('code.patient.seq')
        obj = super(HospitalPatient, self).create(vals_list)
        # print(obj)
        return obj
