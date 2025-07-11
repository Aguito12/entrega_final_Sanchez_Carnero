## TuPrimeraPaginaSanchezCarnero - Proyecto Centro de Estética (Coderhouse)

# 💅 Centro de Estética

¡Bienvenidos al **Centro de Estética**!  
Sitio web desarrollado en Python y Django, orientado a gestionar un centro de estética. Incluye funcionalidades como promociones, tratamientos, reservas y gestión de usuarios.

---

## 📑 Descripción

Este proyecto es una aplicación web estilo blog, adaptada a la temática de un centro de estética.  
Cuenta con:
- Registro y autenticación de usuarios
- Perfiles de usuario editables con avatar, biografía y más
- Creación, edición y visualización de promociones
- Gestión de tratamientos y reservas
- Sistema de consultas
- Panel de administración completo

---

## 🛠️ Tecnologías utilizadas

- **Python 3.13**
- **Django 5.2.2**
- **Bootstrap 5.3**
- **SQLite**
- **django-ckeditor** (para campos de texto enriquecido)
- **Pillow** (manejo de imágenes)

---

## 🚀 Instalación

### Clonar el repositorio

```powershell
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

### Crear entorno virtual

```powershell
python -m venv .venv
```

### Activar entorno virtual (Windows)

```powershell
.venv\Scripts\activate
```

### Instalar dependencias

```powershell
pip install -r requirements.txt
```

### Migrar base de datos

```powershell
python manage.py migrate
```

### Crear superusuario

```powershell
python manage.py createsuperuser
```

### Correr el servidor

```powershell
python manage.py runserver
```

---

## 👤 Usuarios

### Registro

- Usuarios pueden registrarse y crear su perfil.
- Campos requeridos:
  - Nombre de usuario
  - Nombre
  - Apellido
  - Email
  - Teléfono
  - Contraseña
  - Avatar
  - Biografía
  - Fecha de nacimiento

### Login / Logout

- Usuarios pueden iniciar sesión y cerrar sesión desde el menú principal.

---

## 📄 Funcionalidades

✅ **Home / Inicio**  
- Página inicial con presentación visual del centro de estética.

✅ **Acerca de mí**  
- Ruta `/about/` con información sobre el creador del sitio.

✅ **Promociones**  
- Listado de promociones disponibles.
- Visualización de detalle de cada promoción.
- Creación, edición y borrado de promociones (solo administradores).
- Texto enriquecido en las descripciones.
- Imagen asociada a cada promoción.

✅ **Tratamientos**  
- Creación y visualización de tratamientos.
- Gestión de reservas por parte de usuarios.
- Visualización y gestión de reservas en el admin.

✅ **Consultas**  
- Los usuarios pueden enviar consultas.
- Las consultas quedan visibles en el admin para su gestión.

✅ **Perfil de usuario**
- Visualización de datos personales.
- Edición de perfil incluyendo:
  - Nombre
  - Apellido
  - Email
  - Teléfono
  - Avatar
  - Biografía
  - Fecha de nacimiento
  - Cambio de contraseña

✅ **Admin**
- Gestión completa de:
  - Usuarios
  - Promociones
  - Tratamientos
  - Reservas
  - Consultas
  - Clientes
  - Profesionales

---

## 🔗 Navegación

- Home → `/`
- Acerca de mí → `/about/`
- Promociones → `/promociones/`
- Login → `/Cuentas/login/`
- Registro → `/Cuentas/signup/` o `/Cuentas/signup_cliente/`
- Perfil → `/Cuentas/profile/`

---

## 📂 Archivos ignorados en Git

- Base de datos (`db.sqlite3`)
- Carpeta `media/` (imágenes de usuarios)
- Archivos temporales (`__pycache__`, etc.)

---

## 📸 Video demostrativo

Se incluye un video mostrando todas las funcionalidades en menos de 10 minutos.  
(https://youtu.be/UCT3J5tVtjA)

---

## ⚠️ Notas

- La base de datos no se sube al repositorio.
- Para probar el sistema desde cero, crear un superusuario para gestionar datos iniciales.
- Proyecto desarrollado como parte del curso de Python / Django (Coderhouse).

---

## ✅ Verificación de requisitos consignados

### User Story / Brief

* ✅ **Vista "Acerca de mí" en `/about/`**

  * Implementado como página estática con información del autor, accesible desde el menú de navegación.

* ✅ **Vista de blogs en route `/pages/`**

  * Adaptado a “Promociones” en `/promociones/` cumpliendo la misma lógica.

* ✅ **Pantalla de listado de páginas (promociones)**

  * Implementada en `/promociones/`.

* ✅ **“Leer más” navega al detalle**

  * Cada promoción tiene botón “Leer más” que lleva al detalle.

* ✅ **Mensaje “No hay páginas aún”**

  * Implementado para cuando no existen promociones.

* ✅ **Edición o borrado solo logueado**

  * Crear, editar o eliminar promociones solo lo puede hacer el admin o superuser.

---

### Piezas sugeridas

* ✅ **NavBar**

  * Heredado en el template base, presente en todas las páginas.

* ✅ **Home**

  * Vista inicial.

* ✅ **About**

  * Implementado en `/about/`.

* ✅ **Pages** (Promociones)

  * Implementado como `/promociones/`.

* ✅ **Login**

  * Implementado en `/Cuentas/login/`.

* ✅ **Signup**

  * Implementado en `/Cuentas/signup/` y `/Cuentas/signup_cliente/`.

* ✅ **Profile**

  * Implementado en `/Cuentas/profile/`.

* ✅ **Logout**

  * Disponible desde el NavBar.

* ✅ **Get pages**

  * Listado de promociones.

* ✅ **Get page**

  * Vista de detalle de cada promoción.

* ✅ **Create page**

  * Creación de promociones, restringida al admin.

* ✅ **Update page**

  * Edición de promociones, restringida al admin.

* ✅ **Delete page**

  * Eliminación de promociones, restringida al admin.

* ✅ **Get profile**

  * Vista de perfil del usuario.

* ✅ **Update profile**

  * Permite modificar datos del perfil y contraseña.

---

### Requisitos base

* ✅ **Entrega individual**

  * Trabajo individual.

* ✅ **Repositorio en GitHub**

  * Confirmado.

* ✅ **Readme**

  * Este documento.

* ✅ **Video demostrativo**

  * https://www.youtube.com/watch?v=UCT3J5tVtjA

* ✅ **No subir `db.sqlite3`**

  * Ignorado en `.gitignore`.

* ✅ **Uso de herencia de templates**

  * Base template con NavBar y bloques.

* ✅ **gitignore**

  * Incluye:

    * `__pycache__`
    * `db.sqlite3`
    * `media`

* ✅ **requirements.txt actualizado**

  * Confirmado.

* ✅ **Manejo de forms con imágenes**

  * Adaptado en templates, views y models.

* ✅ **Mínimo 2 CBV**

  * Se usan varias:

    * `PromocionListView`
    * `PromocionDetailView`
    * `ProfileUpdateView`

* ✅ **Mínimo un mixin en CBV**

  * `LoginRequiredMixin` usado en múltiples CBVs.

* ✅ **Mínimo un decorador en view común**

  * `@login_required` usado en vistas como `profile_view`.

* ✅ **Vista Home**

  * Implementada.

* ✅ **Vista About**

  * Implementada.

* ✅ **Modelo principal con campos requeridos**

  * Modelo `Promocion`:

    * 2 CharField → `titulo`, `subtitulo`
    * Texto enriquecido → `descripcion` (ckeditor)
    * Imagen → `imagen`
    * Fecha → `fecha`

* ✅ **Listado parcial de objetos**

  * Listado de promociones muestra título, subtítulo truncado y fecha.

* ✅ **Mensaje si no hay objetos**

  * Implementado.

* ✅ **Detalle del objeto**

  * Implementado.

* ✅ **Creación, edición, borrado**

  * Implementado (solo admins).

* ✅ **Modelos registrados en admin**

  * Todos registrados:

    * Promocion
    * Profesional
    * Tratamiento
    * Reserva
    * Consulta
    * Cliente

* ✅ **App para usuarios**

  * Implementada como `Cuentas`.

* ✅ **Login, Logout, Registro**

  * Implementados.

* ✅ **Registro solicita campos obligatorios**

  * Username, email, password, más datos adicionales.

* ✅ **Vista de perfil**

  * Implementada.

* ✅ **Vista de edición de perfil**

  * Implementada.

* ✅ **Cambio de contraseña**

  * Implementado dentro de edición de perfil.

---

### Requisitos extra (opcionales)

* ✅ **Consultas**

  * Sistema de consultas implementado y gestionable en admin.

* ✅ **Reserva de tratamientos**

  * Implementado.

* ✅ **Avatar visible en NavBar**

  * Implementado.

---

## 🚀 Estado final

✅ **¡TODOS LOS REQUISITOS DE LA CONSIGNA HAN SIDO CUMPLIDOS!** 🎉

---

## 👩‍💻 Autor

- Nombre y Apellido: Maria Agostina Sanchez Carnero
- GitHub: [Tu Usuario](https://github.com/tu-usuario)
- Comisión: 78110-python
