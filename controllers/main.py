import requests, json, datetime

from odoo import http, _, exceptions
from odoo.http import request, Response
from datetime import datetime, timedelta


# Function to generate an error response in JSON format
def error_response(error, msg, code):
    return {
        "jsonrpc": "2.0",
        "id": None,
        "error": {
            "code": code,
            "message": msg,
            "data": {
                "name": str(error),
                "debug": "",
                "message": msg,
            }
        },
    }


class marketingApi(http.Controller):

    # Save leads data
    @http.route(
        '/api/v1/marketing/save-leads',
        type='http', auth='none', methos=['POST'], cors='*', csrf=False)
    def save_lead_data(self, **post):
        try:
            name = post['name']
            email = post['email']
            phone_number = post['number']
        except KeyError as e:
            msg = "Missing data"
            res = error_response(e, msg, 400)
            return http.Response(
                json.dumps(res),
                status=404,
                mimetype='application/json'
            )
        try:
            leads = request.env['motion.leads'].sudo()
            new_lead = {
                'name': name,
                'email': email,
                'phone_number': phone_number,
                'department': post['department'] or '',
                'message': post['message'] or ''
            }
            leads.create(new_lead)
            res = {
                "jsonrpc": "2.0",
                "id": None,
                "result": "Lead save successfully"
            }
            return http.Response(
                json.dumps(res),
                status=200,
                mimetype='application/json'
            )
        except KeyError as e:
            msg = "Oops, something went wrong."
            res = error_response(e, msg, 500)
            return http.Response(
                json.dumps(res),
                status=500,
                mimetype='application/json'
            )