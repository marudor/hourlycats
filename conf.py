from os import path

# that's what you get fom twitter
# https://dev.twitter.com/
consumer_key='IqQnGlrbg0HohuWC34wTSA'
consumer_secret='ifmmEsxyj87ohuYOfZI9DCJ5oqVsoxITEeZWQsBdTw'

# place the token and token_secret you get from the authurl.py here
token='1411214749-NfPvqKt656LbqSEd9n3arHfJVXPx5JLM5nCeVeI'
token_secret= '6qz6Rlo2Wxpjf2owbpS5ZMG5Rw5LrtSCkuMWuhDVs'

# other configs #
tweetMessage = 'HourlyCats presents:'

pathToCats = '/home/marudor/projects/KatzenBilder'
# set errorCats = '' to delete submit fail images
# or a sub path to save the kittens
pathToErrorCats = '/home/marudor/projects/KatzenBilderError'
tryPostingCats = 9

# make dir checks!
if not path.isdir(pathToCats):
	raise "pathToCats", pathToCats, "does NOT exist!"

if pathToErrorCats != '' and not path.isdir(pathToErrorCats):
	raise "pathToErrorCats", pathToErrorCats, "does NOT exist! set it to '' or create path!"
