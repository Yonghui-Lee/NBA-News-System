from django.shortcuts import render, get_object_or_404,reverse
import json
from collections import Counter
from teams.models import Team, Person, News, cNews
from django.http import HttpResponse
from jieba import lcut
import datetime
JSON_FILE = 'InvertedIndex.json'
dicSet = json.load(open(JSON_FILE))
dicData = dicSet

'''
import jieba


all_words = []
for i in News.objects.all():
    cut = lcut(i.title_text+i.content_text)
    all_words.extend(cut)

set_all_words = set(all_words)
print(len(set_all_words))

num = 0
invert_index = dict()
for b in set_all_words:
    num += 1
    print(num)
    temp = []
    for j in range(1, News.objects.count()):

        field = News.objects.get(pk=j)

        split_field = lcut(field.title_text+field.content_text)

        if b in split_field:
            temp.append(j)
    invert_index[b] = temp
json_dic2 = json.dumps(invert_index,sort_keys=True,indent=4,separators=(',',':'),ensure_ascii=False)
print(invert_index)
with open(r'InvertedIndex.json','w')as f:
    f.write(json_dic2)'''


def index(request):
    latest_team_list = Team.objects.order_by('-news_int')
    return render(request, 'teams/index.html', {'team_list': latest_team_list})


def detail(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    person_list = team.person_set.all()
    news_list = team.news_set.all()
    return render(request, 'teams/detail.html', {'team': team, 'person_list': person_list, 'news_list': news_list})


def newsdetail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    for i in Team.objects.all():
        kk=i.name_text
        news.content_text = news.content_text.replace(kk, '<a href="{}">'.format(reverse('teams:detail',kwargs={'team_id':i.id})) + kk + '</a>')
        news.title_text = news.title_text.replace(kk, '<a href="{}">'.format(reverse('teams:detail',kwargs={'team_id':i.id})) + kk+ '</a>')

        for j in i.person_set.all():
            news.content_text = news.content_text.replace(j.firstname_text, '<a href="{}">'.format(reverse('teams:detail',kwargs={'team_id':i.id})) + j.firstname_text + '</a>')
            news.title_text = news.title_text.replace(j.firstname_text, '<a href="{}">'.format(reverse('teams:detail',kwargs={'team_id':i.id})) + j.firstname_text + '</a>')
            news.content_text = news.content_text.replace(j.lastname_text, '<a href="{}">'.format(reverse('teams:detail',kwargs={'team_id':i.id})) + j.lastname_text + '</a>')
            news.title_text = news.title_text.replace(j.lastname_text, '<a href="{}">'.format(reverse('teams:detail',kwargs={'team_id':i.id})) +j.lastname_text + '</a>')
            news.content_text = news.content_text.replace(j.firstname_text+'-'+j.lastname_text, '<a href="{}">'.format(
                reverse('teams:detail', kwargs={'team_id': i.id})) + j.firstname_text+'-'+j.lastname_text + '</a>')
            news.title_text = news.title_text.replace(j.firstname_text+'-'+j.lastname_text, '<a href="{}">'.format(
                reverse('teams:detail', kwargs={'team_id': i.id})) + j.firstname_text+'-'+j.lastname_text + '</a>')
    return render(request, 'teams/newsdetail.html', {'news': news})


def search(request):
    # 返回HTML页面时,使用render来渲染和打包
    return render(request, 'teams/search.html')


def searching(request):
    oldtime = datetime.datetime.now()
    list2 = []
    cnews_list = []
    fc = lcut(request.GET['word'])
    for f in fc:
        print(fc)
        try:
            list2.extend(dicData[f])
        except:
            print("no this word: {}".format(f))
    res = Counter(list2)

    list1 = sorted(res.items(), key=lambda x: x[1],reverse=True)
    for l in list1:
        m = News.objects.get(pk=int(l[0]))
        p = cNews(posttime_text=m.posttime_text,title_text=m.title_text,cid=m.id,author_text=m.author_text,
                  content_text=m.content_text)
        for f2 in fc:
            p.content_text = p.content_text.replace(f2, '<span style="color:red">' + f2 + '</span>')
            p.title_text = p.title_text.replace(f2, '<span style="color:red">' + f2 + '</span>')
        cnews_list.append(p)
    newtime = datetime.datetime.now()
    runtime = (newtime - oldtime).microseconds
    return render(request, 'teams/searching.html', {'word': request.GET['word'], 'news_list': cnews_list,
                                                    'num':len(cnews_list),'runtime': runtime/1000000.0})



'''
def hhdetail(request):

    JSON_FILE = "data.json"
    num = 0
    dicSet = json.load(open(JSON_FILE))
    dicData = dicSet

    p = Team.objects.get(id=1)
    for dic in dicData:
        p = Team.objects.get(id=1)
        if dic['title'].find(str(p.name_text)) != -1 or dic['content'].find(str(p.name_text)) != -1:
            p.news_set.create(title_text=dic["title"], author_text=dic["name"], posttime_text=dic["time"],
                              content_text=dic["content"])
            num += 1
            continue

        for i in range(9,38):
            p = Team.objects.get(id=i)
            if dic['title'].find(str(p.name_text))!=-1 or dic['content'].find(str(p.name_text))!=-1:
                p.news_set.create(title_text=dic["title"], author_text=dic["name"], posttime_text=dic["time"],
                            content_text=dic["content"])
                num+=1
                break

        if num>1500:
            break

    return HttpResponse("You're looking at question")
'''

'''
def hhdetail(request):
    for m in Team.objects.all():
        m.news_int = m.news_set.count()
        m.save()

    return HttpResponse("You're looking at question")'''