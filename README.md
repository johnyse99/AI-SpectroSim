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



## 💻 Instalación y Uso

1. **Clonar el repositorio:**
   Instalar dependencias: pip install -r requirements.txt
   Ejecutar la app: streamlit run app.py
