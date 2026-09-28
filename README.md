# Simple TCP Port Scanner (Phase 1 — Network & Automation)

A lightweight, multi-port TCP connectivity scanner built with native Python sockets. This tool verifies open communication ports on a target IP/host by executing full TCP 3-Way Handshakes.

---

## Purpose & Security Context

In network reconnaissance and defensive vulnerability management, understanding open ports is critical. An exposed port represents an entry vector where a service is actively listening for incoming network packets.

This project demonstrates:
* Low-level socket programming using the OSI Transport Layer (Layer 4).
* Systematic inspection of listening TCP ports.
* Non-blocking network timeout controls.

---

## How It Works (Line-by-Line Breakdown)

| Code Block / Concept | Purpose & Mechanism |
| :--- | :--- |
| `import socket` | Imports Python's low-level networking interface to communicate directly with OS kernel sockets. |
| `target_ip = "127.0.0.1"` | Specifies the target endpoint. Resolves to localhost loopback for non-destructive local testing. |
| `socket.AF_INET` | Specifies the Address Family: IPv4 (32-bit IP addressing). |
| `socket.SOCK_STREAM` | Specifies the Transport Protocol: TCP (Connection-oriented, 3-Way Handshake). |
| `s.settimeout(1.0)` | Prevents the script from hanging indefinitely if a firewall drops the SYN packet (timeout in seconds). |
| `s.connect_ex((ip, port))` | Attempts TCP handshake. Returns `0` on successful handshake (`OPEN`), or an OS error code on failure. |
| `s.close()` | Closes the socket descriptor and frees allocated kernel network buffers. Must run inside the loop. |

---

## Usage

1. Clone or download the repository:
   ```bash
   git clone github.com/Raihan-143/python_security_toolkit.git
   cd simple-tcp-port-scanner

## Author
Md. Raihan Hasan Rana - Cybersecurity Enthusi  