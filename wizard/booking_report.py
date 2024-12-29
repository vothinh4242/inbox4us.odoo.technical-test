from odoo import models, fields, api
from odoo.exceptions import UserError


class BookingReport(models.TransientModel):
    _name = 'booking.report'
    _description = 'Booking Report'

    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)

    def action_generate_report(self):
        self.ensure_one()
        if self.start_date > self.end_date:
            raise UserError("Start Date must be earlier than End Date.")

        bookings = self.env['hotel.booking'].search([
            ('check_in_date', '>=', self.start_date),
            ('check_out_date', '<=', self.end_date)
        ])

        return {
            'type': 'ir.actions.act_window',
            'name': 'Booking Report',
            'res_model': 'hotel.booking',
            'view_mode': 'graph',
            'target': 'current',
            'domain': [('id', 'in', bookings.ids)],
        }

