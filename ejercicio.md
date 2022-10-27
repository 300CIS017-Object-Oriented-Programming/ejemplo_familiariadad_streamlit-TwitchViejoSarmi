# Enunciado del proyecto

## Dirección posgrados

# Ejemplo de proyecto

Evaluador de entregas parciales - anteproyecto

Información introductoria disponible en: [Esta presentación](https://docs.google.com/presentation/d/1YZ56m2BQTawpqtSPkPywT94yGARn5N7J/edit?usp=sharing&ouid=112367552149011376006&rtpof=true&sd=true)

Diagramas disponibles en draw.io en este [link](https://drive.google.com/file/d/15jLY0d9PIlFykmX-SicIs_8e5i72VUsF/view?usp=sharing): 
## Configuracion

### Instalación del archivo requirements.txt

* Ejecutar el siguiente comando en consola ubicado en la carpeta raiz del proyecto

> ``pip install -r requirements.txt``

* Espere a que descarguen las dependencias. Esto puede tomar un tiempo. Si encuentra algún error revise la consola,
  busque en internet y corrija
* Corra su programa dando click derecho en el archivo run.py > "Run run.py"
* Si necesita correrlo en debug seleccione el mismo archivo pero corralo en modo debug
  > ``run.py > "Debug run"``

## Actividades

## Familiariaridad con streamlit
1. Ejecute el proyecto. Abra el navegador y verifique que puede navegar entre todas las pestañas
2. Personalice el mensaje que sale en la opción "About"
3. Explorar los controles de streamlit.
    1. Agregue al menos dos controles de tipo "input widgets" en el archivo PruebaPage
    2. Intente organizar el contenido en dos columnas
    3. Pruebe el contenedor expander. Ponga texto dentro de este contenedor
    4. Haga una lista de chequeo.  Defina el código para que según lo que según lo que seleccione se muestre un texto diferent
4. Funcionamiento de controles en la clase `MainView`
    1. En qué parte de ese archivo se dibuja la barra lateral.
    2. Observe el método `controlar_menu` del archivo MainView. ¿Para qué sirve la variable `self.menu_actual`?
    3. Intente agregar una nueva opción a la barra lateral y pruebe que funciona

## Funciones especiales en python
* Investigue para qué sirve el método ``__str__``

