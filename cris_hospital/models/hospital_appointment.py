from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Appointment"
    _rec_name = 'patient_id'

    patient_id = fields.Many2one(comodel_name='hospital.patient', string="Patient")
    gender = fields.Selection(related='patient_id.gender')
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)
    ref = fields.Char(string="Reference")
    prescription = fields.Html(string="Prescription")
    priority = fields.Selection(
            [
                ('0', 'Very Low'),
                ('1', 'Low'),
                ('2', 'Normal'),
                ('3', 'High')
            ], 
            string='Priority'
        )
    state = fields.Selection(
        selection= [
            ('draft', 'Draft'),
            ('in_consultation', 'In Consultation'),
            ('done', 'Done'),
            ('cancel', 'Canceled')
        ],
        default="draft",
        string="Status",
        required=True,
    )
    

    # It's better to use related than this
    # This is just a sample of onchange
    @api.onchange("patient_id")
    def _onchange_patient_id(self):
        self.ref = self.patient_id.ref


    def action_test(self):
        print("Button Clicked!")