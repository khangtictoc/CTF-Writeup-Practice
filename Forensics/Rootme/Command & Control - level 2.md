# Command & Control - level 2 ✍

**Title**: Memory analysis

**Point**: 15 Points

**Level**: Easy

**Description:** Congratulations Berthier, thanks to your help the computer has been identified. You have requested a memory dump but before starting your analysis you wanted to take a look at the antivirus’ logs. Unfortunately, you forgot to write down the workstation’s hostname. But since you have its memory dump you should be able to get it back!

The validation flag is the workstation’s hostname.

The uncompressed memory dump md5 hash is e3a902d4d44e0f7bd9cb29865e0a15de

## Solution:

Tool Used: `Volatility`

You received a multi-layer compressed file.

Extract with **Bzip2**: `bzip2 -d ch2.tbz2`<br>
Extract with **POSIX tar archive**: `tar -xf ch2.tar`

Now we have a dumped file **ch2.dmp**. We can get computer's **hostname** throught `registry`. It usually store in this path `HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\ComputerName\ComputerName`

For example, in my computer:

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/160636282-a1f340c5-3ea0-4786-8ee6-aa4cbe08dfe1.png"></p>

First, dump the overview information to get `Profile` values:

```bash
./volatility_2.6_lin64_standalone -f ch2.dmp imageinfo
```

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/160637037-7eb1cb52-135a-4a81-b0e2-2c13b8aa189e.png"></p>


Use profile `Win7SP0x86` or any profile you like to examine and show all `hivelist`. 

```
./volatility_2.6_lin64_standalone -f ch2.dmp --profile=Win7SP0x86 hivelist
```

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/160641755-c2e2809b-4c06-4557-b1ea-4699222a4111.png"></p>

We need to dump the information at specific address (we're interested in `\REGISTRY\MACHINE\SYSTEM` at virtual address of `0x8b21c008`) in hivelist and extract the value. Use `-K` to specify the rest of the **KPCR address**: 

```
./volatility_2.6_lin64_standalone -f ch2.dmp --profile=Win7SP0x86 printkey -o 0x8b21c008  -K 'ControlSet001\Control\ComputerName\ComputerName'
```

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/160641123-c45d94ed-25fd-4839-b2eb-eb272be61fad.png"></p>


FLag: **WIN-ETSA91RKCFP**
