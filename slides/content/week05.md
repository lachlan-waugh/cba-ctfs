---
title: "05: forensics"
layout: "bundle"
outputs: ["Reveal"]
---

## We'll get started at 13:05

---

{{< slide class="center" >}}
# Digital Forensics & Incident Response
## Week05

---

## disclaimer
* many of the tools and techniques discussed in these sessions could be used against real websites/applications
* don't do that

---

## acknowledgement of country
* We begin by acknowledging the Traditional Custodians of the land on which we meet, and pay our respects to their Elders past and present. We extend that arespect to Aboriginal and Torres Strait Islander peoples here today.

---

{{% section %}}

## what will we cover this session
* hash cracking
* network packet analysis
* drive analysis
* memory analysis

{{% /section %}}

---

## password / hash cracking

---

### what is the purpose of this?
* if we find a hash, how do we find the original value?
    * think of SQLi, where we can dump the database?
    * what if we find hashes of other things?
* what about finding a password protected file, how do we open it?

---

### what do we do
* think back to the first session where we found additional subdomains/web content using a brute forcing script
* just do the same thing?
* try out every password until one of them works?

---

### some things to note
* there's a lot of different hashing algorithms, you'll need to know what format the hash is otherwise you can't really bruteforce it
* also you should consider whether the hash is salted
* hashcat & john both have options for these

---

### Demo

{{% /section %}}

---

## Forensics

---

{{% section %}}

## Network forensics

---

### What is a packet?
* a chunk of data, forming part of a complete message

* max packet size is about 65kb, so what happens when you stream a movie 

---

### What is in a packet

* All packets contain a header and a payload

* Payload is all the data

* Header contains any metadata (e.g. length, protocol, source, destination)

---

### OSI What
![](/assets/img/week04/osi_model.jpg)

---

### What is a packet capture?
* Intercepting packets travelling across a network, and logging them to a file

> What could be a problem with this?

---

### Demo

{{% /section %}}

---

{{% section %}}

### wireshark
> how to use it

---

### filters
* there's two types of filters
    * display filters: match metadata about the packet (e.g. source ip, protocol) 
    * pattern matching: match content in the filter (e.g. packet bytes/details)

---

### display filters
* just a boolean expression (similar to C)
    * `(f_1 eq AAA && f_2 ne BBB) || f_3`
* you can search by
    * **protocol** (e.g. `http`) 
    * **ip** (e.g. `ip.src_host` and `ip.dst_host`)
    * and a bunch more [here](https://wiki.wireshark.org/DisplayFilters) and [here](https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html)

---

### following conversation
each packet will be tied to a "conversation"
* you can follow them by
    * right clicking a packet > `follow X stream`
    * filtering for `X.stream eq N`

> `X` would be `TCP` or `UDP`

> `N` would be a number

---

### what should I be looking for
* wierd IPs being communicated with
* files being downloaded/uploaded
* you can look for communicaion made at the same as evidence you found

---

### decrypting traffic
Some traffic will be encrypted (e.g. SSH/HTTPS), so you won't be able to read the packets
* Edit > Preferences
* Protocols > TLS

> There you can you upload the tls/ssl keys to decrypt the traffic

---

## Demo

{{% /section %}}

---

{{% section %}}

## memory forensics

---

### what is it?
* investigating a dump of the RAM from a computer system

---

### when is this useful
> when?

---

### when is this useful
* there's a lot you can't get from a harddisk image
    * if/when a program was executed
    * how it was executed (arguments, lifespan)

* some malware never touches the disk

---

### fileless malware
* even if it never touches disk, at some point, it has to be in memory
* process hollowing: when a legitimate process is paused, duplicated, and then it's executable memory is replaced with malicious code
* this can bypass simple AVs which ignore whitelisted/trusted services

> read more [here](https://www.trellix.com/en-au/security-awareness/ransomware/what-is-fileless-malware.html) and [here](https://www.crowdstrike.com/cybersecurity-101/malware/fileless-malware/)

---

![](/assets/img/week05/inmemory-malware.png)

---

### what could you find in memory?
> what

---

### what could you find in memory?
* recently executed commands
* running processes, and their code/DLLs
* drivers & daemons
* passwords, security keys, security information

{{% /section %}}

---

### what processes are sus ඞ
{{% fragment %}}
obfuscate names/paths (drop some malware in a system location and give it a legitimate name)
{{% /fragment %}}
{{% fragment %}}
misspelled versions of proper system processes
{{% /fragment %}}
{{% fragment %}}
proper system names in wrong location
{{% /fragment %}}
{{% fragment %}}
duplicate processes that should only spawn once
{{% /fragment %}}
{{% fragment %}}
processes that have a parent they shouldn’t
{{% /fragment %}}
{{% fragment %}}
system processes with start time much later in life
{{% /fragment %}}
{{% fragment %}}
system processes running under a user account
{{% /fragment %}}

---

{{% section %}}

### volatility
> cause RAM is volatile lol

---

### list all the processes
* `windows.pstree`
    * get processes tree (not hidden)
* `windows.pslist`
    * get process list (EPROCESS)
* `windows.psscan`
    * get hidden process list (e.g. malware)

---

### dumping a process
* `windows.dumpfiles --pid <PID>`
    * get the executable & DLLs
* `windows.memmap --dump --pid <PID>`
    * get all memory resident pages
* `windows.dllist --pid <PID>`
    * list the DLLs used by a process

---

### see how a process was started
* `windows.cmdline`
    * shows the arguments used for the process
* `windows.envars [--pid <pid>]`
    * display process environment variables
* `windows.handles --pid <pid>`
    * show files, threads, etc a process has opened

---

### registries
* `windows.registry.hivescan`
    * TODO
* `windows.registry.hivelist`
    * TODO
* `windows.registry.printkey -K "Path\To\Key"`
    * TODO 

---

### viewing files
* `windows.filescan`
    * TODO
* `windows.dumpfiles`
    * TODO
* `windows.dumpfiles --virtaddr <o>`
    * TODO
* `windows.dumpfiles --physaddr <o>`
    * TODO

---

### networking
* `windows.netscan`
    * TODO
* `windows.netstat`
    * TODO 

---

### pattern match strings
* `windows.strings --strings-file ./strings_file`
    * TODO 
* `windows.vadyarascan --yara-rules "https://" --pid <PIDS>`
    * TODO
* `yarascan.YaraScan --yara-rules <R>`
    * TODO

---

### dumping hashes
* `windows.hashdump`
    * grab common windows hashes (SAM+SYSTEM)
* `windows.cachedump`
    * grab domain cache hashes inside the registry
* `windows.lsadump`
    * grab lsa secrets

---

### reference list
* command list can be found [here](https://github.com/volatilityfoundation/volatility/wiki/Command-Reference)
* some other [stuff](https://book.hacktricks.xyz/generic-methodologies-and-resources/basic-forensic-methodology/memory-dump-analysis/volatility-cheatsheet)

---

## Demo

{{% /section %}}

---

### next week
* reverse engineering?

---

## thanks!
that's all :)
