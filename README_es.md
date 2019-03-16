# Repositorio de diseño (artwork)
Este es el repositorio que utiliza el [equipo de diseño de openSUSE](https://en.opensuse.org/openSUSE:Artwork_team).
Aunque el uso de un sistema de control de versiones como git puede ser un poco intimidatorio a la hora de utilizarlo, sobre todo por las personas menos técnicas, este pequeño manual quiere solucionar eso.

Git es de lejos la mejor opción para crear de manera colaborativa. Además la plataforma de GitHub es relativamente sencilla de utilizar.


## Licencia
Todo el contenido está publicaco bajo la licencia [CC-BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) a menos que se indique lo contrario

## Cómo contribuir
### Ajustes iniciales
Si desea modificar o añadir material de nuestro repositorio, necesitará primero seguir algunos pasos iniciales:

 1. Registrarse con una cuenta de GitHub, si todavía no dispone de una
 2. Instalar git en su equipo si todavía no lo tiene instalado (Bien sea usando YaST en openSUSE o mediante la línea de comandos como root o utilizando sudo escriba el comando: zypper install git)
 3. Ver en la ayuda de GitHub cómo configurar su cuenta y cómo subir su clave SSH
 4. Pida mediante un correo electrónico a admin@opensuse.org que se añada su cuenta de usuario al equipo "artwork" en GitHub, lo que le dará permisos de escritura en el repositorio.
 5. Ejecute los siguientes comandos en la línea de comandos como un usuario normal:
     1. git config --global user.email "mi_correo@dirección.com" (obviamente con su dirección de cuenta de correo ;))
     2. git config --global user.name "John Doe" (de nuevo reemplazando el ejemplo con su nombre real)
 6. Escoja alguna carpeta donde quiera que se guarden sus archivos. Por ejemplo: ~/Documentos y vaya a ella en la línea de comandos mediante el comando cd ~/Documentos
 7. Descargue el repositorio en su equipo clonando el repositorio almacenado en GitHub, mediante el siguiente comando: git clone git@github.com:openSUSE/artwork.git 
 8. Espere a que finalice la operación. Finalmente obtendrá una carpeta llamada "artwork" dentro de la carpeta ~/Documentos que será una copia exacta del contenido del repositorio de GitHub

### Flujo de trabajo
#### Descargando los cambios más recientes (pull)
Para poder obtener los cambios más recientes ejecute el siguiente comando:

```shell
git pull
```

Eso descargará las últimas novedades de todo lo que está en el repositorio de GitHub y lo almacenará en su disco.

Por supuesto, el comando necesita ser ejecutado estando en su carpeta "arwork" local de su equipo (Por ejemplo: ~/Documentos/artwork)

#### Añadir nuevos archivos o carpetas
Cuando crea un nuevo archivo o carpeta, debe decirle a git que le gustaría añadirlo al repositorio, utilizando el siguiente comando:

```shell
git add nombre_archivo
```

(Reemplanzado el nombre_archivo del ejemplo por el nombre del archivo o carpeta que quiere añadir).

Tenga en cuenta que añadir un archivo no hace que se suba directamente al repositorio, simplemente le hemos dicho a git que queremos poner el archivo en cuestión bajo el control de versiones para que lo tenga en cuenta.

#### Realizando los cambios (commit)
Cuando cambia un archivo y quiere guardar el estado en el que se encuentra en el repositorio (por ejemplo si piensa que es bastante bueno para que pueda ser utilizado por otras personas), debe utilizar el siguiente comando:

```shell
git commit -m "algún comentario descriptivo sobre el cambio que he realizado" nombre_archivo
```

Por favor utilice comentarios descriptivos, esto ayudará a cualquier persona el poder hacer un seguimiento de los cambios que se han realizado.
También asegúrese de poner los comentarios entre comillas ("") o la línea de comandos los interpretará como varios comandos de git, lo que no es cierto, y le dará errores.

También puede hacer "commit" de varios archivos al mismo tiempo, lo que es más correcto cuando los cambios afectan a muchos archivos
(por ejemplo si cambió la paleta de colores de varios archivos de Inkscape). De esa manera, sus cambios se mostrarán como una única acción en el historial de cambios del repositorio.

Para hace eso, simplemente pase varios nombres de archivos al comando de git commit, como en este ejemplo:

```shell
git commit -m "cambiada la paleta de colores de rojo" archivo1 archivo2 archivo3
```

También puede hacer un "commit" de todos los cambios, de todos los archivos, de su copia local de su repositorio utilizando el parámetro -a (all), como en este ejemplo:

```shell
git commit -m "cambiado el texto en todos los fondos de escritorio" -a
```

#### Enviando los cambios (push)

Cuando ha hecho un "commit" de los cambios como hemos visto anteriormente, git solo almacena estos en su repositorio local en su disco duro,
y no en el repositorio de GitHub, lo que significa que nadie más que usted podrá ver sus cambios.

git funciona de esa manera porque quizás decidió hacer los cambios de manera local, y hacer un seguimiento de esos cambios en su disco duro para poder revertirlos a versiones anteriores, sin necesidad de enviar, por el momento, esos cambios a otra gente con la que trabaje.

Una vez que quiera enviar esos cambios a todas las personas, deberá ejecutar el comando "push" para enviarlos al repositorio de GitHub, con el siguiente comando:

```shell
git push
```

Tenga en cuenta que la primera vez que ejecute git push, tendrá que utilizar el siguiente comando: __git push origin master__

En sucesivas ocasiones simplemente tendrá que ejecutar __git push__

Además, cuando este ejecutando ese comando, es posible que alguien más este realizando la misma acción con otros archivos.
Git le indicará que revise lo que está pasando y deberá hacer un git pull antes que git push

#### Estado (status)
Mediante el comando git status, puede comprobar si tiene archivos en su disco duro que tienen cambios (o si hay nuevos archivos o archivos eliminados) que todavía no han sido realizados.

```shell
git status
```

Puede dar una respuesta similar a esta:

```shell
# On branch master
# Changed but not updated:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#       modified:   git-mini-howto.txt
#
no changes added to commit (use "git add" and/or "git commit -a")
```

Este mensaje significa que el archivo git-mini-howto.txt está modificado de manera local:
Ha realizado cambios en ese archivo, pero esos cambios (todavía) no se han enviado.

#### Eliminando archivos
Si quiere eliminar archivos del repositorio, utilice el comando git rm
en vez de eliminarlo como normalmente haría con el gestor de archivos que utilice o únicamente mediante el comando rm:

```shell
git rm filename
```

Eliminar un archivo es considerado como un cambio más para git, por tanto después deberá realizarlo mediante "commit" siguiendo alguno de los ejemplos que hemos visto antes y después enviarlo al repositorio de GitHub, para que este disponible para todos:

```shell
git commit -a "eliminando archvos obsoletos" -m
git push
```

#### Renombrar o mover archivos o carpetas
Cuando quiera renombrar un archivo o carpeta o moverla a otro lugar, no utilice el comando normal que utilizaría (mv) o el navegador de archivos para hacerlo.
Si lo hace así, git considerará que el archivo renombrado o movido es un archivo o carpeta nuevo y perderá todo el historial de cambios del archivo.

La manera adecuada de hacerlo es utilizando git mv, como en este ejemplo:

```shell
git mv archivo_viejo archivo_nuevo
```

Después deberá hacer un "commit" y un "push" para subir esos cambios al repositorio de GitHub.

#### Historial
Una de las ventajas más obvias de un sistema de control de versiones como git
es la posibilidad de ver el historial de un archivo, que no es más que un registro de las modificaciones que se han realizado en ese archivo,
con los mensajes de "commit", cuando se hicieron esos cambios y quién los hizo.

Para ver el historial de un archivo, puede hacerlo mediante este comando:

```shell
git log nombre_archivo
```

Esto mostrará algo similar a:

```shell
commit bbcf4e3a848d65fc28d1fb6d20d0ce7add040a33
Author: Pascal Bleser <pascal.bleser@opensuse.org>
Date:   Tue Feb 15 23:46:11 2011 +0100

    add LICENSE
```

Sólo existe un cambio en el archivo del ejemplo, pero en él se muestra:

* Quién hizo el cambio: Pascal Bleser
* Cuando se hizo el cambio: Tue Feb 15
* Qué fue lo que se cambió (el mensaje del "commit"): "add LICENSE"

También puede ver todos los cambios realizados en todos el repositorio y no únicamente en un solo archivo, utilizando este comando:

```shell
git log
```

(sin especificar ningún nombre de archivo)

Por favor, tenga en cuenta que el comando git log muestra los mensajes automáticamente utilizando un paginado
(normalmente es /usr/bin/less), lo que le ofrece la posibilidad de poder navegar por el texto
utilizando las teclas de las flechas de cursor, avance/retroceso página...
Para salir de ese paginador simplemente pulse la tecla "q" (sin las comillas).

git log tiene muchas más opciones, le invitamos a leer sobre ellas con la ayuda, escribiendo este comando: git log --help 

### Pendiente

* Documentar cómo regresar a una revisión previa de un archivo (git checkout)
* Mencionar la disponibilidad de usar interfaces gráficas para el uso de git (gitk, qgit, ...)
* Enlazar al otros tutoriales

