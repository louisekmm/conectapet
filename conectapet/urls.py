from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
   
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logged_out'),
    path('profile/edit/password_change/', auth_views.PasswordChangeView.as_view( template_name='password_change.html', success_url='password_change/done/'), name="password_change"),
    path('profile/edit/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name="password_change_done"),
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url='done/'), name="password_reset"),
   
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),  
    path('ajax/load-breeds/', views.load_breeds, name='ajax_load_breeds'),
    
    path('ajax/load-combo_adoption/', views.load_combo_adoption, name='ajax_load_combo_adoptions'),
    path('ajax/add-combo_adoption/', views.add_combo_adoption, name='ajax_add_combo_adoption'),
    path('ajax/available_status/', views.available_adopt_status, name='ajax_available_adopt_status'),
    path('ajax/check-ids/', views.check_ids_pet, name='ajax_check_ids'),
    path('ajax/favorite/', views.favorite_status, name='ajax_favorite_status'),
    
    
    #gerenciar pets
    path('pets/list/<str:type>/', views.PetList.as_view(), name='pet_list'),
    path('pets/view/<int:pk>', views.PetView.as_view(), name='pet_view'),
    path('pets/new', views.PetCreate.as_view(), name='pet_new'),
    path('pets/edit/<int:pk>', views.PetUpdate.as_view(), name='pet_edit'),
    path('pets/delete/<int:pk>', views.PetDelete.as_view(), name='pet_delete'),
]

