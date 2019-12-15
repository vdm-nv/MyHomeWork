parsed_sh_ip_int_br = [('FastEthernet0/0', '15.0.15.1', 'up', 'up'),
                          ('FastEthernet0/1', '10.0.12.1', 'up', 'up'),
                          ('FastEthernet0/2', '10.0.13.1', 'up', 'up'),
                          ('FastEthernet0/3', 'unassigned', 'administratively down', 'down'),
                          ('Loopback0', '10.1.1.1', 'up', 'up'),
                          ('Loopback100', '100.0.0.1', 'up', 'up')]

k =  ['interface', 'address', 'status', 'protocol']
res = []

 for i in parsed_sh_ip_int_br:
     res.append(dict(zip(k,i)))
     print(res)
pprint(res) 
 
 [{'interface': 'FastEthernet0/0',  'address': '15.0.15.1',
 'status': 'up',  'protocol': 'up'},
 {'interface': 'FastEthernet0/1',  'address': '10.0.12.1',
  'status': 'up',  'protocol': 'up'},
 {'interface': 'FastEthernet0/2',  'address': '10.0.13.1',
  'status': 'up',  'protocol': 'up'},
 {'interface': 'FastEthernet0/3',  'address': 'unassigned',
  'status': 'administratively down',  'protocol': 'down'},
 {'interface': 'Loopback0',  'address': '10.1.1.1',
  'status': 'up',  'protocol': 'up'},
 {'interface': 'Loopback100',  'address': '100.0.0.1',
  'status': 'up',  'protocol': 'up'}]
