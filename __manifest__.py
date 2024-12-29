{
    'name': 'Inbox4us Hotel Booking Management',
    'version': '1.0',
    'category': 'Hotel Management',
    'summary': 'Manage hotel room bookings and customers',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/booking_report.xml',
        'wizard/customer_report.xml',
        'views/hotel_booking.xml',
        'views/hotel_customer.xml',
    ],
    'installable': True,
    'application': True,
}