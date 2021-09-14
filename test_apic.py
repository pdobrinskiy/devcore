from  genie.testbed import load
from pprint import pprint
from pyats.topology import loader
from genie.utils import Dq


tb = loader.load('apic.yaml')
apic = tb.devices['apic1']
apic.connect()
output = apic.get('api/node/class/faultInst.json')
pprint (output)

dns = Dq(output).get_values('dn')

pprint (dns)
pprint ('changes from branch1')
pprint ('changes from main')
