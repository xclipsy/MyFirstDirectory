# 🛡️ Validador de Credenciales en Python

Este es un script sencillo de Python diseñado para validar formatos de correo electrónico y robustez de contraseñas de manera simultánea. Es ideal para entender los fundamentos de la manipulación de strings y estructuras de control.

## 🚀 Funcionalidades

El script realiza una doble verificación basada en reglas específicas:

### 📧 Validación de Correo
* Debe tener una longitud mínima de **6 caracteres**.
* No debe contener **espacios en blanco**.
* Debe incluir obligatoriamente un punto (`.`) y una arroba (`@`).

### 🔑 Validación de Contraseña
Para que una contraseña sea considerada válida, debe cumplir con:
* **Longitud mínima:** 8 caracteres.
* **Sin espacios:** No se permiten espacios vacíos.
* **Complejidad:** Debe contener al menos **1 número**, **1 mayúscula** y **1 carácter especial**.

---

## 🛠️ Estructura del Código

El corazón del proyecto es la función `verificar_datos()`, la cual utiliza métodos integrados de Python como:
* `.isspace()` para detectar espacios.
* `.isdigit()` para encontrar números.
* `.isupper()` para validar mayúsculas.
* `.isalnum()` para identificar caracteres especiales.

---

## 💻 Cómo ejecutarlo

1. Asegúrate de tener instalado [Python](https://www.python.org/).
2. Copia el código en un archivo llamado `validador.py`.
3. Ejecútalo desde tu terminal:
   ```bash
   python validador.py
