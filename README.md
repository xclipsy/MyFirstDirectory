# Sistema de Gestión de Inventario

Una aplicación de consola en Python diseñada para gestionar el inventario de un supermercado. Este sistema permite administrar productos, calcular estadísticas y guardar o cargar la información utilizando archivos CSV para asegurar la persistencia de los datos.

## Estructura del Proyecto

El proyecto está modularizado en tres archivos principales para separar la lógica de negocio, la persistencia de datos y la interfaz de usuario:

* **`app.py`**: Es el punto de entrada de la aplicación. Contiene el bucle principal y el menú interactivo que guía al usuario a través de las diferentes opciones del sistema.
* **`servicios.py`**: Módulo que maneja la lógica interna. Incluye las funciones para agregar, mostrar, buscar, actualizar y eliminar productos, además de calcular las estadísticas generales del inventario.
* **`archivos.py`**: Módulo dedicado a la gestión de archivos. Se encarga de guardar el inventario en un archivo `.csv` y de leerlo, manejando excepciones y validando la integridad de los datos ingresados.

## Características Principales

* **Gestión de Productos (CRUD):** Permite registrar nuevos productos, ver la lista completa, buscar elementos específicos por nombre, actualizar precios y eliminar registros.
* **Validaciones de Entrada:** Asegura que las cantidades y precios ingresados sean números válidos y positivos, evitando que el programa se cierre inesperadamente por errores de tipeo del usuario.
* **Persistencia de Datos (CSV):** * Guarda el estado actual del inventario de forma segura.
    * Al cargar un archivo previo, el sistema detecta filas inválidas y ofrece la opción de **sobrescribir** los datos actuales o **fusionarlos** (sumando cantidades y actualizando precios de productos ya existentes).
* **Estadísticas del Sistema:** Calcula y muestra el valor total del inventario, las unidades totales en stock, el producto más caro y el producto con mayor cantidad almacenada.
* **Manejo de Errores:** Captura y maneja excepciones (como `FileNotFoundError`, `PermissionError` o `UnicodeDecodeError`) para mantener la aplicación en funcionamiento constante.

## Requisitos

* Python 3.x
* No se requieren librerías de terceros (utiliza el módulo nativo `csv`).

## Instalación y Uso

1.  Descarga los tres archivos (`app.py`, `servicios.py`, `archivos.py`) y asegúrate de que estén ubicados en la misma carpeta.
2.  Abre una terminal o línea de comandos en el directorio del proyecto.
3.  Inicia la aplicación ejecutando el archivo principal:

    ```bash
    python app.py
    ```
4.  Utiliza los números del 1 al 9 para navegar por las opciones del menú en pantalla.

## Autor

* Luis José Guerrero Bruges
