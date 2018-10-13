import sched, time, datetime

s = sched.scheduler(time.time, time.sleep)

def get_next_cyclic_time(day_of_week,hour,minute):
    if day_of_week == -1:
        et1 = get_next_daily_time(hour,minute)
        return et1
    d = datetime.datetime.now()
    today_of_week = d.weekday()
    et1 = datetime.datetime(d.year, d.month, d.day, hour, minute)
    if today_of_week == day_of_week:
        if hour*60+minute < d.hour*60+d.minute:
            et1 += datetime.timedelta(days=7)
    else:
        day1 = day_of_week - today_of_week
        if day1 < 0:
            day1 += 7
        et1 += datetime.timedelta(days=day1)
    print('set weekly schedule: next time ',et1,et1.weekday())
    et1 = int(time.mktime(et1.timetuple()))  # UNIX時間に変換
    return et1

def get_next_daily_time(hour,minute):
    d = datetime.datetime.now()
    et1 = datetime.datetime(d.year, d.month, d.day, hour, minute)
    if hour*60+minute <= d.hour*60+d.minute:
        et1 += datetime.timedelta(days=1)
    print('set daily schedule: next time ',et1)
    et1 = int(time.mktime(et1.timetuple()))  # UNIX時間に変換
    return et1

def processing(a):
    print(datetime.datetime.now(), a)

def set_cyclic_schedule(process, day_of_week, hour, minute=0):
    while True:
        et1 = get_next_cyclic_time(day_of_week,hour,minute)
        s.enterabs(et1, 1, process, argument=('event1',))
        s.run()

if __name__ == '__main__' :
    print('曜日を指定してください。[daily:-1, weekly:0-6]')
    d0 = int(input('Mon:0,Tue:1,Wed:2,Thu:3,Fri:4,Sat:5,Sun:6＞'))
    h0 = int(input('時間を指定してください。[0-23]＞'))
    m0 = int(input('分を指定してください。[0-59]＞'))
    set_cyclic_schedule(processing,d0,h0,m0)
