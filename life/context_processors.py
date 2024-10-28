# context_processors.py
from .models import Period

def periods_processor(request):
    # periods = Period.objects.all().order_by('-id')  
    periods = Period.objects.all().order_by('-title')  
    # periods = Period.objects.all() 
# Fetch all periods or filter as needed
    return {'periods': periods}

