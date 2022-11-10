import decimal

from rest_framework import viewsets, status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import UserProfile, Transaction, Category
from .permission import IsOwnerProfileOrReadOnly
from .serializers import UserProfileSerializer, TransactionSerializer, CategorySerializer


class UserProfileListCreateView(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]


class TransactionViewList(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        validate = request.data
        serializer = TransactionSerializer(data=validate)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        user_profile = UserProfile.objects.get(user=self.request.user)
        user_profile.balance_profile = user_profile.balance_profile + decimal.Decimal(serializer.data['sum'])
        user_profile.transaction.add(serializer.data['id'])
        user_profile.save()

        return Response({"created"}, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if pk is None:
            return Response({"Error"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            transaction = Transaction.objects.get(pk=pk)
        except:
            return Response({"Error"}, status=status.HTTP_404_NOT_FOUND)
        user_profile = UserProfile.objects.get(user=self.request.user)
        user_profile.balance_profile = user_profile.balance_profile - transaction.sum

        serializer = self.serializer_class(data=request.data, instance=transaction)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        user_profile.balance_profile = user_profile.balance_profile + decimal.Decimal(serializer.data['sum'])
        user_profile.save()

        return Response({"update"}, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        user_profile = UserProfile.objects.get(user=self.request.user)
        return user_profile.transaction


class CategoryViewList(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        validate = request.data
        serializer = CategorySerializer(data=validate)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        user_profile = UserProfile.objects.get(user=self.request.user)
        user_profile.category.add(serializer.data['id'])
        user_profile.save()

        return Response({"created"}, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        user_profile = UserProfile.objects.get(user=self.request.user)
        return user_profile.category
