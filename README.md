# 🇦🇷 Codigos Postales Argentina

![Estado](https://img.shields.io/badge/status-activo-brightgreen)
![Cobertura](https://img.shields.io/badge/cobertura-nacional-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-yellow)

Dataset reproducible de códigos postales de Argentina construido a partir de fuentes reales y procesos automatizados, con una capa derivada de normalización territorial a nivel departamento.

---

## 🚀 Qué incluye

✔ Cobertura nacional  
✔ Código postal (CPA)  
✔ Provincia (normalizada)  
✔ Partido / Departamento  
✔ Municipio  
✔ Coordenadas (cuando disponibles)  
✔ Tabla derivada con codificación territorial normalizada a nivel departamento  
✔ Pipeline reproducible  

---

## 📦 Estructura

    provincias/
      ├── localidades_gen_correo_ar.py
      └── localidades_cp_maestro.csv

    caba/
      ├── caba_desde_tabla.py
      ├── tabla_ciudad_bsas.csv
      └── caba_codigos_postales.csv

    normalizados/
      ├── cp_provincias_departamentos_normalizados.csv
      └── cp_provincias_departamentos_normalizados.md

---

## 🆕 Novedad

Se incorpora una tabla derivada y validada que relaciona los códigos postales del listado base con una codificación territorial normalizada usando referencias del **IGN**.

Este nuevo archivo permite trabajar directamente a nivel **provincia** y **departamento/partido**, lo que mejora el uso del código postal como clave auxiliar para:

- geolocalización aproximada;
- asignación territorial de registros;
- joins con capas geográficas oficiales;
- validación de datos cargados por usuarios.

---

## ⚙️ Instalación

    pip install pandas requests

---

## ▶️ Uso

### Provincias

    cd provincias
    python localidades_2026.py

### CABA

    cd caba
    python caba_2026.py

### Tabla normalizada

El archivo `cp_provincias_departamentos_normalizados.csv` es un producto derivado listo para análisis, joins o carga en Postgres/PostGIS.

Su metadata descriptiva se documenta en `cp_provincias_departamentos_normalizados.md`.

---

## 🧠 Características técnicas

- Parsing JSON real (no regex)
- Manejo de UTF-8 BOM
- Control de errores del endpoint
- Reintentos automáticos
- Throttling para evitar bloqueos
- Normalización de estructura de datos
- Integración territorial posterior con codificación a nivel departamento

---

## 🔍 Fuente e inspiración

Basado en:
https://github.com/androdron/localidades_AR

Mejoras incorporadas en este repositorio:

- actualización a Python moderno;
- robustez del scraper;
- separación CABA;
- dataset nacional consistente;
- capa derivada con normalización provincia/departamento.

---

## ⚠️ Disclaimer

Fuente no oficial derivada de servicios de Correo Argentino.  
Puede cambiar sin previo aviso.

La tabla territorial normalizada es un **derivado validado** construido a partir de cruces con insumos geográficos oficiales y controles posteriores.

---

## 📊 Estado del proyecto

| Componente | Estado |
|----------|--------|
| Provincias | ✅ |
| CABA | ✅ |
| Normalización provincia/departamento | ✅ |
| Integración Postgres/PostGIS | 🔜 |

---

## 🧩 Próximos pasos

- Integración a Postgres/PostGIS
- Documentar pipeline de normalización territorial en caso de reconstruir queries/scripts intermedios

---

## 📌 Autores

Cristian Páez

Daniela Ruíz
