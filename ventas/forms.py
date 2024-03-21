from django import forms
from ventas.models import *
from decimal import Decimal, InvalidOperation, InvalidOperation, ROUND_HALF_UP
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import HiddenInput
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


from django.forms import DecimalField
from django.utils.translation import gettext_lazy as _


class AgregarClienteForm(forms.ModelForm):

    documentoidentidad = forms.IntegerField(required=True)
    primer_nombre = forms.CharField(max_length=45)
    segundo_nombre = forms.CharField(max_length=45, required=False)
    primer_apellido = forms.CharField(max_length=45)
    segundo_apellido = forms.CharField(max_length=45, required=False)
    genero = forms.CharField(max_length=20)

    telefono = forms.CharField(max_length=20)
    correo = forms.EmailField(max_length=60)

    direccion = forms.CharField(max_length=60)
    barrio = forms.CharField(max_length=45)
    ciudad = forms.ModelChoiceField(queryset=Ciudad.objects.all())

    class Meta:
        model = Cliente
        fields = ('documentoidentidad', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'genero', 'ciudad', 'barrio',
                   'direccion','telefono', 'correo',  'idtipo_comercio', 'idtipo_cliente', 'cod_cliente', 'cupo_credito')
        labels = {'documentoidentidad':'Documento Identidad', 'primer_nombre':'Primer Nombre','segundo_nombre':'Segundo Nombre', 'primer_apellido':'Primer Apellido',
                  'segundo_apellido':'Segundo Apellido', 'genero':'Genero','telefono':'Telefono', 'correo':'Correo Electronico',
                  'direccion':'Direccion', 'barrio':'Barrio','ciudad':'Ciudad', 'idtipo_comercio':'Tipo de Comercio', 
                  "idtipo_cliente":"Tipo de Cliente", "cod_cliente":"Codigo del Cliente", "cupo_credito":"Cupo de Credito"}
        
class EditarClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ('cupo_credito', 'idtipo_comercio', 'idtipo_cliente', 'cod_cliente', 'iddocumento')
        labels = {
            'cupo_credito': 'Cupo de Crédito',
            'idtipo_comercio': 'Tipo de Comercio',
            'idtipo_cliente': 'Tipo de Cliente',
            'cod_cliente': 'Código de Cliente',
            'iddocumento': 'Documento de Identidad (Persona)',
        }
#---------------PERSONA------------
class EditarPersonaForm(forms.ModelForm):
    
    class Meta:
        model = Persona
        fields = ('documentoidentidad', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'genero', 'idcontacto', 'iddireccion')
        labels = {
            'documentoidentidad': 'Documento de Identidad',
            'primer_nombre': 'Primer Nombre',
            'segundo_nombre': 'Segundo Nombre',
            'primer_apellido': 'Primer Apellido',
            'segundo_apellido': 'Segundo Apellido',
            'genero': 'Género',
            'idcontacto': 'Contacto',
            'iddireccion': 'Dirección',
        }
#-----------Empleado -------------
      
class AgregarEmpleadoForm(forms.ModelForm):

    documentoidentidad = forms.IntegerField(required=True)
    primer_nombre = forms.CharField(max_length=45)
    segundo_nombre = forms.CharField(max_length=45, required=False)
    primer_apellido = forms.CharField(max_length=45)
    segundo_apellido = forms.CharField(max_length=45, required=False)
    genero = forms.CharField(max_length=20)

    telefono = forms.CharField(max_length=20)
    correo = forms.EmailField(max_length=60)

    direccion = forms.CharField(max_length=60)
    barrio = forms.CharField(max_length=45)
    ciudad = forms.ModelChoiceField(queryset=Ciudad.objects.all())
    cod_empleado = forms.IntegerField(required=True)
    usuario = forms.IntegerField(required=True)
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))  # Utiliza el widget DateInput
    fecha_ingreso = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))  # Utiliza el widget DateInput
    contrasena = forms.CharField(max_length=60, widget=forms.PasswordInput())


    class Meta:
        model = Empleado
        fields = ['documentoidentidad', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'genero', 'ciudad', 'barrio',
                   'direccion','telefono', 'correo',  'cod_empleado', 'fecha_nacimiento', 'fecha_ingreso', 'salario', 'rh', 'idarl', 'ideps', 'idfondo_pension', 'idcargo_empleado','idrolusuario'] 
        labels = {'documentoidentidad':'Documento Identidad', 'primer_nombre':'Primer Nombre','segundo_nombre':'Segundo Nombre', 'primer_apellido':'Primer Apellido',
                  'segundo_apellido':'Segundo Apellido', 'genero':'Genero','telefono':'Telefono', 'correo':'Correo Electronico',
                  'direccion':'Direccion', 'barrio':'Barrio','ciudad':'Ciudad', 'cod_empleado':'Codigo Empleado', 
                  "fecha_ingresa":"Fecha Ingreso", "salario":"Salario Basico", "fecha_nacimiento":"Fecha Nacimiento", "fecha_ingreso":"Fecha Ingreso", "rh":"RH","idarl":"ARL", "ideps":"EPS", "idfondo_pensoion":"Fondo Pension",
                   "idcargo_empleado":"Cargo Empleado", "idusuario":"Usuario","contrasena":"Contraseña","idrolusuario":"Role Designado"}

"""
class EditarEmpleadoForm(forms.ModelForm):
    documentoidentidad = forms.IntegerField(required=True)
    primer_nombre = forms.CharField(max_length=45)
    segundo_nombre = forms.CharField(max_length=45, required=False)
    primer_apellido = forms.CharField(max_length=45)
    segundo_apellido = forms.CharField(max_length=45, required=False)
    genero = forms.CharField(max_length=20)

    telefono = forms.CharField(max_length=20)
    correo = forms.EmailField(max_length=60)

    direccion = forms.CharField(max_length=60)
    barrio = forms.CharField(max_length=45)
    ciudad = forms.ModelChoiceField(queryset=Ciudad.objects.all())
    idtipo_comercio = forms.ModelChoiceField(queryset=TipoComercio.objects.all())
    idtipo_cliente = forms.ModelChoiceField(queryset=TipoCliente.objects.all())

    class Meta:
        model = Cliente
        fields = ['documentoidentidad', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'genero', 'ciudad', 'barrio',
                   'direccion','telefono', 'correo',  'idtipo_comercio', 'idtipo_cliente', 'cod_cliente', 'cupo_credito'] 
        labels = {'documentoidentidad':'Documento Identidad', 'primer_nombre':'Primer Nombre','segundo_nombre':'Segundo Nombre', 'primer_apellido':'Primer Apellido',
                  'segundo_apellido':'Segundo Apellido', 'genero':'Genero','telefono':'Telefono', 'correo':'Correo Electronico',
                  'direccion':'Direccion', 'barrio':'Barrio','ciudad':'Ciudad', 'idtipo_comercio':'Tipo de Comercio', 
                  "idtipo_cliente":"Tipo de Cliente", "cod_cliente":"Codigo del Cliente", "cupo_credito":"Cupo de Credito"}
        
        
        widgets = {
            'cod_cliente':forms.TextInput(attrs={'type': 'text', 'id': 'codcliente_editar'}),
            'documentoidentidad':forms.TextInput(attrs={'id': 'documentoidentidad_editar'}),
            'primer_nombre':forms.TextInput(attrs={'id':'primnombre_editar'}),
            'segundo_nombre':forms.TextInput(attrs={'id':'segundonom_editar'}),
            'primer_apellido':forms.TextInput(attrs={'id':'primapellido_editar'}), 
            'segundo_apellido':forms.TextInput(attrs={'id':'segapellido_editar'}),
            'genero':forms.TextInput(attrs={'id':'genero_editar'}),
            'ciudad':forms.TextInput(attrs={'id':'ciudad_editar'}),
            'barrio':forms.TextInput(attrs={'id':'barrio_editar'}),
            'direccion':forms.TextInput(attrs={'id':'direccion_editar'}),
            'telefono':forms.TextInput(attrs={'id':'telefono_editar'}),
            'correo':forms.TextInput(attrs={'id':'correo_editar'}),   
            'idtipo_comercio':forms.TextInput(attrs={'id':'tipocomercio_editar'}),
            'idtipo_cliente':forms.TextInput(attrs={'id':'tipocliente_editar'}),
            'cupo_credito':forms.TextInput(attrs={'id':'cupocredito_editar'}),}


"""
#------------------- PRODUCTOS-----------------------------

class AgregarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'precio_venta', 'descripcion_producto', 'cantidad_productos', 'idcategoria_producto', 'idtalla', 'cod_producto']
        labels = {
            'nombre_producto': 'Producto',
            'precio_venta': 'Precio',
            'descripcion_producto': 'Descripción',
            'cantidad_productos': 'Cantidad de Productos',
            'idcategoria_producto': 'Categoría Producto',
            'idtalla': 'Talla',
            'cod_producto': 'Codigo Producto'
        }




class EditarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'precio_venta', 'descripcion_producto', 'cantidad_productos', 'idcategoria_producto', 'idtalla', 'cod_producto']
        labels = {
            'nombre_producto': 'Producto',
            'precio_venta': 'Precio',
            'descripcion_producto': 'Descripción',
            'cantidad_productos': 'Cantidad de Productos',
            'idcategoria_producto': 'Categoría Producto',
            'idtalla': 'Talla',
            'cod_producto': 'Codigo Producto'
        }



#-----------------------INVENTARIOS -----------------------------

class AgregarInventarioForm(forms.ModelForm):

    class Meta:
        model = Inventario
        fields = ['idinventario','fecha_inventario','cantidad_productos', 'cod_producto','idtipo_movimiento','cod_empleado', 'idtalla', 'idubicacion_inventario'] 
        labels = {'idinventario':'Cod Inventario','cantidad_productos':'Cantidad Productos','cod_producto': 'Codigo Producto',
                   'cod_empleado': 'Codigo Empleado', 'idtalla':'Talla','idtipomovimiento_movimiento':'Tipo Movimiento', 'idubicacioninventarioinv':'Ubicacion Producto'}

class EditarInventarioForm(forms.ModelForm):

    class Meta:
        model = Inventario
        fields = ['idinventario', 'fecha_inventario', 'cantidad_productos', 'cod_producto', 'idtipo_movimiento', 'cod_empleado', 'idtalla', 'idubicacion_inventario']
        labels = {'idinventario': 'Cod Inventario', 'fecha_inventario': 'Fecha Inventario', 'cantidad_productos': 'Cantidad Productos', 'cod_producto': 'Codigo Producto',
                   'cod_empleado': 'Codigo Empleado', 'idtalla': 'Talla', 'idtipo_movimiento': 'Tipo Movimiento', 'idubicacion_inventario': 'Ubicacion Producto'}
        
#------------------- VENTAS -----------------

class AgregarVentaForm(forms.ModelForm):
    
    cod_cliente = forms.ModelChoiceField(queryset=Cliente.objects.all())
    # Otros campos de AgregarVentaForm...

    descuento_porcentaje = forms.DecimalField(
        label='Descuento (%)',
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )

    class Meta:
        model = Venta
        fields = ['idventa', 'fecha_venta', 'cod_empleado', 'cod_cliente']
        labels = {'idventa': 'No. Venta', 'fecha_venta': 'fecha_venta', 'cod_empleado': 'Vendido por:', 'cod_cliente': 'Cliente a Facturar'}
        widgets = {}

    def clean(self):
        cleaned_data = super().clean()
        cantidad_productos = cleaned_data.get('cantidad_productos')
        precio_venta = cleaned_data.get('precio_venta')
        descuento_porcentaje = cleaned_data.get('descuento_porcentaje')

        if cantidad_productos is not None and precio_venta is not None and descuento_porcentaje is not None:
            total_venta = cantidad_productos * precio_venta
            descuento_venta = total_venta * (descuento_porcentaje / 100)
            total_venta_con_descuento = total_venta - descuento_venta

            cleaned_data['descuento_venta'] = descuento_venta
            cleaned_data['total_venta'] = total_venta_con_descuento

        cod_producto = cleaned_data.get('cod_producto')
        if cod_producto:
            producto = Producto.objects.get(cod_producto=cod_producto)
            if producto.cantidad_productos is not None and cantidad_productos is not None and producto.cantidad_productos < cantidad_productos:
                raise forms.ValidationError("No hay suficientes productos en el inventario.")

        return cleaned_data








class EditarVentaForm(forms.ModelForm):
    total_venta = forms.DecimalField(label='Total Venta', disabled=True, required=False)

    class Meta:
        model = Venta
        fields = ['idventa', 'fecha_venta', 'cantidad_productos', 'descuento_venta', 'precio_venta', 'total_venta', 'cod_empleado', 'cod_producto', 'cod_cliente'] 
        labels = {'idventa':'No. Venta', 'fecha_venta':'Fecha de Venta', 'cantidad_productos':'Cantidad Productos', 'descuento_venta':'Total Descuento', 'precio_venta':'Valor Unidad', 'total_venta':'Total Venta:', 'cod_empleado':'Vendido por:', 'cod_producto':'Producto', 'cod_cliente':'Cliente a Facturar'}
       

    def __init__(self, *args, **kwargs):
        super(EditarVentaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar'))

    def clean(self):
        cleaned_data = super().clean()
        cantidad_productos = int(cleaned_data.get('cantidad_productos'))
        precio_venta = Decimal(cleaned_data.get('cod_producto').precio_venta)
        descuento_venta = Decimal(cleaned_data.get('descuento_venta'))

        if cantidad_productos is not None and precio_venta is not None and descuento_venta is not None:
            total_venta = cantidad_productos * precio_venta - descuento_venta
            cleaned_data['total_venta'] = total_venta

        return cleaned_data

    #-----------------------NOVEDAD EMPLEADO -----------------------------

class AgregarNovedadEmpleadoForm(forms.ModelForm):
    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'})) 
    fechafin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'})) 

    class Meta:
        model = Novedadpersonal
        fields = ['idnovedadpersonal','fecha_inicio','fechafin', 'descripcion','idtiponovedad_personal','codigo_empleado'] 
        labels = {'idnovedadpersonal':'Cod Novedad','fecha_inicio':'Fecha Inicial','fechafin': 'Fecha Final',
                   'cod_empleado': 'Codigo Empleado', 'descripcion':'Descripcion','idtiponovedad_personal':'Tipo Novedad'}


    #-----------------------PQRS -----------------------------

class AgregarPqrsForm(forms.ModelForm):

    class Meta:
        model = Pqr
        fields = ['idpqr','fecha_inicio','fecha_cierre', 'motivo_pqr','cod_empleado','cod_cliente', 'idtipopqr', 'idestadopqr'] 
        labels = {'idpqr':'Cod Pqrs','fecha_inicio':'Fecha Inicial','fecha_cierre': 'Fecha Cierre', 'motivo_pqr':'Descripcion',
                   'cod_empleado': 'Codigo Empleado', 'cod_cliente':'Cliente', 'idtipopqr':'Tipo Pqrs', 'idestadopqr':'Estado Actual'}
        exclude = ['fecha_cierre']

    #-----------------------Novedad Producto -----------------------------

class AgregarNovedadProductoForm(forms.ModelForm):


    class Meta:
        model = Novedadproducto
        fields = ['idnovedad_producto','fecha_novedad','descripcion','cantidad_productos','tiponovedad_producto','cod_producto','cod_empleado','idinventario'] 
        labels = {'idnovedadproducto':'Cod Novedad','fecha_novedad':'Fecha Novedad','cantidad_productos':'Cantidad de Prodcutos','tiponovedad_producto':'tipo de Novedad',
                   'cod_empleado': 'Codigo Empleado', 'descripcion':'Descripcion','cod_producto':'Producto','idinventario':'No. Inventario'}



class EditarNovedadProductoForm(forms.ModelForm):
    class Meta:
        model = Novedadproducto
        fields = ['fecha_novedad', 'descripcion', 'cantidad_productos', 'tiponovedad_producto', 'cod_producto', 'cod_empleado', 'idinventario']
        labels = {
            'fecha_novedad': 'Fecha Novedad',
            'cantidad_productos': 'Cantidad de Productos',
            'tiponovedad_producto': 'Tipo de Novedad',
            'cod_empleado': 'Codigo Empleado',
            'descripcion': 'Descripcion',
            'cod_producto': 'Producto',
            'idinventario': 'No. Inventario'
        }

