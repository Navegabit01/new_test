# Gestión de Artículos y Pedidos

## Descripción

Esta aplicación permite la gestión de artículos y pedidos. Está construida con Django y Django REST Framework, y utiliza JWT para la autenticación. La arquitectura sigue principios SOLID y la arquitectura hexagonal para una estructura limpia y mantenible.

## Instalación y Configuración

1. **Clona el repositorio:**

   ```bash
   git clone <url-del-repositorio>
   cd <nombre-del-repositorio>

## Construye la imagen de Docker y corre el contenedor:

* Copiar código
```bash docker build -t myproject .
docker run --name myproject -p 8000:8000 myproject
Ejecuta las migraciones:

docker exec -it myproject python manage.py migrate
Ejecuta las pruebas:

docker exec -it myproject coverage run manage.py test
coverage report
```

## Uso de la API
La aplicación expone una API RESTful para la gestión de artículos y pedidos. A continuación se describen los endpoints disponibles:

Autenticación
Para interactuar con los endpoints protegidos, primero necesitas obtener un token JWT.

### Obtener Token:

URL: /api/token/

Método: POST

Body:

json
Copiar código
``` 
{
    "username": "tu_usuario",
    "password": "tu_contraseña"
}
```
Respuesta:

json
```
{
    "access": "token_de_acceso",
    "refresh": "token_de_actualización"
}
```
Usa el token de acceso en el header Authorization: Bearer <token> para las solicitudes a los endpoints protegidos.

## Artículos

### Crear Artículo:

URL: /api/items/

Método: POST

Body:

json
Copiar código
```
{
    "reference": "REF123",
    "name": "Nombre del Artículo",
    "description": "Descripción del Artículo",
    "price_without_tax": "100.00",
    "tax": "15.00"
}
```
Respuesta:

json
```
{
    "id": 1,
    "reference": "REF123",
    "name": "Nombre del Artículo",
    "description": "Descripción del Artículo",
    "price_without_tax": "100.00",
    "tax": "15.00",
    "created_at": "2024-09-01T00:00:00Z"
}
```

## Obtener Artículo:

URL: /api/items/{id}/

Método: GET

Respuesta:

json
```
{
    "id": 1,
    "reference": "REF123",
    "name": "Nombre del Artículo",
    "description": "Descripción del Artículo",
    "price_without_tax": "100.00",
    "tax": "15.00",
    "created_at": "2024-09-01T00:00:00Z"
}
```
## Actualizar Artículo:

URL: /api/items/{id}/

Método: PUT

Body:

json
Copiar código
```
{
    "reference": "REF124",
    "name": "Nombre Actualizado",
    "description": "Descripción Actualizada",
    "price_without_tax": "120.00",
    "tax": "18.00"
}
```
Respuesta:

json
```
{
    "id": 1,
    "reference": "REF124",
    "name": "Nombre Actualizado",
    "description": "Descripción Actualizada",
    "price_without_tax": "120.00",
    "tax": "18.00",
    "created_at": "2024-09-01T00:00:00Z"
}
```
## Eliminar Artículo:

URL: /api/items/{id}/
Método: DELETE
Respuesta: 204 No Content
Pedidos

## Crear Pedido:

URL: /api/orders/

Método: POST

Body:

json
Copiar código
```
{
    "created_at": "2024-09-01T00:00:00Z",
    "items": [
        {
            "item_id": 1,
            "quantity": 2
        }
    ]
}
```
Respuesta:

json
```
{
    "id": 1,
    "items": [
        {
            "item": {
                "id": 1,
                "reference": "REF123",
                "name": "Nombre del Artículo",
                "description": "Descripción del Artículo",
                "price_without_tax": "100.00",
                "tax": "15.00"
            },
            "quantity": 2
        }
    ],
    "created_at": "2024-09-01T00:00:00Z"
}
```

## Obtener Pedido:

URL: /api/orders/{id}/

Método: GET

Respuesta:

json
```
{
    "id": 1,
    "items": [
        {
            "item": {
                "id": 1,
                "reference": "REF123",
                "name": "Nombre del Artículo",
                "description": "Descripción del Artículo",
                "price_without_tax": "100.00",
                "tax": "15.00"
            },
            "quantity": 2
        }
    ],
    "created_at": "2024-09-01T00:00:00Z"
}
```
## Actualizar Pedido:

URL: /api/orders/{id}/

Método: PUT

Body:

json
Copiar código
```
{
    "created_at": "2024-09-01T00:00:00Z",
    "items": [
        {
            "item_id": 1,
            "quantity": 3
        }
    ]
}
```
Respuesta:

json
```
{
    "id": 1,
    "items": [
        {
            "item": {
                "id": 1,
                "reference": "REF123",
                "name": "Nombre del Artículo",
                "description": "Descripción del Artículo",
                "price_without_tax": "100.00",
                "tax": "15.00"
            },
            "quantity": 3
        }
    ],
    "created_at": "2024-09-01T00:00:00Z"
}
```
## Eliminar Pedido:

URL: /api/orders/{id}/
Método: DELETE
Respuesta: 204 No Content
Pruebas

El proyecto utiliza coverage para asegurar una cobertura de pruebas del 100%. Para ejecutar las pruebas y ver el informe de cobertura, utiliza el siguiente comando:

bash
```
docker exec -it myproject coverage run manage.py test
docker exec -it myproject coverage report
```

Contribución
Si deseas contribuir al proyecto, realiza un fork del repositorio, realiza tus cambios y envía una solicitud de extracción (pull request). Asegúrate de que las pruebas se ejecuten correctamente y de que la cobertura de pruebas sea del 100%.

Licencia
Este proyecto está licenciado bajo la MIT License.

Contacto
Para cualquier pregunta, puedes contactar a navegabit.2020@gmail.com