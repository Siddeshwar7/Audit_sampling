import streamlit as st
import subprocess
from PIL import Image

process1 = subprocess.Popen(["Rscript", "Audit_sampling.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result1 = process1.communicate()
st.write(result1)

