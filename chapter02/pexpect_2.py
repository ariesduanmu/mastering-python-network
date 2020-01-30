#!/usr/bin/python3
import pexpect

device_ips = ['192.168.2.101']
username = 'test'
password = 'test'

for device_ip in device_ips:
	print(f'connecting {device_ip}...')
	child = pexpect.spawn(f'telnet {device_ip}')
	child.expect('login:', timeout=5)
	child.sendline(username)
	child.expect('Password:')
	child.sendline(password)
	child.interact()