from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistration, LoginForm, EditForm, Search, Edit
from .models import Developer, Employee, Technology
from .forms import AddDeveloper
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login


def index(request):
    developer = Developer.objects.all()
    technology = Technology.objects.all()
    for tech in technology:
        result = tech.technology.all()
        print(result)
    context = {'developer': developer}
    return render(request, 'homepage.html', context)


def index1(request):
    developer1 = Developer.objects.all()
    print("In views index1 function")
    context1 = {'developer': developer1}
    print("got context1")
    return render(request, 'Show_developers.html', context1)


def forget(request):
    return render(request, 'Forgot_password.html')


def register(request):
    form = UserRegistration()
    developer1 = Developer.objects.all()
    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            context = {'form': form, 'developer': developer1}
            return render(request, 'homepage.html', context)
    else:
        form = UserRegistration()
        context = {
            "form": form
        }
        return render(request, 'register.html', context=context)


# def register(request):
#     if request.method == 'POST':
#         form = UserRegistration(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             # user = authenticate(username=username, password=raw_password)
#             user = form.save()
#             auth_login(request, user)
#             return redirect('home')
#     else:
#         form = UserRegistration()
#     return render(request, 'register.html', {'form': form})


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')
            username1 = Employee.objects.filter(username=username).first()
            # password1 = Employee.objects.filter(password=password)
            # print("========",username1, password1)

            # user = authenticate(username=username1, password=password1)

            if str(username) == str(username1):
                return redirect("/home")
            else:
                return HttpResponse("Invalid username or password.")
        else:
            return HttpResponse("Invalid form details.")
            form = LoginForm()
    return render(request=request, template_name="login.html", context={"form": form})


# @login_required
def edit(request, id=None):
    instance = get_object_or_404(Developer, id=id)
    form = EditForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponse('Details Updated Successfully!')
    return render(request, 'Edit_developer.html', {'form': form})


def post_collection(request):
    developer = Developer.objects.all()
    context = {'developer': developer}

    return render(request, "Show_developers.html", context)


def get_data(request):
    form = AddDeveloper()
    if request.method == "POST":
        # print(request.POST)
        form = AddDeveloper(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Developer added successfully!")

    context = {'form': form}
    return render(request, 'developer_form.html', context)


def edit_data(request):
    form = EditForm()
    if request.method == "POST":
        # print(request.POST)
        form = EditForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'developer_form.html', context)


def edit1(request):
    form = Edit()
    # print(form.data['name'])
    developer = Developer.objects.all()
    for dev in developer:
        print(dev.name)

    if request.method == "POST":
        form = Edit(request.POST)
        if form.is_valid():
            return redirect()
        else:
            form = Edit()

        return render(request, 'edit.html', {'form': form})
        # context = {'form': form}
    # return render(request, 'edit.html', context)
    # developer = developer
    # id = id
    # print(id)

    # elif request.method == "POST":

    return redirect('/edit/', developer)


def delete_dev(request, id=None):
    developer = Developer.objects.all()
    # for dev in developer:
    # print(dev)
    result = Developer.objects.filter(id=id).delete()
    return HttpResponse("Developer deleted successfully!")


def search_dev(request, pk=None):
    form = Search()

    if request.method == "POST":
        # print(request.POST)
        form = Search(request.POST)
        developer = Developer.objects.all()
        for dev in developer:
            for tech in dev.technology.all():
                print(tech)
        # print(developer)
        if form.is_valid():
            location1 = form.cleaned_data['location']
            technology1 = form.cleaned_data['technology']
            domain1 = form.cleaned_data['domain']

            # print(location1, technology1, domain1)

            location2 = Developer.objects.get(location=location1)
            # technology2 =Developer.objects.filter(technology=technology1)
            # technology2 = Technology.technology
            technology2 = Technology.objects.all()
            # for tech in technology2:
            #     result = Developer.objects.get(technology=technology1)
            #     print("=======",result)
            # print("=========",location2)

            # result = Developer.objects.filter(technology = technology1)

            # print("Result",result)
            # Developer.objects.prefetch_related(location__technology)
            # score = Developer.objects.get(score=developer.score)
            for dev in developer:
                for tech in dev.technology.all():
                    for dom in dev.domain.all():
                        for tech1 in technology1:
                            for dom1 in domain1:
                                if location1 == dev.location and tech1 == tech and dom1 == dom:
                                    return HttpResponse(dev.name)
            # id=request.POST['id']
            # tech1 = Technology.objects.get(technology=technology1)
            # print("from db",technology1)
            # print(technology1.name, technology1.id)
            # technology = list(tech1)tag__id__in=news.tag.all()
            # result = Developer.objects.filter(location=location1, technology=tech1.id)

            # result=Developer.objects.filter(location=location1,technology=4)

        #   loc = Developer.objects.filter(pk=pk)
        # print(technology)
        #     location = Developer.objects.filter(location=form['location']).filter(technology=form['technology']).filter(domain=form['domain'])
        #     score = Developer.objects.get(score=developer.score)
        #     #technology = Developer.objects.get(technology=Developer.technology.all)
        #     # domain = Developer.objects.get(domain=Developer.domain.all)
        #
        #
        #     if location== True and (score == max(developer.score)):
        #         return HttpResponse(developer.name)

        # else:
        # return HttpResponse("Developer not found!")
        else:
            return HttpResponse("Enter details properly!")

    context = {'form': form}
    return render(request, 'Search.html', context)
