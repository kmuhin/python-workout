# Examples of regex strings for use in Python re module

regex online testing https://regex101.com/

## show cdp neighbor

    (?P<dev_neighb>^\S+)\s+(?P<int_local>\w+ \S+)\s+\d+\s+((?:\w )+)\s+\S+\s+(?P<int_neighb>\w+ \S+)$

captures: device id, local interface, port id
examples command output:
1.
    R4>show cdp neighbors
    Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                      S - Switch, H - Host, I - IGMP, r - Repeater

    Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
    SW1              Eth 0/0            131          S I      WS-C3750- Eth 0/4
    R5               Eth 0/1            132        R S I      2811      Eth 0/1
2.
    R2>show cdp neighbors
    Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                      S - Switch, H - Host, I - IGMP, r - Repeater

    Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
    SW1              Eth 0/0            125          S I      WS-C3750- Eth 0/2
    R5               Eth 0/1            150        R S I      2811      Eth 0/0
    R6               Eth 0/2            150        R S I      2811      Eth 0/1

## show dhcp snooping binding

    (?P<mac>\S+)\s+(?P<ip>[\d.]+)\s+\d+\s+\S+\s+(?P<vlan>\d+)\s+(?P<port>\S+)$

captures: mac, ip, vlan, interface
examples command output:
1. 
    MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
    ------------------  ---------------  ----------  -------------  ----  --------------------
    00:09:BB:3D:D6:58   10.1.10.2        86250       dhcp-snooping   10    FastEthernet0/1
    00:04:A3:3E:5B:69   10.1.5.2         63951       dhcp-snooping   5     FastEthernet0/10
    00:05:B3:7E:9B:60   10.1.5.4         63253       dhcp-snooping   5     FastEthernet0/9
    00:07:BC:3F:A6:50   10.1.10.6        76260       dhcp-snooping   10    FastEthernet0/3
    00:09:BC:3F:A6:50   192.168.100.100  76260       dhcp-snooping   1     FastEthernet0/7
    Total number of bindings: 5

2.
    MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
    ------------------  ---------------  ----------  -------------  ----  --------------------
    00:A9:BB:3D:D6:58   10.1.10.20       86250       dhcp-snooping   10    FastEthernet0/7
    00:B4:A3:3E:5B:69   10.1.5.20        63951       dhcp-snooping   5     FastEthernet0/5
    00:C5:B3:7E:9B:60   10.1.5.40        63253       dhcp-snooping   5     FastEthernet0/9
    00:A9:BC:3F:A6:50   10.1.10.60       76260       dhcp-snooping   20    FastEthernet0/2
    Total number of bindings: 4
3.
    MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
    ------------------  ---------------  ----------  -------------  ----  --------------------
    00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
    00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
    Total number of bindings: 2


## sh version 

    Version (?P<ios>\S+),.+uptime is (?P<uptime>.+?)\n.+System image file is \"(?P<image>\S+?)\" 
    required flags: re.DOTALL(single line)

captures: ios version, uptime, image file name
example command output:

    Cisco IOS Software, 1841 Software (C1841-ADVIPSERVICESK9-M), Version 12.4(15)T1, RELEASE SOFTWARE (fc2)
    Technical Support: http://www.cisco.com/techsupport
    Copyright (c) 1986-2007 by Cisco Systems, Inc.
    Compiled Wed 18-Jul-07 04:52 by pt_team
     
    ROM: System Bootstrap, Version 12.3(8r)T8, RELEASE SOFTWARE (fc1)
     
    router uptime is 15 days, 8 hours, 32 minutes
    System returned to ROM by power-on
    System image file is "flash:c1841-advipservicesk9-mz.124-15.T1.bin"
 

