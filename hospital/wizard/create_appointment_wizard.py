from odoo.models import TransientModel
from odoo import fields
class CreateAppointmentWizard(TransientModel):
    _name = "create.appointment.wizard"
    _description = 'Create Appointment Wizard'

    name = fields.Char(
        string='Name',
        required=False)

    def create_appointment_action(self):
        print("test")
        print(f'{self}'.center(80,'#'))
        print(*dir(self),sep='\n')
        print('#'*80)

