from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.views import View
from .models import settingsLog
import json
import re

#Direcciones ip validas
# Nombre A(Nodo) o PC1
A = "192.168.3.2"
# Nombre B(Nodo) o PC2
B = "192.169.3.2"

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
        pattern = r"Denegar\s+el\s+acceso\s+de\s+(PC1|A|PC2|B)\s+a\s+internet" # Dependiendo de la cantidad de hosts que se tengan se debe agregar o quitar elementos en el (PC1|A|PC2|B).
        ipt = jd['input']
        res = re.search(pattern,ipt)
        if res: # Se encontro el patron
            if ("PC1" in ipt) or ("A" in ipt): #Nodo A o PC1
                otp = "$ configure terminal $ access-list extended block-out $ deny ip "+str(A)+" any $ exit $ interface eth0 $ ip access-group block-out in $ exit"
                settingsLog.objects.create(input=jd['input'],output=otp)
                datos = {'message':"Success"}
                return JsonResponse(datos)
            else: #Nodo B o PC2
                otp = "$ configure terminal $ access-list extended block-out $ deny ip "+str(B)+" any $ exit $ interface eth0 $ ip access-group block-out in $ exit"
                settingsLog.objects.create(input=jd['input'],output=otp)
                datos = {'message':"Success"}
                return JsonResponse(datos)
        else: # Caso contrario error de sintaxis
            datos = {'message':'Command not found'}
            return JsonResponse(datos)
    def put(self,request): # No lo vamos a usar en teoria
        pass
    def delete(self,request): # No lo vamos a usar en teoria
        pass