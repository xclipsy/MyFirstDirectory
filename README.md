# 🚗 Sistema de Gestión de Parqueadero

Este es un script sencillo en **Python** diseñado para administrar la ocupación de un parqueadero de 10 espacios. Permite registrar ingresos, salidas y mantiene la información persistente mediante un archivo de texto local.

## 📋 Características

*   **Persistencia de Datos:** Carga automáticamente el estado previo desde un archivo `registro_parqueadero.txt`.
*   **Gestión Automática:** Busca el primer espacio disponible (marcado con `_`) para nuevos ingresos.
*   **Validaciones:** 
    *   Verifica si el parqueadero está lleno.
    *   Confirma si una placa existe antes de intentar retirarla.
*   **Guardado Final:** Al cerrar el sistema, actualiza el archivo de texto con el estado actual.

## 🛠️ Requisitos

*   Python 3.x

## 🚀 Instrucciones de Uso

1.  **Ejecución:**
    Corre el script desde tu terminal o IDE:
    ```bash
    python nombre_de_tu_archivo.py
    ```

2.  **Operaciones:**
    *   **Ingresar:** Escribe `ingresar` y luego la placa del vehículo. El sistema le asignará el primer lugar libre.
    *   **Sacar:** Escribe `sacar` e ingresa la placa exacta para liberar el espacio.

3.  **Finalización:**
    Cuando el sistema pregunte si desea realizar otra operación, escribe `no`. Esto cerrará el programa y guardará los datos en el archivo `.txt`.

## 📂 Estructura del Proyecto

*   `codigo.py`: Archivo principal con la lógica del sistema.
*   `registro_parqueadero.txt`: Base de datos plana donde se almacenan las placas o espacios vacíos.

---
**Nota:** Si el archivo `registro_parqueadero.txt` no existe, el programa lo creará automáticamente con 10 espacios vacíos en la primera ejecución.
