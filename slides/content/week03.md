---
title: "week03: serverside"
layout: "bundle"
outputs: ["Reveal"]
---

## We'll get started at 13:05

---

{{< slide class="center" >}}
# server-side exploitation
## week03

---

## disclaimer
* many of the tools and techniques discussed in these sessions could be used against real applications
* dont do that

---

## acknowledgement of country
* We begin by acknowledging the Traditional Custodians of the land on which we meet, and pay our respects to their Elders past and present. We extend that arespect to Aboriginal and Torres Strait Islander peoples here today.

---

### housekeeping 
did anyone try out any of the challenges? how did you go?

---

{{% section %}}

## what will we cover this session
* SQLi
* SSTI
* SSRF
* LFI

{{% /section %}}

---

{{% section %}}

## SQL
Structured Query Language

* e.g. SQLite, PostgreSQL, MySQL, MSSQL Server

---

> Fingerprinting
* work out the flavour/version
	* **MySQL**: `Version()`
	* **SQLite**: `sqlite_version()`
	* **MSSQL**: `@@Version`

---

> Finding the schema
* what tables exist, what do they look like?
	* **MySQL**: `information_schema.[tables|columns]`
	* **SQLite**: `sqlite_[master|schema]`
	* **MSSQL**: `SHOW TABLES; DESCRIBE <table_name>`

---

Queries >
* `SELECT <column> FROM <table>;`
* `INSERT INTO table VALUES (a, b);`
* `UPDATE table SET ... = ...`
* ~~`DELETE FROM table ...`~~ (*pls dont*)
* `-- a comment (also #)`

---

`SELECT \* FROM table WHERE ...`
* `col =  ...`
* `col >  ...`
* `col <  ...` 
* `col <> ...	#` not equals (!=)
* `col LIKE ...	#` regexp
  * `_` `(.)` and `%` `(.*)` are wildcards

---

`SELECT user, pass FROM users UNION SELECT title, author FROM blogs`
```
  user	  pass	     id	  title   author	THE UNION
|=======|=======|   |===|=======|=======|   |=======|=======|
| admin	| admin	|   | 1 | blog1 | melon |   | admin | admin |
| melon	| water	|   | 2 | blog2 | admin |   | melon | water |
|=======|=======|   | 3 | blog3 | admin |   | blog1 | melon |
		            |===|=======|=======|   | blog2 | admin |
		 		                     	    | blog3 | admin |
      users		            blogs   	    |=======|=======|
```

---

## Notes on UNIONs
* The query needs to extract the same number of columns from both tables
* The data-type for the columns must be compatible
* You can also UNION the same table

{{% /section %}}

---

{{% section %}}

## SQLi
SQL Injection

* *TLDR*: blindly trusting user input is bad

* What if we injected control characters which changed how the database interprets the query? e.g. inject our own `UNIONs/WHEREs/etc`

* How could it tell the difference?

---

### How does SQLi work

```sql
SELECT * FROM users WHERE user = '{input}' AND password = '{...}'
```

&nbsp;  

If our input was: `' OR 1=1 --`

```sql
--                        vvvvvvvvvvvvvvvvvvvv
SELECT * FROM users WHERE user = '' OR 1=1 --'and password = '...'
--                        ^^^^^^^^^^^^^^^^^^^^
-- user = '' is always false, but 1=1 is always true
-- so this will return every user from the database
```

---

### Issues you may encounter
* Syntax needs to be correct, or you'll throw an error
  * so, determine syntax through errors/fingerprint

* You have SQLi in `items`, but want `users`
  * find out the tables? (database schema)
  * include that table with a `UNION`

---

## [Demo](https://github.com/lachlan-waugh/cba/tree/main/demos/server-side/sqli)

{{% /section %}}

---

{{% section %}}

## SSTI
Server-side template injection

Templating engines (eg. Jinja2, Pug) use templates to inject code and variables into static files

---

### what is templating
similar to using variables in print

```python
print('Hello ' + name)
```

&nbsp;

except you're using it for writing web content
```html
<!-- index.html -->
<h1>Hello {{name}}</h1>
<div>it is currently {{time}}</div>
```

```python
# main.py
render_template("index.html", name="melon", time=datetime.utcnow)
```

---

### how to exploit this?
what if we tricked the template rendering into thinking our user-supplied content was code?

* if our username was `{{7*7}}`, it would evaluated to 49

* Jinja2: `{{`\<CODE HERE\>`}}` e.g. `{{ 'A'*3 }}` => `AAA`

---

## [Demo](https://github.com/lachlan-waugh/cba/tree/main/demos/server-side/ssti)

{{% /section %}}

---

## SSRF
{{% section %}}

### Server-side request forgery
Trick a server into doing stuff it doesn't intend to

* Consider a website w/ a database in the backend
* You can access the website, website can access the database, but you can't access the database. 
* What if we tricked the website into making a request to that database when it doesn't intend to?

---

![](/assets/img/week03/ssrf.png)

---

### Exploitation
* Internal services might (often will) be less secure than externally facing ones
* What can we do?
  * Retrieve/disclose information (ssi/lfi)
  * Remote code execution / Reverse shells?
  * Other bad stuff

---

## [Demo](https://github.com/lachlan-waugh/cba/tree/main/demos/server-side/ssrf)

{{% /section %}}

---

{{% section %}}

### LFI
Local File Inclusion

* Tricking a server to include a local file in it's output
* In SSRF we tricked the server into downloading content from something running in it's network
* What if instead, we told it do download a local file?

---

### Directory traversal
* If you can download a file from the server from a certain location, e.g.:
    * `https://website.com/files/file1`

* You could try access a file from other locations:
    * `https://website.com/files/../../../../other/file`

> `..` refers to the parent directory, so we're navigating up the file system to find other files hosted locally

---

### Idk, something else
* When making a request (think back to SSRF), we provide a url/uri e.g. `https://website.com`
    * `https://` is the scheme and tells the server to access it over the internet (basically)
    * `file://` is another scheme, telling the server to instead look at the local file system
    * give it `file:///path/to/some/file`

---

### Something to note
> the `/proc/self/` directory contains information about the currently running process, you can use this to disclose information: e.g. environment variables, current path, etc

---

## [Demo](https://github.com/lachlan-waugh/cba/tree/main/demos/server-side/lfi)

{{% /section %}}

---

### suggested challenges
* [picoctf](https://play.picoctf.org/practice?category=1&page=1) (look at web exploitation)
* [overthewire natas](https://overthewire.org/wargames/natas/)

---

### next week
binary exploitation
* programming logic errors
* buffer overflows (maybe? idk)

---

## thanks!
that's all :)
