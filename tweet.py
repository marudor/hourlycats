import os, random, tweetpony
from conf import *


def postCat():
	catString = ''
	catPosted = False
	errorCounter = 0

	while catPosted is False and errorCounter < tryPostingCats:
		catString = random.choice(os.listdir(pathToCats))
		if doPost(catString) is True:
			catPosted = True
		else:
			errorCounter += 1

	if errorCounter > 0:
		print "had", errorCounter, "errors"

	if catPosted:
		print "Posted " + catString


def doPost(catString):
	sendingOk = True
	cat = open("%s/%s" % (pathToCats, catString))

	try:
		api = tweetpony.API(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=token, access_token_secret=token_secret)
		api.update_status_with_media(status=tweetMessage, media=cat)
	except tweetpony.APIError as e:
		sendingOk = False
		if e.code == 193:
			if pathToErrorCats == '':
				os.remove("%s/%s" % (pathToCats, catString))
			else:
				os.rename("%s/%s" % (pathToCats, catString), "%s/%s" % (pathToErrorCats, catString))
		else:
			raise e
	except Exception as ex:
		os.rename("%s/%s" % (pathToCats, catString), "%s/%s" % (pathToErrorCats, catString))
		raise ex

	return sendingOk

if __name__ == "__main__":
	postCat()
