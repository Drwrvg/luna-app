
import streamlit as st

st.set_page_config(page_title="LUNA - Asistente DBT", layout="centered")
st.title("🌙 LUNA - Asistente en habilidades DBT")
st.subheader("Living with Understanding, Navigation, and Acceptance")

st.markdown("---")
st.write("Selecciona una habilidad que quieras explorar con LUNA:")

opciones = [
    "Pros y Contras",
    "SALVARAS",
    "ACEPTAS",
    "Calmarse con los cinco sentidos"
]

eleccion = st.selectbox("🧠 Habilidades de Tolerancia al Malestar", opciones)

def mostrar_roleplay(habilidad):
    if habilidad == "Pros y Contras":
        st.markdown("### Pros y Contras 🧾")
        st.write("💬 *LUNA*: Entiendo que estás en un momento difícil. ¿Quieres que pensemos junt@s en los pros y contras de actuar por impulso versus usar una habilidad?")
        accion = st.radio("¿Cuál es la acción que estás considerando?", ["Autolesionarme", "Evitar la situación", "Hablar con alguien", "Otra"])
        if st.button("Ver análisis"):
            st.success("Gracias por compartirlo. Vamos a ver juntos los posibles pros y contras.")
            st.markdown("#### ✅ Pros de actuar impulsivamente:")
            st.write("- Alivio momentáneo del malestar.")
            st.markdown("#### ❌ Contras de actuar impulsivamente:")
            st.write("- Consecuencias físicas o emocionales a largo plazo.
- Aumenta la culpa o vergüenza.")
            st.markdown("#### ✅ Pros de usar una habilidad:")
            st.write("- Cuidado de ti mism@.
- Refuerzas tu autoestima.
- Reduces el daño.")
            st.markdown("#### ❌ Contras de usar una habilidad:")
            st.write("- No tendrás alivio inmediato.
- Requiere esfuerzo emocional.")
            st.info("💡 *LUNA*: Recuerda, hacer lo difícil a veces es lo más valiente. Estoy aquí contigo.")

    elif habilidad == "SALVARAS":
        st.markdown("### SALVARAS 🛟")
        st.write("💬 *LUNA*: Esta habilidad nos ayuda a distraernos con propósito. ¿Te gustaría probarla ahora?")
        if st.button("Sí, guíame"):
            st.markdown("""
            **S**: Contribuye con alguien  
            **A**: Activa tus sentidos  
            **L**: Lee algo interesante  
            **V**: Ve algo que te relaje  
            **A**: Ayuda a otros o haz voluntariado  
            **R**: Recuerda algo positivo  
            **A**: Actividad física  
            **S**: Sonríe, aunque no tengas ganas  
            """)
            st.info("💡 *LUNA*: ¿Cuál de estas te llama la atención para hacer ahora? Escríbemela o piensa en ella, ¡y vamos juntas!")

    elif habilidad == "ACEPTAS":
        st.markdown("### ACEPTAS 🎭")
        st.write("💬 *LUNA*: Esta habilidad usa distracción consciente. Vamos paso a paso.")
        st.markdown("""
        **A**: Actividades  
        **C**: Contribuir  
        **E**: Emociones opuestas  
        **P**: Pensamientos opuestos  
        **T**: Trasladarse mentalmente  
        **A**: Animales o naturaleza  
        **S**: Sensaciones intensas  
        """)
        eleccion = st.selectbox("¿Cuál quieres probar?", ["Actividades", "Emociones opuestas", "Trasladarte mentalmente", "Sensaciones intensas"])
        if eleccion:
            st.success(f"Vamos a probar: {eleccion}.")
            st.info(f"💬 *LUNA*: Estoy contigo, solo respira. Esta elección puede ayudarte a tolerar el momento difícil sin hacerte daño.")

    elif habilidad == "Calmarse con los cinco sentidos":
        st.markdown("### Calmarse con los cinco sentidos 👃👂👀👅🖐️")
        st.write("💬 *LUNA*: Vamos a usar tus sentidos para ayudarte a regularte.")
        st.markdown("""
        - 👀 Vista: mira algo bonito, observa colores.  
        - 👂 Oído: pon música calmada o sonidos naturales.  
        - 👃 Olfato: huele aceites esenciales o tu perfume favorito.  
        - 👅 Gusto: come algo sabroso y despacio.  
        - 🖐️ Tacto: acaricia algo suave o siente una textura agradable.  
        """)
        st.success("💡 *LUNA*: ¿Cuál de estos te llama la atención ahora? Puedes hacerlo ahora mismo. Yo te acompaño mientras lo haces.")
        st.markdown("*Estoy aquí. Solo por este momento, estás segur@.*")

mostrar_roleplay(eleccion)
