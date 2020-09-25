from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Products, HistoryOfProduct
from ..extra.paginations import SmallResultSetPagination
from .serializers import ListProductsSerializer, HistoryOfUserProductSerializer


class ListOfProducts(ListAPIView):
    serializer_class = ListProductsSerializer
    pagination_class = SmallResultSetPagination
    queryset = Products.objects.filter(published=True)


class AddToBasketView(APIView):
    def post(self, request, item_id):
        product = request.session.get('product', [])
        product.append(item_id)
        request.session['product'] = product
        return Response("вы добавили в корзину", status=status.HTTP_200_OK)


class GetToBasketView(APIView):
    def get(self, request):
        products_id = request.session.get('product')
        products = Products.objects.filter(id__in=products_id)
        serializer = ListProductsSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ListOfHistoryView(ListAPIView):
    serializer_class = HistoryOfUserProductSerializer
    pagination_class = SmallResultSetPagination
    queryset = HistoryOfProduct.objects.all()

    def get_queryset(self):
        user = self.request.user
        history = self.queryset.filter(user=user)

        return history
