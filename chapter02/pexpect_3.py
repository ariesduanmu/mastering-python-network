#!/usr/bin/python3

# pexpect using ssh connect

import getpass
from pexpect import pxssh

device_ips = ['192.168.2.101', '192.168.2.102']
username = input('Username: ')
password = getpass.getpass('Password: ')

for device_ip in device_ips:
	output_file_name = f'{device_ip}_output.txt'
	print(f'connecting {device_ip}...')
	child = pxssh.pxssh()
	child.login(device_ip, username.strip(), password.strip(), auto_prompt_reset=False)
	
	with open(output_file_name, 'wb') as f:
		child.sendline('ip addr')
		child.expect('[#$] ')
		f.write(child.before)

	child.logout()