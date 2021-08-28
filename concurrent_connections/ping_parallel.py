#!/usr/bin/env python3

import subprocess
import ipaddress
from concurrent.futures import ThreadPoolExecutor

def ping_ip(address):
    try:
        ipaddress.ip_address(address)
    except ValueError:
        print(address.ljust(20), 'incorrect address')
        return False
    result = subprocess.run(['ping', '-W1', '-nc3', address], 
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL)
    if not result.returncode:
        print(address.ljust(20))
        return True
    else:
        return False


def run_parallel():
    iplist = [f'10.0.2.{n}' for n in range(1,254)]
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(ping_ip, iplist)

run_parallel()
