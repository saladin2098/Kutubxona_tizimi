from django.shortcuts import render, redirect

from .models import  *
from university.models import *
def all_students (request):
    if request.method == 'POST':
        Student.objects.create(
            ism = request.POST.get("i"),
            guruh = request.POST.get("g"),
            guvohnoma = request.POST.get("gh"),
            kitob_soni = request.POST.get("k_s"),
            bitiruvchi = request.POST.get("b")
        )
        return redirect("/students/")
    talabalar = Student.objects.all()
    malumot = {
        "students" : talabalar
    }
    return render(request,"students.html",malumot)
def all_data(request):
    kitoblar = kitob.objects.all()
    engkop = kitob.objects.order_by("-sahifa")[0:3]

    data = {"books" : kitoblar , "most" : engkop}
    return render(request,"data.html",data)
def kitob_edit(request , pk):
    if request.method == "POST":
        kitob.objects.filter(id=pk).update(
            nomi = request.POST.get("n"),
            sahifa = request.POST.get("s"),
            janr = request.POST.get("j"),
            muallif = Muallif.objects.get(id = request.POST.get("m"))
        )
        return redirect("/data/")
    return render(request,"kitob_edit.html",{"books" : kitob.objects.get(id=pk),
                                             "mualliflar" :Muallif.objects.all })



def all_mualliflar(request):
    if request.method == "POST" :
        Muallif.objects.create(
            nomi = request.POST.get("n"),
            ism = request.POST.get("i"),
            tirik = request.POST.get("tr"),
            yosh = request.POST.get("y"),
            jins = request.POST.get("j"),
            kitoblar_soni = request.POST.get("k_s")
        )
        return redirect("/mualliflar/")
    maulliflar = Muallif.objects.all()
    eng_qarisi = Muallif.objects.order_by("-yosh")[0:3]
    data2 = {"authors" : maulliflar , "oldest" : eng_qarisi}
    return render(request,"mualliflar.html", data2)
def muallif_edit(request ,pk):
    if request.method == "POST":
        Muallif.objects.filter(id=pk).update(
            nomi = request.POST.get("n"),
            ism = request.POST.get("i"),
            tirik = request.POST.get("tr"),
            yosh = request.POST.get("y"),
            jins = request.POST.get("j"),
            kitoblar_soni = request.POST.get("k_s")
        )
        return redirect("/mualliflar/")

    return render(request,"muallif-edit.html" , {"muallif" : Muallif.objects.get(id=pk)})
def student_och(request , pk ):
    Student.objects.filter(id = pk).delete()

    return redirect("/students/")
def student_edit(request , pk):
    if request.method == "POST":
        Student.objects.filter(id=pk).update(
            ism = request.POST.get("i"),
            guruh = request.POST.get("g"),
            guvohnoma = request.POST.get("gh"),
            kitob_soni = request.POST.get("k_s"),
            bitiruvchi = request.POST.get("b")
        )
        return redirect("/students/")



    return render(request,"student-edit.html" , {"student" :  Student.objects.get(id=pk)})

def muallif_och(request,pk):
    Muallif.objects.filter(id = pk).delete()
    return redirect("/mualliflar/")
def kitob_och(request,pk):
    kitob.objects.filter(id = pk).delete()
    return redirect("/data/")
def all_recordlar(request):
    if request.method == "POST":
        record.objects.create(
            sana = request.POST.get("s"),
            qaytardi = request.POST.get("q"),
            qaytarish_sana = request.POST.get("q_s"),
            student = Student.objects.get(id=request.POST.get("st")),
            kitob = kitob.objects.get(id=request.POST.get("k"))
         )
        return redirect("/recordlar/")
    data3 = {"rekordlar" : record.objects.all() ,
             "kitoblar" : kitob.objects.all(),
             "studentlar" : Student.objects.all()
             }
    return render(request,"recordlar.html",data3)

