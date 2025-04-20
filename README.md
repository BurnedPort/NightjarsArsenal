# 🦉 NightjarsArsenal  
**by BurnedPort**

A personal cybersecurity toolkit forged from spite, obsession, and a deep fascination with system weakness. Each tool in this arsenal is hand-crafted — no bloat, no filler, just surgical precision.

> *Built to recon. Built to exploit. Built to haunt logs forever.*

---

## ⚙️ Current Modules

### 👁️ Monocular  
> A lightweight yet sharp-eyed TCP port scanner with banner-grabbing functionality.  
> Built for speed. Built for stealth. Built to peek before you pounce.

**Features:**
- Adjustable TCP port ranges
- HTTP banner grabbing via HEAD
- Argparse CLI interface
- Optional emoji output for terminal flavor

```bash
py Monocular.py -t scanme.nmap.org -s 1 -e 100
```

---

### 🦅 Talon  
> A stealthy, adaptive login bruteforcer designed to rip through weak auth.  
> Integrates with MistRaven for cloaking. Lightweight, modular, and lethal.

**Features:**
- Argparse-ready with smart defaults
- Supports username + password lists
- Custom field name support (`-f username,password`)
- Built-in stealth delay + header randomization
- Fail-string detection and strategy switching coming soon

```bash
py Talon.py -u http://localhost:5000/login -U users.txt -P passwords.txt -f username,password -s "Invalid login"
```

---

### 🌫️ MistRaven  
> A stealth-layer library for Talon and future tools.  
> Randomizes headers, adds delay variance, helps evade detection.

**Functions:**
- `stealth_headers()` → Rotates User-Agent, Accept-Language, etc.
- `stealth_sleep(delay)` → Adds natural randomness to request timing

---

### 🪓 Clutch  
> A directory brute-forcer designed to rip through obscurity.  
> Finds hidden paths, dev panels, backup files, and more.

**Features:**
- Wordlist-based path discovery
- Designed for speed and modularity
- Ideal for chaining into privilege escalation or RCE

```bash
py Clutch.py -u http://target.com -w wordlists/dirs.txt
```

---

## 🔜 Roadmap

- Rule-based password mutation engine (mutate_mode)
- Markov chain password prediction
- PassGAN integration for heavy brute mode
- Strategy switcher based on response behavior
- Stealth payload dropper (GhostWing)

---

## 🖤 Philosophy

**NightjarsArsenal** isn’t meant to impress companies.  
It’s built for self-mastery, practical skill, and walking your own path through the world of exploitation.  
Every tool is a feather. Together, they form wings.

