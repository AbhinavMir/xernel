---
draft: false
title: "Day 2: Getting TinyCore up to speed"
---

I used UTM because I am on MacOS. Why? Because my Linux machine needs a 3-pin outlet, which for some reason my home in Boston, a center for technology, does not have. Anyway, so I am using UTM. On UTM, you can download the TinyCore ISO and get it running by just loading it via virtualise, going to setting, disabling UEFI and changing architecture to x86_64. 

Why TinyCore? 17 MiB is an insanely beautiful number for size of a distro. But there are also a lot of customisations to be made which gets me excited. 

First, we don't have gcc or make. So we need to get them. We can do this by using the package manager. 

```bash
tce-ab
// then "click" search
// look for the gcc you want
// "click" install
```

Click = press enter on your option since you are on a terminal, because TinyCore is a minimal distro.
