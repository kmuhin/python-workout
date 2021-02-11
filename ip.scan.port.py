import socket
import ipaddress
import sys
from multiprocessing.dummy import Pool as ThreadPool


def port_scan(ip):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result=sock.connect_ex((str(ip),scanport))
    except:
        pass
    finally:
        sock.close()

    if result == 0:
        return str(ip)
    else:
        return None


if len(sys.argv)<2:
    print('Usage with a subnet:',sys.argv[0],'x.x.x.x/x')
    sys.exit(1)

if len(sys.argv)>2:
        scanport=int(sys.argv[2])
else:
        scanport=3389

hosts_to_scan=ipaddress.ip_network(sys.argv[1]).hosts()

if hosts_to_scan is None:
    sys.exit(1)

port_scan_pool = ThreadPool(100)

port_scan_result = port_scan_pool.map(port_scan,hosts_to_scan)
try:
    port_scan_pool.join()
    port_scan_pool.close()
except:
    pass

    # Filter the result to only include IP-addresses
hosts_with_port_3389_open = [x for x in port_scan_result if x is not None]


# print(*hosts_with_port_3389_open,sep='\n')
for i in hosts_with_port_3389_open:
    try:
        dns=socket.gethostbyaddr(i)
    except:
        dns=['']
    #{:0>3}.{:0>3}.{:0>3}.{:0>3}'.format(*a.split('.'))
    print('{:16} {}'.format(i,dns[0]))
print('='*16)
print('Total:{:10}'.format(len(hosts_with_port_3389_open)))