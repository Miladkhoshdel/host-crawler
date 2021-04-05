# Created with Love by Milad khoshdel (miladkhoshdel@gmail.com)

from netaddr import *
import socket

known_ports = [22,3389,80,443,135,445]
result = []
open_ports = []


line = input("Enter File Name: ")
with open(line, encoding='utf8') as f:
    for target in f:
        print("\nCrawling on " + target)
        if "/" in target:
            ip_range = IPNetwork(target)
            for i in ip_range:
                print ('Starting scan on host: ', i)
                for j in known_ports:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(0.005)
                    conn = s.connect_ex((str(i), j))
                    if(conn == 0) :
                        open_ports.append(j)
                    s.close()
                if len(open_ports):
                    result.append(str(i) + "\t" + socket.getfqdn(str(i),) + " \t" + str(open_ports))
                    open_ports.clear()
    print("\n===================== Result =====================")
    for i in result:
        print(i)
