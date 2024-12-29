from odoo import models, fields, api
from odoo.exceptions import UserError


class Customer(models.TransientModel):
    _name = 'customer.report'
    _description = 'Booking Report'

    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)

    def action_generate_report(self):
        self.ensure_one()
        if self.start_date > self.end_date:
            raise UserError("Start Date must be earlier than End Date.")

        customers = self.env['hotel.customer'].search([
            ('create_date', '>=', self.start_date),
            ('create_date', '<=', self.end_date)
        ])

        return {
            'type': 'ir.actions.act_window',
            'name': 'Customer Report',
            'res_model': 'hotel.customer',
            'view_mode': 'graph',
            'target': 'current',
            'domain': [('id', 'in', customers.ids)],
        }