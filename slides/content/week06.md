---
title: "06: reverse engineering"
layout: "bundle"
outputs: ["Reveal"]
---

## We'll get started at 13:05

---

{{< slide class="center" >}}
# TODO
## Week06

---

{{% section %}}

## disclaimer
* many of the tools and techniques discussed in these sessions could be used against real websites/applications
* don't do that

---

## acknowledgement of country
* We begin by acknowledging the Traditional Custodians of the land on which we meet, and pay our respects to their Elders past and present. We extend that respect to Aboriginal and Torres Strait Islander peoples here today.

---

## what will we cover this session
* The CTF
* static analysis
* dynamic analysis

{{% /section %}}

---

{{% section %}}

## CTF
* 9am 11/09 - 10pm 15/09
* join [discord](https://discord.gg/7xUrnhXWu)
* prizes: prezzee vouchers

---

### web
* the bulk of the challenges as these are the most natural and fun
* a mix of client-side and server-side vulnerabilities
* you get a link to a website, you need to exploit it to (rce, session fixation?)

---

### forensics
* no drive/network/memory forensics as it's a massive effort to make them, and I'd rather spend the effort on web ones
* wierd-encoding
* strange looking file
* password/hash cracking

---

### binary
* you'll want access to a linux system (use a VM)
* this can be a lot more conceptually difficult than the other sections, don't worry if it can be harder.

---

### reverse-engineering
* what we'll cover in this session
* you get an application, and you need to work out what the original source code was
* or you need to mess with the application to get it to print the flag

---

### osint (Open Source Intelligence)
* ethical stalking:tm:
* given an image: where was this picture taken
* given a person's name/email, find their social media and maybe something they leaked about themselves

---

### crypto
* don't roll your own
* given a crypto algorithm and an something encrypted/hashed with it, can you find the original input? 

---

### misc
* anything that doesn't fit in another category
* can be a good starting point as it doesn't necessarily require 

---

## notes
* not everything in the challenges will have been covered in the sessions
* if it isn't, there'll be a hint

---

## preparations
* Reread the slides
* Look at the demos
* Do some of the challenges I suggested during the sessions

---

## questions

{{% /section %}}

---

{{% section %}}
## reverse engineering
the process of deconstructing a program to work out it's underlying code, architecture, design, etc

* essentially getting the source code of an application, without being given it

---

### what types of reverse engineering are there?
* static analysis: examine an executable without running it (disassembler)
* dynamic analysis: examine an executable by running it (debugger)

---

### to note:
* if you've written programs before, chances are you've used a debugger
* the process of debugging code (setting breakpoints, changing values during execution) is a lot dynamic analysis

{{% /section %}}

---

{{% section %}}

## static analysis
trying to understand the program by determining the original source code

---

### suggestions
* pattern recognition
* ignore the noise
* 

---

### x86 assembly instructions
```
mov         # move a value into a register
add/sub     # 
inc/dec     # 
and/or/xor  # 
```

---

### some more
```
lea         # dereference pointer, move that value
pop/push    # grab from/put something on stack
cmp         # 
jmp         # jump to another memory location
je/jne      # jumps based on a condition
```

* read more [here](https://www.cs.virginia.edu/~evans/cs216/guides/x86.html)

{{% /section %}}

---

{{% section %}}

## dynamic analysis
trying to understand the program by running it, and seeing how it behaviours

---

### the most basic way
* just run the program
* see how it responds to certain input
* see what paths you can traverse

---

### more advanced
* actual debuggers (e.g. gdb)
* if you've ever used cheat engine, it's essentially the same idea
* cheat engine is actually a really powerful tool

---

### breakpoints
`break *X`, where X is
* an address e.g. `0x12345678`
* a function e.g. `main`

---

### fuzzing
* another type of dynamic tool you can use
* basically just generates a bunch of input, and tries to get the application to crash

{{% /section %}}

---

### How to practice
* Just write some basic code, and run it through an analysis tool.
* It's not just C programs that can be reversed, python also compiles modules into bytecode (.pyc files), which could also be reversed
* try to identify patterns that appear

---

### next week
CTF :)

---

## thanks!
that's all :)
