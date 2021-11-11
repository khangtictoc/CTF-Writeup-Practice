# Where are the robots ❓
**Tags:** Web Exploitation<br>
**Point:** 100<br>
**Description:** AUTHOR: ZARATEC/DANNY<br>
Can you find the robots? https://jupiter.challenges.picoctf.org/problem/36474/ (link) or http://jupiter.challenges.picoctf.org:36474

## Write-up: 📝
Robots.txt is a text file webmasters create to instruct web robots (typically search engine robots) how to crawl pages on their website. The robots are exactly "What part of the website could tell you where the creator doesn't want you to look?" mentioned in the hint. 
### Solution: 💯
```
1. You should read carefully about "What is robots.txt" at the following link "https://moz.com/learn/seo/robotstxt"
2. Access current website and add "robots.txt/" at the end of URL
3. There you see a website with a content: 
User-agent: *
Disallow: /477ce.html
4. Go into URL above by adding (/477ce.html) at the end of given challenge URL (see Step 2)
5. You will see the flag here.
```

#### The Flag (for reference): ✔️
```
picoCTF{ca1cu1at1ng_Mach1n3s_477ce}
```
