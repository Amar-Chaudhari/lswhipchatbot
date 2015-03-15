__author__ = 'amarchaudhari'
import config
import requests
from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings


class BonjourPlugin(WillPlugin):

    @respond_to("switchport status (?P<server_id>.[BWND]*)")
    def say_bonjour_will(self, message,server_id):
        self.reply(message, "server online"+str(server_id))

