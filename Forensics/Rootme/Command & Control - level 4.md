# Command & Control - level 4 ✍

**Title**: Malware analysis

**Point**: 35 Points

**Level**: Medium

**Description:** Berthier, thanks to this new information about the processes running on the workstation, it’s clear that this malware is used to exfiltrate data. Find out the ip of the internal server targeted by the hackers!

The validation flag should have this format : IP:PORT

The uncompressed memory dump md5 hash is e3a902d4d44e0f7bd9cb29865e0a15de

## Solution:

Tool Used: `Volatility`

Continued from **Command & Control - level 3**. We've known that there's a running malicious process with PID `2772` - it's a backdoor. Now let's take a deep look into this process and see its connection' info.

```
/volatility_2.6_lin64_standalone -f ch2.dmp --profile=Win7SP0x86 netscan | grep 2772
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160743498-72c4c94a-283d-4c80-b883-872c2a541ae0.png"> </p>

This is not the port and IP address we're searching. Maybe the reason is attacker had killed the process prior to dumping files. Check **CONSOLE_INFORMATION**:

```
 ./volatility_2.6_lin64_standalone -f ch2.dmp --profile=Win7SP0x86 consoles 
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160744691-f54cb3e2-caff-45f0-ae83-b3fd94bedcec.png"> </p>

There're some application need to be understood:
- tcprelay.exe . Create a tcp thread to connect to a remote 
- consolehost.exe 
- 



FLag: ****
