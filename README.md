# Aproximación de Traza

## 1. Descripción general del proyecto

**Aproximación de Traza** es una aplicación interactiva que permite calcular y aproximar la longitud de la traza entre el cilindro \(x^2 + y^2 = a^2\) (con \(a > 0\)) y el plano \(x + y + 2z = 8\) utilizando una Suma de Riemann. El proyecto proporciona una interfaz gráfica amigable para ingresar parámetros y visualizar resultados, facilitando el aprendizaje y la experimentación en cálculo vectorial.

## 2. Tecnologías utilizadas

- **Python**: Lenguaje principal de desarrollo.
- **CustomTkinter**: Framework para interfaces gráficas modernas en Python.
- **Pillow**: Manipulación y visualización de imágenes.
- **Conda**: Gestión de entornos y dependencias.
- **PyInstaller**: Empaquetado y generación de ejecutables standalone.

## 3. Instrucciones de instalación

Sigue estos pasos para preparar el entorno de desarrollo:

1. **Clona el repositorio**  
   ```sh
   git clone <URL_DEL_REPOSITORIO>
   cd Aproximacion_De_Traza
   ```

2. **Configura el entorno con Conda (recomendado)**  
   ```sh
   conda env create --file environment.yml
   conda activate aproximacion_de_traza
   ```

   *O bien, usando pip:*
   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Verifica la instalación**  
   Asegúrate de tener Python 3.x y las dependencias instaladas correctamente.

## 4. Dependencias

Principales dependencias (ver [`requirements.txt`](requirements.txt) y `environment.yml`):

- `customtkinter`
- `Pillow`
- `pyinstaller`

## 5. Ejemplos de uso

Para ejecutar la aplicación principal desde el entorno configurado:

```sh
python src/aproximacion_de_traza.py
```

Esto abrirá la interfaz gráfica donde podrás ingresar los parámetros y calcular la longitud de la traza.

## 6. Estructura del proyecto

```
Aproximacion_De_Traza/
├── Aproximacion_De_Traza.code-workspace
├── README.md
├── environment.yml
├── requirements.txt
├── aproximacion_de_traza.spec
├── assets/
│   └── logo.ico
├── images/
│   ├── area.png
│   └── traza.png
└── src/
    ├── aproximacion_de_traza.py
    └── proyecto_calculo_vectorial.py
```

## 7. Generación de ejecutable

Para crear un ejecutable standalone con PyInstaller:

1. **Asegúrate de tener PyInstaller instalado**  
   (Incluido en el entorno si usaste `environment.yml` o `requirements.txt`).

2. **Ejecuta PyInstaller con el archivo `.spec`**  
   Desde la raíz del proyecto, ejecuta:
   ```sh
   pyinstaller aproximacion_de_traza.spec
   ```

3. **Archivos generados**  
   El ejecutable y sus recursos se encontrarán en la carpeta `dist` (excluida del control de versiones).

**Recomendaciones:**
- Verifica que las rutas de imágenes y recursos sean relativas y estén correctamente incluidas en el archivo `.spec`.
- Si modificas la estructura de carpetas o añades recursos, actualiza el archivo `.spec` en la sección `datas`.