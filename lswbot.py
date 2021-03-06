__author__ = 'amarchaudhari'
import config
import requests
from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings


class GetSwitchPortStatus(WillPlugin):

    @respond_to("switchport status (?P<server_id>.*)")
    def say_switchport_status(self, message,server_id=None):
        if server_id:
            full_server_id = "BWND"+str(server_id)
            lsw_key = config.lsw_api_key
            # Request: LeaseWeb API (https://api.leaseweb.com/v1/bareMetals)
            try:
                baremetalid=get_baremetal_id(full_server_id)
                if baremetalid:
                        url = "https://api.leaseweb.com/v1/bareMetals/"+str(baremetalid)+"/switchPort"
                        r =requests.get(url,headers={"Accept": "application/json","X-Lsw-Auth": lsw_key })
                        if r.status_code==200:
                            data = r.json()
                            if data['switchPort']['status'] == 'open':
                                self.reply(message,str(data['switchPort']['serverName'])+" : Enabled",color="green")
                            elif data['switchPort']['status'] == 'closed':
                                self.reply(message,str(data['switchPort']['serverName'])+" : Disabled",color="red")
                        elif r.status_code==400:
                            self.reply(message, "BareMetal Server Not found")
                else:
                    self.reply(message, "BareMetal Server Not found")

            except requests.exceptions.Timeout, e:
            #Exception
                self.reply(message, "Request timed out , try again !",color="red")

        else:
            self.reply(message, "No Server ID",color="red")


class SwitchPortDisable(WillPlugin):
        @respond_to("switchport disable (?P<server_id>.*)")
        def say_switchport_disable(self, message,server_id=None):
            if server_id:
                full_server_id = "BWND"+str(server_id)
                lsw_key = config.lsw_api_key
                baremetalid=get_baremetal_id(full_server_id)
                try:
                    if baremetalid:
                        # headers
                        headers = {'Accept': 'application/json','X-Lsw-Auth': lsw_key}
                        apicall = "https://api.leaseweb.com/v1/bareMetals/"+str(baremetalid)+"/switchPort/close"
                        r =requests.post(url=apicall,headers=headers)
                        if r.status_code==200:
                            self.reply(message,"Switch Port of "+str(full_server_id)+" has been Disabled",color="green")
                        elif r.status_code==500:
                            self.reply(message,"Leaseweb api down/not working , try again in a while",color="red")
                        elif r.status_code==404:
                            self.reply(message, "BareMetal Server Not found",color="red")
                    else:
                        self.reply(message, "BareMetal Server Not found",color="red")
                except requests.exceptions.Timeout, e:
                    self.reply(message, "Request timed out , try again !",color="red")

class SwitchPortEnable(WillPlugin):
        @respond_to("switchport enable (?P<server_id>.*)")
        def say_switchport_enable(self, message,server_id=None):
            if server_id:
                full_server_id = "BWND"+str(server_id)
                lsw_key = config.lsw_api_key
                baremetalid=get_baremetal_id(full_server_id)
                try:
                    if baremetalid:
                        # headers
                        headers = {'Accept': 'application/json','X-Lsw-Auth': lsw_key}
                        apicall = "https://api.leaseweb.com/v1/bareMetals/"+str(baremetalid)+"/switchPort/open"
                        r =requests.post(url=apicall,headers=headers)
                        if r.status_code==200:
                            self.reply(message,"Switch Port of "+str(full_server_id)+" has been Enabled",color="green")
                        elif r.status_code==500:
                            self.reply(message,"Leaseweb api down/not working , try again in a while",color="red")
                        elif r.status_code==404:
                            self.reply(message, "BareMetal Server Not found",color="red")
                    else:
                        self.reply(message, "BareMetal Server Not found",color="red")
                except requests.exceptions.Timeout, e:
                    self.reply(message, "Request timed out , try again !",color="red")



def get_baremetal_id(server_id):

            lsw_key = config.lsw_api_key

            try:
                r =requests.get("https://api.leaseweb.com/v1/bareMetals",headers={"Accept": "application/json","X-Lsw-Auth": lsw_key })
                # Success
                print('Response status ' + str(r.status_code))
                data = r.json()
                for server in data['bareMetals']:
                    if server['bareMetal']['serverName'] == server_id:
                        baremetalid=server['bareMetal']['bareMetalId']
                        break
                try:
                    if baremetalid:
                        return baremetalid
                    else:
                        return False
                except UnboundLocalError:
                    return False
            except requests.exceptions.Timeout, e:
                return False



