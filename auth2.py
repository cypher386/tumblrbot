#!/usr/local/bin/python2.7

""" Tumblr API Example - Python CLI
"""

import oauth2
import urlparse
import pytumblr
import json
from inspect import getmembers
import pprint
import pickle

REQUEST_TOKEN_URL = 'http://www.tumblr.com/oauth/request_token'
AUTHORIZATION_URL = 'http://www.tumblr.com/oauth/authorize'
ACCESS_TOKEN_URL = 'http://www.tumblr.com/oauth/access_token'
"""  access tokens
CONSUMER_KEY = ''
CONSUMER_SECRET = 'z7CCAjPJ4CLCLHTNPo3stu4sjXJ0DfQCVAU9rHKPv4rGtdV5dO'

"""


try:
    token = oauth2.Token
    with open('auth.pickle') as infile:
        token = pickle.load(infile)
except IOError as err:


"""  oauth tokens
    oauth_token        = ''
    oauth_token_secret = ''
#    oauth_verifier = ''
"""
#    token = oauth2.Token(oauth_token, oauth_token_secret)
#    token.set_verifier(oauth_verifier)
#    print type(token)
#    print vars(token)




    oauth_verifier = ''
    token = oauth2.Token(oauth_token, oauth_token_secret)
#    token.set_verifier(oauth_verifier)
"""
    print type(token)
    print vars(token)

    with open('auth.pickle', 'w') as outfile:
        pickle.dump(token, outfile)
       #print json.dumps(token), outfile

"""

# submit signed token
consumer =  oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
o_client = oauth2.Client(consumer)

resp, content = o_client.request(ACCESS_TOKEN_URL, "POST")
access_token = dict(urlparse.parse_qsl(content))


tumblr_client = pytumblr.TumblrRestClient(consumer)


print  tumblr_client.submission('jessicastimeline.tumblr.com')[0]['id']
#print asklist

for ask in asklist['posts']:
    if ask['type'] == 'answer':
        if ask['state'] == 'submission':
            print ask
            # client.edit_post('[my blog's name]', id=ask['id'], answer=[whatever I want my bot to answer to any given ask], state='published')

