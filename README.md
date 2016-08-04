# Script para calcular puntaje de la evaluacion curricular del FONDECYT regular 2017

En este repositorio se encuentra un script para calcular el puntaje de la 
evalaución curricular para el concurso FONDECYT regular 2017. ESTE SCRIPT NO ES OFICIAL,
USO BAJO SU PROPIO RIESGO Y RESPONSABILIDAD. El script se corre haciendo:

````shell 
python formula.py
````

Note que debe tener el módulo ```ads``` instalado, y generar un API key en NASA ADS labs. Toda la información
para estos dos pasos se puede encontrar en: https://github.com/andycasey/ads

El script lee un archivo llamado 'bibcodes.txt' con los bibcodes de ADS de los 
papers a considerar. Un bibcode por linea, máximo de 10. Las primeras líneas de un 
archivo 'bibcodes.txt' se ven así:

````text
2014Natur.513..526F
2014AJ....148...29J
...
````

Ademas, debe modificar la línea de 'formula.py'
que dice

````python
PI_name='Jord' 
````

reemplazando por su apellido (o la fracción inicial de este que sea suficiente para un match único, esto 
es útil para problemas con los acentos como en mi caso).

