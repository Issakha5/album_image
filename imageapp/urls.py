from django.urls import path
from django.views.decorators.csrf import csrf_exempt
#from graphene_django.views import GraphQLView
from graphene_file_upload.django import FileUploadGraphQLView
from . import views
from .schema import schema

urlpatterns = [
    path('', views.image_list, name='image_list'),
    path('image/<int:pk>/', views.image_detail, name='image_detail'),
    path('image/new/', views.image_create, name='image_create'),
    path('image/<int:pk>/edit/', views.image_update, name='image_update'),
    path('image/<int:pk>/delete/', views.image_delete, name='image_delete'),
    path("graphql", csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True, schema=schema))),
    #path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),

]
