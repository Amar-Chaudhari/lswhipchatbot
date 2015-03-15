__author__ = 'amarchaudhari'
import config
import httplib
import ConfigParser
# Request: LeaseWeb API (https://api.leaseweb.com/v1/bareMetals)

connection = httplib.HTTPConnection('api.leaseweb.com', 443, timeout = 30)

# Headers

config = ConfigParser.ConfigObj()

headers = {"X-Lsw-Auth": '%s' } % str(config['lsw_api_key'])

# Send synchronously

connection.request('GET', '/v1/bareMetals', None, headers)
try:
	response = connection.getresponse()
	content = response.read()
	# Success
	print('Response status ' + str(response.status))
        print content
except httplib.HTTPException, e:
	# Exception
	print('Exception during request')