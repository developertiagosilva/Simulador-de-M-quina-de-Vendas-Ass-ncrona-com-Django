from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, "app/index.html")


# Endpoint que processa a escolha da bebida
@csrf_exempt # Simplificando para o exemplo local, mas em produção use o CSRF token
def liberar_bebida(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        bebida = data.get('bebida')

        # Nosso "switch" em formato de dicionário Python
        mensagens = {
            'coca': '🥤 Coca-Cola liberada!',
            'guarana': '🍒 Guaraná liberado!',
            'fanta': '🍊 Fanta liberada!'
        }

        if bebida in mensagens:
            return JsonResponse({
                'sucesso': True, 
                'mensagem': mensagens[bebida],
                'bebida': bebida # Devolvemos o nome para o JavaScript saber qual lata animar
            })
        
        return JsonResponse({'sucesso': False, 'mensagem': 'Bebida não encontrada.'}, status=400)
    
    return JsonResponse({'sucesso': False, 'mensagem': 'Método não permitido.'}, status=405)