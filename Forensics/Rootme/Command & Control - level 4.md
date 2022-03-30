# Command & Control - level 4 ✍

**Title**: Malware analysis

**Point**: 35 Points

**Level**: Medium

**Description:** Berthier, thanks to this new information about the processes running on the workstation, it’s clear that this malware is used to exfiltrate data. Find out the ip of the internal server targeted by the hackers!

The validation flag should have this format : IP:PORT

The uncompressed memory dump md5 hash is e3a902d4d44e0f7bd9cb29865e0a15de

## Solution:

Tool Used: `Volatility`

Continued from **Command & Control - level 3**. We've known that there's a running malicious process with PID `2772` - it's a backdoor. Now let's take a deep look into this process and see its connection' info. Use `netscan`:

```
/volatility_2.6_lin64_standalone -f ch2.dmp --profile=Win7SP0x86 netscan | grep 2772
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160743498-72c4c94a-283d-4c80-b883-872c2a541ae0.png"> </p>

This is not the port and IP address we're searching. Maybe the reason is attacker had killed the process prior to dumping files. Check **CONSOLE_INFORMATION**, use `consoles`:

```
 ./volatility_2.6_lin64_standalone -f ch2.dmp --profile=Win7SP0x86 consoles 
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160744691-f54cb3e2-caff-45f0-ae83-b3fd94bedcec.png"> </p>

There're some application need to be understood:
- tcprelay.exe - TCP connection forwarder
- consolehost.exe - needed to run to allow Command Prompt to work with Windows Explorer
- whoami.exe - Display user.

So we can guess attacker opened a shell `cmd.exe` , then used `tcprelay.exe` for TCP port forwarder and `whoami.exe` for checking his user's role. But then he had closed the connection session. Basicly, commands input into `cmd.exe` are processed by `conhost.exe`, so if we're lucky , we could get more information from dumping `conhost.exe` 's memory.

Create new directory for storing **dumped files** and use `memdump` and dump the process `2168`:

```bash
 mkdir testResult && ./volatility_2.6_lin64_standalone -f ch2.dmp --profile=Win7SP0x86 memdump -p 2772 -D testResult
```
Then go to `testResult` dir and read all information relating to `tcprelay.exe` command:

```bash
strings 2168.dmp | grep tcpreplay
```

<p align="center"><img src="https://user-images.githubusercontent.com/48288606/160811558-f814eaa7-ee28-4892-a7fd-5054bbc2a638.png"> </p>

We can see the connection has been built by hacker and then closed.



FLag: **192.168.0.22:3389**
