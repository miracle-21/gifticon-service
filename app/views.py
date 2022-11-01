import json

from django.http      import JsonResponse
from django.views     import View

from app.models import *

class ProductView(View):
    def get(self, request):
        results = [
            {
                'id' : product.id,
                'name' : product.name,
                'demand' : product.demand,
                'supply' : product.supply,
            } for product in Product.objects.all()
        ]
        return JsonResponse({'results' : results}, status = 200)

class ProductUserView(View):
    def get(self, request):
        results = [
            {
                'id' : waiting.id,
                'user' : waiting.user_id,
                'waiting_number' : waiting.waiting_number,
            } for waiting in UserWaiting.objects.all()
        ]
        return JsonResponse({'results' : results}, status = 200)

    def post(self, request, user_id):
        data = json.loads(request.body)

        name = data['name']

        product = Product.objects.get(name=name)
        if product.demand - product.supply > 0:
            product.supply += 1

            product.save()

            return JsonResponse({'message' : '판매 등록 완료'}, status = 200)
        else:
            count = len(UserWaiting.objects.filter(product_id=product.id)) + 1
            UserWaiting.objects.create(
                user_id = user_id,
                product_id = product.id,
                waiting_number = count
            )

            return JsonResponse({'message' : f'판매 대기중(대기번호 {count}번)'}, status = 201)