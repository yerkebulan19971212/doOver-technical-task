from django.urls import path
from .views import ListOfProducts, AddToBasketView, GetToBasketView, ListOfHistoryView


app_name = "products"
urlpatterns = [
    path('product-list/', ListOfProducts.as_view(), name="product_list"),
    path('add-to-cart/<int:item_id>/', AddToBasketView.as_view(), name="add_to_cart"),
    path('get-product-from-basket/', GetToBasketView.as_view(), name="get_product"),
    path('list-of-history/', ListOfHistoryView.as_view(), name="list_of_product")
]
