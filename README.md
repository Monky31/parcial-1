# parcial-1

-----

## Mi Aplicación Tkinter

Esta es una aplicación de demostración construida con la librería `tkinter` de Python, diseñada para explorar y practicar la creación de interfaces gráficas de usuario (GUI). La aplicación presenta un diseño simple con un menú superior, dos marcos principales y varios botones interactivos.

### Funcionalidades principales

  * **Cambio de color de fondo**: Al hacer clic en el botón **"Cambiar color de fondo"**, el color de la ventana principal cambia cíclicamente a través de una paleta de colores predefinida (verde, azul, amarillo, gris).
  * **Cambio de texto dinámico**: El botón **"Cambiar texto"** modifica el texto de una etiqueta dentro del marco derecho de la aplicación.
  * **Mensajes de diálogo**:
      * El botón **"Mostrar mensaje"** abre una pequeña ventana emergente con un mensaje simple.
      * El menú **"Inicio"** incluye una opción de **"Tutorial de la aplicación"** que explica las funciones básicas.
      * La opción **"Salir"** del menú **"Inicio"** muestra un cuadro de confirmación antes de cerrar la aplicación.
  * **Organización de la interfaz**:
      * La ventana está dividida en dos marcos (izquierdo y derecho) que ayudan a organizar los elementos.
      * El marco izquierdo contiene la etiqueta de bienvenida y los botones.
      * El marco derecho contiene una etiqueta de texto que se actualiza dinámicamente.
  * **Información de la aplicación**: El menú **"Ayuda"** y **"Acerca de"** contienen opciones que brindan información sobre las funcionalidades de la aplicación y los detalles del autor.

### Requisitos

Para ejecutar esta aplicación, solo necesitas tener Python instalado en tu sistema. La librería `tkinter` generalmente viene preinstalada con Python, por lo que no es necesario instalar dependencias adicionales.

### Uso

1.  Guarda el código en un archivo llamado `parcial.py`.
2.  Abre una terminal y navega al directorio donde guardaste el archivo.
3.  Ejecuta el siguiente comando:

<!-- end list -->

```bash
python parcial.py
```

### Detalles del autor

  * **Autor**: Mateo Lastra Castillo
  * **Propósito**: Practicar la creación de interfaces gráficas con menús, marcos, botones y etiquetas.

**Nota**: El programa intenta cargar un ícono de la aplicación llamado `app_icon.ico`. Si este archivo no se encuentra en el mismo directorio, la aplicación se ejecutará sin un ícono, pero funcionará sin problemas.
