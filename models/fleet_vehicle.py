from odoo import fields, models
from odoo.exceptions import UserError

import datetime, pytz, json, logging, warnings
_logger = logging.getLogger(__name__)


class vehicle(models.Model):
    _inherit = "fleet.vehicle"

    engine = fields.Boolean(default = True, tracking = True)

    def send_command(self, vals):
        host, session = self.env['res.config.settings'].sudo()._get_session_information()

        vehicle = self.search([["gps1_id","=", int(vals["data"])]])
        device=vehicle.gps1_id

        if(vehicle.engine==True):
            command="engineStop"
        else:
            command="engineResume"
        
        data = {
            "atributes":{},
            "deviceId": vehicle.gps1_id.solesgps_id,
            "type": command
        }        
        response = session.post(
            f"{host}/commands/send",
            json=data
        )        
        
        if response.status_code not in (200,202,204):
            raise UserError(f"Error actualizando Traccar: {response.text}")

        data=response.text
       
        if command =="engineResume":
            vehicle.engine=True
        else:
            vehicle.engine=False        
        return data
 
