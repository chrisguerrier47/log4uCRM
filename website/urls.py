from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>/', views.customer_record, name='record'),
    path('delete_record/<int:pk>/', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>/', views.update_record, name='update_record'),
]


# When the user visits /register/, the register_user view is called,
# which creates and passes a SignUpForm instance to the register.html template.
# {{ form.as_p }} will render the fields of the SignUpForm in the form.

# When the user visits /login/, the login_user view is called,
# which creates and passes a LoginForm instance to the login.html template.
# {{ form.as_p }} will render the fields of the LoginForm in the form.
