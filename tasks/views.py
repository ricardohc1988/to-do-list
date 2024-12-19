from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated

class TaskListCreateAPIView(generics.ListCreateAPIView):
    # Permite obtener solo las tareas del usuario autenticado
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Solo obtiene tareas del usuario autenticado
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Asocia la tarea al usuario autenticado
        serializer.save(user=self.request.user)

