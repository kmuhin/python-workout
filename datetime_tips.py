from datetime import datetime, timezone, time, timedelta


def p(message, *args):
    if args:
        print(' ', message.ljust(35), str(args[0]).ljust(35), *args[1:])
    else:
        print(' ', message)


# now
now = datetime.now()
print(type(now))
p('now', now)

# combine date and time
d_combined = datetime.combine(now, time(4, 0))
p('now date and time=4:00', d_combined)

# min max time
## replace
## 1.14 µs ± 3.38 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
dt_min = now.replace(hour=0, minute=0, second=0, microsecond=0)
dt_max = now.replace(hour=23, minute=59, second=59, microsecond=999999)
p('now min time as .replace():', dt_min)
p('now max time as .replace():', dt_max)
## combine
## 266 ns ± 1.41 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
dt_min = datetime.combine(now, time.min)
dt_max = datetime.combine(now, time.max)
p('now min time as .combine():', dt_min, '- .combine() is much faster')
p('now max time as .combine():', dt_max, '- .combine() is much faster')

# custom date 2020-09-06 01:21
ddate = datetime(2020, 9, 6, 1, 21)
p('ddate', ddate)

# yesterday timedelta
yesterday = (datetime.now() - timedelta(days=1))
print('yesterday: ', yesterday)
print('- 1 hour:', (datetime.now() - timedelta(hours=1)))

# str: 2020-09-06 01:21
# 8.39 µs ± 98.5 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
ddate_formated = f'{ddate:%Y-%m-%d %H:%M}'
print('ddate_formated type is ', type(ddate_formated))
p('ddate_formated as %Y-%m-%d %H:%M', ddate_formated)

# same str with isoformat: 2020-09-06 01:21
# 1.26 µs ± 28 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
ddate_formated = ddate.isoformat(timespec='minutes', sep=' ')
print('ddate_formated type is ', type(ddate_formated))
p('ddate_formated as .isoformat()', ddate_formated, '- isoformat() is much faster')

# timestamp, unixtime
# the timestamp is always utc
# float
now_timestamp = now.timestamp()
print('datetime.timestamp() is ', type(now_timestamp))
p('now timestamp', now_timestamp, '- the timestamp is always utc')
p('ddate timestamp', ddate.timestamp())

# change zone to UTC
print('change time zone to UTC with datetime.astimezone(timezone.utc)')
now_utc = now.astimezone(timezone.utc)
ddate_utc = ddate.astimezone(timezone.utc)
p('now.utc timestamp', now_utc.timestamp(), '- same as original')
p('ddate_utc timestamp', ddate_utc.timestamp())

# replace zone to UTC
# float: 1599356278.589493
print('replace time zone to UTC with datetime.replace(tzinfo=timezone.utc)')
print('now_utc and  now_zone_replaced are not the same')
now_zone_replaced = now.replace(tzinfo=timezone.utc)
ddate_zone_replaced = ddate.replace(tzinfo=timezone.utc)
p('now_zone_replaced', now_zone_replaced)
p('ddate_zone_replaced', ddate_zone_replaced)
p('now_zone_replaced timestamp', now_zone_replaced.timestamp(), '- same as original')
p('ddate_zone_replaced timestamp', ddate_zone_replaced.timestamp())

p('now_zone_replaced - now', now_zone_replaced - now_utc)
