from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.urls import include,path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/' , include('api_usuario.api.urls')),
    path('producto/', include('api_producto.api.urls')),
    #path('sku/', include('api_producto.api.urls')),

]

urlpatterns += [

    re_path(r'^Imagen_Producto/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,} )



]
