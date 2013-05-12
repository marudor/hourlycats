from os import path

# that's what you get fom twitter
# https://dev.twitter.com/
consumer_key = 'Put your Apps Consumer Key here'
consumer_secret = 'Pur your Apps Consumer Secret here'

# place the token and token_secret you get from the authurl.py here
token = ''
token_secret = ''

# other configs #
tweetMessage = "HourlyCats presents:"

pathToCats = 'cats'
# set errorCats = '' to delete submit fail images
# or a sub path to save the kittens
pathToErrorCats = 'error_cats'
tryPostingCats = 9

# make dir checks!
if not path.isdir(pathToCats):
	raise "pathToCats", pathToCats, "does NOT exist!"

if not path.isdir(pathToErrorCats):
	raise "pathToErrorCats", pathToErrorCats, "does NOT exist! set it to '' or create path!"