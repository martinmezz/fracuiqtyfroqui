import streamlit as st

st.set_page_config(page_title="Test fracuiqtyfroqui", layout="wide")

st.title("✅ Deploy de prueba – fracuiqtyfroqui")

st.markdown(
    """
    Esto es solo un *smoke test*.

    - Código viene del repo de GitHub.
    - Está corriendo en Streamlit Cloud (o el hosting que uses).
    - Si ves esto en el celu: **la vuelta GitHub → deploy → teléfono funciona**.
    """
)

st.sidebar.header("Controles")
valor = st.sidebar.slider("Elegí un número", 0, 100, 42)
st.write(f"Valor elegido: **{valor}**")