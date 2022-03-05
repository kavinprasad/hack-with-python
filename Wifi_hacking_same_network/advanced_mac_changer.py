####### change mac address script #######

import subprocess
import optparse
import re


#python change_mac_address.py  --interface eth0 --mac 00:99:88:44:22:11

def get_options():
  parser = optparse.OptionParser()
  parser.add_option("-i", "--interface", dest="interfaces", help="Used to select the interface")
  parser.add_option("-m", "--mac", dest="new_macs",help="Use to select the mac")
  (options, arguments)=parser.parse_args()
  if not options.interfaces:
    parser.error("Interface is not specified. Use --help to get info")
  elif not options.new_macs:
    parser.error("Mac Id not specified. Use --help to get info")
  else:
    return options

#interface = options.interface
#new_mac = options.new_mac



#safe and security
def change_mac(interface,new_mac):
  subprocess.call(["ifconfig" , interface , "down"])
  subprocess.call(["ifconfig" , interface , "hw" , "ether" ,new_mac])
  subprocess.call(["ifconfig" , interface , "up"])
  
def get_mac_address(interface):
  ifconfig_result = subprocess.check_output("ifconfig ",interface)
  filter_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w" , ifconfig_result)
  if filter_result:
    print(filter_result.group(0))
  else:
    print("MAC Address Not Found")


options = get_options()
mac_address_filter_results = get_mac_address(options.interfaces)
print("Current MAC = " + str(mac_address_filter_results))


change_mac(options.interfaces,options.new_macs)

mac_address_filter_results = get_mac_address(options.interfaces)
if (mac_address_filter_results == options.new_macs):
  print("MAC Address Changed To : " , mac_address_filter_results)
else:
  print("MAC Address is not changed")















#unsafe and unsecurity

#interface = input("Enter The Interface : ")
#new_mac = input("Enter The Mac Address : ")

#subprocess.call("ifconfig " + interface + " down")
#subprocess.call("ifconfig " + interface + " hw" + " ether " + new_mac)
#subprocess.call("ifconfig " + interface + " up")
#subprocess.call("ifconfig")

#Print("----------Mac Address Changed Successfully---------")

   
    
    
    
