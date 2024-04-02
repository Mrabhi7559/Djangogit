from django.shortcuts import render
from django.urls import reverse_lazy
from app.models import Movie
from app.forms import Movieform
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

# def home(request):
#     m=Movie.objects.all()
#     return render(request,'home.html',{'m':m})

class HomeView(ListView):
    model=Movie
    template_name="home.html"
    context_object_name='m'

    # def get_queryset(self):
    #     queryset=self.get_queryset().filter(year=2023)
    #     return queryset
# def detail(request,n):
#     m=Movie.objects.get(id=n)
#     return render(request, 'detail.html', {'m': m})

class Detail(DetailView):
    model=Movie
    template_name="detail.html"
    context_object_name='m'


# def add(request):
#     if(request.method=='POST'):
#         form=Movieform(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return home(request)
#     form=Movieform()
#     return render(request,"add.html", {'form':form})

class AddMovie(CreateView):
    model=Movie
    template_name="add.html"
    fields=['name','year','desc','image']
    success_url=reverse_lazy('app:home')

# def update(request,n):
#     s=Movie.objects.get(id=n)

    # if(request.method=='POST'):
    #     form=Movieform(request.POST,request.FILES,instance=s)
    #     if form.is_valid():
    #         form.save()
    #         return home(request)
    # form=Movieform(instance=s)
    # return render(request,"edit.html", {'form':form})

class Update(UpdateView):
    model=Movie
    template_name="add.html"
    fields=['name','year','desc','image']
    success_url=reverse_lazy('app:home')
# def delete(request,n):
#     s=Movie.objects.get(id=n)
#     s.delete()
#     return home(request)

class Delete(DeleteView):
    model=Movie
    template_name="delete.html"
    success_url = reverse_lazy('app:home')
