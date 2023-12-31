# Local Authority ❓

**Tags:** Web Exploitation

**Point:** 100 points

**Description:** 
Can you get the flag?<br>
Go to [this](http://saturn.picoctf.net:52194/) website and see what you can discover.

### Solution: 💯

Enter arbitrary **username** and **password**, then the page's directed to error one. Open "Developer Tool" -> Source -> secure.js 

```javascript

function checkPassword(username, password)
{
  if( username === 'admin' && password === 'strongPassword098765' )
  {
    return true;
  }
  else
  {
    return false;
  }
}
```
Username: **admin**

Password: **strongPassword098765**

#### The Flag (for reference): ✔️
```
picoCTF{j5_15_7r4n5p4r3n7_6309e949}
```
