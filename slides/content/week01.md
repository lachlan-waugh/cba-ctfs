---
title: "ctfs && recon"
layout: "bundle"
outputs: ["Reveal"]
---

## We'll get started at ??:05

---

{{< slide class="center" >}}
# week01
## What is a ctf && recon 

---

{{% section %}}

## what is a ctf

---

## what are we going to cover
* recon

---

### injection vulnerabilities 
> how the following simple code could be used to get full server takeover

```C
#include <stdio.h>

int main(void) {
    char buffer[64];
    gets(buffer);
}
```
 
---

{{% /section %}}

---

{{% section %}}

## reconnaisance
* asymmetry of attack and defense

---

## passive recon

---

## demo

---

## active recon

---

## subdomain/subdirectory
* bruteforcing over dns vs http

---

## port enumeration

---

## considerations
* very noisy
* might be blocked

---

## demo

{{% /section %}}

---

## thank you
we're done!
