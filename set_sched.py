# from crontab import CronTab
#
# cron = CronTab(tab="""  * * * * * command """)
# job  = cron.new(command='ls -lt')
#
# job.minute.every(1)
#
# # job.run()
# job.every_reboot()
#
# # for cron in CronTabs():
# #     print(cron)
#

import sched, time, datetime

s = sched.scheduler(time.time, time.sleep)

def set_weekly_timer(day_of_week,hour,minute):
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
    print('set timer: ',et1,et1.weekday())
    et1 = int(time.mktime(et1.timetuple()))  # UNIX時間に変換
    return et1

def processing(a):
    print(datetime.datetime.now(), a)

def schedule(day_of_week, hour, minute=0):
    while True:
        # d0 = int(input('曜日を指定してください。月曜0～日曜6＞'))
        # h0 = int(input('時間を指定してください。0-23＞'))
        # m0 = int(input('分を指定してください。0-59＞'))
        et1 = set_weekly_timer(day_of_week,hour,minute)
        s.enterabs(et1, 1, processing, argument=('event1',))
        s.run()

# if __name__ == '__main__' :
#     schedule(3,6,6)
