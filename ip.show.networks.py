import ipaddress
import locale
locale.setlocale(locale.LC_ALL, '')

#print('{:>6} {:16} {:13} {}'.format('prefix','mask','addresses','networks'))
print('begin')
print("begin")
print(
    f"{'prefix':>6}"
    f" {'mask':16}"
    f" {'addresses':13}"
    f" {'networks'}"
)

for i in range(0,33):
    ip='0.0.0.0/'+str(i)
    a=ipaddress.IPv4Network(ip)
#    print('%-2d : %16s : %s' % (a.prefixlen,a.netmask,a.num_addresses))
#    print('{:6d} {:<16} {:,13} {:,.0f}'.format(a.prefixlen,str(a.netmask),a.num_addresses,a.num_addresses/256))
    print(
        f"{a.prefixlen:6d}"
        f" {str(a.netmask):<16}"
        f" {a.num_addresses:13n}"
        f" {a.num_addresses/256:,.0f}"
    )
