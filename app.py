import streamlit as st
from responseprocessing import generate_response


def index() :
    st.title("SG AI Week 14")
    st.text("Ini adalah teks")
    st.header("Tutorial Streamlit")
    nama = st.text_input(label="Nama", value="Masukan nama anda disini", key="input1")
    nim = st.text_input("NIM", key="input2")

    if nama :
        st.text("Nama: " + nama)
        if len(nim) == 12 :
            st.text("NIM: " + nim)

    box = st.selectbox("Pilih jurusan: ", ["RPL", "IF", "DS", "IT"])
    st.write("pilihan anda adalah \n " + box)
    st.text("pilihan anda adalah \n " + box)

    umur = st.slider("umur", 1, 70, 100)
    st.write(umur)

    gender = st.radio('Gender', ['Pria', 'Wanita'])
    if gender == 'Pria' :
        st.write(f"Hello Mr.{nama}")
    else :
        st.write(f"Hello Mrs.{nama}")

    list_hobi = st.text_area("Hobi", "Main bola, main game")
    list_hobi = [x.strip() for x in list_hobi.split(',')]

    st.write(list_hobi)

    st.divider()
    st.image("https://static.promediateknologi.id/crop/0x0:0x0/0x0/webp/photo/p2/222/2024/08/18/WhatsApp-Image-2024-08-17-at-140220-4284981413.jpeg", caption="gambar kucing", width=200)

    st.markdown(
        '[ini link ke google](https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwi2gdDT566KAxVwSmwGHd8lFJAQPAgJ)'
    )

    st.markdown('# header')
    st.header('header')
    st.markdown('## header 2')
    st.markdown('###### header 6')

    import pandas as pd

    data = {
        'Pekerjaan': ['Programmer', 'Dokter', 'Pengacara'],
        'Tier': ["E", "SS", "A"]
    }

    df = pd.DataFrame(data)
    st.dataframe(data=df, use_container_width=True)

    st.title("Buka Data")
    file = st.file_uploader('Pilih file', type=['jpg', 'csv'])

    if file is not None:
        st.write(file.type)

        if file.type == "image/jpeg" :
            st.image(file)
        else :
            data = pd.read_csv(file)
            st.dataframe(data)

    st.divider()

    num1 = st.number_input("Masukkan angka pertama", value=0)
    num2 = st.number_input("Masukkan angka kedua", value=0)

    operasi = st.radio('Pilih operasi', ["Penjumlahan", "Pengurangan", "Pembagian", "Perkalian"])

    if st.button('hitung') :
        if operasi == "Penjumlahan" :
            hasil = num1 + num2
        elif operasi == "Pengurangan" :
            hasil = num1 - num2


        st.success(f'Hasil {operasi} : {hasil}')

def direct_chat(text, role):
    with st.chat_message(role):
        st.write(text)

def chatbot() :
    st.header("Tampilan chatbot")
    prompt = st.chat_input("ketik sesuatu")
    if prompt :
        direct_chat(prompt, role="user")
        response = generate_response(prompt)
        direct_chat(response, role="assistant")

st.sidebar.title('Menu')
st.sidebar.header('Profile')
if st.sidebar.checkbox('Biodata') :
    st.sidebar.text(f"nama: {nama} \nNIM: {nim}")
choice = st.sidebar.radio(label="Pilihan", options=["index", "chatbot"])
if choice == "index" :
    index()
else :
    chatbot()