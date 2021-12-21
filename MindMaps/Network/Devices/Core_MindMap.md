
# Core
##  Device Information

### Serial number: 12345679
### Device Type: WS-C6509-E
### Version: 15.5(1)SY7
### Operating System: IOS
## Interface Counts
### Gi ints: 108
### Te ints: 72
### Virtual ints: 32
## Device Inventory
### WS-C6509-E
#### Chassis 2 WS-C6509-E
#### Chassis 2 Cisco Systems, Inc. Catalyst 6500 9-slot Chassis System
#### 123456789
### WS-C6K-VTT-E
#### Chassis 2 WS-C6K-VTT-E 3
#### Chassis 2 VTT-E FRU 3
#### 123456789
### CLK-7600
#### Chassis 2 CLK-7600 2
#### Chassis 2 OSR-7600 Clock FRU 2
#### 123456789
### WS-X6908-10G
#### Chassis 2 7
#### Chassis 2 WS-X6908-10G DCEF2T 8 port 10GE Rev. 1.2
#### 123456789
### WS-F6K-DFC4-E
#### Chassis 2 WS-F6K-DFC4-E Distributed Forwarding Card 4 EARL 1 sub-module of 7
#### Chassis 2 WS-F6K-DFC4-E Distributed Forwarding Card 4 Rev. 1.2
#### 123456789
### X2-10GB-SR
#### Chassis 2 Transceiver Te2/7/8
#### Chassis 2 X2 Transceiver 10Gbase-SR Te2/7/8
#### 123456789
### X2-10GB-LR
#### Chassis 2 Transceiver Te2/7/4
#### Chassis 2 X2 Transceiver 10Gbase-LR Te2/7/4
#### 123456789
### C6800-16P10G
#### Chassis 2 2
#### Chassis 2 C6800-16P10G DCEF2T 4 port 40GE / 16 port 10GE Rev. 1.2
#### 123456789
### C6800-DFC
#### Chassis 2 C6800-DFC Distributed Forwarding Card 4 EARL 1 sub-module of 2
#### Chassis 2 C6800-DFC Distributed Forwarding Card 4 Rev. 1.2
#### 123456789
### SFP-10G-SR
#### Chassis 2 Transceiver Te2/2/6
#### Chassis 2 SFP+ Transceiver 10Gbase-SR Te2/2/6
#### 123456789
### Unspecified
#### Chassis 2 Transceiver Gi2/9/45
#### Chassis 2 SFP Transceiver 1000BaseT Gi2/9/45
#### 123456789
### VS-SUP2T-10G
#### Chassis 2 6
#### Chassis 2 VS-SUP2T-10G 5 ports Supervisor Engine 2T 10GE w/ CTS Rev. 1.5
#### 123456789
### VS-F6K-MSFC5
#### Chassis 2 msfc sub-module of 6
#### Chassis 2 VS-F6K-MSFC5 CPU Daughterboard Rev. 2.0
#### 123456789
### VS-F6K-PFC4
#### Chassis 2 VS-F6K-PFC4 Policy Feature Card 4 EARL 1 sub-module of 6
#### Chassis 2 VS-F6K-PFC4 Policy Feature Card 4 Rev. 1.2
#### 123456789
### WS-X6848-SFP
#### Chassis 2 9
#### Chassis 2 WS-X6848-SFP CEF720 48 port 1000mb SFP Rev. 3.0
#### 123456789
### WS-F6K-DFC4-A
#### Chassis 2 WS-F6K-DFC4-A Distributed Forwarding Card 4 EARL 1 sub-module of 9
#### Chassis 2 WS-F6K-DFC4-A Distributed Forwarding Card 4 Rev. 1.0
#### 123456789
### GLC-SX-MMD
#### Chassis 2 Transceiver Gi2/9/47
#### Chassis 2 SFP Transceiver 1000BaseSX Gi2/9/47
#### 123456789
### GLC-LH-SMD
#### Chassis 2 Transceiver Gi2/9/6
#### Chassis 2 SFP Transceiver 1000BaseLH Gi2/9/6
#### 123456789
### WS-C6509-E-FAN
#### Chassis 2 WS-C6509-E-FAN 1
#### Chassis 2 Enhanced 9-slot Fan Tray 1
#### 123456789
### WS-CAC-6000W
#### Chassis 2 PS 2 WS-CAC-6000W
#### Chassis 2 AC power supply, 6000 watt 2
#### 123456789
### GLC-T
#### Chassis 2 Transceiver Gi2/9/48
#### Chassis 2 SFP Transceiver 1000BaseT Gi2/9/48
#### 123456789
## Vlans
### 10 - RED
#### active
#### Interfaces
##### TenGigabitEthernet1/1/4
##### TenGigabitEthernet1/2/2
##### TenGigabitEthernet1/2/4
### 20 - BLUE
#### active
#### Interfaces
##### TenGigabitEthernet1/2/3
##### TenGigabitEthernet1/2/5
##### TenGigabitEthernet1/2/7
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
## neighbors
### CDP
#### Port-channel1
##### Routed Port-channel
##### **Local Interfaces**: 
###### TenGigabitEthernet1/1/1 
###### TenGigabitEthernet2/1/1
##### **Remote Interfaces** 
###### TenGigabitEthernet2/1/1 
###### TenGigabitEthernet1/1/1
##### **IP Address:**192.168.1.5
##### ***DIST***
#### Port-channel2
##### Switched Port-channel
##### **VLAN(s)**: 10,20
##### **Local Interfaces**: 
###### TenGigabitEthernet1/1/2 
###### TenGigabitEthernet2/1/2
##### **Remote Interfaces** 
###### TwentyFiveGigE1/1/1 
###### TwentyFiveGigE2/1/1
##### **IP Address:**192.168.2.5
##### ***Catalyst Switch 1***
#### Nexus Switch 1
##### **Platform**: N77-C7706
##### **Local Port**:TenGigabitEthernet1/1/7
##### **Remote Port**:Ethernet1/3
## MAC Addresses
### 10
#### 1111.2222.3333
#### aaaa.bbbb.cccc
### 20
#### 1111.2222.3333
#### aaaa.bbbb.cccc
## ARP table
## ARP table
### Vlan10
#### 192.168.1.10
##### age: -
##### Link Layer Address: 1111.2222.3333
##### protocol: Internet
### Port-channel1
#### 192.168.2.10
##### age: 120
##### Link Layer Address: aaaa.bbbb.cccc
##### protocol: Internet
#### 192.168.1.5
##### age: -
##### Link Layer Address: 0008.e3ff.fe50
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
##### 0008.e3ff.fc04
##### Enabled: True
##### never
##### never
#### Port-channel3.10
##### 0008.e3ff.fc04
##### Enabled: True
##### 
##### 
#### Port-channel3.20
##### 0008.e3ff.fc04
##### Enabled: True
##### 
##### 
### Tunnels
#### Tunnel1
##### 
##### Enabled: True
##### never
##### never
### Vlans
#### Vlan10
##### 0008.e3ff.fc04
##### Enabled: False
##### never
##### never
#### Vlan20
##### 0008.e3ff.fc04
##### Enabled: True
##### 02:09:04
##### never
### Loopbacks
#### Loopback0
##### 
##### Enabled: True
##### never
##### never
### Ethernet
### FastEthernet
### GigabitEthernet
#### GigabitEthernet1/5/1
##### 
##### Enabled: False
##### never
##### never
### 2.5 GigabitEthernet
### Ten GigabitEthernet
#### TenGigabitEthernet1/1/1
##### 
##### Enabled: True
##### never
##### never
### TwentyFive GigabitEthernet
### Forty GigabitEthernet