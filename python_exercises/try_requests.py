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



