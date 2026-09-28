import socket


#Nmap official safe target testing
target_host = "Scanme.nmap.org"
target_port = 22 #SSH port (Which is given first banner result)

print(f"---Attempting Banner Grab on {target_host}:{target_port}---")

try:
    #IPV4 , TCP make
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3.0) #waiting 3secnds for data

    #Connect to the target host and port
    s.connect((target_host, target_port))

    #Receive 1024bytes from the server
    raw_banner = s.recv(1024)

    #Decode the banner from bytes to string
    clean_banner = raw_banner.decode(errors="ignore").strip()

    print(f"[+] Banner: {clean_banner}")

    s.close()

except socket.timeout:
    print(f"[-] Connection timed out (No banner received)")

except Exception as e:
    print(f"[-] An error occurred: {e}")