# ----------------
# Python
# ----------------
import os
import sys
import time
import json
import shutil
import logging
import ast
import re
from pyats import aetest
from pyats import topology
from pyats.log.utils import banner
from jinja2 import Environment, FileSystemLoader
from general_functionalities import ParseShowCommandFunction

# ----------------
# Get logger for script
# ----------------

log = logging.getLogger(__name__)

# ----------------
# Template Directory
# ----------------

template_dir = 'Templates/'
env = Environment(loader=FileSystemLoader(template_dir))

# ----------------
# AE Test Setup
# ----------------
class common_setup(aetest.CommonSetup):
    """Common Setup section"""
    @aetest.subsection
    def connect_sh_devices(self, testbed):
        """Connect to all the devices"""
        testbed.connect()

# ----------------
# Test Case #1
# ----------------
class Collect_Information(aetest.Testcase):
    """Parse all the commands"""

    @aetest.test
    def parse(self, testbed, section, steps):
        """ Testcase Setup section """
        # ---------------------------------------
        # Loop over devices
        # ---------------------------------------
        for device in testbed:
            # ---------------------------------------
            # Execute parser for various show commands
            # ---------------------------------------

            ### Show ARP Table
            full_arp_list={}
            if device.type != 'switch':
                if device.os == 'nxos':
                    self.parsed_show_vrf = ParseShowCommandFunction.parse_show_command(steps, device, "show vrf")
                    for item in self.parsed_show_vrf['vrfs']:
                        self.parsed_show_arp = ParseShowCommandFunction.parse_show_command(steps, device, f"show ip arp vrf {item}")
                        full_arp_list[item] = self.parsed_show_arp['interfaces']
                else:
                    self.parsed_show_vrf = ParseShowCommandFunction.parse_show_command(steps, device, "show vrf")
                    self.parsed_show_arp = ParseShowCommandFunction.parse_show_command(steps, device, "show arp ")
                    full_arp_list['default'] = self.parsed_show_arp['interfaces']
                    for item in self.parsed_show_vrf['vrf']:
                        if item != "mgmtVrf":
                            self.parsed_show_arp = ParseShowCommandFunction.parse_show_command(steps, device, f"show arp vrf {item}")
                            full_arp_list[item] = self.parsed_show_arp['interfaces']
    
                print(full_arp_list)

            ### Show CDP Neighbors Detail           
            self.parsed_show_cdp_neighbors_detail = ParseShowCommandFunction.parse_show_command(steps, device, "show cdp neighbors detail")

            ### Show LLDP Neighbors Detail           
            self.parsed_show_lldp_neighbors_detail = ParseShowCommandFunction.parse_show_command(steps, device, "show lldp neighbors detail")

            ### Show Etherchannel/Port-Channel Summary
            if device.os == 'nxos':
                self.parsed_show_etherchannel_summary = ParseShowCommandFunction.parse_show_command(steps, device, "show port-channel summary")
            else:
                self.parsed_show_etherchannel_summary = ParseShowCommandFunction.parse_show_command(steps, device, "show etherchannel summary")

            ### Show Interfaces
            if device.os != 'nxos':
                self.parsed_show_int = ParseShowCommandFunction.parse_show_command(steps, device, "show interfaces")

            ### Show Interfaces Trunk
            if device.os != 'nxos':
                self.parsed_show_interfaces_trunk = ParseShowCommandFunction.parse_show_command(steps, device, "show interfaces trunk")

            ### Show Inventory
            self.parsed_show_inventory = ParseShowCommandFunction.parse_show_command(steps, device, "show inventory")

            ### Show MAC Address-Table
            self.parsed_show_mac_address_table = ParseShowCommandFunction.parse_show_command(steps, device, "show mac address-table")

            ### Show Version
            self.parsed_show_version = ParseShowCommandFunction.parse_show_command(steps, device, "show version")

            ### Show VLAN
            self.parsed_show_vlan = ParseShowCommandFunction.parse_show_command(steps, device, "show vlan")

            ### Show VRF
            if device.type != 'switch':
                self.parsed_show_vrf = ParseShowCommandFunction.parse_show_command(steps, device, "show vrf")

            # ---------------------------------------
            # Create JSON, YAML, CSV, MD, HTML, HTML Mind Map files from the Parsed Data
            # ---------------------------------------         
            
            with steps.start('Store data',continue_=True) as step:

                ###############################
                # Genie Show Command Section
                ###############################

                ### Check CDP Neighbor is not empty
                if self.parsed_show_cdp_neighbors_detail is not None:

                    ### Create list of CDP neighbors to remove duplicate entries and remove DNS address String
                    neighborList=[]
                    if self.parsed_show_cdp_neighbors_detail['index'] is not None:  
                        for item in self.parsed_show_cdp_neighbors_detail['index']:
                            if self.parsed_show_cdp_neighbors_detail['index'][item]['device_id'] is not None:
                                neighborList.append(self.parsed_show_cdp_neighbors_detail['index'][item]['device_id'])
                            else:
                                neighborList.append(self.parsed_show_cdp_neighbors_detail['index'][item]['platform'])

                    if self.parsed_show_lldp_neighbors_detail is not None:  
                        for int in self.parsed_show_lldp_neighbors_detail['interfaces']:
                            for port in self.parsed_show_lldp_neighbors_detail['interfaces'][int]['port_id']:
                                for neighbor in self.parsed_show_lldp_neighbors_detail['interfaces'][int]['port_id'][port]['neighbors']:
                                    neighborList.append(neighbor)

                    neighborList = list( dict.fromkeys(neighborList) )

                    ## create per device informational MindMap
                    formatted_device_map_template = env.get_template('formattedDeviceMap.j2')
                    
                    if device.type == 'switch':
                        self.parsed_show_vrf={}

                    if device.os == 'nxos':
                        self.parsed_show_int='Parser Broken'
                        self.parsed_show_interfaces_trunk='Parser Broken'

                    print(device.os)

                    parsed_output_type = formatted_device_map_template.render(
                        inventory_hostname=device.alias,
                        device_os=device.os,
                        sh_arp_parsed=full_arp_list,
                        sh_cdp_neigh_det_parsed=self.parsed_show_cdp_neighbors_detail['index'],
                        sh_parse_lldp_detail=self.parsed_show_lldp_neighbors_detail,
                        sh_pc_sum_parsed=self.parsed_show_etherchannel_summary,
                        sh_int_parsed=self.parsed_show_int,
                        sh_trunk_parsed=self.parsed_show_interfaces_trunk,
                        sh_inventory_parsed=self.parsed_show_inventory,
                        sh_mac_table_parsed=self.parsed_show_mac_address_table['mac_table'],
                        sh_version_parsed=self.parsed_show_version,
                        sh_vlan_parsed=self.parsed_show_vlan['vlans'],
                        sh_vrf_parsed=self.parsed_show_vrf                      
                        )

                    with open(f"Network/Devices/{ device.alias }_MindMap.md", "w") as fh:
                        fh.write(parsed_output_type)               
                        fh.close()

                    os.system(f'markmap --no-open Network/Devices/{ device.alias }_MindMap.md --output Network/Devices/{ device.alias }_MindMap.html')

                    ### Create L2 Topology - Core
                    l2_core_map_template = env.get_template('l2_core_neighbor.j2')
                    if device.role=='core':
                        parsed_output_type = l2_core_map_template.render(
                            inventory_hostname=device.alias,
                            neighbors=neighborList
                            )
                        
                        with open(f"Network/L2_MindMap.md", "w") as fh:
                            fh.write(parsed_output_type)               
                            fh.close()

                    ### Modify L2 Topology - Distribution
                    l2_dist_map_template = env.get_template('l2_dist_neighbor.j2')
                    if device.role=='dist':
                        parsed_output_type = l2_dist_map_template.render(
                            device_testbed = testbed.devices,
                            inventory_hostname=device.alias,
                            neighbors=neighborList
                            )

                        temp = open('temp', 'w')
                        with open(f'Network/L2_MindMap.md', 'r') as fh:
                            for line in fh:
                                if line.startswith('## [' + device.alias):
                                    line = parsed_output_type
                                temp.write(line)
                        temp.close()
                        shutil.move('temp', 'Network/L2_MindMap.md')                          

                    ### Modify L2 Topology - Access
                    l2_access_map_template = env.get_template('l2_access_neighbor.j2')
                    if device.role=='access':
                        print(device.alias)
                        parsed_output_type = l2_access_map_template.render(
                            device_testbed = testbed.devices,
                            inventory_hostname=device.alias,
                            neighbors=neighborList
                            )

                        temp2 = open('temp2', 'w')
                        with open(f'Network/L2_MindMap.md', 'r') as fh:
                            for line in fh:
                                if line.startswith('### [' + device.alias):
                                    print('HIT')
                                    line = parsed_output_type
                                temp2.write(line)
                        temp2.close()
                        shutil.move('temp2', 'Network/L2_MindMap.md')

                    os.system(f'markmap --no-open Network/L2_MindMap.md --output Network/L2_MindMap.html')
        
        with steps.start('Disconnect from devices',continue_=True) as step:
            testbed.disconnect()
