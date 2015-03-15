__author__ = 'amarchaudhari'
import config
import requests
from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings


class LswBot(WillPlugin):

    @respond_to("switchport status (?P<server_id>.*)")
    def say_switchport_status(self, message,server_id):
        if server_id:
            # Request: LeaseWeb API (https://api.leaseweb.com/v1/bareMetals)
            lsw_key = config.lsw_api_key
            # Send synchronously
            try:
                r =requests.get("https://api.leaseweb.com/v1/bareMetals",headers={"Accept": "application/json","X-Lsw-Auth": lsw_key })
                # Success
                print('Response status ' + str(r.status_code))
                data = r.json()
                for server in data['bareMetals']:
                    if server['bareMetal']['serverName'] == server_id:
                        status=server
                        break
                if status:
                    self.reply(message, status)
                else:
                    self.reply(message, "Status could not be determined")
            except requests.exceptions.Timeout, e:
            #Exception
                self.reply(message, "Request timed out , try again !")

        else:
            self.reply(message, "No Server ID")

