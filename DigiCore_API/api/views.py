from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.views import View
from .models import settingsLog
import json
import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
# Create your views here.
class viewHandler(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self,request):
        settings = list(settingsLog.objects.values())
        if len(settings)>0:
            datos = {'message':"Success",'settings':settings}
        else:
            datos = {'message':"Not Found"}
        return JsonResponse(datos)
    def post(self,request):
        #print(request.body)
        jd=json.loads(request.body)
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        words = word_tokenize(jd['input'])
        segmentation = nltk.pos_tag(words) # Tokens Generados
        print(segmentation)
        datos = {'message':"Success"}
        return JsonResponse(datos)
    def put(self,request): # No lo vamos a usar en teoria
        pass
    def delete(self,request): # No lo vamos a usar en teoria
        pass