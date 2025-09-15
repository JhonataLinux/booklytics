import sys
from streamlit.web import cli as stcli

sys.argy = ["streamlit", "run", "app.py"]
sys.exit(stcli.main())# Escreva o seu código aqui :-)
