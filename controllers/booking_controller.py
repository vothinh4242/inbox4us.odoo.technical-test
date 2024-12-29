import jwt
from odoo import http
from odoo.http import request

SECRET_KEY = 'your_secret_key_here'

def jwt_required(func):
    def wrapper(*args, **kwargs):
        token = request.httprequest.headers.get('Authorization')
        if not token:
            return {'error': 'Token is missing'}, 401

        try:
            token = token.split(" ")[1]
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            user_id = data['user_id']
            request.env.user = request.env['res.users'].sudo().browse(user_id)
        except Exception as e:
            return {'error': 'Token is invalid'}, 401

        return func(*args, **kwargs)
    return wrapper

class BookingController(http.Controller):

    @http.route('/api/v1/booking', type='json', auth='public', methods=['POST'], cors='*', csrf=False)
    @jwt_required
    def create_booking(self, **kwargs):
        room_id = kwargs.get('room_id')
        customer_id = kwargs.get('customer_id')
        checkin_date = kwargs.get('checkin_date')
        checkout_date = kwargs.get('checkout_date')

        if not room_id or not customer_id or not checkin_date or not checkout_date:
            return {'error': 'Missing required parameters'}

        room = request.env['hotel.room'].sudo().browse(room_id)
        if room.status != 'available':
            return {'error': 'Room is not available'}

        booking = request.env['hotel.booking'].sudo().create({
            'room_id': room_id,
            'customer_id': customer_id,
            'check_in_date': checkin_date,
            'check_out_date': checkout_date,
        })

        room.sudo().write({'status': 'booked'})

        return {'message': 'Booking created successfully', 'booking_id': booking.id}