# Who are you?❓
**Tags:** Web Exploitation<br>
**Point:** 100  <br>
**Description:** Let me in. Let me iiiiiiinnnnnnnnnnnnnnnnnnnn http://mercury.picoctf.net:39114/ <br>
Hint:
- It ain't much, but it's an RFC https://tools.ietf.org/html/rfc2616

## Write-up: 📝

As we login, we can see an alert: `Only people who use the official PicoBrowser are allowed on this site!`

It requires the browser we're using is "PicoBrowser". So we use Burpsuite to intercept our request and modify UA header `User-Agent: PicoBrowser`. Then forward the request. Reference: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent

The warnings: `I don't trust users visiting from another site.`

As we're accessing this site from another site, it don't trust us. So we have a way to prove that we're visiting from its sites. We have **Referer** header which notifies server the page where user get in it from. Add **Referer** header `Referer: http://mercury.picoctf.net:39114/` . Reference: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer

The warnings: `Sorry, this site only worked in 2018.`

This time, we have to get a "time machine" to get back to 2018. We can use **Date** header to specify the year **2018** to bypass. Add **Date** header: `Date: Wed, 21 Oct 2018 07:28:00 GMT`. Reference: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Date

The warning: `I don't trust users who can be tracked.`

We avoid tracking by using **DNT** header. Add **DNT** header and set to 1 `DNT:1`. Reference: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/DNT

The warning: `This website is only for people from Sweden.`

We could specify the originating IP address of a client connecting to a web server by **X-Forwarded-For** header. Add this header with the IPs in Sweden that we searched ([some samples](https://www.nirsoft.net/countryip/se.html). Reference: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For

The warning: `You're in Sweden but you don't speak Swedish?`

We use **Accept-Language** header to indicate the languages user wants. Change this header `Accept-Language: sv`. We can look up language code abbreviation in [here](https://www.science.co.il/language/Locale-codes.php). Reference: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language

Payload (all needed headers):
```
User-Agent: PicoBrowser
Referer: http://mercury.picoctf.net:39114/
Date: Wed, 21 Oct 2018 07:28:00 GMT
DNT:1
X-Forwarded-For: 31.15.32.0
Accept-Language: sv
```

#### The Flag (for reference): ✔️
```
picoCTF{http_h34d3rs_v3ry_c0Ol_much_w0w_20ace0e4}
```
