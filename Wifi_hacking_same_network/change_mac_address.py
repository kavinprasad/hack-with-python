####### change mac address script #######

import subprocess
import optparse


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

#interface = options.interfaces
#new_mac = options.new_macs


#safe and security
def change_mac(interface,new_mac):
	print("Changing Mac Address " + interface + " To " + new_mac)
	subprocess.call(["ifconfig" , interface , "down"])
	subprocess.call(["ifconfig" , interface , "hw" , "ether" ,new_mac])
	subprocess.call(["ifconfig" , interface , "up"])
	
options=get_options()
change_mac(options.interfaces,options.new_macs)

print("---------------Mac Address Changed Successfully---------------")







#unsafe and unsecurity

#interface = input("Enter The Interface : ")
#new_mac = input("Enter The Mac Address : ")

#subprocess.call("ifconfig " + interface + " down")
#subprocess.call("ifconfig " + interface + " hw" + " ether " + new_mac)
#subprocess.call("ifconfig " + interface + " up")
#subprocess.call("ifconfig")

#Print("----------Mac Address Changed Successfully---------")

   
