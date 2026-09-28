## ⚡ Multi-Threaded Engine (`threaded_scanner.py`)

Upgraded the sequential scanner to leverage parallel execution using Python's `concurrent.futures.ThreadPoolExecutor`.

* **Concurrency Model:** 50 worker threads scanning simultaneously.
* **Performance Gain:** Reduced scan latency for ports 1–1024 from ~15 minutes down to seconds.
* **Findings on Localhost:**
  * `Port 135 (Microsoft RPC)`: System Endpoint Mapper.
  * `Port 445 (Microsoft SMB)`: Server Message Block (critical network vector).