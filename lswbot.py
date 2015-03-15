__author__ = 'amarchaudhari'
import config
import httplib
import json
# Request: LeaseWeb API (https://api.leaseweb.com/v1/bareMetals)

connection = httplib.HTTPSConnection('api.leaseweb.com', 443, timeout = 30)

# Headers
lsw_key = config.lsw_api_key
headers = {"X-Lsw-Auth": lsw_key }

# Send synchronously

connection.request('GET', '/v1/bareMetals', None, headers)
try:
    response = connection.getresponse()
    content = response.read()
    # Success
    print('Response status ' + str(response.status))
    data = json.load(content)
    for server in data:
        #if server.bareMetal['serverName'] == "BWND069":
            print server

except httplib.HTTPException, e:
    # Exception
    print('Exception during request')