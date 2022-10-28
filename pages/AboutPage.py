import streamlit as st
from controller.AppController import AppController


def mostrar():
    return """
        #### 
        Aplicación de **streamlit**.

        Este es un ejemplo de lo que se puede hacer en este framework.

        ####
        Ejemplo elaborado para @   por Luisa Rincón.

        """



# Main call
if __name__ == "__main__":
    st.write(mostrar())