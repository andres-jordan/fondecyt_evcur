# Scripts para calcular puntaje de la evaluacion curricular del FONDECYT regular 2017

En este repositorio se encuentran dos script para calcular (```formula.py```) y 
optimizar (```opimitzer.py```) el puntaje de la 
evalaución curricular para el concurso FONDECYT regular 2017. ESTOS SCRIPTS NO SON OFICIALES,
USO BAJO SU PROPIO RIESGO Y RESPONSABILIDAD. Los scripts se corre haciendo:

````shell 
python formula.py
python optimize.py
````

Note que debe tener el módulo ```ads``` instalado, y generar un API key en NASA ADS labs. Toda la información
para estos dos pasos se puede encontrar en: https://github.com/andycasey/ads

Los scripts leen archivos llamados ```bibcodes.txt (formula.py)``` y ```bibcodes_opt.txt (optimizer.py)``` con los bibcodes de ADS de los 
papers a considerar. Un bibcode por linea, máximo de 10 para ```forumula.py``` y al menos 10 para ```optimize.py```. Las primeras líneas de un 
archivo ```bibcodes*.txt``` se ven así:

````text
2014Natur.513..526F
2014AJ....148...29J
...
````

Ademas, debe modificar la línea de ```formula.py``` y ```optimizer.py```
que dice

````python
PI_name='Jord' 
````

reemplazando por su apellido (o la fracción inicial de este que sea suficiente para un match único, esto 
es útil para problemas con los acentos como en mi caso).

El script ```optimizer.py``` encuentra el mejor set de 10 papers probando **TODOS** los subconjuntos de tamaño 10 del set de papers en el archivo ```bibcodes_opt.txt```, asi que su tiempo de ejecución escala rapidamente.

