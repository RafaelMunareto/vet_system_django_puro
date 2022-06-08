from home.models import Urls
from django.db.models import Q

def buscador(request):
    """CARREGA O BUSCADOR NO TEMPLATE BASE"""
    
    if 'search' in request.GET:
        search = request.GET['search']
    else:
        search = ''
        
        
    if search == '':
        urls = Urls.objects.all().distinct()
    else:
        urls = Urls.objects.filter(Q(urls__icontains=search) | Q(nome__icontains=search) | Q(descricao__icontains=search)).order_by('nome')
        
    return {'urls' : urls, 'search':search}


def menu(request):
    """CARREGA AS PÁGINAS NO MENU"""
    
    clientes = Urls.objects.filter(grupo='clientes').distinct()
    pacientes = Urls.objects.filter(grupo='pacientes').distinct()
    administrativo =  Urls.objects.filter(grupo='administrativo').distinct()
    parceiros =  Urls.objects.filter(grupo='parceiros').distinct()
    agendamentos =  Urls.objects.filter(grupo='agendamentos').distinct()
        
    return {'clientes' : clientes,
            'pacientes' : pacientes,
            'administrativo' : administrativo,
            'parceiros' : parceiros,
            'agendamentos' : agendamentos
            }