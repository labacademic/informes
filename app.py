import streamlit as st
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="Asistente de Cursos", page_icon="🧑‍🏫")

st.title("🎓 Asistente de Cursos Online")

# Tarifarios
preventa_forecasting = datetime(2025, 6, 15)
preventa_econometria = datetime(2025, 6, 29)

# Nuevas fechas de pre-venta
preventa_series_python = datetime(2025, 6, 22)
preventa_ml_forecasting = datetime(2025, 7, 20)
preventa_fundamentos_econometria = datetime(2025, 7, 6)
preventa_modelos_estadisticos_r = datetime(2025, 8, 3)

# Paso 1: Selección inicial con opción preseleccionada
opcion = st.radio("¿Qué te interesa conocer hoy?", ["📆 Cursos mensuales", "📚 Programas de 2 meses"], index=1)

# Cursos y programas
cursos = {
    "Forecasting con Python (julio)": {
        "duracion": "42 horas académicas",
        "inicio": "2 de julio",
        "fin": "22 de agosto",
        "descripcion": "📊 **Técnicas de Forecasting con Python**\n\nAprende a identificar los componentes clave de las series temporales, como la tendencia, estacionalidad y ciclos, para aplicar métodos clásicos como Holt-Winters y Prophet. Además, se desarrollan habilidades para evaluar la precisión de los modelos utilizando métricas de error, mejorando la confiabilidad de los pronósticos. En una segunda fase, se exploran modelos avanzados de machine learning como Random Forest, KNN, XGBoost y N-BEATS, optimizando su rendimiento mediante una adecuada selección de variables y manejo de datos.",
        "precio": {
            "normal": {"soles": 300, "dolares": 90},
            "preventa": {"soles": 200, "dolares": 60},
            "corporativo": {"soles": 160, "dolares": 50},
            "fecha_preventa": preventa_forecasting
        },
        "inscripcion": "https://wa.me/51926488484?text=%F0%9F%8E%89%20%21Hola%21%20Estoy%20interesado%20en%20inscribirme%20en%20el%20curso%20Forecasting%20con%20Python%20%28julio%29.%20%3FMe%20puedes%20dar%20más%20información%3F%20%F0%9F%93%9D",
        "informes": "https://wa.me/51926488484?text=%F0%9F%93%9A%20%21Hola%21%20Quisiera%20consultar%20información%20sobre%20los%20informes%20y%20descuentos%20para%20el%20curso%20Forecasting%20con%20Python%20%28julio%29.%20Gracias.%20%F0%9F%99%8C"
    },
    "Econometría aplicada con R (julio)": {
        "duracion": "42 horas académicas",
        "inicio": "17 de julio",
        "fin": "9 de septiembre",
        "descripcion": "📘 **Programa de Econometría Aplicada con R**\n\nEste programa aborda los principios fundamentales de la econometría mediante dos módulos. El primero cubre estadística inferencial y regresión lineal, aplicando estos conceptos con datos reales, como los microdatos de la ENAHO. El segundo módulo profundiza en técnicas avanzadas de modelado, como la regresión lineal múltiple, modelos lineales generalizados y modelos de elección discreta. Además, se exploran herramientas estadísticas y de machine learning para resolver problemas reales del mercado laboral y otras áreas.",
        "precio": {
            "normal": {"soles": 300, "dolares": 90},
            "preventa": {"soles": 200, "dolares": 60},
            "corporativo": {"soles": 160, "dolares": 50},
            "fecha_preventa": preventa_econometria
        },
        "inscripcion": "https://wa.me/51960553600?text=%F0%9F%8E%89%20%21Hola%21%20Estoy%20interesado%20en%20inscribirme%20en%20el%20curso%20Econometría%20aplicada%20con%20R%20%28julio%29.%20%3FMe%20puedes%20dar%20más%20información%3F%20%F0%9F%93%9D",
        "informes": "https://wa.me/51960553600?text=%F0%9F%93%9A%20%21Hola%21%20Quisiera%20consultar%20información%20sobre%20los%20informes%20y%20descuentos%20para%20Econometría%20aplicada%20con%20R%20%28julio%29.%20Gracias.%20%F0%9F%99%8C"
    },
    "Análisis y modelamiento de series de tiempo con Python": {
        "duracion": "21 horas académicas",
        "inicio": "2 de julio",
        "fin": "25 de julio",
        "descripcion": "📊 **Análisis y Modelamiento de Series Temporales con Python**\n\nDesarrolla la capacidad para identificar los principales componentes de las series temporales, como tendencias, estacionalidad y ciclos. Aplica algoritmos clásicos como Holt-Winters y Prophet para crear pronósticos, y utiliza métricas como RMSE, MAE y MAPE para evaluar la precisión de los modelos. Aprende a modelar la estacionalidad y los ciclos y ajusta los errores de predicción de manera efectiva.",
        "precio": {
            "normal": {"soles": 160, "dolares": 50},
            "preventa": {"soles": 120, "dolares": 38},
            "corporativo": {"soles": 100, "dolares": 30},
            "fecha_preventa": preventa_series_python
        },
        "inscripcion": "https://wa.me/51926488484?text=%F0%9F%8E%89%20%21Hola%21%20Estoy%20interesado%20en%20inscribirme%20en%20el%20curso%20Análisis%20y%20modelamiento%20de%20series%20de%20tiempo%20con%20Python.%20%3FMe%20puedes%20dar%20más%20información%3F%20%F0%9F%93%9D",
        "informes": "https://wa.me/51926488484?text=%F0%9F%93%9A%20%21Hola%21%20Quisiera%20consultar%20información%20sobre%20los%20informes%20y%20descuentos%20para%20Análisis%20y%20modelamiento%20de%20series%20de%20tiempo%20con%20Python.%20Gracias.%20%F0%9F%99%8C"
    },
    "Modelos de machine learning para forecasting con Python": {
        "duracion": "21 horas académicas",
        "inicio": "30 de julio",
        "fin": "22 de agosto",
        "descripcion": "💻 **Modelos de Machine Learning para Forecasting con Python**\n\nDomina las técnicas avanzadas de machine learning para la predicción de series temporales. Explora el uso de Random Forest, KNN, XGBoost y N-BEATS, optimizando su desempeño mediante una correcta selección de variables y la preparación adecuada de los datos. El curso te permite desarrollar soluciones robustas y escalables para pronósticos más precisos en escenarios reales.",
        "precio": {
            "normal": {"soles": 160, "dolares": 50},
            "preventa": {"soles": 120, "dolares": 38},
            "corporativo": {"soles": 100, "dolares": 30},
            "fecha_preventa": preventa_ml_forecasting
        },
        "inscripcion": "https://wa.me/51926488484?text=%F0%9F%8E%89%20%21Hola%21%20Estoy%20interesado%20en%20inscribirme%20en%20el%20curso%20Modelos%20de%20Machine%20Learning%20para%20Forecasting%20con%20Python.%20%3FMe%20puedes%20dar%20más%20información%3F%20%F0%9F%93%9D",
        "informes": "https://wa.me/51926488484?text=%F0%9F%93%9A%20%21Hola%21%20Quisiera%20consultar%20información%20sobre%20los%20informes%20y%20descuentos%20para%20Modelos%20de%20Machine%20Learning%20para%20Forecasting%20con%20Python.%20Gracias.%20%F0%9F%99%8C"
    },
    "Fundamentos de econometría con R": {
        "duracion": "21 horas académicas",
        "inicio": "17 de julio",
        "fin": "12 de agosto",
        "descripcion": "🔹 **Fundamentos de Econometría con R**\n\nEste módulo cubre las bases de la estadística inferencial, abordando pruebas de hipótesis, análisis de varianza (ANOVA) y la regresión lineal. Se aprende a usar técnicas como variables dummy, efectos diferenciales y regresión polinómica para analizar datos económicos. Además, se desarrollan habilidades para realizar estimaciones y realizar interpretaciones de parámetros y pruebas de hipótesis con datos reales, como los de la ENAHO.",
        "precio": {
            "normal": {"soles": 160, "dolares": 50},
            "preventa": {"soles": 120, "dolares": 38},
            "corporativo": {"soles": 100, "dolares": 30},
            "fecha_preventa": preventa_fundamentos_econometria
        },
        "inscripcion": "https://wa.me/51960553600?text=%F0%9F%8E%89%20%21Hola%21%20Estoy%20interesado%20en%20inscribirme%20en%20el%20curso%20Fundamentos%20de%20Econometría%20con%20R.%20%3FMe%20puedes%20dar%20más%20información%3F%20%F0%9F%93%9D",
        "informes": "https://wa.me/51960553600?text=%F0%9F%93%9A%20%21Hola%21%20Quisiera%20consultar%20información%20sobre%20los%20informes%20y%20descuentos%20para%20Fundamentos%20de%20Econometría%20con%20R.%20Gracias.%20%F0%9F%99%8C"
    },
    "Modelos estadísticos con R": {
        "duracion": "21 horas académicas",
        "inicio": "14 de agosto",
        "fin": "9 de septiembre",
        "descripcion": "🔹 **Modelos Estadísticos con R**\n\nEn este módulo se trabaja con la regresión lineal múltiple, modelado con distribuciones de Poisson y Gamma, y modelos de elección discreta como Logit binario y multinomial. También se analizan modelos aditivos como GAM y Loess para predecir patrones no lineales, con un enfoque práctico para la solución de problemas estadísticos complejos.",
        "precio": {
            "normal": {"soles": 160, "dolares": 50},
            "preventa": {"soles": 120, "dolares": 38},
            "corporativo": {"soles": 100, "dolares": 30},
            "fecha_preventa": preventa_modelos_estadisticos_r
        },
        "inscripcion": "https://wa.me/51960553600?text=%F0%9F%8E%89%20%21Hola%21%20Estoy%20interesado%20en%20inscribirme%20en%20el%20curso%20Modelos%20Estadísticos%20con%20R.%20%3FMe%20puedes%20dar%20más%20información%3F%20%F0%9F%93%9D",
        "informes": "https://wa.me/51960553600?text=%F0%9F%93%9A%20%21Hola%21%20Quisiera%20consultar%20información%20sobre%20los%20informes%20y%20descuentos%20para%20Modelos%20Estadísticos%20con%20R.%20Gracias.%20%F0%9F%99%8C"
    }
}

# Enlace único para organizaciones estudiantiles
enlace_organizaciones_estudiantiles = "https://wa.me/51951851874?text=%F0%9F%8E%93%20%21Hola%21%20Estoy%20interesado%20en%20descuentos%20para%20organizaciones%20estudiantiles.%20%3FMe%20puedes%20dar%20más%20información%3F%20%F0%9F%A4%9D"

# Función para mostrar los enlaces
def mostrar_links(curso_sel):
    curso_data = cursos[curso_sel]
    
    # Enlace personalizado para inscripción e informes según el curso
    enlace_inscripcion = curso_data['inscripcion']
    enlace_informes = curso_data['informes']
    
    st.markdown(f"""
    - ¿Quieres inscribirte? [Haz clic aquí]({enlace_inscripcion})  
    - ¿Quieres consultar nuestra política de descuento para ex alumnos, matrículas nacionales, internacionales, matriculas en bloques o beneficios para estudiantes? [Haz clic aquí]({enlace_informes})  
    - ¿Quieres conseguir descuentos para tu organización estudiantiles? [Haz clic aquí]({enlace_organizaciones_estudiantiles})
    """)

# Paso 2: Mostrar según selección
def mostrar_tabla_precio(precios):
    data = {
        "Tarifario": ["Normal", "Pre-venta", "Corporativo (3 o más)"],
        "Soles": [f"S/.{precios['normal']['soles']}", 
                  f"S/.{precios['preventa']['soles']}" if precios['preventa'] else f"S/.{precios['normal']['soles']}",
                  f"S/.{precios['corporativo']['soles']}"],
        "Dólares": [f"${precios['normal']['dolares']}",
                    f"${precios['preventa']['dolares']}" if precios['preventa'] else f"${precios['normal']['dolares']}",
                    f"${precios['corporativo']['dolares']}"]
    }
    
    df = pd.DataFrame(data)
    st.dataframe(df)

    # Mostrar mensaje de pre-venta
    hoy = datetime.now()
    if precios['preventa'] and hoy <= precios['fecha_preventa']:
        st.markdown(f"**¡Aprovecha la pre-venta hasta {precios['fecha_preventa'].strftime('%d de %B')}!**")
    elif not precios['preventa']:
        st.markdown("**¿Consulta nuestro precio de pre venta?**")
    else:
        st.markdown(f"**La pre-venta ha terminado, pero sigue disponible a precio normal.**")

    # Mensaje de pagos internacionales
    st.markdown("**Pagos internacionales a través de PayPal.**")

if opcion == "📆 Cursos mensuales":
    curso_sel = st.selectbox("Selecciona un curso mensual para más información:", [
        "Análisis y modelamiento de series de tiempo con Python",
        "Modelos de machine learning para forecasting con Python",
        "Fundamentos de econometría con R",
        "Modelos estadísticos con R"
    ])
    datos = cursos[curso_sel]
    st.markdown(f"### 🗓 {curso_sel}")
    st.markdown(f"{datos['descripcion']}")
    st.markdown(f"- **Duración**: {datos['duracion']}")
    st.markdown(f"- **Inicio**: {datos['inicio']}")
    st.markdown(f"- **Fin**: {datos['fin']}")

    # Mostrar tabla de precios
    precio = datos['precio']
    mostrar_tabla_precio(precio)

    # Mostrar enlaces personalizados
    mostrar_links(curso_sel)

elif opcion == "📚 Programas de 2 meses":
    prog_sel = st.selectbox("Selecciona un programa:", [
        "Forecasting con Python (julio)",
        "Econometría aplicada con R (julio)"
    ])
    datos = cursos[prog_sel]
    st.markdown(f"### 🗓 {prog_sel}")
    st.markdown(f"{datos['descripcion']}")
    st.markdown(f"- **Duración total**: {datos['duracion']}")
    st.markdown(f"- **Inicio**: {datos['inicio']}")
    st.markdown(f"- **Fin**: {datos['fin']}")

    # Mostrar tabla de precios
    precio = datos['precio']
    mostrar_tabla_precio(precio)

    # Mostrar enlaces personalizados
    mostrar_links(prog_sel)
