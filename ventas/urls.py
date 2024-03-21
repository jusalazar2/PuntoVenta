from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('home', views.home, name='home'),
    
    path('index', views.index, name='index'),


    #----------- CLIENTES----------------
    path('Ventas', views.ventas_vista, name='Ventas'),
    path('clientes/', views.clientes_vista, name='Clientes'),
    path('agregar_Cliente/', views.agregar_Cliente_vista, name='agregarCliente'),
    path('editar_Cliente/<int:cod_cliente>/', views.editar_Cliente_vista, name='editarCliente'),


    path('eiminar_Cliente/', views.eliminar_Cliente_vista, name='eliminarCliente'),
    #------EMPLEADO ----------
    path('empleados/', views.empleados_vista, name='Empleados'),
    path('agregar_Empleado/', views.agregar_Empleado_vista, name='agregarEmpleado'),
    path('editar_Empleado/', views.editar_Empleado_vista, name='editarEmpleado'),
    path('eiminar_Empleado/', views.eliminar_Empleado_vista, name='eliminarEmpleado'),
    #---------PRODUCTOS--------------
    path('productos/', views.productos_vista, name='Productos'),
    path('agregar_Producto/', views.agregar_Producto_vista, name='agregarProducto'),
    path('editarProducto/<cod_producto>/', views.editarProducto, name='editarProducto'),
    path('eiminar_Producto/', views.eliminar_Producto_vista, name='eliminarProducto'),
    #-------------- INVENTARIO --------------------------
   path('inventarios/', views.inventarios_vista, name='Inventarios'),
   path('agregar_Inventario/', views.agregar_Inventario_vista, name='agregarInventario'),
   # path('editar_Producto/', views.editar_Inventario_vista, name='editarInventario'),
   path('eiminar_Inventario/', views.eliminar_Inventario_vista, name='eliminarInventario'),
   path('editarInventario/<int:idinventario>/', views.editarInventario, name='editarInventario'),
   path('actualizar-inventario/<str:producto_id>/<str:talla_id>/<int:cantidad>/', views.actualizar_inventario, name='actualizar_inventario'),
   #---------------- VENTAS ----------------------

   path('agregar_Venta/', views.agregar_Venta_vista, name='agregarVenta'),
   # path('editar_Producto/', views.editar_Inventario_vista, name='editarInventario'),
   path('eiminar_Venta/', views.eliminar_Venta_vista, name='eliminarVenta'),
   path('editarVenta/<int:idventa>/', views.editarVenta, name='editarVenta'),
    #-------------- NOVEDADES PERSONAL --------------------------
   path('novedades_empleados/', views.novedad_Empleado_vista, name='NovedadesEmpleados'),
   path('agregar_Novedad_Empleado/', views.agregar_Novedad_Empleado_vista, name='agregarNovedadEmpleado'),
   
   path('eiminar_NovedadEmpleado/', views.eliminar_Novedad_Empleado_vista, name='eliminarNovedadEmpleado'),

       #-------------- PQRS --------------------------
   path('pqrs/', views.pqrs_vista, name='Pqrs'),
   path('agregar_pqrs/', views.agregar_Pqrs_vista, name='agregarPqrs'),
   
   path('eiminar_pqrs/', views.eliminar_Pqrs_vista, name='eliminarPqrs'),

       #-------------- COTIZACION --------------------------
   path('novedades_Productos/', views.novedad_Producto_vista, name='novedadesProductos'),
   path('agregar_Novedad_Producto/', views.agregar_Novedad_Producto_vista, name='agregarNovedadProducto'),
   path('editarNovedadProd/<int:idnovedad_producto>/', views.editarNovedadProducto, name='editarNovedad'),
   
   path('eiminar_Novedad_Producto/', views.eliminar_Novedad_Producto_vista, name='eliminarNovedadProducto'),
   path('get-precio/<str:cod_producto>/', views.get_precio_producto, name='get_precio_producto'),
   path('get-tallas/<str:cod_producto>/', views.get_tallas_disponibles, name='get_tallas_disponibles'),
   path('calcular-precio/<str:producto_id>/<int:cantidad>/', views.calcular_precio, name='calcular_precio'),
   #-------------------------CONTACTO----------------
   path('contacto/', views.contacto, name='contacto'),





]
