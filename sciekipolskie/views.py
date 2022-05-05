from django.shortcuts import render, redirect
from django.views import View
from .models import ListOfWorkers
from django.http import HttpResponse

workers_name = ['Am Li', 'Vi Jay', 'Ri Ulun', 'Ano Horf']
workers_id = [94061995, 94061996, 94061997, 94061998, 94061994]


# Create your views here.
class RepresentList(View):
    def get(self, request):
        # for i in range(len(workers_name)):
        #     worker_instance = ListOfWorkers.objects.create(name=workers_name[i], id_of_worker=workers_id[i])
        workers = ListOfWorkers.objects.all()
        return render(request, 'workers.html', context={"workers":workers})

class AddNewWorkerView(View):
    def get(self, request):
        return render(request, 'add_worker.html')

    def post(self, request):
        worker_name = request.POST.get("name")
        personal_id = request.POST.get("id_of_worker")
        ListOfWorkers.objects.create(name=worker_name, id_of_worker=personal_id)
        return redirect("main_list")

class DetailsAboutWorkerView(View):
    def get(self, request, id_of_worker):
        detailsAboutWorker = ListOfWorkers.objects.get(id=id_of_worker)
        return render(request, "details_about_worker.html", {'worker': detailsAboutWorker})

class AddNewTaskView(View):
    def get(self, request, id_of_worker):
        detailsAboutWorker = ListOfWorkers.objects.get(id=id_of_worker)
        return render(request, "details_about_worker.html", {'worker': detailsAboutWorker})

    def post(self, request, id_of_worker):
        pass