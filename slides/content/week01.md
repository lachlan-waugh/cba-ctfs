---
title: "ctfs && recon"
layout: "bundle"
outputs: ["Reveal"]
---

## We'll get started at 13:05

---

{{< slide class="center" >}}
# week01
## what is a ctf && recon 

---

## disclaimer
* a lot of the tools and techniques discussed in these sessions could be used against real websites and infrastructure
* don't do that
* dont be mean

---

## acknowledgement of country
* We begin by acknowledging the Traditional Custodians of the land on which we meet, and pay our respects to their Elders past and present. We extend that arespect to Aboriginal and Torres Strait Islander peoples here today.

---

{{% section %}}

## what will we cover this session
* what is a CTF
    * what types of vulnerabilities are there

* reconnaissance
    * what is it/when do you use it
    * passive
    * active

---

## what are we going to cover later
* 01 what is a ctf/recon
* 02 frontend web exploits
* 03 backend web exploits
* 04 digital forensics
* 05 network forensics
* 06 binary exploitation
* 07 further binary exploitation
* 08 privilege escalation

---

## what is a ctf
> essentially a "hacking" competition

* exploiting some vulnerability in an application/ server/ etc to steal a flag (which is intended to be "confidential information"), e.g., 
    * breaking into a database and stealing passwords
    * tricking banking software to give you money
    * making the server think you're an administrator

---

## what types of ctfs are there
* real-world "pentester-training" ones
    * e.g. HackTheBox, TryHackMe
    * formulaic: run tools, find a CVE PoC, etc
* fun ones (more of a "game")
    * e.g. [PicoCTF](https://picoctf.org/), [DUCTF](https://github.com/DownUnderCTF/Challenges_2022_Public), [DefCon CTF](#TODO), [Google CTF](https://capturetheflag.withgoogle.com/)
    * build your own exploit, etc

> im not biased I swear

{{% /section %}}

---

{{% section %}}

## what type of vulnerabilities might you exploit?

---

### injection vulnerabilities
> TLDR: tricking a program to execute our user supplied input as code

---

## is this code vulnerable??
```C
#include <stdio.h>

int main(void) {
    char buffer[64];
    gets(buffer);
    return 0;
}
```

---

## is this code vulnerable??
```C
#include <stdio.h>

int main(void) {
    char buffer[16];
    gets(buffer);
    return 0;
}
```

> yes

`AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x62\x92\x04\x08`

---

## why?
```
            0x18  [  ARGS  ] <- Parameters
            0x14  [  EIP   ] <- Stored Return Pointer
            0x10  [  EBP   ] <- Stored Frame Pointer
            0x0C  [  AAAA  ] <- these are local vars
            0x08  [  AAAA  ]
            0x04  [  AAAA  ]
            0x00  [  AAAA  ]
```

it's a buffer overflow, you write past the end of the array and overwrite variables stored in memory near it

---

## is this code vulnerable??
```python
from flask import Flask, request, render_template_string
app = Flask(__name__)

@app.route('/')
def home():
    template = "blah blah here's some content {}"
    data = request.args.get('data', ''))
    return render_template_string(template.format(data))

if __name__ == '__main__':
    app.run()
```

---

## is this code vulnerable??
```python
from flask import Flask, request, render_template_string
app = Flask(__name__)

@app.route('/')
def home():
    template = "blah blah here's some content {}"
    data = request.args.get('data', ''))
    return render_template_string(template.format(data))

if __name__ == '__main__':
    app.run()
```

> yes (its a serverside template injection)

{{ namespace.\_\_init\_\_.\_\_globals\_\_.os.popen('id') }}

---

### why?
> unsantisied user input

* it's dangerous when data is treated as control
    * e.g. the username can change the flow of the program
* tricking a program to execute code instead of reading or writing data

---

### a side note
* ctfs are hard: they aren't intuitive and they take a long time
* at some point, everyone was where you are now
* there's more resources out there (youtube videos, ctf/cve writeups) than you could read/watch in 10 lifetimes (hopefully that's not too daunting)

---

### resources
* ctfs
    * [ringzer0](https://ringzer0ctf.com/challenges), [juice-shop](https://owasp.org/www-project-juice-shop/), [picoctf](https://picoctf.org/index.html#picogym), [pheonix](https://exploit.education/phoenix/) 
* youtube videos
    * [john hammond](https://www.youtube.com/@_JohnHammond/videos), [liveoverflow](https://www.youtube.com/@LiveOverflow), [ippsec](https://www.youtube.com/@ippsec/videos)
* good series
    * [intro to binary exploitation](https://www.youtube.com/watch?v=iyAyN3GFM7A&list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN)

> most of the resources will be on my website [waugh.zip/cba-ctfs](https://waugh.zip/cba-ctfs)

{{% /section %}}

---

{{% section %}}

## reconnaissance

---

## what is recon
* these should always be your first steps
* essentially everything that isn't exploitation
    * looking at a website
    * reading the html source
    * giving a application input it doesn't expect (e.g., code, a really big input, a file type it doesn't expect)

---

## why is it important?
* asymmetry of attack and defence
    * defenders need to defend everything
    * attackers only need a single vulnerability
* important to expand your attack surface
* understand what the application does, before trying to exploit it

---

## passive recon
* finding web content
* information leaked in local files (e.g. robots.txt, sitemap.xml, javascript files, html comments)
* surely nobody would expose information in [HTML](https://www.malwarebytes.com/blog/news/2022/02/journalist-wont-be-indicted-for-hacking-for-viewing-a-state-websites-html)

---

## demo
> website.com (don't try it at home)

---

## active recon
* grabbing a big list of words, and seeing if any of them resolve:
    * as a subdomain: <word>.example.com
    * as a subdirectory: example.com/<word>
    * as a port: example.com:<word> 
* also [linpeas](https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS), [sqlmap](https://github.com/sqlmapproject/sqlmap), [metasploit](https://www.metasploit.com/)

---

## subdomain/subdirectory/port
* subdirectory: another part of the same site
    * gobuster, dirbuster, etc
* subdomain: another server
    * also gobuster, dirbuster
* port: another application
    * nmap
 
> [seclists](https://github.com/danielmiessler/SecLists) and [wordlists](https://github.com/kkrypt0nn/wordlists) can be helpful wordlists

---

## demo 

---

## bruteforcing considerations
* very noisy
    * bruteforcing over dns vs http
    * you might be blocked
* not everything is a bruteforcing challenge
    * in a real engagement they'd get angry

{{% /section %}}

---

### practice
> do some of the challenges on picoctf web exploitation [here](https://play.picoctf.org/practice/challenge/173?category=1&page=1)

---

## next week
> frontend web exploitation (XSS, CSRF, Clickjacking)

---

## thank you
> we're done! any questions?
