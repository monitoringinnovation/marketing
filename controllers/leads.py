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


class leadsApi(http.Controller):

    # Save leads data
    @http.route(
        '/api/v1/marketing/leads/save-leads',
        type='http', auth='public', methos=['POST'], cors='*', csrf=False)
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

    @http.route(
        '/api/v1/marketing/leads/',
        type='http', auth='public', methos=['GET'], cors='*', csrf=False)
    def leads(self):
        leads = request.env['motion.leads'].sudo().search([])
        lead_data = []
        for lead in leads:
            lead_data.append({
                'name': lead.name,
                'email': lead.email,
                'phone_number': lead.phone_number,
                'department': lead.department,
                'message': lead.message,
                'curr_time': lead.curr_time.strftime("%Y-%m-%d %H:%M:%S"),
            })
        res = {
            "jsonrpc": "2.0",
            "result": lead_data
        }
        return http.Response(
            json.dumps(res),
            status=200,
            mimetype='application/json'
        )