from django.urls import path
from . import views

urlpatterns = [
    # using generic views
    path('', views.product_list_create_view),
    path('<int:pk>/update/', views.product_update_view),
    path('<int:pk>/delete/', views.product_detail_view),
    path('<int:pk>/', views.product_detail_view),

    # using function views (explicit)
    # path('', views.product_alt_view),
    # path('<int:pk>/', views.product_alt_view)
    

]
