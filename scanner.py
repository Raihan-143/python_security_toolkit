import socket

#Target IP & Fixed Ports
target_ip="127.0.0.1"
common_ports=[21,22,80,443,3306]

print(f"--- Scanning Target {target_ip} ---")

#using loop for cheaking all the ports
for port in common_ports:
    #for every port make fresh socket
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0) #waiting for 1sec for response

    result=s.connect_ex((target_ip,port))

    if result==0:
        print(f"[+] Port {port:<5}: OPEN")

    else :
        print(f"[-] Port {port:<5}: CLOSED")

    #Socket close
    s.close()    

    print("--- Scan Completed ---")
    