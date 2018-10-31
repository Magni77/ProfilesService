from django.db.models import Q
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from profiles.models import Profile
from profiles.serializers import ProfileSerializer, BasicProfileSerializer


class ProfileView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    lookup_field = 'user_id'

    def get_queryset(self):
        return Profile.objects.all()


class ProfilesBasicsView(APIView):

    def put(self, request):
        qs = Profile.objects.filter(user_id__in=request.data['ids'])
        serializer = BasicProfileSerializer(qs, many=True)
        return Response(serializer.data)


class ProfileListView(ListAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        queryset = Profile.objects.all()
        username = self.request.query_params.get('username')

        if username:
            queryset = queryset.filter(
                Q(first_name__contains=username) |
                Q(last_name__contains=username)
            )
        return queryset
