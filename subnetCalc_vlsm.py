import ipaddress

import subnetCalc_f1


num_of_subnets = int(input("How many network do you need: "))
user_input_ip = input("What is the ip address: ")
ip_add = ipaddress.IPv4Address(user_input_ip)
hosts = []
for i in range(1, num_of_subnets + 1):
    address_needs = int(input(f"How many host is needed for {i} subnet: "))
    hosts.append(address_needs)

hosts.sort(reverse=True)
print(hosts)

for host in hosts:
    print(f"The necessary ip addresses for subnet with {host} hosts is: ")
    broadcast_address = subnetCalc_f1.calculating_subnet(ip_add, host)
    ip_add = broadcast_address + 1


