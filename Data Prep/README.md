# Data Prep

###  Especificación de archivos:

 - base steps.xlsx : Archivo de Excel que describe la metodología de filtrado de datos paso por paso. Incluye la base final completa.
 - base.csv : Base de datos original, convertida a formato CSV.
 - base.sav : Base de datos original en formato SPSS.
 - baseGenZ.csv : Base de datos filtrada (solo incluye filas que tienen datos exclusivamente en las dos columnas en el rango edad de Gen Z).
 - baseGenZ.xlsx : Idem, pero en archivo de Excel (y quitando las columnas de edad que ya no son necesarias).
 - data.py : Código en Python que realiza el mismo filtrado de datos realizado en Excel, utilizando la librería "pandas".