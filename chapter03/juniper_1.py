from ncclient import manager

conn = manager.connect(
	host='192.168.2.103',
	port='830',
	username='netconf',
	password='netconf!',
	timeout=10,
	device_params={'name':'junos'},
	hostkey_verify=False
	)
result = conn.command('show version', format='text')
print(result)
conn.close_session()