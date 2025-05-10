import streamlit as st

# Fungsi untuk menambahkan background warna coklat muda
def set_background():
    st.markdown(
        """
        <style>
        body {
            background-color: #f5e6d9;
            color: #4a3f35;
        }
        .stButton > button {
            background-color: #8b4513;
            color: white;
            border-radius: 8px;
            font-size: 16px;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
        }
        .stButton > button:hover {
            background-color: #a0522d;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Tambahkan background ke aplikasi
set_background()

# Fungsi untuk menghitung batas kafein harian
def hitung_kafein_ideal(berat_badan_kg, usia, jenis_kelamin, konsumsi_kafein_mg):
    # Batas kafein berdasarkan usia
    if usia < 12:
        batas_kafein_per_kg = 2.5
    elif usia < 18:
        batas_kafein_per_kg = 3.0
    else:
        batas_kafein_per_kg = 5.0 if berat_badan_kg * 5.0 <= 400 else 400 / berat_badan_kg
    
    # Faktor jenis kelamin
    faktor_jenis_kelamin = 0.9 if jenis_kelamin.lower() == "wanita" else 1.0
    
    # Hitung batas harian
    batas_harian = berat_badan_kg * batas_kafein_per_kg * faktor_jenis_kelamin
    
    # Hitung sisa batas aman
    sisa_kafein = batas_harian - konsumsi_kafein_mg
    
    # Status konsumsi
    status = "Aman✅" if sisa_kafein >= 0 else "Berlebihan❗"
    
    return {
        "batas_harian_mg": batas_harian,
        "konsumsi_kafein_mg": konsumsi_kafein_mg,
        "sisa_kafein_mg": sisa_kafein,
        "status": status
    }

# Streamlit app
st.title("☕ Kalkulator Kafein Harian 📊")

# Input data pengguna
berat_badan = st.number_input("Masukkan berat badan (kg):", min_value=1.0, step=0.1)
usia = st.number_input("Masukkan usia (tahun):", min_value=1, step=1)
jenis_kelamin = st.selectbox("Pilih jenis kelamin:", ["Laki-laki", "Wanita"])

st.write("Masukkan total konsumsi kafein hari ini (dalam ml):")
# Input jumlah total ml
ml_total = st.number_input("Total konsumsi minuman (ml):", min_value=0, step=1)

# Kandungan kafein per 100 ml berdasarkan rata-rata konsumsi
# Anda bisa menyesuaikan angka ini sesuai target pengguna
rata_rata_kafein_per_100ml = 25  # Rata-rata kafein dari semua jenis minuman

# Hitung total kafein berdasarkan input
total_kafein = (ml_total / 100) * rata_rata_kafein_per_100ml

# Tombol hitung
if st.button("Hitung"):
    if berat_badan > 0 and usia > 0:
        hasil = hitung_kafein_ideal(berat_badan, usia, jenis_kelamin, total_kafein)
        
        st.subheader("Hasil Kalkulator Kafein")
        st.write(f"**Batas Harian:** {hasil['batas_harian_mg']:.2f} mg")
        st.write(f"**Konsumsi Kafein:** {hasil['konsumsi_kafein_mg']:.2f} mg")
        st.write(f"**Sisa Batas Aman:** {hasil['sisa_kafein_mg']:.2f} mg")
        st.write(f"**Status:** {hasil['status']}")
    else:
        st.error("Mohon isi semua data dengan benar!")



    


  


