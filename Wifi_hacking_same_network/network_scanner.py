#############      Network Scanner       ############

# Running only python 3
import scapy.all as scapy
import argparse


def get_arguments():
  parser = argparse.ArgumentParser()
  parser.add_argument("-r", "--range", dest="range", help="Use --range to scan your Network ")
  options = parser.parse_args()
  if not options.range:
    parser.error("Please Specify An Options ")
  else:
    return options


def scan(ip):  ####scapy.arping(ip)
  arp_request = scapy.ARP(pdst=ip)
  source_destination = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
  final = source_destination / arp_request
  answered_lists = scapy.srp(final, timeout=1, verbose=False)[0]

  result_list = []
  for answer in answered_lists:
    result_dic = {"ip": answer[1].psrc, "mac": answer[1].hwsrc}
    result_list.append(result_dic)
  return result_list


def print_results(results_lists):
  print(
    "________________________________________________\n\nIPADDRESS\t\t MAC ADDRESS\n________________________________________________")

  for result in results_lists:
    print(result["ip"] + "\t\t" + result["mac"])


options = get_arguments()
result_dic = scan(options.range)
print_results(result_dic)
