import streamlit as st
import pandas as pd
import tensorflow as tf
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import joblib

# Configuración de página
st.set_page_config(page_title="Spectrum-ML Analyzer", layout="wide")
st.title("🔬 Simulador de Espectrometría con IA")

# Cargar Modelo y Etiquetas
@st.cache_resource
def load_assets():
    model = tf.keras.models.load_model('./models/modelo_espectrometria.h5')
    elementos = joblib.load('./models/etiquetas_elementos.pkl')
    return model, elementos

model, lista_elementos = load_assets()

# --- BARRA LATERAL: Control de Mezcla ---
st.sidebar.header("Configuración de la Muestra")
intensidades = {}
for el in lista_elementos:
    intensidades[el] = st.sidebar.slider(f"Concentración de {el}", 0.0, 1.0, 0.0)

# --- LÓGICA DE SIMULACIÓN ---
x_range = np.linspace(350, 800, 1000)
espectro_final = np.zeros_like(x_range)

# Diccionario interno de líneas (mismo que en el entrenamiento)
db = {
    "Hidrogeno": [656.3, 486.1, 434.0],
    "Helio": [587.6, 667.8, 501.5],
    "Sodio": [589.0, 589.6],
    "Calcio": [422.7, 393.4]
}

for el, int_val in intensidades.items():
    if int_val > 0:
        for linea in db[el]:
            espectro_final += int_val * np.exp(-(x_range - linea)**2 / (2 * 1.5**2))

# Agregar ruido mínimo para realismo
espectro_final += np.random.normal(0, 0.01, 1000)
espectro_norm = np.clip(espectro_final / (espectro_final.max() if espectro_final.max() > 0 else 1), 0, 1)

# --- PREDICCIÓN CON EL MODELO ---
input_vec = espectro_norm.reshape(1, 1000, 1)
prediccion = model.predict(input_vec)[0]

# --- VISUALIZACIÓN ---
col1, col2 = st.columns([2, 1])

with col1:
    fig = go.Figure()

    # 1. Dibujar el espectro base
    fig.add_trace(go.Scatter(
        x=x_range, 
        y=espectro_norm, 
        name="Espectro Analizado", 
        line=dict(color='white', width=2)
    ))

    # 2. Resaltar zonas de elementos detectados (Probabilidad > 0.5)
    colores_zonas = {
        "Hidrogeno": "rgba(255, 0, 0, 0.2)",   # Rojo traslúcido
        "Helio": "rgba(255, 255, 0, 0.2)",     # Amarillo traslúcido
        "Sodio": "rgba(255, 165, 0, 0.2)",     # Naranja traslúcido
        "Calcio": "rgba(0, 255, 255, 0.2)"     # Cian traslúcido
    }

    # Iterar sobre las predicciones
    for i, el in enumerate(lista_elementos):
        prob = prediccion[i]
        
        if prob > 0.5:  # Si la IA está segura del elemento
            lineas_teoricas = db[el]
            
            # Dibujar una franja vertical por cada línea del elemento detectado
            # --- CONFIGURACIÓN DE COLORES ---
            colores_zonas = {
                "Hidrogeno": "rgba(255, 0, 0, 0.2)",
                "Helio": "rgba(255, 255, 0, 0.2)",
                "Sodio": "rgba(255, 165, 0, 0.2)",
                "Calcio": "rgba(0, 0, 255, 0.2)"
            }
            for j, lambda_pico in enumerate(lineas_teoricas):
                fig.add_vrect(
                    x0=lambda_pico - 3, x1=lambda_pico + 3, # Margen de error de 3nm
                    fillcolor=colores_zonas.get(el, "rgba(200, 200, 200, 0.2)"),
                    layer="below", 
                    line_width=0,
                    annotation_text=f"{el}" if j == 0 else "", # Etiqueta solo en el primer pico
                    annotation_position="top left"
                )

    fig.update_layout(
        template="plotly_dark", 
        title="Análisis Espectral con Detección de Patrones IA",
        xaxis_title="Longitud de onda (nm)",
        yaxis_title="Intensidad Normalizada",
        hovermode="x unified"
    )
    
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Análisis de la IA")
    for i, el in enumerate(lista_elementos):
        prob = prediccion[i]
        color = "green" if prob > 0.5 else "grey"
        st.write(f"**{el}**")
        st.progress(float(prob))
        st.caption(f"Confianza: {prob:.2%}")

# --- CORRECCIÓN LÍNEA 121 ---
# Extraemos los nombres y valores directamente de lo que el usuario mueve en los sliders
nombres = list(intensidades.keys())
reales = list(intensidades.values())


# --- 4. EL NUEVO CÓDIGO DE ANÁLISIS CUANTITATIVO ---
st.divider() 
st.subheader("📊 Análisis Cuantitativo de la IA")

# 1. Extraemos los datos de los sliders
nombres_elementos = list(intensidades.keys())
valores_reales = list(intensidades.values())

# 2. Preparamos las columnas
col1, col2 = st.columns([1, 1])

with col1:
    st.write("**Distribución Estimada (Composición)**")
    # CAMBIO CLAVE: Usamos 'prediccion' en lugar de 'preds'
    df_pie = pd.DataFrame({
        "Elemento": nombres_elementos,
        "Concentración": prediccion  # Quitamos el [0] si 'prediccion' ya es una lista simple
    })
    # Definimos colores fijos para que todo el simulador sea coherente
    color_map = {
        "Hidrogeno": "red",
        "Helio": "yellow",
        "Sodio": "orange",
        "Calcio": "blue"
    }

    # Actualizamos la llamada al gráfico
    fig_pie = px.pie(df_pie, values='Concentración', names='Elemento', hole=.3,
                    color='Elemento', color_discrete_map=color_map)
    st.plotly_chart(fig_pie, use_container_width=True)

with col2:
    st.write("**Comparativa: Real vs Predicho**")
    df_comp = pd.DataFrame({
        "Elemento": nombres_elementos,
        "Real": valores_reales,
        "IA": prediccion
    }).set_index("Elemento")

    st.bar_chart(df_comp)

