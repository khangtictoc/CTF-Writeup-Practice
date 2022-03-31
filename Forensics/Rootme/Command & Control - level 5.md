# Command & Control - level 5 ✍

**Title**: Memory analysis

**Point**: 25 Points

**Level**: Medium

**Description:** Berthier, the malware seems to be manually maintened on the workstations. Therefore it’s likely that the hackers have found all of the computers’ passwords.
Since ACME’s computer fleet seems to be up to date, it’s probably only due to password weakness. John, the system administrator doesn’t believe you. Prove him wrong!

Find john password.

The uncompressed memory dump md5 hash is e3a902d4d44e0f7bd9cb29865e0a15de

## Solution:

Tool Used: `Volatility`, `John the Ripper`

Continued from **Command & Control - level 4**. Our task is find **John's password**.

This one is quite easy. Since we know the term "Security Accounts Manager" (SAM). [Reference link](https://www.top-password.com/blog/tag/windows-sam-registry-file/#:~:text=The%20SAM%20registry%20file%20is,to%20log%20into%20Windows%20accounts.)

The SAM registry file is located on your system at `C:\WINDOWS\system32\config`, but it is locked and cannot be moved or copied while Windows is running. The main function of the Security Accounts Manager is holding onto the passwords used to log into Windows accounts

SAM stores password under **hash strings**. We can use some tools to crack if the password is weak enough.

First, show all hives in system. Use `hivelist`:

```
./volatility_2.6_lin64_standalone -f ch2.dmp --profile=Win7SP0x86 hivelist
```

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/160874709-15f28675-5b8e-4cdd-b62e-dce93245fb09.png" > </p>

Then dump **SAM file** to find hash password. Use `hashdump` with `-y` option points to virtual address of  `\REGISTRY\MACHINE\SYSTEM` and `-s` points to that of `\SystemRoot\System32\Config\SAM`. [View usages here](https://github.com/volatilityfoundation/volatility/wiki/Command-Reference#hashdump)

```
./volatility_2.6_lin64_standalone -f ch2.dmp --profile=Win7SP0x86 hashdump -y 0x8b21c008 -s 0x9aad6148 > ~/hashedPassword.txt
```

Redirect to a `hashedPassword.txt` file for further use. Take a quick glance in its content:

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/160875833-24b0e06a-7f36-4ca9-ba7b-d3b268aca31f.png" > </p>

> Have a deep look if you like ! [SAM file structure](https://www.yg.ht/blog/blog/archives/339/what-is-aad3b435b51404eeaad3b435b51404ee) / [LM and NT hash](http://www.adshotgyan.com/2012/02/lm-hash-and-nt-hash.html) 

We just care of cracking **NT** hash. Cracking **LM** won't give valid result (this's just for backward compatibility). I use built-in tool `john` (or you can use `johnny`) to crack this hash string, use default `rockyou.txt` wordlist which is available in **Kali Linux**.

```
cp /usr/share/wordlists/rockyou.txt.gz ~ && gzip -d ~/rockyou.txt.gz
```

Just for convenient using :)) -> Then use this wordlist with `john` to crack this "mess" stored in `hashedPassword.txt`:

```
john --wordlist=~/rockyou.txt --format=NT ~/hashedPassword.tx
```

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/160878375-5ac4e8fb-6564-46a1-ab1a-1a8e0f27f61d.png" > </p>

Wonderful !!! `passw0rd` is password for `(John Doe)`

Flag: **passw0rd**



