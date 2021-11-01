# weeby.py
API Wrapper in Python for WeebyAPI\
Checkout WeebyAPI : https://weebyapi.xyz \
Get your API token here : https://weebyapi.xyz/discord \
Discord Bot using WeebyAPI : https://github.com/asheeeshh/Kanna-Chan

## Installation
```python
pip install weeby.py
```

## Using JSON Response method
```python
import weeby

my_weeby = weeby.Weeby('your_weebyAPI_token_goes_here')

# Random Message
# types available -> 8ball, belikebill, dadjoke, geography, joke, roast
my_weeby.get_json_response().random(type="roast") # Returns String

# Random Animal Image
# types available -> bird, bunny, cat, dog, fox, goose, kangaroo, koala, lizard, panda
my_weeby.get_json_response().animal_image(type="cat") # Returns Image URL

# Random Meme from SubReddit
# types available -> meme, memes, wholesome, dank
my_weeby.get_json_response().meme(type="meme") # Returns List with Image URL and PermaLink

# Random Word
# types available -> random, halloween, christmas, list
my_weeby.get_json_response().word(type="random") # Returns random word or list of words

# Lyrics
my_weeby.get_json_response().lyrics(track="6 months by john k") 
# Returns Lyrics of the song (JSON Response)

# WeebyAPI Stats
my_weeby.get_json_response().stats() # Return JSON with stats of WeebyAPI
```

## Using Image Effect Method
```python
import weeby
from PIL import Image
from io import BytesIO

my_weeby = weeby.Weeby('your_weebyAPI_token_goes_here')

# General Effects
'''
Types available -> blur, contrast, edge, greyscale, invert, pixelize, sepia, sharpen, 
silhouette, threshold, blurple, invertedthreshold, invertedgreyscale
Returns Image Buffer
Image type -> .png/.jpg/.gif
'''
image = my_weeby.apply_effect().general(image_url="your_image_url", type="greyscale")
im = Image.open(BytesIO(image))
im.save("generated.png")

# Intensity Effects
'''
Types avaialable -> brightness, darkness, distort
Returns Image Buffer
Image type -> .png/.jpg/.gif
'''
image = my_weeby.apply_effect().intensity(image_url="your_image_url", type="darkness", 
intensity=50)
im = Image.open(BytesIO(image))
im.save("generated.png")

# Level Effects
'''
Types avaialable -> fisheye, desaturate
Returns Image Buffer
Image type -> .png/.jpg/.gif
'''
image = my_weeby.apply_effect().intensity(image_url="your_image_url", type="desaturate",
level=10)
im = Image.open(BytesIO(image))
im.save("generated.png")

# Resize Image (Limit: 1-2000 for both width and height)
''' 
Returns Image Buffer
Image type -> .png/.jpg/.gif
'''
image = my_weeby.apply_effect().intensity(image_url="your_image__url", width=200, height=200)
im = Image.open(BytesIO(image))
im.save("generated.png")
```

## Using Overlays Method
```python
import weeby
from PIL import Image
from io import BytesIO

my_weeby = weeby.Weeby('your_weebyAPI_token_goes_here')

'''
Types of Overlays available :approved, bazinga, caution, christmas, easter, fire, glass, 
halloween, hearts, jail, rainbow, rejected, simp, snow, thuglife, balance, brilliance, bravery

Image Type: .jpg/.png/.gif

Returns: Image Buffer (Asset)
'''
image = my_weeby.set_overlay().overlay(image_url="your_image_url" type="jail")
im = Image.open(BytesIO(image))
im.save("generated.png)
```

## GIF Method
```python
import weeby

'''
Types of GIF available: akko, angry, baka, bath, boom, boop, beer, bite, blush, bonk, bored,
cheer, chase, clap, confused, cookie, cringe, cry, cuddle, dab, dance, facepalm, feed, flower, 
fly, gabriel, glomp, grin, happy, hate, handhold, highfive, hug, icecream, kick, kiss, laugh, lick, 
love, lurk, miyano, nervous, no, nom, nuzzle, panic, pat, pikachu, poke, pout, punch, rawr, 
run, sagiri, shrug, sip, slap, sleepy, smug, stare, sword, tease, teleport, think, throw, 
thumbs, tickle, triggered, wag, wave, wedding, wink, yes, zerotwo

Returns : GIF URL
'''
my_weeby.get_gif().gif(type="baka")
```

## Generator Method
```python
import weeby

my_weeby = weeby.Weeby('your_weebyAPI_token_goes_here')

# One Image
'''
Types Available: 3000years, airpods, amiajoke, bad, beautiful,
berniemittens, bobross, challenger, delet, dexter, fear, garbage, heman, jokeoverhead, painting, patrick, photograph, picture, respect, sacred, thumbs, tobecontinued, truth, wanted, wedontdothathere, whodidthis, worthless, leonardopointing, jojoshock, hot, soraselfie, helivesinyou, stonks, mycollectiongrows, tableflip, tattoo, leonardoglass, standingkitty, rickripswall, wynaut, berniefinancialsupport, vsaucecomputer, waitthatsillegal

Image type: .gif/.png/.jpg
Returns: Image Buffer
'''
buffer = my_weeby.generate().one_image(type="", url="")

# Two Images
'''
Types Available: batslap, bed, crush, cuddle, dwightscared, hug, nani, peterglasses, samepicture, ship, whowouldwin, expectreality, amogus

Image Type: .gif/.png/.jpg
Returns: Image Buffer
'''
buffer = my_weeby.generate().two_image(type="", url1="", url2="")

# Text
'''
Types Available: belikebill, clyde, hollywoodstar
Returns: Image Buffer
'''
buffer = my_weeby.generate().text(type="", text="")

# Two Text
'''
Types Available: drakeposting, spiderman, twobuttons, tuxedopooh, icarly
Returns: Image Buffer
'''
buffer = my_weeby.generate().two_text(type="", text1="", text2="")

# Image & Text
'''
Types Avilable: achievement, bartchalkboard, changemymind, lisapresentation, jimwhiteboard

Returns: Image Buffer
'''
buffer = my_weeby.generate().image_text(type="", url="", text="")

# Eject
'''
url: link to the image -> .gif/.png/.jpg
text: name/username of the user
outcome: imposter/notimposter/ejected

Returns: Image Buffer
'''
buffer = my_weeby.generate().eject(url="", text="", outcome="")

# Friendship
'''
url1: link to first image -> .gif/.png/.jpg
url2: link to second image -> .gif/.png/.jpg
text1: name of first user
text2: name of second user

Returns: Image Buffer
'''
buffer = my_weeby.generate().friendship(url1="", url2="", text1="", text2="")

# Demotivational
'''
url: link to image -> .gif/.png/.jpg
title: title -> str
text: text -> str

Returns: Image Buffer
'''
buffer = my_weeby.generate().demotivational(url="", title="", text="")

# RIP
'''
url: link to image -> .gif/.png/.jpg
name: name of the user
message: text to display

Returns: Image Buffer
'''
buffer = my_weeby.generate().rip(url="", name="", message="")

# Tweet
'''
url: link to image -> /gif/.png/.jpg
name: name of the user
text: text to display

Returns: Image Buffer
'''
buffer = my_weeby.generate().tweet(url="", name="", text="")

# Tweet Fetch
'''
name: name of the user
text: text to display

Returns: Image Buffer
'''
buffer = my_weeby.generate().tweet_fetch(name="", text="")

# Triggered
'''
url: link to image -> .gif/.png/.jpg
tint: bool -> True/False

Returns: Image Buffer (gif)
'''
buffer = my_weeby.generate().triggered(url="", tint=True)

# Currency
'''
type: type of currency | dollar, euro, pound, yen
amount: amount -> int

Returns: Image Buffer
'''
buffer = my_weeby.generate().currency(type="", amount=10)

# Color
'''
hex: hex code of color without the '#'

Returns: Image Buffer
'''
buffer = my_weeby.generate().color(hex="")

# This is Spotify
'''
url: link to image -> .gif/.png/.jpg
hex: hex code of color without the '#'
text: text to display

Returns: Image Buffer
'''
buffer = my_weeby.generate().spotify(url="", hex="", text="")

# Spotify Now Playing
'''
url: link to image -> .gif/.png/.jpg
title: title of song 
artist: artist name
album: album name

Returns: Image Buffer
'''
buffer = my_weeby.generate().spotifynp(url="", title="", artist="", album="")
```

## Ending Note

- Consider leaving a ⭐ if you found this library helpful.
- Follow me ***[here](https://github.com/asheeeshh)***
- Contributions to the project are most welcome!
- Feel free to fork this repo and contribute.
- Thank You!

