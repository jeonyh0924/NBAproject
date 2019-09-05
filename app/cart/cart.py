# from decimal import Decimal
# from django.conf import settings
#
# from members.models import Player
#
#
# class Cart(object):
#     # 장바구니를 관리하는 데 도움이되는 장바구니 클래스를 만듭니다.
#     def __init__(self, request):  # request objects로 카트를 초기화해야합니다.
#         self.session = request.session  # self.session = request.session을 사용하여 현재 세션을 저장하면
#         # Cart 클래스에서 다른 방법으로 카트를 사용할 수 있습니다.
#
#         cart = self.session.get(settings.CART_SESSION_ID)
#         # 현재 세션에서 get 메소드를 사용하여 카트를 가져 오려고합니다.
#
#         if not cart:
#             # 세션에 장바구니가없는 경우 세션에서 빈 사전을 설정하여 11 행에 빈 장바구니를 설정합니다.
#             cart = self.session[settings.CART_SESSION_ID] = {}
#
#         self.cart = cart
#
#     def add(self, player, quantity=1, update_quantity=False):
#         # 장바구니에 제품을 추가하는 방법을 만듭니다.
#         # add 메소드는 매개 변수로 ( self, product, amount = 1, update_quantity = False )를 사용합니다.
#
#         player_id = str(player.id)
#         # 카트 내용 사전의 키로 product_id를 사용합니다.
#         # Django는 json을 사용하여 세션 데이터를 직렬화하고 json은 문자열 이름 만 허용하므로 product id를 문자열로 변환합니다.
#
#         if player_id not in self.cart:
#             self.cart[player_id] = {'quantity': 0, 'price': str(player.price)}
#             #  제품 ID가 핵심이며 우리가 유지하는 가치는 제품의 수량과 가격을 가진 사전입니다.
#             #  또한 직렬화하기 위해 제품 가격을 문자열로 변환합니다.
#         if update_quantity:
#             self.cart[player_id]['quantity'] = quantity
#         else:
#             self.cart[player_id]['quantity'] += quantity
#         self.save()
#         # 카트를 세션에 저장합니다.
#
#     def save(self):
#         # 장바구니의 변경 사항을 추적하고 self.session.modified = True를 사용하여 세션을 수정 된 것으로 표시하는 저장 방법을 만듭니다.
#         self.session[settings.CART_SESSION_ID] = self.cart
#         self.session.modified = True
#
#     def remove(self, player):
#         # 장바구니에서 단일 제품을 제거하고 세션에 장바구니를 저장하는 방법을 만듭니다.
#         player_id = str(player.id)
#         if player_id in self.cart:
#             del self.cart[player_id]
#             self.save()
#
#     def __iter__(self):
#         # 카트에 포함 된 항목을 반복하고 관련 제품 인스턴스를 얻는 데 도움이되는 __iter __ (자체) 방법을 정의합니다.
#         player_ids = self.cart.keys()
#         player = Player.objects.filter(id__in=player_ids)
#         for player in player:
#             self.cart[str(player.id)]['player'] = player
#
#         for item in self.cart.values():
#             item['price'] = Decimal(item['price'])
#             item['total_price'] = item['price']
#             yield item
#
#     def __len__(self):
#         # 장바구니에 담은 총 품목 수를 반환하는 len 메소드를 정의합니다.
#         return sum(item['quantity'] for item in self.cart.values())
#
#     def get_total_price(self):
#         # 카트에있는 품목의 총 비용을 얻기 위해 get_total_price 메소드를 정의합니다.
#         return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
#
#     def clear(self):
#         # 장바구니 세션을 지우는 방법을 정의합니다.a
#         del self.session[settings.CART_SESSION_ID]
#         self.session.modified = True


from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_ID)
        if not cart:
            cart = self.session[settings.CART_ID] = {}
        self.cart = cart
        # self.coupon_id = self.session.get('coupon_id')

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']

            yield item

    def add(self, product, quantity=1, is_update=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}

        if is_update:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session[settings.CART_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del (self.cart[product_id])
            self.save()

    def clear(self):
        self.session[settings.CART_ID] = {}
        # self.session['coupon_id'] = None
        self.session.modified = True

    def get_product_total(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
