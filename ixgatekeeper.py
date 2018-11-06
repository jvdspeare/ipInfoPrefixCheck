import requests
import ipaddress


# user input of asn, ip subnet in cidr notation and ipinfo.io token
def user_input(asn_prompt, cidr_prompt, token_prompt):
    user_input.asn = input(asn_prompt)
    cidr_input = input(cidr_prompt)
    user_input.cidr = cidr_input.split(', ')
    user_input.token = input(token_prompt)


# define the network and broadcast ip addresses from the ip subnet, given in cidr notation
def cidr_ip(cidr):
    ip_range = ipaddress.ip_network(cidr)
    cidr_ip.response = [ip_range.network_address, ip_range.broadcast_address]


# api call to ipinfo.io to return ip address information
def ip_info(ip, token):
    response = requests.get(url='http://ipinfo.io/' + str(ip) + '?token=' + str(token))
    ip_info.response = response.json()


# lookup the network and broadcast address for the ip subnet on ipinfo.io
def ip_check(asn, cidr, ipinfo_token):
    ip_info_org = list()
    cidr_ip(cidr)
    cidr_ip.response
    for i in cidr_ip.response:
        ip_info(i, ipinfo_token)
        ip_info_org.append(ip_info.response['org'])
    if ip_info_org[0] == ip_info_org[1]:
        if asn in ip_info_org[0] and asn in ip_info_org[1]:
            ip_check.response = True
        else:
            ip_check.response = False
    else:
        ip_check.response = False


# prompt user for input
user_input('Enter ASN:', 'Enter IP Subnet:', 'ipinfo.io Token:')

# run ip_check for each ip subnet
for i in user_input.cidr:
    ip_check(user_input.asn, i, user_input.token)
    if ip_check.response is True:
        print(i + ' is associated with AS' + user_input.asn)
    else:
        print(i + ' is NOT associated with AS' + user_input.asn)
