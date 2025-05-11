import streamlit as st

st.set_page_config(page_title="LUNA - Habilidades DBT", layout="centered")
st.title("🌙 LUNA - Asistente DBT en Crisis")
st.markdown("Bienvenido. ¿Qué habilidad DBT quieres practicar hoy?")

menu = ["Pros y Contras", "STOP", "TIP", "ACEPTAS", "SALVARAS", "5 Sentidos"]
choice = st.selectbox("Selecciona una habilidad:", menu)

if choice == "Pros y Contras":
    st.subheader("💭 Pros y Contras")
    st.write("Hablemos sobre tus opciones...")
    st.text("LUNA: Veamos los beneficios de resistir el impulso frente a ceder a él...")
elif choice == "STOP":
    st.subheader("🛑 STOP")
    st.text("LUNA: Detente. Respira. Observa. Procede con atención.")
# ... Agregar más roleplays según sea necesario