# author still testing the code 
import os
import subprocess

filename = ".ssh/config"

if not os.path.exists(".ssh"):
    os.makedirs(".ssh")
    print("ssh folder created\n")

if os.path.exists(filename):
    print("""
**Config File exists**\n
**Now we editing the same Config file**\n
    """)
    config = open(filename, 'a')
else:
    print("**Creating The ssh config File**\n")
    config = open(filename, 'w')

y ='y' 

if raw_input("Do you want to create ssh key [y/N]. You can skip with Enter: ") == 'y':
    os.system("ssh-keygen -t rsa")
print("\n")

if raw_input("Do you want to show the current IP addresses with (ifconfig) command: [y/N] " ) == 'y':
    os.system("ipconfig | findstr IPv4")
print("\n")


print("Proceeding to Nmap scan")
print("\n")

scan_nmap = raw_input("Enter your IP to scan your network for open ssh ports: ")
subnet_mask = int(raw_input("Enter the subnet mask: "))
scan_option = raw_input("Enter scan option - Recommended (-v): ")

os.system("nmap " + scan_option + " " + str(scan_nmap) + "/" + str(subnet_mask) + "| findstr ssh")
print("\n")

scan_ip_address = raw_input("Enter IP address to scan your network for IP Addresses: ")
subnet_mask2 = int(input("Enter the subnet mask: "))
scan_option2 = raw_input("Enter scan option - Recommended (-v): ")

process = subprocess.Popen(
    "nmap " + scan_option2 + " " + str(scan_ip_address) + "/" + str(subnet_mask2) +  "  |  findstr Discovered",
    shell=True,
    stdout=subprocess.PIPE,
)

stdout_list = process.communicate()[0].decode('utf-8')
command = stdout_list.split('\n')


def ask_for_input(text):
    user_input = None
    while not user_input:
        user_input = raw_input(text)
    return user_input


def ask_for_input_root(text):
    user_input_root = None
    while not user_input_root:
        user_input_root = raw_input(text)
    return user_input_root

template = """
Host {machine_name}
Hostname {selected_ip}
Port {port}
User {user}
"""

try:
    for ip_string in command:
        if ip_string:
            ip = ip_string.split()[-1]
            if raw_input("Discovered IP: " + "(" + ip + ")" + "\n" + "Do you want to select this IP Address [y/N]:") == 'y':
                selected_ip = ip
                machine_name = ask_for_input("Please Enter Machine Name: ")
                root_user = ask_for_input_root("This for the root user:")
                port = raw_input("Please Enter The Port Number. Skip with Enter: ") or '22'
                user = ask_for_input("Please Enter The User: ")
                ssh_to_machine = raw_input("Copy the ssh id to the machine. Do you want to continue (y) ").lower()
                ssh_to_root = raw_input("Copy the ssh id to root. Do you want to continue (y):").lower()

                normal_config = template.format(
                    machine_name=machine_name,
                    root_user=root_user,
                    port=port,
                    user=user,
                    selected_ip=selected_ip,
                )
                config.write(normal_config)

                if ssh_to_root == 'y':
                  root_config = template.format(
                      machine_name=root_user,
                      root_user=root_user,
                      port=port,
                      user='root',
                      selected_ip=selected_ip,
                      )
                  config.write(root_config)

                if ssh_to_machine:
                  os.system("ssh-copy-id " + user + "@" + selected_ip)

                if ssh_to_root:
                   os.system("ssh -t " + user + "@" + selected_ip  + " " + " " " 'sudo cp --parents .ssh/authorized_keys /root/' ")
                print("Finished and starting with the new machine\n\n")

except KeyboardInterrupt:
    config.close()
print("Information saved")
