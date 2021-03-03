from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
import calendar
import datetime as dt

from .models import ToDo
from .forms import ToDoForm

def show_cal(request):
    year = 2021
    month = 3

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
        temporary_cal_data = ['' if day == 0 else str(day) for day in cal_data[i]]
        temporary_list = []
        print(temporary_cal_data)
        for j in range(len(temporary_cal_data)):
            #日付が入っている場合
            if temporary_cal_data[j] != '':
                day += 1
            #日付が入っていない場合
            else:
                temporary_data = [temporary_cal_data[j], '']
                temporary_list.append(temporary_data)
            try:
                #日付の表示を整形
                temporary_date = dt.date(year, month, day)
                date = '{0:%Y-%m-%d}'.format(temporary_date)
                print(date)
                #その日のtaskをtask_listに代入
                task_list = show_task(request, date)
                temporary_data = [temporary_cal_data[j], task_list]
                temporary_list.append(temporary_data)
            #曜日が範囲外になった時を除く
            except ValueError:
                print('x')
            #リストの長さが7になったらmonthly_calenderに追加
            if len(temporary_list) == 7:
                monthly_calendar.append(temporary_list)
                print('append')
                print(temporary_list)
            #日付がその月の日数と同じになったら
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
        'year': year,
        'month': month,
    }
    return render(request, 'all_list/index.html', params)

def show_task(request, date):
    data = ToDo.objects.all()
    task_data = []
    for get_data in data:
        temporary_data = get_data.multi_return()
        if str(temporary_data[1]) == str(date):
            temporary_list = [temporary_data[0], get_data.id, temporary_data[2]]
            task_data.append(temporary_list)
    if len(task_data) == 0:
        task_data.append(['', '', ''])
    return task_data

def create_todo(request):
    #POST送信の処理
    if (request.method == 'POST'):
        form = ToDoForm(request.POST)
        if form.is_valid():
            #formのそれぞれの値を変数に代入
            end = request.POST.get('end')
            task = request.POST.get('task')
            limit = request.POST.get('limit')
            memo = request.POST.get('memo')

            #checkboxの値をbool値に置き換え
            if end == 'on':
                end = True
            else:
                end = False

            #formの値をデータベースに登録
            todo = ToDo()
            todo.end = end
            todo.task = task
            todo.limit = limit
            todo.memo = memo
            todo.save()
        return redirect(to='/all_list/cal')

    #GETアクセス時の処理
    else:
        form = ToDoForm()

    #共通処理
    params = {
        'form': form,
    }

    return render(request, 'all_list/create_todo.html', params)

def edit_todo(request, num):
    #指定されたtaskを取得
    todo = ToDo.objects.get(pk=num)
    if (request.method == 'POST'):
        #編集する
        task = ToDoForm(request.POST, instance=todo)
        task.save()
        return redirect(to='/all_list/cal')
    
    params = {
        'form': ToDoForm(instance=todo),
        'id': num,
    }
    return render(request, 'all_list/edit_todo.html', params)

def delete_todo(request, num):
    #指定されたtaskを取得
    todo = ToDo.objects.get(pk=num)
    if (request.method == 'POST'):
        todo.delete()
        return redirect(to='/all_list/cal')
    
    params = {
        'obj': todo,
        'id': num,
    }
    return render(request, 'all_list/delete_todo.html', params)