# weeby.py
API Wrapper in Python for WeebyAPI

<h2>JSON RESPONSES</h2>

```python
import weeby

my_weeby = weeby.Weeby(token="")


my_weeby.get_json_response().random(type="") #Returns Random Response -> type (8ball, belikebill, dadjoke, geography, joke, roast)

my_weeby.get_json_response().animal_image(type="") #Returns Random Animal Image Links -> type (bird, bunny, cat, dog, fox, goose, kangaroo, koala, lizard, panda)

my_weeby.get_json_response().meme(type="") #Returns Random Meme -> type (meme, memes, wholesome, dank)

my_weeby.get_json_response().word(type="") #Returns Random Word or List of Words -> type (random, halloween, christmas, list)

my_weeby.get_json_response().lyrics(track="") #Returns Lyrics -> track = track name with or without artist name

my_weeby.get_json_response().stats() #Returns WeebyAPI Stats
```
