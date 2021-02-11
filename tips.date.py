from datetime import datetime, timezone, time

def p(message, *args):
    print(' ', message.ljust(35), *args)

#now
now = datetime.now()
print(type(now))
p('now', now)

# combine date and time
d_combined = datetime.combine(now, time(4, 0))
p('now and 4:00', d_combined)

# custom date 2020-09-06 01:21
ddate = datetime(2020, 9, 6, 1, 21)
p('ddate', ddate)

# str: 2020-09-06 01:21
ddate_formated = f'{ddate:%Y-%m-%d %H:%M}'
print('f"{datetime}" is ',type(ddate_formated))
p('ddate_formated', ddate_formated)

# timestamp, unixtime
# float
now_timestamp = now.timestamp()
print('datetime.timestamp() is ', type(now_timestamp))
p('now timestamp', now_timestamp)
p('ddate timestamp', ddate.timestamp())

#change zone to UTC
print('change time zone to UTC with datetime.astimezone(timezone.utc)')
now_utc = now.astimezone(timezone.utc)
ddate_utc = ddate.astimezone(timezone.utc)
p('now.utc timestamp', now_utc.timestamp())
p('ddate_utc timestamp', ddate_utc.timestamp())


# replace zone to UTC
# float: 1599356278.589493
print('replace time zone to UTC with datetime.replace(tzinfo=timezone.utc)')
print('now_utc and  now_zone_replaced are not the same')
now_zone_replaced = now.replace(tzinfo=timezone.utc)
ddate_zone_replaced = ddate.replace(tzinfo=timezone.utc)
p('now_zone_replaced', now_zone_replaced)
p('ddate_zone_replaced', ddate_zone_replaced)
p('now_zone_replaced timestamp', now_zone_replaced.timestamp())
p('ddate_zone_replaced timestamp', ddate_zone_replaced.timestamp())

p('now_zone_replaced - now', now_zone_replaced - now_utc)

