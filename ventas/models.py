from django.db import models
from django.utils import timezone
from decimal import Decimal

# Create your models here.

class RolUsuario(models.Model):
    idrol_usuario = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=45, unique=True, blank=False)

    class Meta:
        verbose_name = 'roldeusuario'
        verbose_name_plural = 'rolesusuario'
    def __str__(self):
        return f"{self.nombre_rol}"


    
class Arl(models.Model):
    idarl = models.AutoField(primary_key=True)
    arl = models.CharField(max_length=45, unique=True, blank=False, null=False)

    class Meta:
        verbose_name = 'ARL'
        verbose_name_plural = 'ARLS'
    def __str__(self):
        return f"{self.arl}"



class Eps(models.Model):
    ideps = models.AutoField(primary_key=True)
    eps = models.CharField(max_length=45, unique=True, blank=False)

    class Meta: 
        verbose_name = 'EPS'
        verbose_name_plural = 'EPSS'
    def __str__(self):
            return f"{self.eps}"


class FondoPension(models.Model):
    idfondo_pension = models.AutoField(primary_key=True)
    fondo_pension = models.CharField(max_length=45, unique=True, blank=False)

    class Meta: 
        verbose_name = 'fondopension'
        verbose_name_plural = 'fondospension'
    def __str__(self):
        return f"{self.fondo_pension}"


class CargoEmpleado(models.Model):
    idcargo_empleado = models.AutoField(primary_key=True)
    cargo_empleado = models.CharField(max_length=45, unique=True, blank=False, null=False)

    class Meta: 
        verbose_name = 'cargoempleado'
        verbose_name_plural = 'cargosempleados'
    def __str__(self):
        return f"{self.cargo_empleado}"


class CategoriaProducto(models.Model):
    idcategoria_producto = models.AutoField(primary_key=True)
    categoria_producto = models.CharField(max_length=45, unique=True, blank=False, null=False)

    class Meta: 
        verbose_name = 'categoriaproducto'
        verbose_name_plural = 'categoriasproducto'
    def __str__(self):
        return f"{self.categoria_producto}"



class Ciudad(models.Model):
    idciudad = models.AutoField(primary_key=True)
    ciudad = models.CharField(max_length=45, blank=False, null=False)

    class Meta: 
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
    def __str__(self):
        return f"{self.ciudad}"



class TipoCliente(models.Model):
    idtipocliente = models.AutoField(primary_key=True)
    tipo_cliente = models.CharField(max_length=45, unique=True, blank=False)

    class Meta: 
        verbose_name = 'tipocliente'
        verbose_name_plural = 'tiposcliente'
    def __str__(self):
        return f"{self.tipo_cliente}"



class TipoComercio(models.Model):
    idtipo_comercio = models.AutoField(primary_key=True)
    tipo_comercio = models.CharField(max_length=45, unique=True, blank=False)

    class Meta: 
        verbose_name = 'tipocomercio'
        verbose_name_plural = 'tiposcomercio'
    def __str__(self):
        return f"{self.tipo_comercio}"


class EstadoComprobante(models.Model):
    idestado_comprobante = models.AutoField(primary_key=True)
    estado_comprobante = models.CharField(max_length=45, unique=True, blank=False)

    class Meta: 
        verbose_name = 'estadocomprobante'
        verbose_name_plural = 'estadoscomprobante'
    def __str__(self):
        return f"{self.estado_comprobante}"


class EstadoPQR(models.Model):
    idestado_pqr = models.AutoField(primary_key=True)
    estado_pqr = models.CharField(max_length=45, unique=True, blank=False)

    class Meta: 
        verbose_name = 'estadopqr'
        verbose_name_plural = 'estadospqr'
    def __str__(self):
        return f"{self.estado_pqr}"



class FormaPago(models.Model):
    idforma_pago = models.AutoField(primary_key=True)
    forma_pago = models.CharField(max_length=45, unique=True, blank=False)

    class Meta: 
        verbose_name = 'formapago'
        verbose_name_plural = 'formapago'
    def __str__(self):
        return f"{self.forma_pago}"



class Tipomovimiento(models.Model):
    idtipo_movimiento = models.AutoField(primary_key=True)
    tipo_movimiento = models.CharField(max_length=45, unique=True)

    class Meta: 
        verbose_name = 'tipomovimiento'
        verbose_name_plural = 'tiposmovimiento'
    def __str__(self):
        return f"{self.tipo_movimiento}"


class Tiponovedadpersonal(models.Model):
    idtiponovedad_personal = models.AutoField(primary_key=True)
    novedad_personal = models.CharField(max_length=45, unique=True)

    class Meta: 
        verbose_name = 'tiponovedadpersonal'
        verbose_name_plural = 'tiposnovedadpersonal'
    def __str__(self):
        return f"{self.novedad_personal}"



class Tiponovedadproducto(models.Model):
    idtiponovedad_prodcuto = models.AutoField(primary_key=True)
    novedad_producto = models.CharField(max_length=45, unique=True)

    class Meta: 
        verbose_name = 'Tiponovedadproducto'
        verbose_name_plural = 'Tiposnovedadproducto'
    def __str__(self):
        return f"{self.novedad_producto}"


class TipoPQR(models.Model):
    idtipo_pqr = models.AutoField(primary_key=True)
    tipo_pqr = models.CharField(max_length=45, unique=True)

    class Meta: 
        verbose_name = 'Tipopqr'
        verbose_name_plural = 'Tipospqr'
    def __str__(self):
        return f"{self.tipo_pqr}"



class Ubicacioninventario(models.Model):
    idubicacion_inv = models.AutoField(primary_key=True)
    ubicacion_inventario = models.CharField(max_length=45, unique=True)

    class Meta: 
        verbose_name = 'ubicacioninventario'
        verbose_name_plural = 'ubicacionesnventario'
    def __str__(self):
        return f"{self.ubicacion_inventario}"


class Talla(models.Model):
    idtalla = models.AutoField(primary_key=True)
    talla = models.CharField(max_length=45, unique=True)

    class Meta: 
        verbose_name = 'talla'
        verbose_name_plural = 'tallas'
    def __str__(self):
        return f"{self.talla}"


class Contacto(models.Model):
    idcontacto = models.AutoField(primary_key=True)
    telefono = models.CharField(max_length=20, unique=True)
    correo = models.EmailField(max_length=60, unique=True)

    class Meta: 
        verbose_name = 'contacto'
        verbose_name_plural = 'contactos'
    def __str__(self):
        return f"{self.idcontacto} "



class Direccion(models.Model):
    iddireccion = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=60)
    barrio = models.CharField(max_length=45)
    idciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    class Meta: 
        verbose_name = 'direccion'
        verbose_name_plural = 'direcciones'
    def __str__(self):
        return f"{self.iddireccion}"



class Usuarioid(models.Model):
    idusuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=45)
    contrasena = models.CharField(max_length=25, blank=False, null=False)

    class Meta: 
        verbose_name = 'usuarioID'
        verbose_name_plural = 'usuariosID'
    def __str__(self):
        return f"{self.idusuario}"



class Persona(models.Model):
    documentoidentidad = models.IntegerField(primary_key=True, unique=True, blank=False, null=False)
    primer_nombre = models.CharField(max_length=45, null=False, blank=False)
    segundo_nombre = models.CharField(max_length=45, blank=True, null=True)
    primer_apellido = models.CharField(max_length=45, null=False, blank=False)
    segundo_apellido = models.CharField(max_length=45, blank=True, null=True)
    genero = models.CharField(max_length=20, null=False, blank=False)
    idcontacto = models.OneToOneField(Contacto, on_delete=models.CASCADE) 
    iddireccion = models.OneToOneField(Direccion, on_delete=models.CASCADE) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta: 
        verbose_name = 'persona'
        verbose_name_plural = 'personas'
    def __str__(self):
        return f"{self.documentoidentidad}"

    
class Cliente(models.Model):
    cod_cliente = models.IntegerField(primary_key=True, unique=True, blank=False, null=False)
    cupo_credito = models.IntegerField()
    iddocumento = models.ForeignKey(Persona, on_delete=models.CASCADE)
    idtipo_comercio = models.ForeignKey(TipoComercio, on_delete=models.CASCADE)
    idtipo_cliente = models.ForeignKey(TipoCliente,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta: 
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
    def __str__(self):
        return f"{self.cod_cliente}"
    



class Empleado(models.Model):
    cod_empleado = models.IntegerField(primary_key=True, unique=True, blank=False, null=False)
    fecha_ingreso = models.DateField(null=False, blank=False)
    salario = models.FloatField(null=False, blank=False)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    rh = models.CharField(null=False, blank=False, max_length=5)
    iddocumento = models.ForeignKey(Persona, on_delete=models.CASCADE)
    idarl = models.ForeignKey(Arl, on_delete=models.CASCADE)
    ideps = models.ForeignKey(Eps, on_delete=models.CASCADE)
    idfondo_pension = models.ForeignKey(FondoPension, on_delete=models.CASCADE)
    idcargo_empleado = models.ForeignKey(CargoEmpleado, on_delete=models.CASCADE)
    idusuario = models.ForeignKey(Usuarioid, on_delete=models.CASCADE)
    idrolusuario = models.ForeignKey(RolUsuario, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name = 'empleado'
        verbose_name_plural = 'empleados'
    def __str__(self):
        return f"{self.iddocumento.primer_nombre} {self.iddocumento.primer_apellido}"


class Producto(models.Model):
    cod_producto = models.CharField(primary_key=True, unique=True, blank=False, null=False, max_length=15)
    nombre_producto = models.CharField(max_length=45, null=False)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    descripcion_producto = models.CharField(max_length=45)
    cantidad_productos = models.PositiveIntegerField(null=False)
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)
    idcategoria_producto = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    idtalla = models.ForeignKey(Talla, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
    def __str__(self):
        return f"{self.nombre_producto} {self.precio_venta} "



class Novedadpersonal(models.Model):
    idnovedadpersonal = models.AutoField(primary_key=True)
    fecha_inicio = models.DateField(null=False, blank=False)
    fechafin = models.DateField(null=True, blank=True)
    descripcion = models.CharField(max_length=90, null=False, blank=False)
    idtiponovedad_personal = models.ForeignKey(Tiponovedadpersonal, on_delete=models.CASCADE)
    codigo_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name = 'novedadpersonal'
        verbose_name_plural = 'novedadespersonal'
    def __str__(self):
        return f"{self.idnovedadpersonal}"



class Pqr(models.Model):
    idpqr = models.AutoField(primary_key=True)  
    fecha_inicio = models.DateTimeField(null=False, blank=False, default=timezone.now)
    motivo_pqr = models.CharField(max_length=250, null=False, blank=False)
    fecha_cierre = models.DateField(null=True, blank=True)
    cod_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)  
    cod_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  
    idtipopqr = models.ForeignKey(TipoPQR, on_delete=models.CASCADE)  
    idestadopqr = models.ForeignKey(EstadoPQR, on_delete=models.CASCADE) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name = 'PQR'
        verbose_name_plural = 'PQRS'
    def __str__(self):
        return f"{self.idpqr}"

class Cotizacion(models.Model):
    idcotizacion = models.AutoField(primary_key=True)  
    fecha_cotizacion = models.DateTimeField(auto_now_add=True)  
    cantidad_productos = models.PositiveIntegerField() 
    valortotal_productos = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)  
    descuento = models.IntegerField(null=True, blank=True)
    cod_cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)  
    cod_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)  
    cod_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name = 'cotizacion'
        verbose_name_plural = 'cotizaciones'
    def __str__(self):
        return f"{self.idcotizacion}"




class Venta(models.Model):
    idventa = models.AutoField(primary_key=True)
    cantidad_productos = models.IntegerField(null=True, blank=True)
    descuento_venta = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0.0)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0.0)
    total_venta = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    fecha_venta = models.DateTimeField(null=False, blank=False, default=timezone.now)
    cod_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cod_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    cod_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'venta'
        verbose_name_plural = 'ventas'

    
def save(self, *args, **kwargs):
    if self.cod_producto:
        producto = self.cod_producto
        producto.cantidad_productos -= self.cantidad_productos
        producto.save()

    # Convertir self.precio_venta a Decimal
    precio_venta_decimal = Decimal(str(self.precio_venta))

    # Calcular el total de la venta
    total_venta = 0
    for detalle_venta in self.detalle_venta_set.all():
        subtotal = detalle_venta.cantidad_productos * detalle_venta.precio_venta
        total_venta += subtotal

    total_venta -= self.descuento_venta

    # Asignar el total de la venta calculado
    self.total_venta = total_venta

    # Verificar que total_venta no sea None o un valor vacío
    if self.total_venta is None or self.total_venta == '':
        raise ValueError("El campo 'total_venta' no puede ser nulo o vacío")

    super(Venta, self).save(*args, **kwargs)


  



class Inventario(models.Model):
    idinventario = models.AutoField(primary_key=True)  
    fecha_inventario = models.DateField(null=False, blank=False, default=timezone.now) 
    cantidad_productos = models.IntegerField(null=False, blank=False)  
    cod_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  
    idtipo_movimiento = models.ForeignKey(Tipomovimiento, on_delete=models.CASCADE)  
    cod_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    idtalla = models.ForeignKey(Talla, on_delete=models.CASCADE)  
    idubicacion_inventario = models.ForeignKey(Ubicacioninventario, on_delete=models.CASCADE)  
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name = 'inventario'
        verbose_name_plural = 'inventarios'
    def __str__(self):
        return f"{self.idinventario}"


class Comprobanteventa(models.Model):
    idcomprobante_venta = models.AutoField(primary_key=True)  
    idventa = models.ForeignKey(Venta, null=False,on_delete=models.CASCADE)  
    fecha_comprobante = models.DateTimeField(auto_now_add=True)  
    idforma_pago = models.ForeignKey(FormaPago, on_delete=models.CASCADE)  
    idestado_comprobante = models.ForeignKey(EstadoComprobante, on_delete=models.CASCADE)  
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name = 'compobanteventa'
        verbose_name_plural = 'comprobantesventa'
    def __str__(self):
        return f"{self.idcomprobante_venta}"


class Novedadproducto(models.Model):
    idnovedad_producto = models.AutoField(primary_key=True)
    fecha_novedad = models.DateField(null=False, blank=False, default=timezone.now) 
    descripcion = models.CharField(max_length=100, null=False)
    cantidad_productos = models.PositiveIntegerField()
    tiponovedad_producto = models.ForeignKey(Tiponovedadproducto, on_delete=models.CASCADE)
    cod_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cod_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    idinventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name = 'novedadproducto'
        verbose_name_plural = 'novedadesproducto'
    def __str__(self):
        return f"{self.idnovedad_producto}"

