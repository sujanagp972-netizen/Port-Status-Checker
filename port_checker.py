import socket

host = input("Enter the system name or IP address: ")
port = int(input("Enter the port number: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)

result = sock.connect_ex((host, port))

if result == 0:
    print(f"Port {port} is OPEN on {host}")
else:
    print(f"Port {port} is CLOSED on {host}")

sock.close()