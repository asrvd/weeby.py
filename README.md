# weeby.py
API Wrapper in Python for WeebyAPI\
Checkout WeebyAPI : https://weebyapi.xyz \
Get your API token here : https://weebyapi.xyz/discord \
Discord Bot using WeebyAPI : https://github.com/asheeeshh/Kanna-Chan

## Import Statement
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

## Generator Method Coming Soon ♥
