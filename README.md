# AI-SpectroSim
Simulador de Espectrometría con Deep Learning

# 🔬 AI-SpectroSim: Simulador de Espectrometría con Deep Learning

¡Bienvenido a **AI-SpectroSim**! Este proyecto utiliza Redes Neuronales Convencionales (CNN) para identificar y cuantificar la composición química de muestras gaseosas a partir de su firma espectral. 

Es una herramienta diseñada para cerrar la brecha entre la **Física Atómica** y la **Inteligencia Artificial Aplicada**.



## 🚀 Descripción del Proyecto
El simulador permite a los usuarios mezclar concentraciones de **Hidrógeno, Helio, Sodio y Calcio**. La IA analiza el espectro resultante (que incluye ruido de laboratorio simulado) para:
1.  **Detectar** la presencia de elementos (Clasificación).
2.  **Cuantificar** el porcentaje exacto de cada uno (Regresión).

## 🛠️ Estructura Modular del Proyecto
Siguiendo las mejores prácticas de ML Ops, el proyecto se divide en tres fases críticas:

* **Fase Descriptiva:** Generación de espectros teóricos basados en las líneas de emisión de Bohr y adición de ruido estocástico.
* **Fase Predictiva:** Arquitectura CNN entrenada para regresión de concentraciones mediante pérdida MSE (Mean Squared Error).
* **Fase Prescriptiva:** Interfaz interactiva en **Streamlit** que permite realizar experimentos en tiempo real.

## 📊 Visualización de Resultados
El proyecto incluye un panel de control avanzado que compara en tiempo real la **Muestra Real** vs. la **Estimación de la IA**:

* **Gráfico Espectral:** Visualización de picos e identificación de zonas por elemento.
* **Distribución de Composición:** Gráfico de tarta dinámico que desglosa la mezcla detectada.
* **Comparativa Real vs. IA:** Gráfico de barras para validar la precisión del modelo.

📚 Tecnologías Utilizadas
    - Python 3.x
    - TensorFlow/Keras: Redes neuronales para regresión.
    - Streamlit: Framework para la interfaz científica.
    - Pandas & Numpy: Manipulación de datos espectrales.
    - Plotly: Gráficos interactivos y dinámicos.

## 💻 Instalación y Uso

1. **Clonar el repositorio:**
2. **Instalar dependencias: pip install -r requirements.txt**
3. **Ejecutar la app: streamlit run app.py**

## ❓ Preguntas de Entrevista (FAQ)
Diseñadas para demostrar el dominio técnico del proyecto:
1. ¿Por qué utilizaste una pérdida MSE en lugar de Cross-Entropy?
Respuesta: Dado que el objetivo es la regresión (predecir concentraciones continuas del 0 al 1) y no solo clasificar, el error cuadrático medio permite a la IA aprender la distancia numérica exacta entre la realidad y la predicción.

2. ¿Cómo manejas el ruido en los datos de laboratorio?
Respuesta: Durante la fase descriptiva, se aplica un ruido normal (np.random.normal) para asegurar que el modelo sea robusto y no se sobreajuste a firmas espectrales perfectas, simulando condiciones reales de sensores.

3. ¿Por qué este proyecto es compatible con Streamlit desde su origen?
Respuesta: El proyecto sigue una arquitectura modular donde los scripts se reescriben completamente para mantener la consistencia, permitiendo que la interfaz web acceda directamente a las funciones de predicción sin dependencias externas complejas.

## 📄 Licencia
Este proyecto se distribuye bajo la licencia MIT. Su propósito es estrictamente educativo y de investigación, desarrollado como una solución de Data Science Aplicada para el sector público y financiero.
Nota para reclutadores: Este proyecto demuestra mi capacidad para transformar teorías físicas complejas en herramientas digitales funcionales. Mi enfoque no es solo "hacer que el código corra", sino mantener una estructura modular, reproducible y documentada que sea lista para entornos de producción.
   
