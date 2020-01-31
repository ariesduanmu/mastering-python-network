from ncclient import manager
from ncclient.xml_ import new_ele
from ncclient.xml_ import sub_ele

def connect(host, port, user, password):
	conn = manager.connect(host=host,
		                   port=port,
		                   username=user,
		                   password=password,
		                   timeout=10,
		                   device_params={'name':'junos'},
		                   hostkey_verify=False)
	return conn

def show_cmds(conn, cmd):
	result = conn.command(cmd, format='text')
	return result

def config_cmds(conn, config):
	conn.lock()
	conn.load_configuration(config=config)
	conn.validate()
	commit_config = conn.commit()
	conn.unlock()
	return commit_config.tostring

conn = connect('192.168.2.103', '830', 'netconf', 'netconf!')

config = new_ele('system')
sub_ele(config, 'host-name').text = 'master'
sub_ele(config, 'domain-name').text = 'python'

print(config_cmds(conn, config))

conn.close_session()