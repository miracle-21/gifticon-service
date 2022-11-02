import json

from django.http      import JsonResponse
from django.views     import View

from app.models import *

class ProductView(View):
    '''
    등록된 기프티콘 종류 조회
    '''
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

class ProductSaleView(View):
    '''
    판매 대기중인 기프티콘 조회
    '''
    def get(self, request):
        results = [
            {
                'id' : waiting.id,
                'user' : waiting.user_id,
                'product' : waiting.product_id,
                'waiting' : waiting.waiting,
            } for waiting in Waiting.objects.all()
        ]
        return JsonResponse({'results' : results}, status = 200)

    '''
    기프티콘 판매
    설명: 등록가능개수(demand)를 초과한 경우에는 대기번호 부여, 그 외에는 '판매 등록 완료' 메세지 반환.
    '''
    def post(self, request, user_id):
        data = json.loads(request.body)

        name = data['name']

        product = Product.objects.get(name=name)

        #등록가능개수(demand)를 초과하지 않은 경우
        if product.demand - product.supply > 0:
            product.supply += 1

            product.save()

            return JsonResponse({'message' : '판매 등록 완료'}, status = 200)
        #등록가능개수(demand)를 초과한 경우 대기번호 발생
        else:
            count = len(Waiting.objects.filter(product_id=product.id)) + 1
            Waiting.objects.create(
                user_id = user_id,
                product_id = product.id,
                waiting = count
            )

            return JsonResponse({'message' : f'판매 대기중(대기번호 {count}번)'}, status = 201)

class ProductOrderView(View):
    '''
    기프티콘 구매
    설명: 구매자가 기프티콘을 구매하면 supply가 구매 개수만큼 감소한다.
          웨이팅도 구매 개수만큼 감소하고, supply가 웨이팅 감소 개수만큼 증가한다.
    '''
    def patch(self, request, product_id):
        data = json.loads(request.body)
        count = data['count']
        product = Product.objects.get(id=product_id)

        if product.supply >= count:
            product.supply -= count

            product.save()
        else:
            return JsonResponse({'message' : '상품 구매 대기'}, status = 200)
        
        # 웨이팅 번호 감소
        add = product.demand - product.supply
        waitings = Waiting.objects.filter(product_id=product_id)
        if add > 0 and len(waitings) > 0:
            for waiting in waitings:
                if waiting.waiting - add <= 0:
                    product.supply += 1
                    waiting.delete()
                else:
                    waiting.waiting -= add
                    waiting.save()
            product.save()

        return JsonResponse({'message' : f'{product.name} {count}개 구매 완료'}, status = 200)
