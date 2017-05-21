from django.shortcuts import render,HttpResponse
import json
import requests
# Create your views here.

def index(request):
    return HttpResponse('Welcome')
def test(request):
    return HttpResponse('My second welcome')
def profile(request):
    parseData=[]
    if request.method=='POST':
        username=request.POST.get('user')
        usernames=username.split(' ')
       # return HttpResponse(usernames[0]+" "+usernames[1])
        for username in usernames:
            req=requests.get('https://api.github.com/users/'+username)
            jsonList=[]
            jsonList.append(json.loads(req.text))
            userData={}
            for data in jsonList:
                if 'name' in data:
                    userData['name']=data['name']
                if 'blog' in data:
                    userData['blog']=""
                    if "http" not in data['blog'] and len(data['blog'])!=0:
                        userData['blog'] ="https://"
                    userData['blog']+=data['blog']
                if 'email' in data:
                    userData['email'] = data['email']
                if 'public_gists' in data:
                    userData['public_gists'] = data['public_gists']
                if 'public_repos' in data:
                    userData['public_repos'] = data['public_repos']
                if 'avatar_url' in data:
                    userData['avatar_url'] = data['avatar_url']
                if 'followers' in data:
                    userData['followers'] = data['followers']
                if 'following' in data:
                    userData['following'] = data['following']
            parseData.append(userData)
        return render(request,'app/profile.html',{'data':parseData})
    return render(request,'app/profile.html')
