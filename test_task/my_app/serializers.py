from rest_framework import serializers

from .models import UserProfile, Category, Transaction


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        return Category.objects.create(**validated_data)


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.sum = validated_data.get('sum', instance.sum)
        instance.category = validated_data.get('category', instance.category)
        instance.organization = validated_data.get('organization', instance.organization)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'
        read_only_fields = ['balance_profile']


class StatisticSerializer(UserProfileSerializer):
    # category = CategorySerializer(many=True)
    transaction = TransactionSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = ['user', 'transaction', 'balance_profile']
