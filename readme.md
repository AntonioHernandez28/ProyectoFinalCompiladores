Proyecto Final Compiladores 
A01382469

Avance 1: 
Analizador Léxico y Sintáctico Funcionando. 
Prueba dada en la descripción del proyecto fue ejecutada con éxito. 

Pendiente: 
- Modificar Diágramas para que los arreglos se reconozcan sin duplicar código. 
- Poder manejar expresiones entre paréntesis (). 
- Llamada a Función con múltiples argumentos. 


Avance 2: 
Para este avance se crearon las clases necesarias para el Directorio de Funciones y la Tabla de Variables, además se creó la clase del Cubo Semántico. 
También se solucionaron los pendientes del avance 1. 

Pendiente: 
- Hay algunos errores con respecto a las expresiones. 

Avance 3: 
Para este avance con el fin de comenzar a generar cuádruplos se creó la clase stack y se establecieron los puntos neurálgicos para guardar las funciones en el directorio de funciones. 
Al terminar se probó que las funciones void y principal son reconocidas y guardadas con éxito en el directorio de funciones. También se corrigieron los errores con respecto a las expresiones en el análisis léxico y sintáctico. 

Pendientes: 
- Hay errores con las funciones que no son voids, se tendrá que checar desde el análisis léxico y sintáctico de dónde viene el problema. 
- Una vez solucionado los errores se debe también implementar el guardado de variables para cada función. 

Notas extra: Para este avance se dejaron pendientes importantes debido a que se priorizó estudiar para el parcial que es el próximo lunes pero tan pronto pase el parcial se trabajará en los pendientes y volver al corriente para el avance 4. 

Pendientes: 
- Manejar las variables globales. Además en principal las variables y quads se agregan a la última función declarada y no al principal. 

Avance 4: 
Cuádruplos funcionando y todo pero sólo dan problema cuando va a tomar los arreglos como si fuera una variable. 

# Bugs to fix: 
- Write array at certain index. DONE *?*
- Fix bug in exp that allows compare something with empty :( DONE

Avance 5: 
Cuádruplos de funciones funcionan bien, los gosub, ERA, y el goto a principal funcionan de manera correcta. Los parámetros funcionan de manera correcta y se guardan de manera correcta. Se corrigió el error de cuando marcaba vacío cuando eran más de un parámetro. Se corrigió el bug de ciclo infinito cuando había un error de sintáxis. 

Pendientes: 
Memoria ya está empezado pero como no ha sido probada no fue incluida en este commit. 
- Máquina Virtual 

Bugs to fix: 
- Quad For da un error (while ya funciona perfecto)
