#!/usr/bin/python

import sys
import requests
import hashlib
import time
import simplejson

TOKEN = 'm198sOkJEn37DjqZ32lpRu76xmw288xSQ9'
SECRET = 'iEk21fuwZApXlz93750dmW22pw389dPwOk'
HASH_PATTERN = '0001110111101110001111010101111011010001001110011000110001000110'
BASE_URL = 'https://feelinsonice.appspot.com'

def main(args):
    if len(args) < 2:
        print "usage: python sc-findusers.py <username> <password> <number1,number2,...>"
        exit(0)

    # log in
    ts = time.mktime(time.gmtime())
    params = {'username': args[1], 'password': args[2], 'timestamp': ts}

    r = sc_request('/ph/login', params, TOKEN, ts)

    # subsequent API calls should use this token instead of the static token
    auth_token = r['auth_token']

    ts = time.mktime(time.gmtime())
    numbers = {}
    for number in args[3].split(','):
        numbers[number] = number

    numbers_json = simplejson.dumps(numbers)
    params = {'username': args[1], 'timestamp': ts, 'numbers': numbers_json, 'countryCode': 'US'}
    try:
        r = sc_request('/ph/find_friends', params, auth_token, ts)
    except:
        print 'error: failed to retrieve numbers results'
        exit(0)

    print '\nsuccess: found %d results:' % len(r['results'])

    for number in r['results']:
        print '\tnumber: ' + number['display']
        print '\tusername: ' + number['name']
        print ''





def sc_request(uri, post_params, tok, ts):
    url = BASE_URL + uri
    post_params['req_token'] = sc_hash(tok, ts)
    r = requests.post(url, data = post_params)
    r.raise_for_status()
    return r.json()


# seriously, snapchat team?
def sc_hash(tok, ts):
	h1 = hashlib.sha256(SECRET + tok).hexdigest()
	h2 = hashlib.sha256(str(ts) + SECRET).hexdigest()
	
	result = ''
	for i in range(0, len(HASH_PATTERN)):
		if HASH_PATTERN[i] == '0':
			result += h1[i]
		else:
			result += h2[i]
			
	return result
		


	
if __name__ == "__main__":
	main(sys.argv)
