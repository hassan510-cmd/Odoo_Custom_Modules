from odoo import fields, models, api


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'reservations'

    name = fields.Char()
    patient_id = fields.Many2one(
        comodel_name='hospital.patient',
        string='Patient_id',
        required=False)
    age = fields.Integer(
        string='Age',
        required=False,
        related='patient_id.patient_age')

    gender = fields.Selection(

        string='Gender',
        selection=[
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other')
        ],
        required=True, default='other')

    appointment_date = fields.Date(
        string='Appointment_date',
        required=False)
    checkup_date = fields.Datetime(
        string='Checkup_date',
        required=False)
    image = fields.Binary(string='patient image', related='patient_id.image')

    @api.onchange('patient_id')
    def onchange_patient_id(self):

        if self.patient_id:
            if self.patient_id.gender:
                self.gender=self.patient_id.gender
