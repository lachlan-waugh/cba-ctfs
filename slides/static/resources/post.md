# Example
> There's a couple different ways to send requests to example

&nbsp;

## directly
```python
import requests, urllib3, re

cert  = ('/path/to/cert.pem', '/path/to/cert.key')

# Create the post
page = requests.post(
	"https://login.example.com",
	data = {"username": "melon", "password": "Hunter2"},
	certs=cert
)

# you could extract the session cookie like so!
cookie = re.search(r"session=(.+?);", page.headers['Set-Cookie']).group(1)
print(cookie)

# now we can use that cookie, and send it to another page maybe?
page = requests.get("https://example.com/view/", certs=cert, cookies = { 'session': cookie })
print(page.text)
```

&nbsp;

## Proxying through BurpSuite
* This has the benefit of allowing you to use BurpSuite to
	* intercept the requests
	* view the history of your requests

```python
import requests, urllib3, re

# helpful, as it ignores the annoying HTTPS error message
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

proxy = { "https": "http://127.0.0.1:8080", "http" : "http://127.0.0.1:8080" }

page = requests.post("https://login.example.com",
	proxies = proxy,
	verify = False, # IMPORTANT: otherwise you'll get errors due to BurpSuites self-signed cert
	data = {"username": "melon", "password": "Hunter2"}
)

# you could extract the session cookie like so!
cookie = re.search(r"session=(.+?);", page.headers['Set-Cookie']).group(1)
print(cookie)

# now we can use that cookie, and send it to another page maybe?
page = requests.get(
	"https://example.com/view/",
	proxies = proxy, 
	verify = False,
	cookies = { 'session': cookie }
)
print(page.text)
```

&nbsp;

## request.session
* Using a requests session allows you to maintain a persistent session
* You won't need to explicitly include your credentials with every request
* This would also work with the certs, just use `s.certs = (...)` from above

```python
import requests, urllib3, re

# helpful, as it ignores the annoying HTTPS error message
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

s = requests.session()
s.proxies = { "https": "http://127.0.0.1:8080", "http" : "http://127.0.0.1:8080" }
s.verify = False

page = s.post("https://login.example.com", data = {"username": "melon", "password": "Hunter2"})

# you could extract the session cookie like so!
cookie = re.search(r"session=(.+?);", page.headers['Set-Cookie']).group(1)
print(cookie)

# now we can use that cookie, and send it to another page maybe?
page = s.get("https://example.com/view/", cookies = { 'session': cookie })
print(page.text)
```
