import os, tweetpony, imageReduce, time
from catDb import catDb
from conf import *


def postCat():
	db = catDb()
	catString = ''
	catPosted = False
	errorCounter = 0

	while catPosted is False and errorCounter < tryPostingCats:
		catString = db.getCat()
		if doPost(catString) is True:
			db.countThatCat(catString)
			catPosted = True
		else:
			errorCounter += 1
			time.sleep(1)  # don't spam the server!

	if errorCounter > 0:
		print "had", errorCounter, "errors"

	if catPosted:
		print "Posted " + catString

	db.saveDb()


def doPost(catString):
	sendingOk = True
	cat = open("%s/%s" % (pathToCats, catString))

	try:
		api = tweetpony.API(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=token, access_token_secret=token_secret)
		api.update_status_with_media(status=tweetMessage, media=cat)
	except tweetpony.APIError as e:
		sendingOk = False
		if e.code == 193:
			# Image to big. lets reduce quality to 90, resave it - should be small enough then.
			imageReduce.reduceQuality("%s/%s" % (pathToCats, catString), 90)
		else:
			raise e
	except Exception as ex:
		os.rename("%s/%s" % (pathToCats, catString), "%s/%s" % (pathToErrorCats, catString))
		raise ex

	return sendingOk

if __name__ == "__main__":
	postCat()
