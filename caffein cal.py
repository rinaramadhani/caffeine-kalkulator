import streamlit as st

# Tambahkan background image & style
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://i.pinimg.com/736x/9b/e8/32/9be83278b48a97b9218b58f236c2be28.jpg")
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
    }
    .main {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 0px;
        border-radius: 10px;
        margin-top: 5%;
    }
    .title {
        color: Black;
        text-align: center;
    }
    h3 {
        color: Black;
    }
    .custom-text {
        color: Black;
        font-size: 16px;
        font-family: 'Calibri', 'Segoe UI', sans-serif;
    }
    .fakta-seru {
        position: fixed;
        bottom: 10px;
        left: 10px;
        background-color: rgba(255,255,255,0.9);
        padding: 12px 18px;
        border-radius: 10px;
        font-size: 14px;
        font-family: 'Segoe UI', sans-serif;
        box-shadow: 0 0 10px rgba(0,0,0,0.2);
        max-width: 300px;
    }
    </style>
""", unsafe_allow_html=True)

# Fungsi untuk menghitung batas aman konsumsi kafein
def hitung_batas_aman_kafein(usia, jenis_kelamin):
    if usia < 18:
        return 100  # Anak-anak
    elif jenis_kelamin == "Laki-laki":
        return 400  # Dewasa laki-laki
    else:
        return 300  # Dewasa perempuan

# Fungsi untuk menghitung konsumsi kafein berdasarkan jenis minuman
def hitung_kafein_terkonsumsi(jenis_minuman, ml):
    kandungan_kafein = {
        "Minuman Soda": 10,      # mg per 100 ml
        "Minuman Coklat": 5,    # mg per 100 ml
        "Kopi": 40,             # mg per 100 ml
        "Minuman Berenergi": 30, # mg per 100 ml
        "Matcha": 25,           # mg per 100 ml
        "Espresso": 212,        # mg per 100 ml
        "Teh Hijau": 12,        # mg per 100 ml
        "Teh Hitam": 47,        # mg per 100 ml
        "Cappuccino": 77,       # mg per 100 ml
        "Americano": 94         # mg per 100 ml
    }
    return (kandungan_kafein.get(jenis_minuman, 0) * ml) / 100

# Sidebar navigasi
menu = st.sidebar.radio("Navigasi", ["Home", "Kalkulator Kafein", "Tentang Kami"])

# Halaman Home
if menu == "Home":
    st.title("Selamat Datang di Kalkulator Kafein☕")
    st.write("""
    *Kalkulator Kafein Harian* membantu Anda mengetahui batas aman konsumsi kafein berdasarkan usia, jenis kelamin, 
    dan jenis minuman. Gunakan fitur ini untuk menjaga kesehatan Anda dan keluarga! 
    Pilih menu *Kalkulator Kafein* untuk memulai perhitungan. 🤩
    """)

    st.subheader("Apa Itu Kafein?🤔")
    st.write("""
    Kafein adalah senyawa alami yang ditemukan dalam daun dan biji berbagai tanaman seperti kopi, teh, dan kakao. 
    Kafein bekerja sebagai stimulan yang mempengaruhi sistem saraf pusat untuk meningkatkan energi dan kewaspadaan sementara.
    """)

    st.subheader("Manfaat Kafein🤫:")
    st.markdown("""
    - ✅ Meningkatkan fokus dan konsentrasi  
    - ✅ Membantu mengurangi rasa lelah  
    - ✅ Meningkatkan performa olahraga  
    - ✅ Dapat membantu suasana hati (mood booster)  
    """)

    st.subheader("Efek Samping Kafein Jika Berlebihan😵:")
    st.markdown("""
    - ❌ Gangguan tidur dan insomnia  
    - ❌ Jantung berdebar (palpitasi)  
    - ❌ Kecemasan dan gelisah  
    - ❌ Gangguan pencernaan seperti sakit perut atau asam lambung naik  
    - ❌ Ketergantungan kafein (caffeine withdrawal)  
    """)

    st.info("Ingat, konsumsi kafein yang bijak dapat memberikan manfaat. Namun, pastikan tetap dalam batas yang aman setiap harinya.")

# Halaman Kalkulator Kafein
elif menu == "Kalkulator Kafein":
    # Judul aplikasi
    st.title("Kalkulator Batas Kafein Harian☕")

    # Input dari pengguna
    berat_badan = st.number_input("Berat Badan (kg):", min_value=0.0, step=0.1)
    usia = st.number_input("Usia (tahun):", min_value=0, step=1)
    jenis_kelamin = st.radio("Jenis Kelamin:", ["Laki-laki", "Perempuan"])
    jenis_minuman = st.selectbox(
        "Sumber Kafein:",
        ["Minuman Soda", "Minuman Coklat", "Kopi", "Minuman Berenergi", "Matcha", "Espresso", "Teh Hijau", "Teh Hitam", "Cappuccino", "Americano"]
    )
    ml_dikonsumsi = st.number_input("Berapa ml yang diminum:", min_value=0, step=1)

    # Hitung hasil
    if st.button("Hitung"):
        batas_aman = hitung_batas_aman_kafein(usia, jenis_kelamin)
        kafein_terkonsumsi = hitung_kafein_terkonsumsi(jenis_minuman, ml_dikonsumsi)
        sisa_kafein = max(batas_aman - kafein_terkonsumsi, 0)

        # Tampilkan hasil
        st.subheader("Hasil Perhitungan:")
        st.write(f"**Batas Harian:** {batas_aman} mg")
        st.write(f"**Konsumsi Kafein:** {kafein_terkonsumsi:.2f} mg")
        st.write(f"**Sisa Batas Aman:** {sisa_kafein:.2f} mg")

        if sisa_kafein > 0:
            st.write(f"**Status:** Aman✅, Anda masih dalam batas konsumsi kafein yang aman😊.")
        else:
            st.warning("**Status:** Tidak Aman❗, Anda telah melewati batas konsumsi kafein harian yang aman!😔")

# Halaman Tentang Kami
elif menu == "Tentang Kami":
    st.title("Tentang Kami")
    st.write("""
    **Kalkulator Batas Kafein Harian** adalah aplikasi sederhana yang dirancang untuk membantu Anda mengelola konsumsi kafein dengan mudah.
    
    **Pengembang:**
    - Aplikasi ini dibuat oleh **Kelompok 9** sebagai bagian dari proyek pembelajaran.
    - Tujuannya adalah memberikan alat yang praktis untuk menjaga kesehatan dengan membatasi konsumsi kafein berlebih.

    **Fitur Utama:**
    - Perhitungan batas kafein berdasarkan usia dan jenis kelamin.
    - Kalkulasi konsumsi kafein dari berbagai jenis minuman.
    - Informasi yang interaktif dan mudah digunakan.

    **Terima kasih telah menggunakan aplikasi kami! 😊**
    """)
