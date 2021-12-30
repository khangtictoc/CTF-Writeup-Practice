# Some Assembly Required 1 ❓
**Tags:** Web Exploitation<br>
**Point:** 70  <br>
**Description:** http://mercury.picoctf.net:1896/index.html <br>
Hint: (None)


## Write-up: 📝

- A checking-flag program. There is an input box to examine the flag. Try to view the source code.

![image](https://user-images.githubusercontent.com/48288606/147685188-edf3e89c-cab8-4d2d-9088-03f6bf11175a.png)

- The button is applied **on click** event and the site import an external javascript code for this. Now jumping to that file 

![image](https://user-images.githubusercontent.com/48288606/147685535-9dc3e327-eca0-44b0-be75-1f0eda102f6b.png)

- Just a java-obfuscated code. Let's try to make it "prettier", use [this](http://jsnice.org/). <br>
Code:

```javascript
'use strict';
const _0x402c = ["value", "2wfTpTR", "instantiate", "275341bEPcme", "innerHTML", "1195047NznhZg", "1qfevql", "input", "1699808QuoWhA", "Correct!", "check_flag", "Incorrect!", "./JIFxzHyW8W", "23SMpAuA", "802698XOMSrr", "charCodeAt", "474547vVoGDO", "getElementById", "instance", "copy_char", "43591XxcWUl", "504454llVtzW", "arrayBuffer", "2NIQmVj", "result"];
const _0x4e0e = function(url, whensCollection) {
  /** @type {number} */
  url = url - 470;
  let _0x402c6f = _0x402c[url];
  return _0x402c6f;
};
(function(data, oldPassword) {
  const toMonths = _0x4e0e;
  for (; !![];) {
    try {
      const userPsd = -parseInt(toMonths(491)) + parseInt(toMonths(493)) + -parseInt(toMonths(475)) * -parseInt(toMonths(473)) + -parseInt(toMonths(482)) * -parseInt(toMonths(483)) + -parseInt(toMonths(478)) * parseInt(toMonths(480)) + parseInt(toMonths(472)) * parseInt(toMonths(490)) + -parseInt(toMonths(485));
      if (userPsd === oldPassword) {
        break;
      } else {
        data["push"](data["shift"]());
      }
    } catch (_0x41d31a) {
      data["push"](data["shift"]());
    }
  }
})(_0x402c, 627907);
let exports;
(async() => {
  const findMiddlePosition = _0x4e0e;
  let leftBranch = await fetch(findMiddlePosition(489));
  let rightBranch = await WebAssembly[findMiddlePosition(479)](await leftBranch[findMiddlePosition(474)]());
  let module = rightBranch[findMiddlePosition(470)];
  exports = module["exports"];
})();
/**
 * @return {undefined}
 */
function onButtonPress() {
  const navigatePop = _0x4e0e;
  let params = document["getElementById"](navigatePop(484))[navigatePop(477)];
  for (let i = 0; i < params["length"]; i++) {
    exports[navigatePop(471)](params[navigatePop(492)](i), i);
  }
  exports["copy_char"](0, params["length"]);
  if (exports[navigatePop(487)]() == 1) {
    document[navigatePop(494)](navigatePop(476))[navigatePop(481)] = navigatePop(486);
  } else {
    document[navigatePop(494)](navigatePop(476))[navigatePop(481)] = navigatePop(488);
  }
}
;
```
Examine **exports** through **async()** function. We get the values of **findMiddlePosition** with each index through debug:

```javascript
(async() => {
  const findMiddlePosition = _0x4e0e;
  let leftBranch = await fetch("./JIFxzHyW8W");
  let rightBranch = await WebAssembly["instantiate"](await leftBranch["arrayBuffer"]());
  let module = rightBranch["instance"];
  exports = module["exports"];
})();
```
So **onButtonPress** event will get each characters of user input and then send to web assembly script created by **async** function and our input will be checked by the function of **check_flag**. 

```
file JIFxzHyW8W                                
JIFxzHyW8W: WebAssembly (wasm) binary module version 0x1 (MVP)
```

```javascript
function onButtonPress() {
  const navigatePop = _0x4e0e;
  let params = document["getElementById"]("input")["value"];
  for (let i = 0; i < params["length"]; i++) {
    exports["copy_char"](params["charCodeAt"](i), i);
  }
  exports["copy_char"](0, params["length"]);
  if (exports["check_flag"]() == 1) {
    document["getElementById"]("result")["innerHTML"] = "Correct!";
  } else {
    document["getElementById"]("result")["innerHTML"] = "Incorrect!";
  }
}
;
```

Go to the path of web assembly at http://mercury.picoctf.net:1896/JIFxzHyW8W and download it <br>
`wget http://mercury.picoctf.net:1896/JIFxzHyW8W`
Read the file, as we see, it's not human-readable text. **We could see flag at the end of the file and submit the challenge.** If we're not sure about this, we use a tool to convert from **".wasm** file to **".wat"**, which is readable. Read document and set up as the following link: https://github.com/WebAssembly/wabt <br>
Try to reverse to pseudo code : `bin/wasm-decompile JIFxzHyW8W -o test.dcmp `
Dig into 2 function **check_flag** and **copy** to understand more:
```
data d_picoCTFa2843c6ba4157dc1bc052(offset: 1024) =
"picoCTF{a2843c6ba4157dc1bc052818a6242c3f}\00\00";
```
The actual flag is saved at offset 1024.
```
export function check_flag():int {
  var a:int = 0;
  var b:int = 1072;
  var c:int = 1024;
  var d:int = strcmp(c, b);
  var e:int = d;
  var f:int = a;
  var g:int = e != f;
  var h:int = -1;
  var i:int = g ^ h;
  var j:int = 1;
  var k:int = i & j;
  return k;
}

function copy(a:int, b:int) {
  var c:int = g_a;
  var d:int = 16;
  var e:int_ptr = c - d;
  e[3] = a;
  e[2] = b;
  var f:int = e[3];
  var g:byte_ptr = e[2];
  g[1072] = f;
}
```





#### The Flag (for reference): ✔️
```
picoCTF{a2843c6ba4157dc1bc052818a6242c3f}
```
