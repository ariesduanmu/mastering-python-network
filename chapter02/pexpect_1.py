#!/usr/bin/python3
# pexpect overview
import pexpect

device_ips = ['192.168.2.101', '192.168.2.102']
username = 'test'
password = 'test'

for device_ip in device_ips:
	print(f'connecting {device_ip}...')
	child = pexpect.spawn(f'telnet {device_ip}')
	child.expect('login:')
	child.sendline(username)
	child.expect('Password:')
	child.sendline(password)
	child.expect('[#$] ')
	child.sendline('ip addr')
	child.expect('[#$] ')
	print(child.before.decode())
	child.sendline('exit')