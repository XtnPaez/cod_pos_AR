# 🇦🇷 Codigos Postales Argentina

![Estado](https://img.shields.io/badge/status-activo-brightgreen)
![Cobertura](https://img.shields.io/badge/cobertura-nacional-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-yellow)

Dataset reproducible de códigos postales de Argentina construido a partir de fuentes reales y procesos automatizados.

---

## 🚀 Qué incluye

✔ Cobertura nacional  
✔ Código postal (CPA)  
✔ Provincia (normalizada)  
✔ Partido / Departamento  
✔ Municipio  
✔ Coordenadas (cuando disponibles)  
✔ Pipeline reproducible  

---

## 📦 Estructura

```
provincias/
  ├── localidades_gen_correo_ar.py
  └── localidades_cp_maestro.csv

caba/
  ├── caba_desde_tabla.py
  ├── tabla_ciudad_bsas.csv
  └── caba_codigos_postales.csv
```

---

## ⚙️ Instalación

```
pip install pandas requests
```

---

## ▶️ Uso

### Provincias
```
cd provincias
python localidades_2026.py
```

### CABA
```
cd caba
python caba_2026.py
```

---

## 🧠 Características técnicas

- Parsing JSON real (no regex)
- Manejo de UTF-8 BOM
- Control de errores del endpoint
- Reintentos automáticos
- Throttling para evitar bloqueos
- Normalización de estructura de datos

---

## 🔍 Fuente e inspiración

Basado en:
https://github.com/androdron/localidades_AR

¡Gracias... totales!

Mejoras:
- Actualización a Python moderno
- Robustez del scraper
- Separación CABA
- Dataset consistente

---

## ⚠️ Disclaimer

Fuente no oficial derivada de servicios de Correo Argentino.  
Puede cambiar sin previo aviso.

---

## 📊 Estado del proyecto

| Componente | Estado |
|----------|--------|
| Provincias | ✅ |
| CABA | ✅ |
| Integración | 🔜 |

---

## 🧩 Próximos pasos

- Integración a Postgres/PostGIS
- API de consulta
- Versionado de datasets
- Validación contra fuentes oficiales

---

## 📌 Autores

Cristian Paez
Daniela Ruíz