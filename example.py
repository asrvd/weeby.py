import weeby

my_weeby = weeby.Weeby('your_token')

print(my_weeby.get_json_response().random("roast")['response'])