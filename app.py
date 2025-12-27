import streamlit as st

# 1. Pengaturan Tampilan Agar Terlihat Seperti App Murni
st.set_page_config(page_title="Shopee Profit Master", page_icon="🧡", layout="centered")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            [data-testid="stSidebar"] {display: none;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 2. Judul Aplikasi
st.title("🧡 Shopee Cuan Calculator")
st.markdown("---")

# 3. Input Data Produk
col1, col2 = st.columns(2)
with col1:
    modal_barang = st.number_input("Modal Produk (HPP)", min_value=0, value=50000, step=1000)
    harga_jual = st.number_input("Rencana Harga Jual", min_value=0, value=75000, step=1000)

with col2:
    biaya_admin = st.number_input("Biaya Admin (%)", min_value=0.0, value=6.0, step=0.1)
    biaya_layanan = st.number_input("Biaya Layanan (FO/CB) (%)", min_value=0.0, value=4.0, step=0.1)

# 4. Perhitungan Logika Shopee
total_potongan_persen = biaya_admin + biaya_layanan
nominal_potongan = (total_potongan_persen / 100) * harga_jual
pendapatan_bersih = harga_jual - nominal_potongan - modal_barang
margin_persen = (pendapatan_bersih / harga_jual) * 100 if harga_jual > 0 else 0

# 5. Tampilan Hasil (Layout Dashboard)
st.subheader("📊 Hasil Analisa")
c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Potongan Shopee", f"Rp {nominal_potongan:,.0f}")
with c2:
    st.metric("Cuan Bersih", f"Rp {pendapatan_bersih:,.0f}")
with c3:
    st.metric("Margin (%)", f"{margin_persen:.1f}%")

# 6. Indikator Kesehatan Bisnis
if margin_persen > 20:
    st.success("🔥 Cuan Tebal! Aman untuk iklan.")
elif 10 <= margin_persen <= 20:
    st.warning("⚠️ Cuan Tipis. Hati-hati dengan biaya iklan!")
else:
    st.error("🚨 Bahaya! Margin terlalu rendah, cek lagi biaya admin Anda.")

st.info(f"Uang yang masuk ke saldo penjual: Rp {harga_jual - nominal_potongan:,.0f}")
