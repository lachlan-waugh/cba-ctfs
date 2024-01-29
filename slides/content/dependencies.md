---
title: "dependencies"
layout: "bundle"
outputs: ["Reveal"]
---

{{< slide class="center" >}}
## supply chain attacks
### lunch & learn

---

### overview
* intentionally malicious
    * dependency confusion
* unintentionally malicious

---

### OSS
<img src="/assets/img/dependencies/oss.png" width="400px"/>

---

dependencies

npm config set <registry url>
npm install --registry=XYZ
pip install -r --extra-index-url <registry url> requirements.txt

---

{{% section %}}

### intentionally malicious
peacenotwar

---

### dependency confusion


[read more](https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610)

---

### typosquatting


{{% /section %}}

---

{{% section %}}

### unintentionally malicious
e.g. from compromise

---

nodeipc

{{% /section %}}

---

{{% section %}}

{{% /section %}}

---

## Thank you
We're done!
