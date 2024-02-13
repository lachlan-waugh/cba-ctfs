---
title: "heap"
layout: "bundle"
outputs: ["Reveal"]
---

{{< slide class="center" >}}
## allocator exploitation
### lunch & learn

---

### overview
* what is a heap
* malloc basics
* use after free
* double free
* applications

---

{{% section %}}

### what is the heap
* section of memory for
    * long living stuff
    * stuff you don't know the size of at compile time

* stack is used for short lived stuff (e.g. local variables for a function)

---

### memory stuff

<img src="/assets/img/heap/memory.png" width="50%"/>

---

### when are they used
```C
int do_stuff(void) {
    int i = 1;                  // stored on the stack
    int j = malloc(sizeof(int)) // stored on the heap
    // i disappears at the end of the do stuff function
    // j doesn't, it needs to be explicitly free()'d
}
```
&nbsp;

> also in python

```python
i = 0   # stored on stack
j = []  # stored on heap 
```

{{% /section %}}

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

## heap overflow
```C
[ 000000F ] >
[ 0000000 ] > // chunk 1 (in use)
[ 0000000 ] >
[ 000000F ] }
[ 0000000 ] } // chunk 2 (free)
[ 0000000 ] }
```

> if you could write enough into chunk 1, you could overwrite content in chunk 2

---

## heap overflow
if you wrote `A` x `8` + `B` x `12` into a chunk of size `4`

```C
[ 000000F ] >
[ AAAAAAA ] > // chunk 1 (in use)
[ AAAAAAA ] >
[ BBBBBBB ] }
[ BBBBBBB ] } // chunk 2 (free)
[ BBBBBBB ] }
```

---

## use after free
free doesn't actually NULL out the reference

```C
char *string = malloc(10 * sizeof(char));
printf("string = %p\n", string);
// string = 0x5da5101

free(string);

printf("string = %p\n", string);
// string = 0x5da5101
```

---

### forging chunks
manipulate the metadata of the chunk after its freed

```C
free(chunk)     // bin: chunk -> NULL
*chunk = "AAAA" // bin: chunk -> 0x41414141 -> ????
malloc(...)     // bin: 0x41414141 -> ????
malloc(...)     // bin: ????
// the second call to malloc returns 0x41414141
```

---

## double free
what if we free()'d the same chunk twice?

```C
free(chunk)     // bin: chunk -> NULL
free(chunk)     // bin: chunk -> chunk -> chunk -> ...

malloc(...)     // bin: chunk -> chunk -> chunk -> ...
malloc(...)     // bin: chunk -> chunk -> chunk -> ...
```

---

## demo

---

### realism
a struct with a function pointer isn't that realistic, but..

```C
struct user_t {
    char *name;
    int level;
}

void set_name(struct user_t *user) {
    // ...
    fgets(user->name, 100, stdin);
    // ...
}
```

> arbitary writes

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

### relevance in other languages

* [UAF in Python](https://pwn.win/2022/05/11/python-buffered-reader.html)
* [Double free in Chrome](https://github.com/advisories/GHSA-524r-c4hc-2m74)
* [UAF in Golang](https://github.com/golang/go/issues/35777)

> python is just fancy C

---

### questions?
