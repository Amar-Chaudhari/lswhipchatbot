__author__ = 'amarchaudhari'
import config
import requests

# Request: LeaseWeb API (https://api.leaseweb.com/v1/bareMetals)
lsw_key = config.lsw_api_key


# Headers

# Send synchronously
try:
    r =requests.get("https://api.leaseweb.com/v1/bareMetals",headers={"Accept": "application/json","X-Lsw-Auth": lsw_key })
    # Success
    print('Response status ' + str(r.status_code))
    data = r.json()
    for server in data['bareMetals']:
        if server.bareMetal['serverName'] == 'BWND012':
            print server

except requests.exceptions.Timeout, e:
    # Exception
    print('Exception during request')