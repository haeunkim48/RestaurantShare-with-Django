from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from shareRes.models import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendEmail(request):
    checked_res_list = request.POST.getlist('checks')
    inputReceiver = request.POST['inputReceiver']
    inputTitle = request.POST['inputTitle']
    inputContent = request.POST['inputContent']

    mail_html = "<html><body>"
    mail_html += "<h1>맛집 공유</h1> "
    mail_html += "<p>"+inputContent+"<br>"
    mail_html += "발신자님께서 공유하신 맛집은 다음과 같습니다.</p>"

    for checked_res_id in checked_res_list:
        restaruant=Restaurant.objects.get(id = checked_res_id)
        mail_html += "<h2>"* + restaruant.restaruant_name+"</h3>"
        mail_html += "<h4>"* 관련 링크</h4>"+"<p>"+restaurant.restaurant_link+"</p><br>"
        mail_html += "<h4>"* 상세 내용</h4>"+"<p>"+restaurant.restaurant_content+"</p><br>"
        mail_html += "<h4>"* 관련 키워드</h4>"+"<p>"+restaurant.restaurant_keyword+"</p><br>"
        mail_html += "<br>"
        mail_html += "</body></html>"

        mail_html += "<br>"
    mail_html += "</body></html>"

    #print (mail_html)

    # smtp using 
    server= smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login ("djangoemailtester001@gmail.com", "tester001")

    msg = MIMEMultipart('alternative')
    msg ['Subject'] = inputTitle
    msg['From'] = "djangoemailtester001@gmail.com"
    msg['To'] = inputReceiver (mail_html,'html')
    msg.attach(mail_html)
    print(msg['To'], type(msg['To']))
    server.sendmail(msg['From'], msg['To'].split(','), msg.as_string())
    server.quit()
    return HttpResponseRedirect(reverse('index'))
        



# Create your views here.
def index(request):
    categories = Category.objects.all()
    restaurants = Restaurant.objects.all()
    content = {'categories': categories, 'restaurants' : restaurants}
    # return HttpResponse ("index")
    return render(request, 'shareRes/index.html', content)

def restaurantDetail(request, res_id):
    restaruant = Restaurant.objects.get(id = res_id)
    content = {'restaurant': restaruant}
    # return HttpResponse ("restaruantDetail")
    return render(request, 'shareRes/restaruantDetail.html', content)


def restaurantCreate(request):
    categories = Category.objects.all()
    content = {'categories': categories}
    # return HttpResponse ("restaurantCreate")
    return render(request, 'shareRes/restaruantCreate.html', content)

def Create_restaurant(request):
    category_id = request.POST ['resCategory']
    category = Category.objects.get(id = category_id)
    name = request.POST ['resTitle']
    link = request. POST ['resLink']
    content = request.POST ['resContent']
    keyword = request.POST ['resLoc']
    new_res = Restaurant(category=category, restaurant_name=name, restaurant_link = link, restaurant_content=content, restaurant_keyword=keyword)
    new_res.save()
    return HttpResponseRedirect(reverse('index'))

def categoryCreate(request):
    categories = Category.objects.all()
    content = {'categories': categories}

    # return HttpReponse("categoryCreate")
    return render(request, 'shareRes/categoryCreate.html')

def restaruantUpdate(request, res_id):
    categories = Category.objects.all()
    restaruant = Restaurant.objects.get(id=res_id)
    content = {'categories': categories, 'restaurant': restaurant}
    return render(request, 'shareRes/restaurantUpdate.html', content)

def Delete_restaurant(request):
    res_id= request.POST['resId']
    restaruant = Restaurant.objects.get(id=res_id)
    restaruant.delete()
    return HttpResponseRedirect(reverse('index'))

def Update_restaurant(request):
    resId = request.POST['resId']
    change_category_id = request.POST['resCategory']
    change_category = Category.objects.get(id=change_category_id)
    change_name = request.POST['resTitle']
    change_link = request.POST['resLink']
    change_content = request.POST['resContent']
    change_keyword = request.POST['resLoc']
    before_restaurant= Restaurant.objects.get(id=resId)
    before_restaurant.category= change_category
    before_restaurant.restaruant_name = change_name
    before_restaurant.restaruant_link = change_link
    before_restaurant.restaruant_content = change_content
    before_restaurant.restaruant_keyword = change_keyword
    before_restaurant.save()
    return HttpResponseRedirect(reverse('resDetailPage', kwargs={'res_id':resId}))
    
def Create_category(request):
    category_name = request.POST['categoryName']
    new_category = Category(category_name = category_name)
    new.category.save()
    return HttpResponseRedirect(reverse('index'))
    # return HttpReponse("여기서 category Create 기능을 구현할 거야.")

def Delete_category(request):
    category_id = request.POST['categoryId']
    delete_category = Category.objects.get(id = category_id)
    delete_category.delete()
    return HttpResponseRedirect(reverse('cateCreatePage'))
    


    