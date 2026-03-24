# cp_provincias_departamentos_normalizados.csv

## Descripción

Tabla derivada de integración y normalización de códigos postales de Argentina a nivel **provincia** y **departamento/partido**.

Este archivo consolida el listado original obtenido desde Correo Argentino con una etapa posterior de control y codificación territorial utilizando capas oficiales del **IGN** y una capa de apoyo de **códigos postales/localidades**.

El objetivo del dataset es disponer de una correspondencia confiable entre:

- código postal
- provincia de origen Correo
- partido/departamento de origen Correo
- localidad de origen Correo
- códigos territoriales normalizados
- provincia y departamento normalizados según referencia IGN

---

## Nivel de agregación

**Unidad de registro:** combinación observada de localidad/código postal del origen Correo con su asignación territorial normalizada a nivel departamento.

---

## Cobertura

- **Ámbito:** República Argentina
- **Cobertura geográfica:** nacional
- **Desagregación normalizada:** provincia y departamento/partido

---

## Origen de los datos

### Insumos principales

1. **Listado base de localidades y códigos postales** obtenido a partir de servicios consultables de Correo Argentino.
2. **Capas oficiales del IGN** para codificación territorial.
3. **Capa/listado auxiliar de códigos postales y localidades** utilizada para contraste y validación espacial/nominal.

---

## Proceso de construcción

El archivo fue construido a partir de una etapa posterior al scraping inicial.

De forma resumida, el procedimiento fue:

1. generación del listado base de localidades y códigos postales;
2. cruce del listado con insumos geográficos oficiales;
3. revisión y validación de correspondencias;
4. asignación de códigos normalizados de provincia y departamento;
5. consolidación final en una tabla plana lista para análisis, joins o carga a base de datos.

---

## Validación

El usuario indica que la tabla final fue **revisada y chequeada** antes de su publicación.

No se conserva en este repositorio la traza completa de queries o scripts intermedios utilizados en la etapa de integración territorial. Por lo tanto, este archivo debe considerarse un **derivado validado** a partir del pipeline general del proyecto, aunque no completamente reproducible desde el repositorio actual en su estado presente.

Dicho sin maquillaje: la tabla está validada, pero el backstage SQL se fue de gira.

---

## Estructura de campos

| Campo | Tipo sugerido | Descripción |
|---|---|---|
| `codprov_correo` | entero/cadena | Código de provincia según origen Correo |
| `provincia_correo` | texto | Nombre de provincia según origen Correo |
| `partido_correo` | texto | Partido/departamento informado o derivado del origen Correo |
| `localidad_correo` | texto | Localidad del registro original |
| `cp_correo` | entero/cadena | Código postal asociado al registro |
| `codprov_ign` | entero/cadena | Código de provincia normalizado según referencia IGN |
| `provincia_ign` | texto | Nombre de provincia normalizado según referencia IGN |
| `coddepto_ign` | entero/cadena | Código de departamento/partido normalizado según referencia IGN |
| `departamento_ign` | texto | Nombre de departamento/partido normalizado según referencia IGN |

---

## Usos recomendados

Este archivo puede utilizarse para:

- asignación territorial por código postal;
- normalización de bases de personas, establecimientos o eventos;
- joins con tablas estadísticas y capas geográficas;
- validación de provincia/departamento cuando el dato más confiable disponible es el código postal.

---

## Limitaciones

- La fuente original de códigos postales es **no oficial** en términos de publicación tabular reutilizable, ya que deriva de servicios de consulta de Correo Argentino.
- La correspondencia final provincia/departamento surge de un proceso de integración posterior validado manual y/o analíticamente.
- No reemplaza nomencladores oficiales permanentes ni cartografía oficial de referencia para usos normativos.

---

## Estado

**Estado:** validado y listo para uso

---

## Autoría y mantenimiento

Proyecto mantenido por el equipo del repositorio.

