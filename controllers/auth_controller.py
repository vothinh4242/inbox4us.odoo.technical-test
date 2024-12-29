import jwt
import datetime
from odoo import http
from odoo.http import request


SECRET_KEY = 'your_secret_key_here'


class AuthController(http.Controller):

    # Register a new user
    @http.route('/api/v1/auth/register', type='json', auth="none", methods=['POST'], cors='*', csrf=False)
    def register(self, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        password = kwargs.get('password')

        if not name or not email or not password:
            return {'error': 'Missing required parameters'}

        user = request.env['res.users'].sudo().create({
            'name': name,
            'login': email,
            'password': password,
            'company_ids': [(4, request.env.ref('base.main_company').id)],
            'company_id': request.env.ref('base.main_company').id,
        })

        return {'message': 'User registered successfully'}

    # Login user and generate JWT token
    @http.route('/api/v1/auth/login', type='json', auth='none', methods=['POST'], cors='*', csrf=False)
    def login(self, **kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')

        try:
            # Authenticate user credentials
            request.session.authenticate(request.env.cr.dbname, email, password)
            # Retrieve the user info
            user = request.env['res.users'].sudo().search([('login', '=', email)])
            # Generate a JWT token
            token = jwt.encode({
                'user_id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
            }, SECRET_KEY, algorithm='HS256')

            return {'token': token}
        except Exception as e:
            # Return error if login fails
            return {
                'status': 'error',
                'message': 'Invalid credentials',
                'error': str(e)
            }
