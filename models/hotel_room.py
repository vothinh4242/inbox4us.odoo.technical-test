from odoo import models, fields


class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = 'Hotel Room'

    name = fields.Char(string='Room Number', required=True)
    room_type = fields.Selection([
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
    ], string='Room Type', required=True)
    price_per_night = fields.Float(string='Price per Night', required=True)
    status = fields.Selection([
        ('available', 'Available'),
        ('booked', 'Booked'),
        ('maintenance', 'Maintenance'),
    ], string='Status', default='available')
