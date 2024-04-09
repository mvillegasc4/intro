import streamlit as st
from PIL import Image

st.title(" Bienvenido")

st.header("En este puedo demostrar al mundo las capacidades sobre humanas que poseo")
st.write("Te amo hello kitty.")
image=Image.open("kitty.jpg")
st.image(image, caption= "hello kitty :3")

texto=st.text_input("Escribe algo", "Este es mi texto")
st.write("el texto escrito es", texto)

st.subheader("Ahora Usemos 2 columnas")
col1, col2 = st.columns(2)
with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia de usuario")
  resp=st.checkbox("Estoy de acuerdo")
  if resp:
    st.write("correcto") 
with col2:
  st.subheader("Esta es la segunda")
  modo=st.radio("Que modalidad es la principal de tu interfaz",("Visual", "auditivo", "tactil"))
  if modo=="Visual":
    st.write("holaholahola")
  if modo=="auditivo":
    st.write("holiholiholi")
  if modo=="tactil":
    st.write("holaholiholo")



st.subheader("uso de botones")
if st.button("Presiona el boton"):
  st.write("Gracias por presionar")
else:
  st.write("No has presionado aun")
