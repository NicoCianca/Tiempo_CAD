# Tiempo_CAD
Almacena códigos para un estudio experimental del tiempo de ejecución del CAD.

La resolución de sistemas de ecuaciones polinómicas se puede realizar mediante distintos algoritmos. Uno de ellos es el Algoritmo de Descomposición Cilíndrica (CAD en inglés), este nos permite eliminar grupos de variables en las ecuaciones. El tiempo de cómputo de este algoritmo crece muy rápidamente con las variables asociadas por lo que el grueso de los problemas resultan fácticamente intratable. 

Una alternativa a la reducción de todas las variables en el sistema es realizar una reducción parcial tomando solo algunas ecuaciones del sistema y eliminando algunas de sus variables; la fórmula de la reducción se incorpora al sistema. Si iteramos el procedimiento de tomar reducciones parciales, ¿llegaremos a la solución de nuestro sistema? En caso de conocer los tiempos de cómputo con cierta precisión se pueden diseñar estrategias que nos ayuden a tomar caminos más cortos, si es que se llega a la solución requerida.

Si bien los sistemas que nos interesan tienen ecuaciones de grado 4 y grado 2, en las reducciones parciales van a aparecer ecuaciones de otros grados por lo que es preciso tenerlas en cuenta en el universo de ecuaciones al cual se le analizará cómo se comporta el tiempo de cómputo.
