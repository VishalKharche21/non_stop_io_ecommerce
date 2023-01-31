from django.urls import path,include
from mainapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index,name="index"),
    path("SignUp/",views.csignup,name="signup"),
    path("Login/",views.clogin,name="login"),
    path("Logout/",views.clogout,name="logout"),
    path("Home/",views.Home,name="Home"),
    path("Add-Products/",views.add_products,name="add_products"),
    path("product_list",views.product_list,name="product_list"),
    path("update-product/<int:id>/",views.update_product,name="update_product"),
    path("product-Delete/<int:id>/",views.productDelete,name="productDelete"),
    path("users/",views.users,name="users"),
    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
