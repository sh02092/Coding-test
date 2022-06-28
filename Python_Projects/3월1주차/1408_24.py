
now_time = list(map(int, input().split(':')))
start_time = list(map(int, input().split(':')))

now_sec = now_time[0] * 3600 + now_time[1] * 60 + now_time[2]
start_sec = start_time[0] * 3600 + start_time[1] * 60 + start_time[2]
# now_sec = int(now_sec)
# start_sec = int(start_sec)
total = start_sec + 24*3600 - now_sec

total = int(total)
if total >= 24 * 3600:
    total -= 24 * 3600

total_time = []
hour = total // 3600
total_time.append(hour) # hour
total %= 3600
minute = total // 60
total_time.append(minute) # minute
total %= 60
total_time.append(total) # second

print('%02d:%02d:%02d'%(total_time[0], total_time[1], total_time[2]))