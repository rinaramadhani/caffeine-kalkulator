import streamlit as st

# Fungsi untuk menghitung batas aman konsumsi kafein
def calculate_safe_caffeine(age, gender):
    if age < 18:
        return 100  # Anak-anak
    elif gender == "Laki-laki":
        return 400  # Dewasa laki-laki
    else:
        return 300  # Dewasa perempuan

# Fungsi untuk menghitung konsumsi kafein berdasarkan jenis minuman
def calculate_caffeine_consumed(drink_type, ml):
    caffeine_content = {
        "Minuman Soda": 10,      # mg per 100 ml
        "Minuman Coklat": 5,    # mg per 100 ml
        "Teh": 20,              # mg per 100 ml
        "Kopi": 40,             # mg per 100 ml
        "Minuman Berenergi": 30 # mg per 100 ml
    }
    return (caffeine_content.get(drink_type, 0) * ml) / 100

# Mengatur tema warna background
st.markdown(
    """
    <style>
    body {
        background-color: #f0f8ff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Judul aplikasi
st.title("Kalkulator Konsumsi Kafein")

# Input dari pengguna
weight = st.number_input("Berat Badan (kg):", min_value=0.0, step=0.1)
age = st.number_input("Usia (tahun):", min_value=0, step=1)
gender = st.radio("Jenis Kelamin:", ["Laki-laki", "Perempuan"])
drink_type = st.selectbox(
    "Sumber Kafein:",
    ["Minuman Soda", "Minuman Coklat", "Teh", "Kopi", "Minuman Berenergi"]
)
ml_consumed = st.number_input("Berapa ml yang diminum:", min_value=0, step=1)

# Hitung hasil
if st.button("Hitung"):
    safe_limit = calculate_safe_caffeine(age, gender)
    caffeine_consumed = calculate_caffeine_consumed(drink_type, ml_consumed)
    remaining_caffeine = max(safe_limit - caffeine_consumed, 0)

    # Tampilkan hasil
    st.subheader("Hasil Perhitungan:")
    st.write(f"Batas konsumsi kafein harian yang aman: {safe_limit} mg")
    st.write(f"Kafein yang telah Anda konsumsi: {caffeine_consumed:.2f} mg")
    st.write(f"Jumlah kafein yang masih boleh dikonsumsi hari ini: {remaining_caffeine:.2f} mg")

    if remaining_caffeine == 0:
        st.warning("Anda telah mencapai atau melewati batas konsumsi kafein harian yang aman!")
