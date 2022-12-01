from django.urls import path

from .views import index, create, update, delete, confirm_delete

urlpatterns = [
  path('', index, name='index'),
  path('criar/', create, name='create'),
  path('atualizar/user_id=<int:user_id>', update, name='update'),
  path('deletar/user_id=<int:user_id>', delete, name='delete'),
  path('confirmar-delecao/<int:user_id>/<str:user_name>', confirm_delete, name='confirm_delete'),
]