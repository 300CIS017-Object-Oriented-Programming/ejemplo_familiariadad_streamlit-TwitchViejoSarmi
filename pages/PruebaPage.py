from io import StringIO
import streamlit as st
import pandas as pd

def probar_streamlit():
    """ Ponga aqui todos los controles de prueba para que entienda como funciona"""
    st.write("Agregue aquí botones, paneles, y opciones tal como se describe en el readme")
    st.button("Soy un boton")

    col1, col2 = st.columns(2)

    with col1:
        st.header("Primer Input:")
        if st.button("Clip"):
            video_file = open('files\#SHORTS LAS PATATAS ESTÁN MALDITAS.mp4', 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes)
            st.markdown("Clip extraído de: [https://www.twitch.tv/viejosarmi](https://www.twitch.tv/viejosarmi)")

            with st.expander("Contexto"):
                st.write("""
                    Habían descubierto un comando de admin de nombre 'patata' cuya función era castigar a quienes lo usaran. Los que lo usaron simplemente las caían rayos y pare de contar. Y bueno, como habrán visto en el clip, a mi me paso otra cosa.
                """)


    with col2:
        st.header("Segundo Input:")
        uploaded_file = st.file_uploader("Ponga foto de los numeros de su tarjeta de credito aqui:")
        if uploaded_file is not None:
            # Se lee el archivo como Bytes
            bytes_data = uploaded_file.getValue()
            st.write(bytes_data)

            # Para convertir a un string basado en IO:
            stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            st.write(stringio)

            # Para leer un archivo como string:
            string_data = stringio.read()
            st.write(string_data)

            # Puede usarse para cualquier archivo (o eso entendí):
            dataframe = pd.read_csv(uploaded_file)
            st.write(dataframe)

        mental_health = st.radio(
            '¿Cómo te sirves un cereal?',
            ('Seleccione','Primero el cereal y luego la leche', 'Primero la leche y luego el cereal')
        )

        if mental_health == 'Seleccione':
            pass
        elif mental_health == 'Primero el cereal y luego la leche':
            st.write('Entendible, tenga un buen día ;).')
        else:
            st.write('¿Te encuentras bien?¿Necesitas un psicólogo?')


# Main call
if __name__ == "__main__":
    probar_streamlit()