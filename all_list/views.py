from django.shortcuts import render
from django.http import HttpResponse
import calendar
import datetime as dt

from .models import ToDo

def show_cal(request):
    year = 2021
    month = 2

    year_and_month = str(year) + "年" + str(month) + "月"

    #day_countにその月の日数を代入
    day_count = calendar.monthrange(year, month)[1]

    #カレンダーの始まりを日曜日から
    calendar.setfirstweekday(6)

    cal_data = calendar.monthcalendar(year, month)
    print(cal_data)

    day = 0

    monthly_calendar = []
    for i in range(len(cal_data)):
        #曜日が入っていない要素は空白にする
        temporary_cal_data = [' ' if day == 0 else str(day) for day in cal_data[i]]
        temporary_list = []
        print(temporary_cal_data)
        for j in range(len(temporary_cal_data)):
            if temporary_cal_data[j] != ' ':
                day += 1
            else:
                temporary_data = [temporary_cal_data[j], '']
                temporary_list.append(temporary_data)
            try:
                #日付の表示を整形
                temporary_date = dt.date(year, month, day)
                date = '{0:%Y-%m-%d}'.format(temporary_date)
                print(date)
                temporary_data = [temporary_cal_data[j], show_task(request, date)]
                temporary_list.append(temporary_data)
            #曜日が範囲外になった時を除く
            except ValueError:
                print('x')
            if len(temporary_list) == 7:
                monthly_calendar.append(temporary_list)
                print('append')
                print(temporary_list)
            if day == day_count:
                day += 1
            print('for')
            print(temporary_list)
            print(len(temporary_list))

    print('mon:')
    print(monthly_calendar)

    params = {
        'year_and_month': year_and_month,
        'monthly_calendar': monthly_calendar,
    }
    return render(request, 'all_list/index.html', params)

def show_task(request, date):
    get_data = ToDo.objects.get()
    task_data = get_data.multi_return()
    if str(task_data[1]) == str(date):
        return task_data[0]
    else:
        return ' '