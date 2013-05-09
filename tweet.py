import os, random, tweetpony

consumer_key = ''
consumer_secret = ''
token = ''
token_secret = ''

def postCat():
	PathToCats = ''
	catString = random.choice(os.listdir(PathToCats))

	cat = open("%s/%s"%(PathToCats,catString)
	api = tweetpony.API(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=token, access_token_secret=token_secret)
	try:
		api.update_status_with_media(status = "HourlyCats presents:", media = cat)
	except tweetpony.APIError as e:
		if e.code == 193:
			os.remove("%s/%s"%(PathToCats,catString))
			postCat()
		else:
			raise e
	print "Posted "+catString

postCat()
