from django.shortcuts import get_object_or_404, render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from magazzino.models import Cassa, ClasseDiMateriale, ContestoScavo, MaterialeInCassa

def index(request):
    return render(request, 'magazzino/index.html')

def classedimateriale_index(request):
    cdm = ClasseDiMateriale.objects.all()
    return render(request, 'magazzino/classedimateriale_list.html', {'cdm': cdm})

def classedimateriale_detail(request, cdm_sigla):
    cdm = get_object_or_404(ClasseDiMateriale, sigla=cdm_sigla)
    return render(request, 'magazzino/classedimateriale_detail.html', {'cdm': cdm})

def classedimateriale_search(request):
    '''Search based on exact match for ClasseDiMateriale `classe` or `sigla`'''

    res = ClasseDiMateriale.objects.filter(classe__icontains=request.GET['search_string'])
    return render(request, 'magazzino/classedimateriale_searchresults.html', {'cdm': res, 'ss': request.GET['search_string']})


class MaterialeInCassaDetailView(DetailView):

    model = MaterialeInCassa

    def get_context_data(self, **kwargs):
        context = super(MaterialeInCassaDetailView, self).get_context_data(**kwargs)
        context['mic'] = context['materialeincassa']
        return context

class MaterialeInCassaUpdate(UpdateView):
    model = MaterialeInCassa
