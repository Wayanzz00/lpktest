import streamlit as st

col1, col2, col3 = st.columns([1, 3, 0.5])
with col3:
    st.markdown=st.page_link("Home.py", label="Home")

with col2:
    st.title ("About Our Group")

st.write=("**Welcome to Our Group!**")

st.header(" ", divider="gray")
 
st.write("**Meet Our Team:**")

st.write("- **Aditiya Prayoga**")
st.write("- **Faiz Awanda A**")
st.write("- **Ilham Alfitrah**")
st.write("- **Syaamil Maulana**")
st.write("- **Wayan Raka S**")


st.header(" ", divider="gray")

st.write('_bagian dari project Praktik Logika dan Pemograman Komputer_')
st.write('Dosen Penanggung Jawab')
st.write('Dewi Pujo Ningsih, M.Si')
