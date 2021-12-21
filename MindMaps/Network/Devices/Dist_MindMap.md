
# Dist
##  Device Information

### Serial number: 12345679
### Device Type: WS-C4500X-16
### Version: 03.11.00.E
### Operating System: IOS-XE
## Interface Counts
### Te ints: 32
### Virtual ints: 27
## Device Inventory
### Switch1 System
#### Cisco Systems, Inc. WS-C4500X-16 2 slot switch
#### 123456789
### Switch1 Supervisor 1 (virtual slot 1)
#### 4500X-16 10GE (SFP+)
#### 123456789
### TenGigabitEthernet1/1/2
#### SFP-10Gbase-SR
#### 123456789
### Switch1 Power Supply 1
#### Power Supply ( AC 750W )
#### 123456789
### Switch1 Power Supply 2
#### Power Supply ( AC 750W )
#### 123456789
### Switch2 System
#### Cisco Systems, Inc. WS-C4500X-16 2 slot switch
#### 123456789
### Switch2 Supervisor 1 (virtual slot 11)
#### 4500X-16 10GE (SFP+)
#### 123456789
### TenGigabitEthernet2/1/2
#### SFP-10Gbase-SR
#### 123456789
### Switch2 Power Supply 1
#### Power Supply ( AC 750W )
#### 123456789
### Switch2 Power Supply 2
#### Power Supply ( AC 750W )
#### 123456789
## Vlans
### 1 - RED
#### active
#### Interfaces
##### TenGigabitEthernet1/1/12
##### TenGigabitEthernet1/1/14
##### TenGigabitEthernet2/1/4
### 99 - BLUE
#### active
#### Interfaces
##### TenGigabitEthernet1/1/1
##### TenGigabitEthernet1/1/5
##### TenGigabitEthernet1/1/10
## VRF / Address Family
### RED - ipv4
#### Route: 0.0.0.0/0 
##### Active: True 
##### Metric: 6
##### Next Hop Index: 1
###### Next Hop: 192.168.100.1
###### Route Preference: 110 
###### Source Protocol: ospf
###### Source Protocol Code: O*IA
#### Route: 192.168.200.0/30
##### Active: True 
##### Metric: 6
##### Next Hop Index: 1
###### Next Hop: 192.168.200.1
###### Route Preference: 110 
###### Source Protocol: ospf
###### Source Protocol Code: O

#### Route: 192.168.1.0/30
##### Active: True 
##### Metric: 

##### Outgoing Interface: Port-channel1
###### Source Protocol: connected
###### Source Protocol Code: C
#### Route: 192.168.1.1/32
##### Active: True 
##### Metric: 

##### Outgoing Interface: Port-channel1
###### Source Protocol: local
###### Source Protocol Code: L
### BLUE - ipv4
#### Route: 0.0.0.0/0 
##### Active: True 
##### Metric: 6
##### Next Hop Index: 1
###### Next Hop: 192.168.150.1
###### Route Preference: 110 
###### Source Protocol: ospf
###### Source Protocol Code: O*IA
#### Route: 192.168.150.0/30
##### Active: True 
##### Metric: 6
##### Next Hop Index: 1
###### Next Hop: 192.168.200.1
###### Route Preference: 110 
###### Source Protocol: ospf
###### Source Protocol Code: O

#### Route: 192.168.250.0/30
##### Active: True 
##### Metric: 

##### Outgoing Interface: Port-channel2
###### Source Protocol: connected
###### Source Protocol Code: C
#### Route: 192.168.250.1/32
##### Active: True 
##### Metric: 

##### Outgoing Interface: Port-channel2
###### Source Protocol: local
###### Source Protocol Code: L
### mgmtVrf
## neighbors
### CDP
#### Port-channel1
##### Routed Port-channel
##### **Local Interfaces**: 
###### TenGigabitEthernet1/1/13 
###### TenGigabitEthernet2/1/13
##### **Remote Interfaces** 
###### TenGigabitEthernet2/1/3 
###### TenGigabitEthernet1/1/3
##### **IP Address:**192.168.1.1
##### ***Core***
#### Port-channel2
##### Switched Port-channel
##### **VLAN(s)**: 10,20
##### **Local Interfaces**: 
###### TenGigabitEthernet1/1/3 
###### TenGigabitEthernet2/1/3
##### **Remote Interfaces** 
###### GigabitEthernet0/15 
###### GigabitEthernet0/16
##### **IP Address:**192.168.2.10
##### ***Catalyst Switch 2***
## MAC Addresses
### 10
#### 1111.2222.3333
#### aaaa.bbbb.cccc
### 20
#### 1111.2222.3333
#### aaaa.bbbb.cccc
## ARP table
### Vlan10
#### 192.168.1.10
##### age: -
##### Link Layer Address: 1111.2222.3333
##### protocol: Internet
### Port-channel1.1
#### 192.168.1.5
##### age: 120
##### Link Layer Address: 1111.2222.3333
##### protocol: Internet
#### 192.168.1.10
##### age: -
##### Link Layer Address: 1111.2222.3333
##### protocol: Internet
## Interfaces
### Key
#### interface type
##### MAC Address
##### Operational Status
##### Last Input
##### Last Output
### Port-Channels
#### Port-channel1
##### 1111.2222.3333
##### Enabled: True
##### 00:00:00
##### never
#### Port-channel1.10
##### 1111.2222.3333
##### Enabled: True
##### 
##### 
### Tunnels
#### Tunnel0
##### 
##### Enabled: True
##### never
##### never
### Vlans
#### Vlan10
##### 1111.2222.3333
##### Enabled: False
##### never
##### never
#### Vlan20
##### 1111.2222.3333
##### Enabled: True
##### 41w3d
##### never
### Loopbacks
### Ethernet
### FastEthernet
#### FastEthernet1
##### 1111.2222.3333
##### Enabled: True
##### never
##### never
### GigabitEthernet
### 2.5 GigabitEthernet
### Ten GigabitEthernet
#### TenGigabitEthernet1/1/1
##### 1111.2222.3333
##### Enabled: False
##### never
##### never
### TwentyFive GigabitEthernet
### Forty GigabitEthernet