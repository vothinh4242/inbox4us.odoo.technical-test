from odoo import http


class BookingController(http.Controller):

    @http.route('/api/bookings', type='json', auth='public', methods=['POST'])
    # @validate_request - TODO: handle request validation - Nice to have
    # @jwt_required - TODO: handle jwt token in the request
    def create_booking(self, **kwargs):
        # TODO: need to handle authentication access token
        # TODO: Implement booking creation logic
        # Note: need to check availability of the room
        pass
