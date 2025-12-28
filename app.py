import streamlit as st
import streamlit.components.v1 as components

# 1. Konfigurasi Halaman & Keamanan Sederhana
st.set_page_config(page_title="Shopee Pricing Assistant Pro", page_icon="🧡", layout="centered")

# Fungsi untuk menyembunyikan elemen Streamlit agar terlihat seperti Web Resmi
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding-top: 0rem; padding-bottom: 0rem;}
    </style>
    """, unsafe_allow_html=True)

# 2. Logika Password (Sederhana agar Anda bisa menjual akses)
# Ganti 'cuan2025' dengan password keinginan Anda
PASSWORD_BENAR = "cuan2025" 

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.title("🔐 Akses Terbatas")
    pwd_input = st.text_input("Masukkan Password Akses:", type="password")
    if st.button("Masuk ke Aplikasi"):
        if pwd_input == PASSWORD_BENAR:
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("Password salah! Silakan hubungi Admin untuk membeli akses.")
            st.markdown(f'<a href="https://wa.me/6281553472658?text=Halo%20Admin,%20saya%20ingin%20membeli%20akses%20Kalkulator%20Shopee" target="_blank"><button style="background-color:#25D366; color:white; border:none; padding:10px 20px; border-radius:10px; cursor:pointer;">Hubungi Admin via WhatsApp</button></a>', unsafe_allow_html=True)
    st.stop()

# 3. Jika Password Benar, Tampilkan Aplikasi Utama Anda
html_code = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
        :root { --shopee-orange: #EE4D2D; --bg: #f4f4f7; --success: #26aa99; }
        body { font-family: 'Inter', sans-serif; background: var(--bg); display: flex; justify-content: center; padding: 10px; margin: 0; }
        .card { background: white; width: 100%; max-width: 480px; border-radius: 24px; box-shadow: 0 15px 35px rgba(0,0,0,0.1); overflow: hidden; margin-bottom: 50px; }
        .header { background: linear-gradient(135deg, #f53d2d, #ff6433); color: white; padding: 25px 20px; text-align: center; }
        .content { padding: 20px; }
        label { display: block; font-size: 10px; font-weight: 800; color: #888; margin-bottom: 8px; text-transform: uppercase; }
        input, select { width: 100%; padding: 14px; border: 2px solid #eee; border-radius: 14px; font-size: 14px; box-sizing: border-box; margin-bottom: 15px; font-weight: 600; }
        .btn-main { width: 100%; background: var(--shopee-orange); color: white; border: none; padding: 18px; border-radius: 14px; font-size: 16px; font-weight: 700; cursor: pointer; box-shadow: 0 4px 15px rgba(238, 77, 45, 0.3); }
        .result-area { display: none; margin-top: 25px; }
        .price-tag { text-align: center; background: #e6f7f4; padding: 20px; border-radius: 18px; margin-bottom: 20px; border: 1px solid #b3e5dc; }
        .suggested-price { display: block; font-size: 32px; font-weight: 800; color: var(--success); }
        .wa-float { position: fixed; bottom: 20px; right: 20px; background: #25D366; color: white; padding: 12px 20px; border-radius: 50px; font-weight: 700; text-decoration: none; box-shadow: 0 4px 10px rgba(0,0,0,0.2); font-size: 14px; display: flex; align-items: center; z-index: 999; }
    </style>
</head>
<body>
<div class="card">
    <div class="header">
        <h1 style="margin:0; font-size: 20px;">Shopee Pricing Assistant</h1>
        <p style="margin:5px 0 0; font-size: 11px; opacity: 0.9;">Official Reseller Tool 2025</p>
    </div>
    <div class="content">
        <label>MODAL PRODUK (RP)</label>
        <input type="text" id="hppInput" placeholder="Contoh: 50.000" oninput="formatRupiah(this)">
        <label>TARGET PROFIT (%)</label>
        <input type="number" id="targetProfit" value="20">
        <button class="btn-main" onclick="hitungHarga()">HITUNG HARGA SEKARANG</button>
        <div id="resultArea" class="result-area">
            <div class="price-tag">
                <span style="font-size: 11px; color: #666;">HARGA JUAL IDEAL:</span>
                <span class="suggested-price" id="resHargaJual"></span>
            </div>
            <p style="font-size: 12px; color: #888; text-align: center;">Gunakan strategi harga coret untuk hasil maksimal.</p>
        </div>
    </div>
</div>

<a href="https://wa.me/6281553472658?text=Halo%20Admin,%20saya%20butuh%20bantuan%20mengenai%20kalkulator%20ini" class="wa-float" target="_blank">
    💬 Tanya Admin
</a>

<script>
    function formatRupiah(el) {
        let val = el.value.replace(/[^,\d]/g, '').toString();
        let split = val.split(',');
        let sisa = split[0].length % 3;
        let rupiah = split[0].substr(0, sisa);
        let ribuan = split[0].substr(sisa).match(/\d{3}/gi);
        if (ribuan) { let separator = sisa ? '.' : ''; rupiah += separator + ribuan.join('.'); }
        el.value = rupiah;
    }
    function hitungHarga() {
        const hppRaw = document.getElementById('hppInput').value.replace(/\./g, '');
        const hpp = parseFloat(hppRaw);
        const profit = parseFloat(document.getElementById('targetProfit').value) / 100;
        if (!hpp) return;
        let hargaJual = (hpp + (hpp * profit) + 1250) / 0.85; // Estimasi potongan rata-rata 15%
        hargaJual = Math.ceil(hargaJual / 100) * 100;
        document.getElementById('resultArea').style.display = 'block';
        document.getElementById('resHargaJual').innerText = "Rp " + hargaJual.toLocaleString('id-ID');
    }
</script>
</body>
</html>
"""

components.html(html_code, height=900, scrolling=True)
