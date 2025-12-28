import streamlit as st
import streamlit.components.v1 as components

# 1. Konfigurasi Halaman & Meta Data
st.set_page_config(page_title="Shopee Smart Pricing 2025", page_icon="🧡", layout="centered")

# CSS UNTUK LOGIN GLASSMORPHISM & UI UTAMA
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Background Gradient Aesthetic */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-size: cover;
    }
    
    /* Container Login */
    .login-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding-top: 80px;
    }

    /* Ikon Profil Bulat (Sesuai Referensi) */
    .profile-circle {
        width: 90px;
        height: 90px;
        background: #2d3436;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: -45px;
        z-index: 10;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        border: 4px solid rgba(255,255,255,0.1);
    }

    /* Kotak Login Glassmorphism */
    .glass-box {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 35px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        padding: 60px 40px 40px 40px;
        width: 100%;
        max-width: 380px;
        box-shadow: 0 25px 50px rgba(0,0,0,0.2);
        text-align: center;
    }

    /* Input Styling agar Teks Terlihat */
    div[data-baseweb="input"] {
        background-color: rgba(0, 0, 0, 0.2) !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
    }
    
    div[data-baseweb="input"] input {
        color: white !important;
        font-weight: 600 !important;
    }

    /* Tombol Login Putih Elegan */
    .stButton>button {
        background: white !important;
        color: #667eea !important;
        border-radius: 12px !important;
        font-weight: 800 !important;
        border: none !important;
        height: 50px;
        transition: 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }

    .login-title {
        color: white;
        font-weight: 800;
        font-size: 20px;
        margin-bottom: 25px;
        letter-spacing: 1px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Logika Authentikasi
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.markdown('<div class="login-wrapper">', unsafe_allow_html=True)
    
    # Elemen Ikon Profil
    st.markdown('''
        <div class="profile-circle">
            <svg width="45" height="45" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                <circle cx="12" cy="7" r="4"></circle>
            </svg>
        </div>
    ''', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="glass-box">', unsafe_allow_html=True)
        st.markdown('<div class="login-title">PRICING CALCULATOR</div>', unsafe_allow_html=True)
        
        pwd = st.text_input("", type="password", placeholder="Masukkan Password Akses")
        
        if st.button("LOGIN TO DASHBOARD", use_container_width=True):
            if pwd == "cuan2025":
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("Password Salah!")
        
        st.markdown('<p style="font-size:12px; color:white; margin-top:20px; opacity:0.8;">"Makin tahu cuanmu, makin menyala peluang suksesmu!"</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# 3. DASHBOARD UTAMA (FULL HTML INTEGRATION)
html_dashboard = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
        body { font-family: 'Inter', sans-serif; background: #f0f2f5; margin: 0; padding: 15px; display: flex; justify-content: center; }
        .card { background: white; width: 100%; max-width: 480px; border-radius: 24px; box-shadow: 0 10px 40px rgba(0,0,0,0.1); overflow: hidden; }
        .header { background: linear-gradient(135deg, #f53d2d, #ff6433); color: white; padding: 30px 20px; text-align: center; }
        .content { padding: 25px; }
        .grid-inputs { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }
        label { display: block; font-size: 11px; font-weight: 800; color: #888; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px; }
        input, select { width: 100%; padding: 14px; border: 2px solid #eee; border-radius: 12px; font-size: 14px; margin-bottom: 15px; box-sizing: border-box; font-weight: 600; }
        .calculate-btn { width: 100%; background: #EE4D2D; color: white; border: none; padding: 18px; border-radius: 15px; font-size: 16px; font-weight: 800; cursor: pointer; transition: 0.3s; box-shadow: 0 8px 20px rgba(238, 77, 45, 0.2); }
        .result-section { display: none; margin-top: 30px; animation: fadeIn 0.5s ease; }
        .price-tag { background: #e6f7f4; border: 1px solid #b3e5dc; border-radius: 20px; padding: 25px; text-align: center; margin-bottom: 20px; }
        .price-text { display: block; font-size: 34px; font-weight: 800; color: #26aa99; }
        .fee-breakdown { background: #fafafa; border-radius: 15px; padding: 20px; border: 1px solid #eee; margin-bottom: 25px; }
        .fee-row { display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 10px; color: #555; }
        .strategy-card { background: white; border-left: 5px solid #EE4D2D; border-radius: 12px; padding: 15px; margin-bottom: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); font-size: 13px; }
        .wa-button { position: fixed; bottom: 25px; right: 25px; background: #25D366; color: white; padding: 15px 25px; border-radius: 50px; text-decoration: none; font-weight: 800; box-shadow: 0 10px 25px rgba(0,0,0,0.2); z-index: 1000; display: flex; align-items: center; gap: 10px; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body>
<div class="card">
    <div class="header">
        <h2 style="margin:0; font-size: 22px;">Shopee Smart Pricing Pro</h2>
        <p style="margin:5px 0 0; font-size: 12px; opacity: 0.8;">Admin, Affiliate & Tax Calculator 2025</p>
    </div>
    <div class="content">
        <label>Modal Produk / HPP (RP)</label>
        <input type="text" id="hppInput" placeholder="Contoh: 100.000" oninput="formatRupiah(this)">
        
        <div class="grid-inputs">
            <div>
                <label>Target Profit (%)</label>
                <input type="number" id="profitInput" value="20">
            </div>
            <div>
                <label>Affiliate (%)</label>
                <input type="number" id="affiliateInput" value="5">
            </div>
        </div>

        <label>Voucher Toko & Kategori</label>
        <div class="grid-inputs">
            <select id="vchInput">
                <option value="0">Voucher 0%</option>
                <option value="0.05">Voucher 5%</option>
                <option value="0.10">Voucher 10%</option>
            </select>
            <select id="katInput">
                <option value="0.08">Grup A (8%)</option>
                <option value="0.06">Grup C (6%)</option>
                <option value="0.04">Grup D (4%)</option>
            </select>
        </div>

        <label>Program Promosi Shopee</label>
        <select id="progInput">
            <option value="0.085">Gratis Ongkir + Cashback XTRA (8.5%)</option>
            <option value="0.04">Gratis Ongkir XTRA (4%)</option>
            <option value="0">Tidak Ikut Program</option>
        </select>

        <button class="calculate-btn" onclick="processData()">REKOMENDASIKAN HARGA</button>

        <div id="resultArea" class="result-section">
            <div class="price-tag">
                <span style="font-size: 11px; font-weight: 800; color: #666;">HARGA JUAL IDEAL</span>
                <span class="price-text" id="resPrice"></span>
            </div>
            <div class="fee-breakdown">
                <div class="fee-row"><span>Admin Shopee:</span> <span id="resAdmin"></span></div>
                <div class="fee-row"><span>Affiliate (+PPN 11%):</span> <span id="resAff"></span></div>
                <div class="fee-row"><span>Potongan Voucher:</span> <span id="resVch"></span></div>
                <div class="fee-row" style="color:#26aa99; font-weight:800; border-top:1px solid #eee; padding-top:10px; margin-top:5px;">
                    <span>Net Profit:</span> <span id="resCuan"></span>
                </div>
            </div>
            <div id="stratContainer"></div>
        </div>
    </div>
</div>

<a href="https://wa.me/6281553472658" class="wa-button" target="_blank">💬 Chat Admin</a>

<script>
    function formatRupiah(el) {
        let val = el.value.replace(/[^,\d]/g, '').toString();
        let split = val.split(',');
        let sisa = split[0].length % 3;
        let rp = split[0].substr(0, sisa);
        let ribu = split[0].substr(sisa).match(/\d{3}/gi);
        if (ribu) { let sep = sisa ? '.' : ''; rp += sep + ribu.join('.'); }
        el.value = rp;
    }

    function processData() {
        const hpp = parseFloat(document.getElementById('hppInput').value.replace(/\./g, ''));
        if(!hpp) return;
        
        const profit = parseFloat(document.getElementById('profitInput').value) / 100;
        const affiliate = (parseFloat(document.getElementById('affiliateInput').value) / 100) * 1.11;
        const voucher = parseFloat(document.getElementById('vchInput').value);
        const kategori = parseFloat(document.getElementById('katInput').value);
        const program = parseFloat(document.getElementById('progInput').value);
        
        const totalFeeRate = kategori + program + voucher + affiliate;
        let jual = (hpp + (hpp * profit) + 1250) / (1 - totalFeeRate);
        jual = Math.ceil(jual / 100) * 100;

        const adminNominal = jual * (kategori + program);
        const affNominal = jual * affiliate;
        const vchNominal = jual * voucher;
        const finalCuan = jual - adminNominal - affNominal - vchNominal - 1250 - hpp;

        document.getElementById('resultArea').style.display = 'block';
        document.getElementById('resPrice').innerText = "Rp " + jual.toLocaleString('id-ID');
        document.getElementById('resAdmin').innerText = "-Rp " + Math.round(adminNominal).toLocaleString('id-ID');
        document.getElementById('resAff').innerText = "-Rp " + Math.round(affNominal).toLocaleString('id-ID');
        document.getElementById('resVch').innerText = "-Rp " + Math.round(vchNominal).toLocaleString('id-ID');
        document.getElementById('resCuan').innerText = "Rp " + Math.round(finalCuan).toLocaleString('id-ID');

        document.getElementById('stratContainer').innerHTML = `
            <div class="strategy-card">🚀 <b>Push Affiliate:</b> Komisi aman, segera hubungi kreator!</div>
            <div class="strat-item">📈 <b>Harga Coret:</b> Set di Rp ` + (Math.ceil(jual*1.3/100)*100).toLocaleString('id-ID') + `</div>
        `;
    }
</script>
</body>
</html>
"""

components.html(html_dashboard, height=1500, scrolling=True)
