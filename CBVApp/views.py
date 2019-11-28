from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView,DeleteView,DetailView,UpdateView,CreateView
from CBVApp.models import Product
from django.urls import reverse_lazy

'''
def hello(request):
     return HttpResponse('<h1>Hello from FBV</h1>')

class Hello(View):
    def get(self,request):
	       return HttpResponse('<h1>Hello from CBV</h1>')
-------------------------------------------------------------------
def hello(request):
    return render(request,'CBVApp/hello.html')

class Hello(TemplateView):
    template_name='CBVApp/hello.html'
------------------------------------------------------------------

def hello(request):
    mydict={'eid':101,'ename':'Alex','salary':12000.00}
    return render(request,'CBVApp/hello.html',context=mydict)

class Hello(TemplateView):
    template_name='CBVApp/hello.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['eid']=1001
        context['ename']='Ram'
        context['salary']=15000.00
        return context
========================================================================

def ProductView(request):
    products=Product.objects.all()
    return render(request,'CBVApp/index.html',context={'products':products})
'''
class ProductListView(ListView):
    model=Product


    #default template name=product_list.html
    #default context name=product_list

class ProductDetailView(DetailView):
    model=Product
    #default template name=product_detail.html
    #default context name=product or objects
class ProductCreateView(CreateView):
    model=Product
    fields='__all__'

class ProductUpdateView(UpdateView):
    model=Product
    fields='__all__'

class ProductDeleteView(DeleteView):
    model=Product
    success_url=reverse_lazy('home')
