import paramiko
import time


MAX_BUFFER = 5000

def clear_buffer(connection):
	if connection.recv_ready():
		return connection.recv(MAX_BUFFER)
	return b""

connection = paramiko.SSHClient()
connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
connection.connect('192.168.2.101', username='test', password='test', look_for_keys=False, allow_agent=False)
new_connection = connection.invoke_shell()
output = clear_buffer(new_connection)
print(output)
new_connection.send('ip addr\n')
time.sleep(3)
output = clear_buffer(new_connection)
print(output)
new_connection.close()