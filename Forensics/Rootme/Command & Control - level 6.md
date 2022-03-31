# Command & Control - level 6 ✍

**Title**: Reverse engineering

**Point**: 50 Points

**Level**: Medium

**Description:** Berthier, before blocking any of the malware’s traffic on our firewalls, we need to make sure we found all its C&C. This will let us know if there are other infected hosts on our network and be certain we’ve locked the attackers out. That’s it Berthier, we’re almost there, reverse this malware!

The validation password is a fully qualified domain name : hote.domaine.tld

The uncompressed memory dump md5 hash is e3a902d4d44e0f7bd9cb29865e0a15de<br>
NB : This challenge require the clearance of the level 3.

## Solution:

Tool Used: `Volatility`, `Hybrid Analysis`

Continued from **Command & Control - level 5**. Our task is find **C&C domain**.

Create a `BckDoorRev` folder for dumped files, dump the whole malignant process with PID `2772` 

```
mkdir BckDoorRev && ./volatility_2.6_lin64_standalone -f ch2.dmp --profile=Win7SP0x86 procdump -p 2772 --dump-dir=BckDoorRev
```

Look like it's a `.exe` file. Just examine the file for sure:

```bash
┌──(virus㉿kali)-[~/Downloads/volatility_2.6_lin64_standalone]
└─$ cd BckDoorRev && file executable.2772.exe
executable.2772.exe: PE32 executable (GUI) Intel 80386 (stripped to external PDB), for MS Windows
```

OK. It's totally a execute file for **Window OS**. Now we try to reverse it. This is not a `Reverse Engineer` topic so I will make [Hybrid Analysis](https://www.hybrid-analysis.com/) analyse for us.

Show all "Network Behavior" in "Incident Response"

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160988180-2da4f907-4c7a-485a-930c-422f652c8b10.png"></p>

This is all the DNS Request to when connecting to a external computer. Submit each domain:

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160988637-991c5ee5-ec21-423e-8904-f3221937d52c.png"></p>

The correct one is `th1sis.l1k3aK3y.org`

Flag: **th1sis.l1k3aK3y.org**



