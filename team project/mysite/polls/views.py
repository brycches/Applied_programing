from django.http import HttpResponse
import sentence_generator

sentence_generator.main()



def index(request):
    return HttpResponse("")