import streamlit as st

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
