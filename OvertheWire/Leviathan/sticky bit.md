The string:

```text
-r-sr-x---
```

is the **file type and permission bits** shown by `ls -l`. Here's the breakdown:

```text
-r-sr-x---
││ │││ └── Others permissions (---)
││ │└┴── Group permissions (r-x)
│└┴──── User (owner) permissions (r-s)
└────── File type (- = regular file)
```

### 1. `-` (First character)

This indicates the **file type**.

Common values:

* `-` = Regular file
* `d` = Directory
* `l` = Symbolic link
* `c` = Character device
* `b` = Block device

So:

```text
-
```

means **this is a regular file**.

---

### 2. `r-s` (Owner permissions)

These are the permissions for the **owner** of the file.

Normally you would see:

```text
rwx
```

But instead you see:

```text
r-s
```

Meaning:

* `r` = owner can read
* `-` = execute bit is replaced
* `s` = **SUID (Set User ID)** is set **and** execute permission is present

So this is equivalent to:

```text
r-x + SUID
```

The important part is the **`s`**.

---

### What is SUID?

The file owner is:

```text
leviathan2
```

So when **anyone executes** this program:

```bash
./check
```

it **runs with the permissions of `leviathan2`**, **not** the user who started it.

For example:

```
You are:        leviathan1
Owner of file:  leviathan2

./check

Program runs as:
leviathan2
```

This is why SUID programs are common in security wargames like **Leviathan**—they let you temporarily act with the file owner's privileges.

Examples from Linux:

```text
/usr/bin/passwd
```

is SUID so ordinary users can update `/etc/shadow`, which only root can normally modify.

---

### 3. `r-x` (Group permissions)

The group is:

```text
leviathan1
```

Permissions:

* `r` = group can read
* `-` = group cannot write
* `x` = group can execute

---

### 4. `---` (Others)

Everyone else has:

* no read
* no write
* no execute

---

## Complete breakdown of your line

```text
-r-sr-x---   1 leviathan2 leviathan1 15080 Jun 24 15:01 check
```

| Part         | Meaning                                     |
| ------------ | ------------------------------------------- |
| `-`          | Regular file                                |
| `r-s`        | Owner can read and execute; SUID is enabled |
| `r-x`        | Group can read and execute                  |
| `---`        | Others have no permissions                  |
| `leviathan2` | File owner                                  |
| `leviathan1` | File group                                  |
| `15080`      | File size (bytes)                           |

### Why this matters in the Leviathan challenge

You're logged in as:

```bash
leviathan1
```

The file is owned by:

```bash
leviathan2
```

Because of the **SUID bit (`s`)**, when you run:

```bash
./check
```

the program executes with **`leviathan2`'s privileges**. If the program has a flaw (which is common in wargames like Leviathan), you may be able to exploit it to access resources that only `leviathan2` can normally read, such as the password for the next level.
