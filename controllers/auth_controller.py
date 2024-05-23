from odoo import http

SECRET_KEY = 'your_secret_key_here'


class AuthController(http.Controller):

    @http.route('/api/register', type='json', auth="none", methods=['POST'], cors='*', csrf=False)
    def register(self, **kwargs):
        # TODO: Implement user registration logic
        pass

    @http.route('/api/login', type='json', auth='none', methods=['POST'], cors='*', csrf=False)
    def login(self, **kwargs):
        # TODO: Implement user login logic and return JWT token
        pass
