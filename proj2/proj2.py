# imported some libraries
import streamlit as st
import openpyxl
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.styles import Border, Side
from openpyxl.styles import PatternFill
import pandas as pd
import os
from datetime import datetime
from openpyxl.utils.dataframe import dataframe_to_rows
from streamlit_option_menu import option_menu



start_time = datetime.now()
st.set_page_config(page_title="Project 2",page_icon=":tada:",layout="wide")

with st.sidebar:
    select = option_menu("Main Menu",["Home","Browse File","Add path"],icons=['house','files','folder'],menu_icon="laptop",default_index=0)
