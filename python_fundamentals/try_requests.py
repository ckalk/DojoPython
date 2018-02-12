''' Here's what I did to install requests... The virtual env I had create earlier is named pyproj.
Let's say you have a project in a directory called myproject. To set up virtualenv for that project:
$ source pyproj/bin/activate
I now see a (pyproj) appear at the beginning of myproject terminal prompt indicating that you are working inside the virtualenv. Then I installed requests in the virtualenv
$ pip install requests '''

import requests
r = requests.get('https://api.github.com/events')
print (r.text)

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)

payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)

# from shannon
# Optional Assignment: The Requests Library 
# Build a simple program that makes use of the requests module.
import requests
import json # so we can interpret the response
# get some info about Luke Skywalker from the starwars api
r = requests.get('https://swapi.co/api/people?search=luke')
# save our response
data = r.json()
# viewing expected output (from swapi documentation) tells us the data we want is in the 'results' key, at the [0] index position, so let's narrow our data down and make a new dict
data_dict = data['results'][0]
# loop through the data to display details in a formatted way
for key, item in data_dict.items():
    if isinstance(item, list) is False:  # for now let's not worry with arrays of url's for subsequent searches (i.e. list of films character has been in)
        print "{}: {}".format(key, item)
#     # print "Weight: {}".format(item['mass'])
#     print "Height: {}".format(item['height'])
