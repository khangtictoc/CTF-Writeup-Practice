# More Cookies ❓
**Tags:** Web Exploitation<br>
**Point:** 90  <br>
**Description:** I forgot Cookies can Be modified Client-side, so now I decided to encrypt them! http://mercury.picoctf.net:25992/

Hint:
- https://en.wikipedia.org/wiki/Homomorphic_encryption
- The search endpoint is only helpful for telling you if you are admin or not, you won't be able to guess the flag name

## Write-up: 📝

- The website requires you to access by **admin** privilege.

We notice that the cookie is `auth_name` contains base64-encoded string. Decrypt it, we still get a string that looks like a key.

- Something relates to Homomorphic Encryption

Refer to [freecodecamp.org](https://www.freecodecamp.org/news/introduction-to-homomorphic-encryption/):


> **Homomorphic Encryption** is a form of encryption that allows users to perform binary operations on encrypted data without ever decrypting the data.

The encrypted key we send to server is used for authenticate user with binary value *is admin not not* by Homomorphic mechanism

- Another hint "CBC" also tell us in the description from the uppercase characters. This means this key is vulnerable to **bitflip** in **CBC mode**.

This vulnerability allows us to modify the content of the ciphertext , and the responding position also be changed. 

<p align="center"><img src="/Web/picoCTF/More_Cookies/img/cbc-bitflip.png"></p>

So the keypoint is that we could bruteforce all the positions of the key that represents, for example, some kind of value `admin = 0` exists, then we can change it to `1`.

Our original key before decrypting only contains [a-z], [a-Z], [0-9] characters, we will go through all of this for each position. The changes will reflects to the string after the server evaluate **admin or not** with its key. Since we control the cookie, we control the "decrypted" string.

Workflow:

<p align="center"><img src="/Web/picoCTF/More_Cookies/img/workflow.png"></p>

I have already the [Python script ](/Web/picoCTF/More_Cookies/solve.py) to do the bruteforce, each step performs:

base64-decode key  &rarr; XOR with value(bitflip)  &rarr;base64-encode  &rarr; Send cookie to server  &rarr; Check if flag is returned?


#### The Flag (for reference): ✔️
```
picoCTF{cO0ki3s_yum_2d20020d}
```
