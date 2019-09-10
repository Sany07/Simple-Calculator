from django.shortcuts import render

# Create your views here.


def home(request):
    if request.method=='POST':
        first= request.POST['first_name']
        last= request.POST['second_number']  

        if request.POST.get('add'):
            res=int(first)+int(last)
            
            contex={
                'name':res
            }
            return render(request,'index.html',contex)
            
        elif request.POST.get('sub'):
            res=int(first)-int(last)
            
            contex={
                'name':res
            }
            return render(request,'index.html',contex)

        elif request.POST.get('mul'):
            res=int(first)*int(last)
            
            contex={
                'name':res
            }
            return render(request,'index.html',contex)

        elif request.POST.get('dev'):
            res=int(first)/int(last)
            
            contex={
                'name':res
            }
            return render(request,'index.html',contex)        
    return render(request,'index.html')


