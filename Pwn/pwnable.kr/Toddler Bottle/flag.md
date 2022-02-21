# Flag

**Description**: 
Papa brought me a packed present! let's open it.

Download : http://pwnable.kr/bin/flag

This is reversing task. all you need is binary

### Solution:

This file has been packed, it means we couldn't debug as the symbolics, tables were removed. Use **'PeID'** or **'DIE(Detect it Easy)'** tool to discover that file was packed with **UPX**.

Keyword reference: [What's is stripped binary files](https://en.wikipedia.org/wiki/Strip_(Unix))

Use IDA to view reversed source code and get the flag

Flag: **UPX...? sounds like a delivery service :)**
