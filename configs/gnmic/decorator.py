cutsheet = {
      'spine1:57400': {
      'ethernet-1/1': {'remote_device': 'leaf1', 'remote_interface': 'ethernet-1/1','remote_role':'leaf'},
      'ethernet-1/2': {'remote_device': 'leaf2', 'remote_interface': 'ethernet-1/1','remote_role':'leaf'},
      'ethernet-1/3': {'remote_device': 'leaf3', 'remote_interface': 'ethernet-1/1','remote_role':'leaf'},
      'ethernet-1/4': {'remote_device': 'leaf4', 'remote_interface': 'ethernet-1/1','remote_role':'leaf'},
      'ethernet-1/5': {'remote_device': 'leaf5', 'remote_interface': 'ethernet-1/1','remote_role':'leaf'},
      'ethernet-1/6': {'remote_device': 'leaf6', 'remote_interface': 'ethernet-1/1','remote_role':'leaf'},
      'role':'leaf'
      },
      'spine2:57400': {
      'ethernet-1/1': {'remote_device': 'leaf1', 'remote_interface': 'ethernet-1/2','remote_role':'leaf'},
      'ethernet-1/2': {'remote_device': 'leaf2', 'remote_interface': 'ethernet-1/2','remote_role':'leaf'},
      'ethernet-1/3': {'remote_device': 'leaf3', 'remote_interface': 'ethernet-1/2','remote_role':'leaf'},
      'ethernet-1/4': {'remote_device': 'leaf4', 'remote_interface': 'ethernet-1/2','remote_role':'leaf'},
      'ethernet-1/5': {'remote_device': 'leaf5', 'remote_interface': 'ethernet-1/2','remote_role':'leaf'},
      'ethernet-1/6': {'remote_device': 'leaf6', 'remote_interface': 'ethernet-1/2','remote_role':'leaf'},
      'role':'spine'
      },
      'leaf1:57400': {
      'ethernet-1/1': {'remote_device': 'spine1', 'remote_interface': 'ethernet-1/1','remote_role':'spine'},
      'ethernet-1/2': {'remote_device': 'spine2', 'remote_interface': 'ethernet-1/1','remote_role':'spine'},
      'ethernet-1/3': {'remote_device': 's1', 'remote_interface': 'eth1','remote_role':'server'},
      'ethernet-1/4': {'remote_device': 's5', 'remote_interface': 'eth1','remote_role':'server'},
      'ethernet-1/5': {'remote_device': 's7', 'remote_interface': 'eth1','remote_role':'server'},
      'role':'leaf'
      },
      'leaf2:57400': {
      'ethernet-1/1': {'remote_device': 'spine1', 'remote_interface': 'ethernet-1/2','remote_role':'spine'},
      'ethernet-1/2': {'remote_device': 'spine2', 'remote_interface': 'ethernet-1/2','remote_role':'spine'},
      'ethernet-1/3': {'remote_device': 's2', 'remote_interface': 'eth1','remote_role':'server'},
      'ethernet-1/6': {'remote_device': 's8', 'remote_interface': 'eth1','remote_role':'server'},
      'role':'leaf'
      },
      'leaf3:57400': {
      'ethernet-1/1': {'remote_device': 'spine1', 'remote_interface': 'ethernet-1/3','remote_role':'spine'},
      'ethernet-1/2': {'remote_device': 'spine2', 'remote_interface': 'ethernet-1/3','remote_role':'spine'},
      'ethernet-1/3': {'remote_device': 's2', 'remote_interface': 'eth2','remote_role':'server'},
      'ethernet-1/6': {'remote_device': 's8', 'remote_interface': 'eth2','remote_role':'server'},
      'role':'leaf'
      },
      'leaf4:57400': {
      'ethernet-1/1': {'remote_device': 'spine1', 'remote_interface': 'ethernet-1/4','remote_role':'spine'},
      'ethernet-1/2': {'remote_device': 'spine2', 'remote_interface': 'ethernet-1/4','remote_role':'spine'},
      'ethernet-1/3': {'remote_device': 's3', 'remote_interface': 'eth1','remote_role':'server'},
      'ethernet-1/4': {'remote_device': 's4', 'remote_interface': 'eth1','remote_role':'server'},
      'ethernet-1/6': {'remote_device': 's8', 'remote_interface': 'eth3','remote_role':'server'},
      'role':'leaf'
      },
      'leaf5:57400': {
      'ethernet-1/1': {'remote_device': 'spine1', 'remote_interface': 'ethernet-1/5','remote_role':'spine'},
      'ethernet-1/2': {'remote_device': 'spine2', 'remote_interface': 'ethernet-1/5','remote_role':'spine'},
      'ethernet-1/4': {'remote_device': 's4', 'remote_interface': 'eth2','remote_role':'server'},
      'ethernet-1/6': {'remote_device': 's8', 'remote_interface': 'eth4','remote_role':'server'},
      'ethernet-1/5': {'remote_device': 's6', 'remote_interface': 'eth1','remote_role':'server'},
      'role':'leaf'
      },
      'leaf6:57400': {
      'ethernet-1/1': {'remote_device': 'spine1', 'remote_interface': 'ethernet-1/6','remote_role':'spine'},
      'ethernet-1/2': {'remote_device': 'spine2', 'remote_interface': 'ethernet-1/6','remote_role':'spine'},
      'ethernet-1/5': {'remote_device': 's6', 'remote_interface': 'eth2','remote_role':'server'},
      'ethernet-1/6': {'remote_device': 's9', 'remote_interface': 'eth1','remote_role':'server'},
      'role':'leaf'
      }
}

def apply(*events):
  for e in events:
      if e.tags.get("source") and e.tags.get("interface_name"):
            source = e.tags["source"]
            interface_name = e.tags["interface_name"]
            if source in cutsheet and interface_name in cutsheet[source]:
                  remote_interface = cutsheet[source][interface_name]['remote_interface']
                  remote_device = cutsheet[source][interface_name]['remote_device']
                  remote_role = cutsheet[source][interface_name]['remote_role']
                  role = cutsheet[source]['role']
                  e.tags['device'] = e.tags['source'].split(':')[0]
                  e.tags['role'] = role
                  e.tags['remote_device'] = remote_device
                  e.tags['remote_interface'] = remote_interface
                  e.tags['remote_role'] = remote_role
  return events
