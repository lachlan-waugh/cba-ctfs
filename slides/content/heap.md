---
title: "heap"
layout: "bundle"
outputs: ["Reveal"]
---


{{< slide class="center" >}}
## heap exploitation
### lunch & learn

---

### overview
* what is a heap
* malloc basics
* use after free
* double free
* applications

---

### what is the heap
section of memory for long living stuff
or stuff you don't know the size of at compile time

e.g. a python array

stack is used for short lived stuff (e.g. local variables for a function)

---

{{% section %}}

### what is malloc
memory allocation

```C
malloc(sizeof(int));
malloc(10 * sizeof(int));
```

&nbsp;

returns a **chunk** of memory of the requested size

---

### free
the opposite of malloc

```C
free(pointer)
```

* given a pointer, give it back to the allocator
* mark it as free (set some metadata)
* puts it in a specific bin depending on size

---

### bins
linked lists of freed chunks

* when a chunk gets freed, it gets put in the bin
* when the allocator wants a chunk, it looks in the bin

---

### types of bins
* fast-bins
* unsorted bins
* small bins
* large bins
* tcache bins

---

### inuse chunks

<img src="/assets/img/heap/inuse_chunk.png" width="70%"/>

---

### free chunk

<img src="/assets/img/heap/free_chunk.png" width="80%"/>

{{% /section %}}

---

{{% section %}}

## exploitation

* the location that used to store user-controlled data, now stores control data (e.g. pointers!)
* could we somehow overwrite that data?
    * forward/back pointer
    * chunk size

---

### to note
* malloc doesn't NULL out the memory it gives you

---

## use after free
C is very lazy

* free doesn't actually NULL out the reference to the pointer

---

## double free

{{% /section %}}

---

{{% section %}}

## other types 
* unlink exploit
* shrinking free chunks
* enlarging free chunks
* house of spirit
* house of lore
* house of force
* house of einherjar
> uhh a lot more

{{% /section %}}

---

### questions?
