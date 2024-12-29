from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HotelBooking(models.Model):
    _name = 'hotel.booking'
    _description = 'Hotel Booking'

    customer_id = fields.Many2one('hotel.customer', string='Customer', required=True)
    room_id = fields.Many2one('hotel.room', string='Room', required=True)
    check_in_date = fields.Date(string='Check-in Date')
    check_out_date = fields.Date(string='Check-out Date')
    total_amount = fields.Float(string='Total Amount', compute='_compute_total_amount', store=True)
    status = fields.Selection([
        ('booked', 'Booked'),
        ('checkin', 'Check-In'),
        ('checkout', 'Check-Out')
    ], string='Status', default='booked', store=True)

    # Compute the total amount based on the number of nights
    @api.depends('room_id', 'check_in_date', 'check_out_date')
    def _compute_total_amount(self):
        for booking in self:
            if booking.check_in_date and booking.check_out_date:
                num_nights = (booking.check_out_date - booking.check_in_date).days
                booking.total_amount = booking.room_id.price_per_night * num_nights

    # Check if the room is already booked for the selected dates
    @api.model
    def create(self, vals):
        self._check_booking_overlap(vals['room_id'], vals['check_in_date'], vals['check_out_date'])
        return super(HotelBooking, self).create(vals)

    # Check if the room is already booked for the selected dates
    def write(self, vals):
        if 'check_in_date' in vals or 'check_out_date' in vals or 'room_id' in vals:
            self._check_booking_overlap(vals.get('room_id', self.room_id.id),
                                        vals.get('check_in_date', self.check_in_date),
                                        vals.get('check_out_date', self.check_out_date))
        return super(HotelBooking, self).write(vals)

    # Check if the room is already booked for the selected dates
    def _check_booking_overlap(self, room_id, check_in_date, check_out_date):
        overlapping_bookings = self.search([
            ('room_id', '=', room_id),
            ('check_in_date', '<', check_out_date),
            ('check_out_date', '>', check_in_date),
            ('id', '!=', self.id)
        ])
        if overlapping_bookings:
            raise ValidationError('The room is already booked for the selected dates.')