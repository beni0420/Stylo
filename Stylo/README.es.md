<div>
  <strong>🇪🇸 Español</strong> | <a href="README.md">🇬🇧 English</a>
</div>


# Stylo – Analizador Lingüístico y Estilométrico Multilingüe impulsado por IA

**Stylo** es una aplicación web inteligente y adaptable diseñada para el análisis estilométrico y lingüístico en tiempo real. Construida con **Flask**, **spaCy** y **Chart.js**, aprovecha pipelines avanzados de Procesamiento de Lenguaje Natural (PLN/NLP) para evaluar métricas de texto, diversidad léxica, estructura sintáctica y verificación automatizada de idiomas en múltiples idiomas (**Español, Inglés, Francés e Italiano**).

---

## Características Principales

* **Integración de Pipelines de IA y NLP**: Impulsado por la tokenización de `spaCy`, etiquetado gramatical (POS tagging) y detección de límites de oraciones para diseccionar la semántica y la sintaxis del texto.
* **Filtros Automatizados de Idioma**: Utiliza `langdetect` para verificar que el texto introducido coincida con el idioma seleccionado, evitando discrepancias multilingües antes de ejecutar los análisis.
* **Validación Inteligente de Contenido**: Aplica un riguroso pipeline de validación (umbrales mínimos de palabras y comprobación de verbos) para asegurar que solo se analicen estructuras oracionales válidas.
* **Métricas Estilométricas Avanzadas**:
  * Recuento total de palabras y cálculo de vocabulario único.
  * Estimación de riqueza léxica (variante de la ratio Type-Token).
  * Análisis de la longitud media de las oraciones.
  * Extracción de las palabras significativas más frecuentes (utilizando `collections.Counter` para filtrar palabras vacías/stopwords y puntuación).
* **Visualización Dinámica de Datos**: Gráficos interactivos impulsados por **Chart.js** renderizados de forma condicional según los criterios de validación.
* **Interfaz UI (Bento Grid / Glassmorphism)**: Estética moderna de panel asimétrico construida con variables CSS personalizadas, diseño adaptativo (responsive) y diccionarios completos de localización multilingüe (`translations.py`).

---

## Tecnologías Utilizadas (Tech Stack)

* **Backend**: Python, Flask, Flask Sessions
* **Motor de NLP**: spaCy (`es_core_news_sm`, `en_core_web_sm`, `fr_core_news_sm`, `it_core_news_sm`), langdetect
* **Frontend**: HTML5, CSS3 Moderno (Glassmorphism y diseños Bento), Chart.js
* **Arquitectura**: Diccionarios de traducción modulares y pipelines de manejo de errores basados en sesiones.

---

## Instalación y Ejecución Local

1. **Clona el repositorio**:
   ```bash
   git clone [https://github.com/tu-usuario/stylo.git](https://github.com/tu-usuario/stylo.git)
   cd stylo

2. **Crea y activa un entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate

3. **Instala las dependencias**:
   ```bash
   pip install flask spacy langdetect

4. **Descarga los modelos de idioma de spaCy**:
   ```bash
   python -m spacy download en_core_web_sm
   python -m spacy download es_core_news_sm
   python -m spacy download fr_core_news_sm
   python -m spacy download it_core_news_sm

5. **Ejecuta la aplicación**:
   ```bash
   python app.py


Abre tu navegador y entra en http://127.0.0.1:5000/.