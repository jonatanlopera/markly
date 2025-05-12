
import streamlit as st
from fpdf import FPDF

st.set_page_config(page_title="Markly - Golden Circle", layout="centered")

st.image("markly_logo.png", width=200)

st.title("✨ Bienvenido a Markly")
st.markdown("Crea tu Golden Circle paso a paso con IA.")

# Simulación de conversación
why = st.text_input("¿Qué te mueve a crear tu marca?")
how = st.text_input("¿Qué haces diferente?")
what = st.text_input("¿Qué ofreces?")

if st.button("Ver mi Golden Circle"):
    st.subheader("🎯 Tu Golden Circle")
    st.write(f"**Why:** {why}")
    st.write(f"**How:** {how}")
    st.write(f"**What:** {what}")

    # Generar PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Tu Golden Circle - Markly", ln=True, align="C")
    pdf.ln(10)
    pdf.multi_cell(0, 10, f"Why: {why}

How: {how}

What: {what}")

    pdf.output("/tmp/markly_circle.pdf")
    with open("/tmp/markly_circle.pdf", "rb") as f:
        st.download_button("📄 Descargar PDF", f, "GoldenCircle_Markly.pdf")

