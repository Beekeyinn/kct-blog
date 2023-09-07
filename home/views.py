from django.shortcuts import render

# Create your views here.
def index(request):
    print("REQUEST METHOD: ",request.method)
    print("PARAMS: ", request.GET)
    data = request.GET.dict()
    return render(request,"index.html",context={"data":data})

def contact(request):
    return render(request,"contact.html")


def about(request):
    return render(request,"about.html")