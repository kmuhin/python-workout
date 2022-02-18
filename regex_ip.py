import re

string_test = r' FastEthernet0/0       10.0.5.1       YES manual up   '

regexp_ip = r' +([\d.]{7,15}) +'

print(re.search(regexp_ip, string_test))
print(re.search(regexp_ip, string_test).groups())
