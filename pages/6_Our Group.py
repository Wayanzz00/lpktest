import streamlit as st

col1, col2, col3 = st.columns([1, 3, 0.5])
with col3:
    st.markdown=st.page_link("Home.py", label="Home")

with col2:
    st.title ("About Our Group")

st.write=("**Welcome to Our Group!**")

st.header(" ", divider="gray")
 
group_info = """
    **Meet Our Team:**

    - **Aditiya Prayoga** 
    - **Faiz Awanda A** 
    - **Ilham Alfitrah** 
    - **Syaamil Maulana** 
    - **Wayan Raka S** 
    """
st.write(group_info)

st.header(" ", divider="gray")

st.write('_bagian dari project Praktik Logika dan Pemograman Komputer_')
st.write('Dosen Penanggung Jawab')
st.write('Dewi Pujo Ningsih, M.Si')