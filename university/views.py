from django.shortcuts import render ,redirect

from .models import  *
def all_fanlar(request):
    if request.method == "POST":
        Subject.objects.create(
            name = request.POST.get("n"),
            speciality = Speciality.objects.get(id=request.POST.get("spe")),

     )
        return redirect("/sub/")
    fanlar = Subject.objects.all()
    d = {"subject" : fanlar,
         "specialities":Speciality.objects.all(),
         "teachers":Teacher.objects.all()
         }
    return render(request,"fanlar.html",d)
def all_yonalishlar(request):
    if request.method == 'POST':
        Speciality.objects.create(
            name = request.POST.get("n"),
            code = request.POST.get("c"),
            start_date = request.POST.get("s_d"),
            is_active = request.POST.get("ac")
        )
        return redirect("/yonalish/")
    spe = Speciality.objects.all()
    d1 = {"spes" : spe}
    return render(request,"yonalishlar.html",d1)
def yonalish_edit(request ,pk):
    if request.method == "POST":
        Speciality.objects.filter(id=pk).update(
            name = request.POST.get("n"),
            code = request.POST.get("c"),
            start_date =request.POST.get("s_d"),
            is_active = request.POST.get("ac")
        )
        return redirect("/yonalish/")
    return render(request,"yonalish-edit.html",{"yonal" : Speciality.objects.get(id=pk)})

def all_ustozlar(request):
    if request.method == "POST":
        Teacher.objects.create(
            first_name = request.POST.get("f_n"),
            last_name = request.POST.get("l_n"),
            degree = request.POST.get("d")
        )
        return redirect("/ustozlar/")
    ustoz = Teacher.objects.all()
    data = {"ustozlar" : ustoz}
    return render(request,"ustozlar.html",data)
def ustoz_edit(request , pk):
    if request.method == "POST":
        Teacher.objects.filter(id=pk).update(
            first_name = request.POST.get("f_n"),
            last_name = request.POST.get("l_n"),
            degree = request.POST.get("d")
        )
        return redirect("/ustozlar/")
    return render(request,"ustoz-edit.html",{"teacher" : Teacher.objects.get(id=pk)})

def ustoz_och(request,pk):
    Teacher.objects.filter(id=pk).delete()
    return redirect("/ustozlar/")
def yonalish_och(request, pk):
    Speciality.objects.filter(id=pk).delete()
    return redirect("/yonalish/")