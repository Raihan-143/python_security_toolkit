## 🔍 Banner Grabbing & Service Detection (`banner_grabber.py`)

Low-level banner enumeration engine that connects to a target host and extracts service signature strings from Layer 7 responses.

* **Target:** `scanme.nmap.org:22` (SSH)
* **Captured Signature:** `SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13`
* **Security Impact:** Reveals explicit daemon versions and operating system distributions, significantly assisting CVE mapping and attack surface assessment.