import os, tweetpony, imageReduce, time, sys, random
from conf import *
from time import gmtime, strftime


def postCat(message):
	catPosted = False
	errorCounter = 0

	while catPosted is False and errorCounter < tryPostingCats:
		catString = random.choice(os.listdir(pathToCats))
		if doPost(catString, message) is True:
			catPosted = True
		else:
			errorCounter += 1
			time.sleep(1)  # don't spam the server!

	if errorCounter > 0:
		print "had", errorCounter, "errors"

	if catPosted:
		print "%s Posted %s" % (strftime("%Y%m%d %H:%M:%S", gmtime()), catString)



def doPost(catString, message):
	sendingOk = True
	cat = open("%s/%s" % (pathToCats, catString))
	if message == None or message == "":
		message = tweetMessage
	try:
		api = tweetpony.API(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=token, access_token_secret=token_secret)
		api.update_status_with_media(status=message, media=cat)
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
	if len(sys.argv) < 3:
		postCat(None)
	elif sys.argv[1] == "-m":
		postCat(sys.argv[2])
	else:
		postCat(None)
