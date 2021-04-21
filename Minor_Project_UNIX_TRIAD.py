#!/usr/bin/python
import socket
import ipaddress
import re
import urllib.parse as urlparse
import requests
import argparse
import scapy.all as scapy

print('''
     :::    ::: ::::    ::: ::::::::::: :::    :::      ::::::::::: :::::::::  :::::::::::     :::     ::::::::: 
    :+:    :+: :+:+:   :+:     :+:     :+:    :+:          :+:     :+:    :+:     :+:       :+: :+:   :+:    :+: 
   +:+    +:+ :+:+:+  +:+     +:+      +:+  +:+           +:+     +:+    +:+     +:+      +:+   +:+  +:+    +:+  
  +#+    +:+ +#+ +:+ +#+     +#+       +#++:+            +#+     +#++:++#:      +#+     +#++:++#++: +#+    +:+   
 +#+    +#+ +#+  +#+#+#     +#+      +#+  +#+           +#+     +#+    +#+     +#+     +#+     +#+ +#+    +#+    
#+#    #+# #+#   #+#+#     #+#     #+#    #+#          #+#     #+#    #+#     #+#     #+#     #+# #+#    #+#     
########  ###    #### ########### ###    ###          ###     ###    ### ########### ###     ### #########       


MADE BY : -
SARTHAK KULSHRESTHA
ANSHUMAN SHARMA
TANVEER SINGH
''')

choose_option = input("Welcome to the tool. Kinldy choose from the following\n1.Port Scanner\n2.Spider Crawler\n3.Network Scanner\n")

if choose_option == '1':
    port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

    port_min = 0
    port_max = 65535

    open_ports = []
    while True:
        ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
    
        try:
            ip_address_obj = ipaddress.ip_address(ip_add_entered)
            print("You entered a valid ip address.")
            break
        except:
            print("You entered an invalid ip address")
    

    while True:
        print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
        port_range = input("Enter port range: ")
        port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
        if port_range_valid:
            port_min = int(port_range_valid.group(1))
            port_max = int(port_range_valid.group(2))
            break

    for port in range(port_min, port_max + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                s.connect((ip_add_entered, port))
                open_ports.append(port)

        except:
            pass

    for port in open_ports:
        print(f"Port {port} is open on {ip_add_entered}.")

if choose_option == '2':
    target_url = input("Enter the URL")
    target_links = []

    def extract_links(url):
        response = requests.get(url)
        return re.findall('(?:href=")(.*?)"', response.content.decode(errors="ignore"))

    def crawl(url):
        href_link = extract_links(url)
        for link in href_link:
            link = urlparse.urljoin(url, link)
        
            if "#" in link:
                link = link.split("#")[0]
        
            if target_url in link and link not in target_links:
                target_links.append(link)
                print(link)
                crawl(link)
    
    try:
        crawl(target_url) 
    except KeyboardInterrupt:
        print("[+] --------------QUITTING----------------")

if choose_option == '3':
import argparse
import scapy.all as scapy

ip = input("Enter IP\n")
def scan(ip):
    
    arp = scapy.ARP(pdst=ip)
    broad = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broad = broad/arp
    answer = scapy.srp(arp_broad, timeout=1, verbose=False)[0]
    client_list = []
    for i in answer:
        client_dict = {"IP":i[1].psrc, "MAC": i[1].hwdst}
        client_list.append(client_dict)
    return client_list

def scan_result(result_list):
    print("IP\t\t\tMAC Address\n--------------------------------------")
    for j in result_list:
        print(j["IP"]+ "\t\t" + j["MAC"])

result = scan(ip)
scan_result(result)
