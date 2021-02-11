import ipaddress
from decorator_timing import timing

# convert ip from string to integer
@timing
def ip2int_math(address):
    ip_int =[int(ip) for ip in address.split('.')]
    res = (16777216 * ip_int[0]) + (65536 * ip_int[1]) + (256 * ip_int[2]) + ip_int[3]
    return res


# convert ip from integer to string
@timing
def int2ip_math(ipnum):
    o1 = int(ipnum / 16777216) % 256
    o2 = int(ipnum / 65536) % 256
    o3 = int(ipnum / 256) % 256
    o4 = int(ipnum) % 256
    return '%(o1)s.%(o2)s.%(o3)s.%(o4)s' % locals()

# convert ip from string to integer with f-strings
# example: int(f'{192:08b}{168:08b}{0:08b}{1:08b}',2)
@timing
def ip2int_bin(address):
    ip_int =[int(ip) for ip in address.split('.')]
    return int(f'{ip_int[0]:08b}{ip_int[1]:08b}{ip_int[2]:08b}{ip_int[3]:08b}',2)


# convert ip from string to integer with ipaddress module
@timing
def ip2int_ipaddress(address):
    return int(ipaddress.IPv4Address(address))

# convert ip from integer to string with ipaddress module
@timing
def int2ip_ipaddress(ipnum):
    return str(ipaddress.IPv4Address(ipnum))


# convert list of ip and ranges of ip to list of pure ip addresses
def convert_ranges_to_ip_list(addresses:list):
    '''
    convert ranges of addresses to list of addresses
    return list of addresses
    input example of ranges: ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
    output: ['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128', '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']
    '''
    result_addresses = []
    for address in addresses:
        ip_range = address.split('-')
        # not ip_range
        if len(ip_range) == 1:
            result_addresses.append(ip_range[0])
            continue
        # range
        # if second part is number, not address.
        if ip_range[1].isdigit():
            prefix, _ = ip_range[0].rsplit('.',1)
            ip_range[1] = prefix+'.'+ip_range[1]
        # convert addresses to int
        ip1_int = int(ipaddress.IPv4Address(ip_range[0]))
        ip2_int = int(ipaddress.IPv4Address(ip_range[1]))
        for ip in range(ip1_int, ip2_int+1):
            result_addresses.append(str(ipaddress.IPv4Address(ip)))
    return result_addresses

if __name__ == '__main__':
    ip = '192.168.0.1'
    ip_int = 3232235521
    print('ip: ', ip)
    print(ip2int_math(ip))
    print(ip2int_bin(ip))
    print(ip2int_ipaddress(ip))
    print('ip_int: ', ip_int)
    print(int2ip_math(ip_int))
    print(int2ip_ipaddress(ip_int))

