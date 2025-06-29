# 🛠️ CyberSec Tool 1 - SimpleReconScanner

🔍 **SimpleReconScanner** is a beginner-friendly Python script for basic network reconnaissance and port scanning.

---

## 🛡️ Features

- Scans TCP ports **1–1024** on a target IP address
- Detects and displays **open ports**
- Performs **banner grabbing** to identify running services

---

## ⚙️ Requirements

- Python 3
- Linux terminal environment (e.g., **Termux**, **Kali**, WSL, etc.)

---

## 🚀 Usage

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Stanley-blik/SimpleReconScanner.git
   cd SimpleReconScanner
   ```

2. *Run the script*:

   ```bash
   python3 recon_tool.py
   ```

3. *Provide the target IP address* when prompted.

---

*🖥️ Example Output*

```
[*] Starting scan on 192.168.56.102

[+] Port 21 is OPEN
    Banner: 220 (vsFTPd 2.3.4)

[+] Port 22 is OPEN
    Banner: SSH-2.0-OpenSSH_4.7p1...
```

---

*⚠️ Legal Disclaimer*

This tool is intended for *educational and ethical penetration testing purposes only*.
Do *NOT* use it on networks you do not own or lack explicit authorization to assess.

---

*📜 License*

This project is licensed under the *MIT License*.
