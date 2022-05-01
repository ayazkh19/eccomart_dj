from django.urls import path
# dot is relative import of the same folder we are import views
from . import views
# this app_name is useful for addressing the urls in templates
# this is used to make dynamic urls in html template files
app_name = "artstore"

# as we are directed by ecommarts urls.py file to this file
# now the server look into the urls of the current app
# to display a view which is imported above
# empty quotes represent index or homepage.
urlpatterns = [
    path('', views.home_page, name='homepage'),
    path('store/', views.store, name='store'),
    path('search/', views.search_product, name='search'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('processCheckout', views.process_checkout, name='processCheckout'),
    path('register/', views.user_registration, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('orders/', views.orders, name='orders')
]