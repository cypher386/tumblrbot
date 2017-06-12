#!/usr/local/bin/python2.7

""" Tumblr API Example - Python CLI
"""

import oauth2
import urlparse
import pytumblr
import json

REQUEST_TOKEN_URL = 'http://www.tumblr.com/oauth/request_token'
AUTHORIZATION_URL = 'http://www.tumblr.com/oauth/authorize'
ACCESS_TOKEN_URL = 'http://www.tumblr.com/oauth/access_token'
"""  access tokens
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
"""

try:
    with open('auth.json') as infile:
        oauth_data = json.load(infile)
except IOError as err:
    print("failed to open auth file, requesting token")

    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    client = oauth2.Client(consumer)
     
    resp, content = client.request(REQUEST_TOKEN_URL, "GET")
    
    request_token = dict(urlparse.parse_qsl(content))
    OAUTH_TOKEN = request_token['oauth_token']
    OAUTH_TOKEN_SECRET = request_token['oauth_token_secret']
    
    print "Request Token:"
    print "    - oauth_token        = %s" % OAUTH_TOKEN
    print "    - oauth_token_secret = %s" % OAUTH_TOKEN_SECRET
    
    print "Go to the following link in your browser:"
    print "%s?oauth_token=%s" % (AUTHORIZATION_URL, request_token['oauth_token'])
    
    oauth_verifier = raw_input('What is the verifier? ')
    #oauth_verifier=''
    token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
    token.set_verifier(oauth_verifier)
    
    with open('auth.json', 'w') as outfile:
        json.dump(token, outfile)
    

# submit signed token
client = oauth2.Client(consumer, token)

resp, content = client.request(ACCESS_TOKEN_URL, "POST")
access_token = dict(urlparse.parse_qsl(content))

print "Access Token:"
print "    - oauth_token        = %s" % access_token['oauth_token']
print "    - oauth_token_secret = %s" % access_token['oauth_token_secret']
print "    - oauth_verifier = %s" % access_token['oatuh_token_verifier']

client = pytumblr.TumblrRestClient(consumer, token) 


print  client.submission('jessicastimeline.tumblr.com')[0]['id']
#kkkprint asklist

for ask in asklist['posts']:
    if ask['type'] == 'answer':
        if ask['state'] == 'submission':
            print ask
            # client.edit_post('[my blog's name]', id=ask['id'], answer=[whatever I want my bot to answer to any given ask], state='published')

