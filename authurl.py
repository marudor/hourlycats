import urlparse
import oauth2 as oauth

consumer_key = 'Put your Apps Consumer Key here'
consumer_secret = 'Pur your Apps Consumer Secret here'

base_url = "https://twitter.com/oauth/"

consumer = oauth.Consumer(consumer_key, consumer_secret)
client = oauth.Client(consumer)

resp, content = client.request(base_url+'request_token', "GET")
if resp['status'] != '200':
    raise Exception("Invalid response %s." % resp['status'])

request_token = dict(urlparse.parse_qsl(content))
print request_token

print "%s?oauth_token=%s" % (base_url+'authorize', request_token['oauth_token'])

pin = raw_input('What is the PIN? ')

token = oauth.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
token.set_verifier(pin)
client = oauth.Client(consumer, token)

resp, content = client.request(base_url+'access_token', "POST")
access_token = dict(urlparse.parse_qsl(content))

print "token: %s" % access_token['oauth_token']
print "secret: %s" % access_token['oauth_token_secret']