import streamlit as st
import streamlit.components.v1 as components

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Shopee Smart Pricing Pro", page_icon="🧡", layout="centered")

# CSS untuk Login Page & Perbaikan Glassmorphism
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Background Full Page */
    .stApp {
        background: url("https://images.unsplash.com/photo-1557683316-973673baf926?q=80&w=2029&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
    }
    
    /* Perbaikan Kotak Glassmorphism */
    .login-container {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 30px;
        padding: 40px 25px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        text-align: center;
        margin-top: 30px;
    }

    /* Penyesuaian Logo agar terlihat */
    .shopee-logo {
        margin-bottom: 20px;
        filter: drop-shadow(0px 4px 4px rgba(0,0,0,0.2));
    }

    .slogan-text {
        color: white;
        font-size: 15px;
        font-style: italic;
        margin-top: 25px;
        line-height: 1.4;
        text-shadow: 1px 1px 5px rgba(0,0,0,0.5);
    }

    /* Input Styling di Login */
    .stTextInput input {
        background: rgba(255, 255, 255, 0.9) !important;
        border-radius: 12px !important;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Logika Login
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    # Layout tengah untuk login
    _, col_mid, _ = st.columns([0.1, 0.8, 0.1])
    
    with col_mid:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        # Menampilkan Logo Shopee dengan benar
        st.image("https://upload.wikimedia.org/wikipedia/commons/f/fe/Shopee.svg", width=100)
        st.markdown("<h1 style='color:white; font-size:24px; margin-bottom:20px;'>Premium Access</h1>", unsafe_allow_html=True)
        
        pwd = st.text_input("PASSWORD AKSES", type="password", placeholder="Masukkan kode...")
        
        if st.button("MULAI ANALISA CUAN", use_container_width=True):
            if pwd == "cuan2025":
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("Password Salah!")
        
        st.markdown('<p class="slogan-text">"Makin tahu cuanmu, makin menyala peluang suksesmu!"</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# 3. KODE APLIKASI UTAMA (Fitur Lengkap Sesuai Permintaan)
html_app = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
        body { font-family: 'Inter', sans-serif; background: #f4f4f7; padding: 15px; margin: 0; display: flex; justify-content: center; }
        .card { background: white; width: 100%; max-width: 450px; border-radius: 28px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); overflow: hidden; }
        .header { background: linear-gradient(135deg, #f53d2d, #ff6433); color: white; padding: 30px 20px; text-align: center; }
        .content { padding: 25px; }
        .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }
        label { display: block; font-size: 11px; font-weight: 800; color: #888; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px; }
        input, select { width: 100%; padding: 15px; border: 2px solid #eee; border-radius: 15px; font-size: 14px; box-sizing: border-box; margin-bottom: 20px; font-weight: 600; transition: 0.3s; }
        input:focus { border-color: #EE4D2D; outline: none; }
        .btn-calc { width: 100%; background: #EE4D2D; color: white; border: none; padding: 20px; border-radius: 16px; font-size: 16px; font-weight: 800; cursor: pointer; box-shadow: 0 10px 20px rgba(238, 77, 45, 0.2); }
        .result-box { display: none; margin-top: 30px; animation: slideUp 0.5s ease; }
        .price-display { text-align: center; background: #e6f7f4; padding: 25px; border-radius: 20px; border: 1px solid #b3e5dc; margin-bottom: 20px; }
        .price-val { display: block; font-size: 36px; font-weight: 800; color: #26aa99; }
        .fee-card { background: #fafafa; padding: 15px; border-radius: 15px; border: 1px solid #eee; font-size: 13px; }
        .fee-item { display: flex; justify-content: space-between; margin-bottom: 8px; color: #555; }
        .strat-card { background: white; border-left: 5px solid #EE4D2D; padding: 15px; border-radius: 12px; font-size: 13px; margin-top: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }
        .wa-btn { position: fixed; bottom: 25px; right: 25px; background: #25D366; color: white; padding: 15px 25px; border-radius: 50px; text-decoration: none; font-weight: bold; box-shadow: 0 10px 20px rgba(0,0,0,0.2); z-index: 9999; display: flex; align-items: center; gap: 8px; }
        @keyframes slideUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body>
<div class="card">
    <div class="header">
        <h2 style="margin:0; font-size: 22px;">Shopee Pricing Pro</h2>
        <p style="margin:5px 0 0; font-size: 12px; opacity: 0.8;">Smart Profit Calculator 2025</p>
    </div>
    <div class="content">
        <label>Modal Produk / HPP (Rp)</label>
        <input type="text" id="hpp" placeholder="Contoh: 100.000" oninput="formatRp(this)">
        
        <div class="grid-2">
            <div>
                <label>Target Profit (%)</label>
                <input type="number" id="profit" value="20">
            </div>
            <div>
                <label>Voucher Toko (%)</label>
                <select id="vch">
                    <option value="0">0%</option>
                    <option value="0.03">3%</option>
                    <option value="0.05">5%</option>
                    <option value="0.10">10%</option>
                </select>
            </div>
        </div>

        <label>Kategori Produk & Program</label>
        <select id="kat">
            <option value="0.08">Grup A (Fashion/Beauty - 8%)</option>
            <option value="0.075">Grup B (Home/Electronic - 7.5%)</option>
            <option value="0.06">Grup C (Hobby/Tools - 6%)</option>
        </select>
        <select id="prog">
            <option value="0">Tanpa Program XTRA</option>
            <option value="0.04">Gratis Ongkir XTRA (4%)</option>
            <option value="0.085">Gratis Ongkir + Cashback (8.5%)</option>
        </select>

        <button class="btn-calc" onclick="calculate()">HITUNG HARGA JUAL IDEAL</button>

        <div id="result" class="result-box">
            <div class="price-display">
                <span style="font-size: 11px; font-weight: 800; color: #666;">HARGA JUAL REKOMENDASI</span>
                <span class="price-val" id="resPrice"></span>
            </div>
            <div class="fee-card">
                <div class="fee-item"><span>Estimasi Admin Shopee:</span> <span id="resFee"></span></div>
                <div class="fee-item"><span>Alokasi Voucher:</span> <span id="resVch"></span></div>
                <div class="fee-item"><span>Biaya Layanan Fix:</span> <span>Rp 1.250</span></div>
                <div class="fee-item" style="color: #26aa99; font-weight: 800; border-top: 1px solid #eee; padding-top: 10px; margin-top: 5px;">
                    <span>Profit Bersih Anda:</span> <span id="resCuan"></span>
                </div>
            </div>
            <div class="strat-card"><strong>💡 Strategi:</strong> Gunakan harga coret 25% lebih tinggi dari hasil di atas agar terlihat sebagai diskon besar bagi pembeli.</div>
        </div>
    </div>
</div>

<a href="https://wa.me/6281553472658?text=Halo%20Admin,%20saya%20ingin%20konsultasi%20kalkulator%20Shopee" class="wa-btn" target="_blank">
    <span>💬 Chat Admin</span>
</a>

<script>
    function formatRp(el) {
        let val = el.value.replace(/[^,\d]/g, '').toString();
        let split = val.split(',');
        let sisa = split[0].length % 3;
        let rp = split[0].substr(0, sisa);
        let ribu = split[0].substr(sisa).match(/\d{3}/gi);
        if (ribu) { let sep = sisa ? '.' : ''; rp += sep + ribu.join('.'); }
        el.value = rp;
    }

    function calculate() {
        const hpp = parseFloat(document.getElementById('hpp').value.replace(/\./g, ''));
        const target = parseFloat(document.getElementById('profit').value) / 100;
        const vchRate = parseFloat(document.getElementById('vch').value);
        const katRate = parseFloat(document.getElementById('kat').value);
        const progRate = parseFloat(document.getElementById('prog').value);
        
        if(!hpp) { alert("Masukkan modal dulu!"); return; }
        
        const totalPotongan = katRate + progRate + vchRate;
        let jual = (hpp + (hpp * target) + 1250) / (1 - totalPotongan);
        jual = Math.ceil(jual / 100) * 100;

        const fee = jual * (katRate + progRate);
        const vchNominal = jual * vchRate;
        const cuan = jual - fee - vchNominal - 1250 - hpp;

        document.getElementById('result').style.display = 'block';
        document.getElementById('resPrice').innerText = "Rp " + jual.toLocaleString('id-ID');
        document.getElementById('resFee').innerText = "-Rp " + Math.round(fee).toLocaleString('id-ID');
        document.getElementById('resVch').innerText = "-Rp " + Math.round(vchNominal).toLocaleString('id-ID');
        document.getElementById('resCuan').innerText = "Rp " + Math.round(cuan).toLocaleString('id-ID');
    }
</script>
</body>
</html>
"""

components.html(html_app, height=1300, scrolling=True)
