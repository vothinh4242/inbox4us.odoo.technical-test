## Inbox4us - Technical Test Requirements for Odoo Hotel Booking Module
### Overview
The candidate is required to complete a custom Odoo module for managing hotel bookings. This module includes room management, booking management, and customer management. Additionally, they need to implement a REST API for authentication and booking management using JWT. Extra points will be given for handling booking statuses and adding parameter validation using decorators.

### Requirements
#### 1. Write REST API for Authentication using JWT
Implement user registration and login endpoints.
Use JWT for token-based authentication.

```
File: controllers/auth_controller.py
```

#### 2. Write API for Making a Booking
Implement an endpoint to create a new booking.
```
File: controllers/booking_controller.py
```

#### Nice to Have (Optional)
- Handle Booking Status: Implement logic to manage booking statuses (checkin, checkout, booked).
- Adding Validation for Parameters Using Decorators: Implement parameter validation using decorators to ensure correct data is provided in the API requests.
- Write postman collection for testing the API.