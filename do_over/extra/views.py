from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Category
from .serializers import ListCategoriesSerializer, SendToEmailSerializer


class CategoriesListView(ListAPIView):
    serializer_class = ListCategoriesSerializer
    queryset = Category.objects.filter(is_active=True, parent__isnull=True)


class SendToEmailView(CreateAPIView):
    serializer_class = SendToEmailSerializer

