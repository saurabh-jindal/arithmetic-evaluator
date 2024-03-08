from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import re
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

@csrf_exempt
def evaluate_expression(request):
    if request.method == 'POST':
        expression = request.POST.get('expression')
        if expression:
            try:
                # Validate expression
                if re.match(r'^\d+[\+\-]\d+(?:[\+\-]\d+)*$', expression):
                    result = eval(expression)
                    return JsonResponse({'result': result})
                else:
                    return JsonResponse({'error': 'Invalid expression format.'}, status=400)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)
        else:
            return JsonResponse({'error': 'Expression is missing.'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)
