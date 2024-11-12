import ipaddress

def calculating_subnet(provided_ip, num_of_host):
    x = ipaddress.IPv4Address(provided_ip)
    y = '{:#b}'.format(x)
    z = " ".join([y[i+2:i+10] for i in range(0, len(y), 8)])

    for i in range(1,32):
        w = 2 ** i
        if w >= num_of_host:
            num_to_divide = i
            break

    network_potion = 33 - num_to_divide
    calculated_value = z[:network_potion+2] + " , " + z[network_potion+2:]
    network_address, host_address = calculated_value.split(" , ")
    network_address1 = (network_address + host_address).replace(" ", "") 
    network_address1 = ipaddress.IPv4Address(int(network_address1, 2))
    host_address = host_address.replace("0", "1")
    broadcast_address = network_address + host_address
    broadcast_address = broadcast_address.replace(" ", "")
    broadcast_address = ipaddress.IPv4Address(int(broadcast_address, 2))
    last_usable_address = broadcast_address - 1
    first_usable_address = network_address1 + 1

    print(f"""
    network address is: {network_address1}/{network_potion}; 
    broadcast address is {broadcast_address}/{network_potion}; 
    first usable address is {first_usable_address}/{network_potion}; 
    last usable address is {last_usable_address}/{network_potion}
    """)
    return broadcast_address




if __name__ == "__main__":
    user_ip = input("What is your ip: ")
    required_hosts = int(input("How many hosts/devices do you need: "))
    calculating_subnet(user_ip,required_hosts)

