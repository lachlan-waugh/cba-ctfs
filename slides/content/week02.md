---
title: "Week02"
layout: "bundle"
outputs: ["Reveal"]
---

## We'll get started at ??:05

---

{{< slide class="center" >}}
# Week02
### T12A COMP1234 

---

## Client-side injection
* HTML Injection
* XSS
* CSRF

---

## HTML injection
{{% section %}}
### HTML injection
* Browsers just render the DOM
* How would it know if tags are user-supplied or server-supplied
* what if our input was just `<s>`?

---

### Know your tags
* Some are paired `<div></div>`
* Some aren't `<img src=.../>`
* what goes in here? `<script>...</script>`

{{% /section %}}

---

## XSS
{{% section %}}
### Cross-site scripting
* another 'mixing of data and control' issue
* Tricking a **browser** into executing your code
    * javascript, php, py-script?
    * we'll just be looking at javascript lol

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

## CSRF
{{% section %}}

### What is it?
* Cross-site request forgery
* Trick a user into performing an unintended action
    * e.g. make them authorize a bank transaction
    * e.g. make them change their email/password
* *kinda similar to SSRF*

---

###

```
<form method="POST" >
```

---

### Demo!

{{% /section %}}


---

## Thank you
We're done!