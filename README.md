# 🦉 NightjarsArsenal  
**by BurnedPort**

A personal cybersecurity toolkit forged from spite, obsession, and a deep fascination with system weakness. Each tool in this arsenal is hand-crafted — no bloat, no filler, just surgical precision.

---

## ⚙️ Current Modules

### 👁️ Monocular  
> A lightweight yet sharp-eyed TCP port scanner with banner-grabbing functionality.  
> Built for speed, built for stealth, built to peek before you pounce.

#### Features:
- Targeted TCP port scanning with adjustable ranges
- Banner grabbing via HTTP HEAD requests
- Argparse interface for clean command-line usage
- Optional emoji output for maximum flex

#### Example usage:
```bash
py Monocular.py -t scanme.nmap.org -s 1 -e 100

