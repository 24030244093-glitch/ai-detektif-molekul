import streamlit as st
import joblib
import numpy as np

# 1. Memuat otak AI (Gunakan cache agar lebih cepat)
@st.cache_resource
def load_model():
    return joblib.load('model_decision_tree.pkl')

model = load_model()

# 2. Mengatur halaman agar lebih menarik bagi anak SMA
st.set_page_config(page_title="Penyelamat Bumi AI", page_icon="🕵️‍♂️", layout="wide")

# --- FITUR BARU 1: SIDEBAR (Menu Samping untuk Edukasi) ---
with st.sidebar:
    st.header("📚 Tahukah Kamu?")
    st.info("Senyawa ramah lingkungan (RB) biasanya memiliki **ikatan kimia yang mudah diputus** oleh bakteri pengurai di alam.")
    st.warning("Sebaliknya, limbah abadi (NRB) sering memiliki ikatan yang rumit, kaku, atau mengandung racun (seperti plastik polimer yang butuh ratusan tahun untuk hancur).")
    st.success("Tugasmu sebagai agen Green Chemistry adalah meracik molekul yang pas agar tidak menjadi monster limbah!")

# --- HALAMAN UTAMA ---
st.title("🕵️‍♂️ Lab Detektif Molekul: Misi Hijau! 🌍")
st.write("Selamat datang di Lab Virtual! Masukkan resep kimia molekul buatanmu di bawah ini, dan biarkan AI kita menebak apakah molekul ini **Pahlawan Lingkungan** atau **Monster Limbah**.")
st.markdown("---")

st.subheader("🧪 Resep Karakteristik Molekul:")
st.write("*(Arahkan kursor ke ikon tanda tanya [?] untuk melihat bocoran materi Kimia!)*")

# Membuat tampilan input menjadi 2 kolom agar rapi
col1, col2 = st.columns(2)

with col1:
    # Menggunakan parameter 'help' untuk memunculkan tooltip rahasia
    spmax_l = st.number_input("1. Panjang Kerangka Molekul (SpMax_L)", value=3.91, help="Semakin panjang, semakin susah diurai! (Gaya tarik antarmolekul lebih kuat)")
    spmax_a = st.number_input("2. Tingkat Kerumitan Cabang (SpMax_A)", value=1.93, help="Molekul bercabang lebih susah diurai! (Bentuknya kaku, enzim bakteri susah masuk)")
    spposa_b = st.number_input("3. Sifat Suka Air / Kepolaran (SpPosA_B)", value=1.20, help="Senyawa polar mudah dilarutkan bakteri! (Ingat Kepolaran SMA!)")
    sm6_bm = st.number_input("4. Kepadatan Molekul (SM6_B)", value=7.25)
    sm6_l = st.number_input("5. Ukuran Ruang Molekul (SM6_L)", value=9.00)

with col2:
    hywi_bm = st.number_input("6. Sifat Benci Air / Hidrofobik (HyWi_B)", value=3.10, help="Senyawa hidrofobik susah diurai! (Seperti minyak, benci air, kaku)")
    ncb = st.number_input("7. Jumlah Ikatan Karbon Rangkap (nCb-)", value=0, step=1)
    c026 = st.number_input("8. Jumlah Atom Kaku (C-026)", value=0, step=1)
    nhm = st.number_input("9. Kandungan Logam/Halogen Beracun (nHM)", value=0, step=1, help="Sangat beracun, bakteri bisa mati! (Seperti Klorin di plastik PVC)")
    spmax_bm = st.number_input("10. Tingkat Kekakuan Struktur (SpMax_B)", value=2.94)

st.markdown("---")

# 3. Tombol Eksekusi dengan Nama Baru
if st.button("🚀 Pindai Molekul Sekarang!", use_container_width=True):
    # Menyusun matriks input (Urutannya tetap dijaga sama persis agar AI tidak bingung)
    input_data = np.array([[spmax_l, spmax_a, spposa_b, sm6_bm, sm6_l, hywi_bm, ncb, c026, nhm, spmax_bm]])
    
    # AI mulai menebak
    prediksi = model.predict(input_data)
    
    # 4. Menampilkan Hasil yang Menarik
    st.subheader("📊 Hasil Pindaian AI Detektif:")
    
    if prediksi[0] == 'RB':
        st.balloons() # Animasi Balon jika misi berhasil!
        st.success("🎉 MISI BERHASIL: **Molekul Ramah Lingkungan (RB)**")
        st.markdown("> **Kesimpulan:** Bakteri pengurai di alam sangat suka mencerna senyawa ini. Bumi aman dari penumpukan limbah!")
    else:
        st.error("⚠️ BAHAYA: **Monster Limbah Abadi (NRB)**")
        st.markdown("> **Peringatan:** Gawat! Struktur molekul ini terlalu rumit, kaku, atau beracun. Jika dibuang ke lingkungan, ia akan bertahan ratusan tahun sebagai polutan. Coba ubah resepnya!")