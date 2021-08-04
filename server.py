import socket
from fileinput import filename

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))
s.listen(1)
print(host)
print("Wait for any in coming connection ...")
conn, addr = s.accept()
print(addr, "Has connected to the server")
file = input(str("Please enter the filename of the file: "))
file = open(filename, 'rb')
file_data = file.read(1024)
conn.send(file_data)
print("Data has been transmitted successfully")
