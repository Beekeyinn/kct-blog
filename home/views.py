from django.shortcuts import render
from home.email import send_contact_email


# Create your views here.
def index(request):
    print("REQUEST METHOD: ", request.method)
    print("PARAMS: ", request.GET)
    data = request.GET.dict()
    return render(request, "index.html", context={"data": data})


def contact(request):
    if request.method == "GET":
        return render(request, "contact.html")
    else:
        data = request.POST
        send_contact_email(
            data.get("message"),
            data.get("email"),
            data.get("name"),
        )
        return render(
            request, "contact.html", {"message": "Thank you for contacting us."}
        )


def about(request):
    return render(request, "about.html")


def handle_404(request):
    return render(request, "errors/404_error.html")


def handle_403(request):
    return render(request, "errors/403_error.html")


def handle_500(request):
    return render(request, "errors/500_error.html")
