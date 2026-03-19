# 🇦🇷 Codigos Postales Argentina (Correo Argentino + CABA)

Dataset actualizado de códigos postales de la República Argentina
generado a partir de:

-   Extracción directa del endpoint de Correo Argentino
-   Procesamiento específico para CABA mediante dataset auxiliar

------------------------------------------------------------------------

## 📦 Estructura del repositorio

. ├── provincias/ │ ├── localidades_2026.py │ └──
localidades_cp_maestro.csv │ ├── caba/ │ ├── caba_2026.py │ ├──
tabla_ciudad_bsas.csv │ └── caba_codigos_postales.csv │ └── README.md

------------------------------------------------------------------------

## 📍 Provincias

Script: provincias/localidades_2026.py

Fuente: - Endpoint interno de Correo Argentino

Salida: provincias/localidades_cp_maestro.csv

------------------------------------------------------------------------

## 🏙️ CABA

Script: caba/caba_2026.py

Fuente: - tabla_ciudad_bsas.csv

Salida: caba/caba_codigos_postales.csv

------------------------------------------------------------------------

## ⚙️ Requisitos

Python 3.10+

pip install pandas requests

------------------------------------------------------------------------

## ▶️ Ejecución

Provincias: cd provincias python localidades_2026.py

CABA: cd caba python caba_2026.py

------------------------------------------------------------------------

## 🔍 Origen e inspiración

https://github.com/androdron/localidades_AR

Autor original: Andrey Musatov

------------------------------------------------------------------------

## ⚠️ Disclaimer

Fuente no oficial. Validar para usos críticos.
