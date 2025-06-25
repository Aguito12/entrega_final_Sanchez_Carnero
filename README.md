## TuPrimeraPaginaSanchezCarnero - Proyecto Centro de Estética (Coderhouse)

Este proyecto es una web para un Centro de Estética desarrollada con Django. Permite la gestión de profesionales, tratamientos y clientes, además de ofrecer funcionalidades específicas para que los clientes puedan registrarse, consultar los servicios disponibles y reservar turnos.

---

## Funcionalidades principales

### Para clientes (página de inicio)
- ✅ **Registrarse como cliente**
- ✅ **Ver tratamientos disponibles**
- ✅ **Ver profesionales disponibles**
- ✅ **Reservar turno para un tratamiento**
- ✅ **Enviar una consulta al centro**

### Para el administrador (superusuario)
- ✅ **Agregar profesionales**
- ✅ **Agregar tratamientos (con descripción, precio y profesional responsable)**
- ✅ **Agregar clientes manualmente**
- ✅ **Visualizar y gestionar la información desde el panel de administración**

---

### Funcionalidades implementadas

✅ Herencia de plantillas (`base.html` y otras como `inicio.html`, `formulario.html`, etc.)  
✅ Tres modelos (`Cliente`, `Profesional`, `Tratamiento`)  
✅ Un formulario por cada modelo para insertar datos  
✅ Un formulario de búsqueda de clientes por nombre  
✅ Administración protegida por Django Admin  



## Modelos utilizados (en `models.py`)

### 1. `Cliente`
Contiene nombre, apellido, email, teléfono.

### 2. `Profesional`
Contiene nombre, apellido, especialidad.

### 3. `Tratamiento`
Incluye nombre, descripción, precio y profesional asociado.

### 4. `Reserva`
Asocia cliente, tratamiento, fecha de turno y un mensaje opcional.

### 5. `Consulta`
Formulario de contacto donde el cliente deja su consulta general.

---

## Formularios (en `forms.py`)

- `ClienteForm` → Para registrar clientes
- `ProfesionalForm` → Para registrar profesionales
- `TratamientoForm` → Para registrar tratamientos
- `ReservaForm` → Para que el cliente reserve un tratamiento
- `ConsultaForm` → Para que el cliente envíe una consulta

---

## Herencia de plantillas
Todas las páginas extienden de `base.html`, aplicando herencia de plantillas HTML según lo requerido por el patrón MVT.

---

## Búsqueda en base de datos
Incluye un formulario que permite buscar clientes por nombre o apellido.

Ruta: `/buscar-cliente/`

---

## Cómo ejecutar el proyecto

1. Clonar el repositorio:
```bash
git clone https://github.com/Aguito12/TuPrimeraPaginaSanchezCarnero.git
```

2. Crear y activar un entorno virtual (opcional pero recomendado):
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Aplicar migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Crear superusuario:
```bash
python manage.py createsuperuser
```

6. Ejecutar el servidor:
```bash
python manage.py runserver
```

7. Acceder desde el navegador:
- Sitio: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`

---

## Estructura del proyecto
```
AppCoder/
├── templates/
│   └── AppCoder/
│       ├── base.html
│       ├── inicio.html
│       ├── ver_tratamientos.html
│       ├── ver_profesionales.html
│       ├── cliente_form.html
│       ├── tratamiento_form.html
│       ├── profesional_form.html
│       ├── reserva_form.html
│       ├── consulta_form.html
│       └── buscar_cliente.html
├── models.py
├── views.py
├── forms.py
└── urls.py
```

---

## Autor
Maria Agostina Sanchez Carnero

## Comisión
78110-python
