---
title: "Week02"
layout: "bundle"
outputs: ["Reveal"]
---

## We'll get started at 13:05

---

{{< slide class="center" >}}
# week02
### client-side exploitation

---

## disclaimer
* many of the tools and techniques discussed in these sessions could be used against real websites/applications
* don't do that

---

## acknowledgement of country
* We begin by acknowledging the Traditional Custodians of the land on which we meet, and pay our respects to their Elders past and present. We extend that arespect to Aboriginal and Torres Strait Islander peoples here today.

---

## Client-side injection
* HTML Injection
* XSS
* CSRF\
* Clickjacking

---

{{% section %}}

### HTML injection
* Browsers just render the DOM
* How would it know if tags are user-supplied or server-supplied
* what if our input was just `<s>`?

---

### why is this dangerous?
most tags aren't really concerning (`<b>`, `<h1>`), but some can be
* `<form>`
* `<iframe>`
* `<script>`
* `<img>`

---

### Know your tags
* Some are paired `<div></div>`
* Some aren't `<img src=.../>`

> just google what they do/how to use them

{{% /section %}}

---

{{% section %}}

### XSS (cross-site scripting)
* another 'mixing of data and control' issue
    * your browser only receives a single stream of data
    * the content of the stream determines if it's control or data
* Tricking a **browser** into executing your code

---

### Reflected XSS
* Payload is part of user input
    * e.g. a search query, cookie, header, etc 
    * anything insecurely rendered on the page

> [`www.example.com/database?q=<script>alert(1)</script>`]()

---

### Stored XSS
* Payload is stored in some database
    * Anybody who visits a certain page will view it
    * e.g. blog posts, twitter (lol)
* generally worse, but more easily detected

---

### DOM-based XSS
* Similar to the others, but the vulnerability comes from modifying the DOM

```html
<script>
const pos=document.URL.indexOf("context=")+8;
document.write(document.URL.substring(pos,document.URL.length));
</script>
```

---

### Demo!

---

### XSS isn't just `<script>` tags
```javascript
// event-handlers
<img src=x onerror=alert(1)/>

// injecting into javascript code
const a = '<user_input>'

// and much more
```

> it's any time you get user supplied input in a javascript context

---

### Some good resources
* [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection)
* [OWASP Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XSS_Filter_Evasion_Cheat_Sheet.html)
* [HackTricks](https://book.hacktricks.xyz/pentesting-web/xss-cross-site-scripting)
* [PortSwigger](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)

{{% /section %}}

---

{{% section %}}

## CSRF
cross-site request forgery

---

### What is it?
* trick a user into performing an unintended action
    * make them authorize a bank transaction
    * make them change their email/password
    * (if they're admin) probably even worse stuff

---

### examples

```html
<a href="http://bank.com/send?to=hacker&amount=10000">Click me!</a>

<img src="http://bank.com/send?to=hacker&amount=1000">
```

---

### Demo!

{{% /section %}}

---

{{% section %}}

## click-jacking

---

### what is it?
A fake form sitting on top of/below a real form

* if you try to interact with the fake form, you'll accidentally interact with the real one. 

---

### where could it come from?
* This could be either local, or external
    * local: same form switch confirm/cancel buttons
    * external: an invisible iframe with a higher z-index

---

### Demo

{{% /section %}}

---

### Practice
* [portswigger labs](https://portswigger.net/web-security/all-labs)
* [ringerzer0](https://ringzer0ctf.com/challenges)
* [juice shop](https://owasp.org/www-project-juice-shop/)

---

### next week
backend vulnerability
* sql injection 
* command injection
* serverside template injection
* file uploads
* serverside request forgery (SSRF)

---

## thanks!
that's all :)
