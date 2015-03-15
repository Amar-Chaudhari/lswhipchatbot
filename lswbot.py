__author__ = 'amarchaudhari'
import config
import requests
from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings


class BonjourPlugin(WillPlugin):

    @respond_to("switchport (status) (BWND[0-9]*)")
    def say_bonjour_will(self, message,status,server_id):
        """bonjour: I know how to say bonjour! In French!"""
        self.reply(message, str(status)+" "+str(server_id))

