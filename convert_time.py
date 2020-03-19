import time, datetime
# convert millisecond to '00:00:39,770'
def format_time(ms):
    # ms = millisecond%1000
    # second = millisecond/1000
    # hour = millisecond/
    td = datetime.timedelta(milliseconds= ms)
    print("millisecond:",ms,"timestamp",str(td))
    return str(td)
    #return time.strftime("%H:%M:%S",timestamp)
start_time = time.localtime()
time.sleep(5)
end_time = time.localtime()

print('start:',time.strftime('%H:%M:%S',start_time),'end',time.strftime('%H:%M:%S',end_time),'during:',
      format_time(1000*(time.mktime(end_time)-time.mktime(start_time) ) ) )

format_time(436)