hourlycats
==========

Prereq:
- oauth2 (pip install oauth2)
- tweetpony (pip install tweetpony)
- pillow (pip install pillow - it is a setuptool friendly fork of PIL. Please remove PIL before you install pillow. You can not use both)

**authurl.py** is used to generate Access Tokens for twitter. Add your Consumer Token/Secret to the script.  
**tweet.py** is for actualy tweeting - same here, add your tokens. (Consumer and generate Access Tokens)

Possible errors:

    TypeError: request() got an unexpected keyword argument 'stream'

Looks like you're using an old version of the requests lib. Try updating it: **sudo pip install -U requests**  
Mine was: **0.14.1**  
More at: https://github.com/Mezgrman/TweetPony/issues/1

    Read-only application cannot POST

Go to dev.twitter.com/apps  
Select your app, then under 'settings' --> 'application type' you will find what you need.  
After that, you HAVE to re-run the **authurl.py**.
