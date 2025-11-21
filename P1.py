import os

li = ["192.168.1.1","192.168.1.41","256.0.1.19"]

for ip in li:
    if os.system(f"ping -n 1 {ip}") == 0:
        print(ip + " is reachable")
    else:
        print(ip + " is Not reachable")