from rest_framework import serializers
from .models import Category, Image, SendToEmail
from ..users.models import User
from django.core.mail import send_mail
from django.conf import settings


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('pk', 'path', )


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ListCategoriesSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('pk', 'name', 'slug', 'children')


class SendToEmailSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120, required=False)
    text = serializers.CharField(
        max_length=None, min_length=None, allow_blank=False,
        trim_whitespace=True
    )

    def create(self, validated_data):
        title = validated_data.pop('title')
        text = validated_data.pop('text')
        users = User.objects.all()
        from_email = settings.DEFAULT_FROM_EMAIL
        email_to = []
        for user in users:
            email_to.append(user.email)
            send_to_email = SendToEmail.objects.create(
                title=title,
                text=text,
                to_email=user.email,
                to_user=user
            )
        print(email_to)
        send_mail(
            title,
            text,
            from_email,
            email_to,
            fail_silently=False
        )
        return send_to_email
