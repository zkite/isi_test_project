from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, get_object_or_404
from dialogs.models import Message, Thread
from dialogs.serializers import MessageSerializer, ThreadSerializer


class CreateThreadView(CreateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

    def post(self, request):
        if not request.user.is_authenticated or request.user.user_type != "ADMIN":
            raise PermissionDenied("User don't have enough permissions")
        return super().post(request)


class CreateMessageView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class GetMessageListView(ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        return get_object_or_404(
            self.request.user.threads, id=self.kwargs['thread']
        ).messages

class GetThreadListView(ListAPIView):
    serializer_class = ThreadSerializer

    def get_queryset(self):
        return self.request.user.threads


class UpdateThreadView(UpdateAPIView):
    serializer_class = ThreadSerializer

    def put(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.user_type != "ADMIN":
            raise PermissionDenied("User don't have enough permissions")
        return super().put(request)

    def get_queryset(self):
        return self.request.user.threads

