from jnpr.junos import Device
import xml.etree.ElementTree as ET
import pprint
import sys

dev = Device(host='192.168.2.103', user='netconf', password='netconf!')
try:
	dev.open()
	print(dev.facts)
except Exception as err:
	print(err)
	sys.exit(1)

result = dev.rpc.get_interface_information(interface_name='em1', terse=True)
pprint.pprint(ET.tostring(result))
dev.close()