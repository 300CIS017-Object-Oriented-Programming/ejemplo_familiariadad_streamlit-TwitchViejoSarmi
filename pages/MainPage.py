import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from controller.AppController import AppController
from model.DatosPersonales import DatosPersonales



class MainPage:

    def __init__(self) -> None:
        super().__init__()

        if 'main_view' not in st.session_state:
            self.menu_actual = "About"
            self.controller = AppController()

            # Variable necesasaria para mantener el estado
            st.session_state['main_view'] = self
        else:
            self.menu_actual = st.session_state.main_view.menu_actual
            self.controller = st.session_state.main_view.controller
            self.btn_buscar_gui = False
        self._inicialializar_layout()

    def _inicialializar_layout(self):
        # Set page title, icon, layout wide (more used space in central area) and sidebar initial state
        st.set_page_config(page_title="Familiariadad streamtlit", page_icon='', layout="wide",
                           initial_sidebar_state="expanded")
        # Defines the number of available columns del area principal
        self.col1, self.col2, self.col3 = st.columns([1, 1, 1])

        # Define lo que abrá en la barra de menu
        #with st.sidebar:
            #self.menu_actual = option_menu("Menu", ["About", "Prueba", "Aspirante"],
                                           #icons=['house', 'gear'], menu_icon="cast", default_index=1)


# Main call
if __name__ == "__main__":
    gui = MainPage()
    #gui.controlar_menu()
