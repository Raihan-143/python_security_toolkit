import socket
import time
from concurrent.futures import ThreadPoolExecutor

# Target IP & Fixed Ports
target_ip = "127.0.0.1"
start_port = 1
end_port = 1024 #first 1024 well-known ports checking

print(f"--- Multi-threaded Scanning Target {target_ip} ---")
start_time = time.time()

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"[+] Port {port:<5} : OPEN")
            
        s.close()
    except Exception:      
        pass               

with ThreadPoolExecutor(max_workers=50) as executor:
    list(executor.map(scan_port, range(start_port, end_port + 1)))

    end_time = time.time()
    print(f"--- Scan Completed in {round(end_time - start_time, 2)} seconds ---")