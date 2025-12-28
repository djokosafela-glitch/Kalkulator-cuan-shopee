import streamlit as st
import streamlit.components.v1 as components

# 1. Konfigurasi Dasar
st.set_page_config(page_title="Shopee Smart Pricing 2025", page_icon="🧡", layout="centered")

# CSS UNTUK LOGIN & BACKGROUND
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Background Gradasi Oranye - Kuning */
    .stApp {
        background: linear-gradient(135deg, #FFB800 0%, #FF4D00 100%);
        background-size: cover;
    }
    
    /* Login Card Solid & Center */
    .login-card {
        background: #ffffff;
        border-radius: 25px;
        padding: 50px 40px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        text-align: center;
        max-width: 400px;
        margin: 100px auto;
    }

    /* Ikon Profil Bulat Solid */
    .user-icon {
        width: 90px;
        height: 90px;
        background: #222;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: -95px auto 25px auto;
        border: 6px solid #FFB800;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    }

    /* Input Password */
    div[data-baseweb="input"] input {
        color: #000 !important;
        text-align: center;
        font-size: 18px;
        font-weight: bold;
    }
    
    .login-title {
        font-weight: 900;
        color: #333;
        margin-bottom: 15px;
        font-size: 24px;
        letter-spacing: -0.5px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Logika Login
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    col1, col2, col3 = st.columns([0.05, 0.9, 0.05])
    with col2:
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        st.markdown('<div class="user-icon"><svg width="45" height="45" viewBox="0 0 24 24" fill="white"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg></div>', unsafe_allow_html=True)
        st.markdown('<div class="login-title">PRICING CALCULATOR</div>', unsafe_allow_html=True)
        st.markdown('<p style="color:#777; font-size:14px; margin-bottom:25px;">Masukkan kode akses premium untuk menghitung profit.</p>', unsafe_allow_html=True)
        
        pwd = st.text_input("", type="password", placeholder="PASSWORD")
        
        if st.button("MASUK KE KALKULATOR", use_container_width=True):
            if pwd == "cuan2025":
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("Akses Ditolak!")
        
        st.markdown('<p style="font-size:12px; color:#FF4D00; font-weight:700; margin-top:30px;">"Makin tahu cuanmu, makin menyala suksesmu!"</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# 3. KODE DASHBOARD UTAMA (VERSI HTML FULL POWER - KATEGORI LENGKAP)
html_full = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
        body { font-family: 'Inter', sans-serif; background: #f0f2f5; padding: 15px; margin: 0; display: flex; justify-content: center; }
        .card { background: white; width: 100%; max-width: 480px; border-radius: 24px; box-shadow: 0 15px 40px rgba(0,0,0,0.12); overflow: hidden; }
        .header { background: linear-gradient(135deg, #FF9900, #FF4D00); color: white; padding: 30px 20px; text-align: center; }
        .content { padding: 25px; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }
        label { display: block; font-size: 11px; font-weight: 800; color: #888; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px; }
        input, select { width: 100%; padding: 15px; border: 2px solid #eee; border-radius: 14px; font-size: 14px; margin-bottom: 20px; box-sizing: border-box; font-weight: 600; transition: 0.3s; }
        input:focus { border-color: #FF4D00; outline: none; }
        .btn-calc { width: 100%; background: #FF4D00; color: white; border: none; padding: 20px; border-radius: 16px; font-size: 16px; font-weight: 800; cursor: pointer; box-shadow: 0 8px 20px rgba(255, 77, 0, 0.3); }
        
        .result-area { display: none; margin-top: 30px; animation: slideUp 0.5s ease; }
        .price-box { background: #fff9f0; border: 1.5px solid #ffe8cc; border-radius: 20px; padding: 25px; text-align: center; margin-bottom: 20px; }
        .price-val { font-size: 36px; font-weight: 800; color: #FF4D00; }
        .detail-card { background: #fafafa; border-radius: 15px; padding: 20px; border: 1px solid #eee; margin-bottom: 25px; }
        .detail-row { display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 10px; color: #444; }
        .strat-box { background: white; border-left: 5px solid #FF9900; padding: 15px; border-radius: 12px; font-size: 13px; margin-bottom: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }
        .wa-float { position: fixed; bottom: 25px; right: 25px; background: #25D366; color: white; padding: 15px 25px; border-radius: 50px; text-decoration: none; font-weight: 800; box-shadow: 0 10px 20px rgba(0,0,0,0.2); z-index: 1000; display: flex; align-items: center; gap: 10px; }
        @keyframes slideUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body>
<div class="card">
    <div class="header">
        <h2 style="margin:0; font-size: 22px;">Shopee Pricing Assistant</h2>
        <p style="margin:5px 0 0; font-size: 12px; opacity: 0.85;">Smart Calculator & Strategy 2025</p>
    </div>
    <div class="content">
        <label>Modal Produk / HPP (RP)</label>
        <input type="text" id="hpp" placeholder="Contoh: 100.000" oninput="formatRp(this)">
        
        <div class="grid">
            <div><label>Target Profit (%)</label><input type="number" id="profit" value="20"></div>
            <div><label>Affiliate (%)</label><input type="number" id="aff" value="5"></div>
        </div>

        <label>Rencana Voucher Toko</label>
        <select id="vch">
            <option value="0">0% (Tanpa Voucher)</option>
            <option value="0.03">Diskon 3%</option>
            <option value="0.05">Diskon 5%</option>
            <option value="0.10">Diskon 10%</option>
        </select>

        <label>Kategori Produk (Grup Admin)</label>
        <select id="kat">
            <option value="0.08">Grup A (Fashion, Kecantikan, Aksesoris HP - 8.0%)</option>
            <option value="0.075">Grup B (Elektronik, Otomotif, Olahraga - 7.5%)</option>
            <option value="0.06">Grup C (Hobi, Alat Musik, Perlengkapan Rumah - 6.0%)</option>
            <option value="0.04">Grup D (FMCG, Makanan & Minuman - 4.0%)</option>
            <option value="0.025">Grup E (Bahan Makanan Segar, Sembako - 2.5%)</option>
        </select>

        <label>Program Promosi Shopee</label>
        <select id="prog">
            <option value="0.085">Gratis Ongkir XTRA + Cashback XTRA (8.5%)</option>
            <option value="0.04">Hanya Gratis Ongkir XTRA (4.0%)</option>
            <option value="0">Tidak Ikut Program (0%)</option>
        </select>

        <button class="btn-calc" onclick="hitung()">HITUNG HARGA REKOMENDASI</button>

        <div id="result" class="result-area">
            <div class="price-box">
                <div style="font-size: 11px; font-weight: 800; color: #888; margin-bottom: 5px;">HARGA JUAL IDEAL</div>
                <div class="price-val" id="resPrice"></div>
            </div>
            <div class="detail-card">
                <div class="detail-row"><span>Potongan Admin + XTRA:</span><span id="resAdmin"></span></div>
                <div class="detail-row"><span>Affiliate (+PPN 11%):</span><span id="resAff"></span></div>
                <div class="detail-row"><span>Potongan Voucher Toko:</span><span id="resVch"></span></div>
                <div class="detail-row"><span>Biaya Proses Fix (Per Order):</span><span>-Rp 1.250</span></div>
                <div class="detail-row" style="border-top: 1.5px solid #eee; padding-top: 10px; margin-top: 10px; font-weight: 800; color: #FF4D00;">
                    <span>Profit Bersih (Cuan):</span><span id="resCuan"></span>
                </div>
            </div>
            <div id="stratList"></div>
        </div>
    </div>
</div>

<a href="https://wa.me/6281553472658" class="wa-float" target="_blank">💬 Konsultasi Admin</a>

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

    function hitung() {
        const hpp = parseFloat(document.getElementById('hpp').value.replace(/\./g, ''));
        if(!hpp) { alert("Masukkan modal dulu!"); return; }
        
        const target = parseFloat(document.getElementById('profit').value) / 100;
        const affRate = (parseFloat(document.getElementById('aff').value) / 100) * 1.11;
        const vchRate = parseFloat(document.getElementById('vch').value);
        const katRate = parseFloat(document.getElementById('kat').value);
        const progRate = parseFloat(document.getElementById('prog').value);
        
        const totalTax = katRate + progRate + vchRate + affRate;
        let jual = (hpp + (hpp * target) + 1250) / (1 - totalTax);
        jual = Math.ceil(jual / 100) * 100;

        const adminNominal = jual * (katRate + progRate);
        const affNominal = jual * affRate;
        const vchNominal = jual * vchRate;
        const cuan = jual - adminNominal - affNominal - vchNominal - 1250 - hpp;

        document.getElementById('result').style.display = 'block';
        document.getElementById('resPrice').innerText = "Rp " + jual.toLocaleString('id-ID');
        document.getElementById('resAdmin').innerText = "-Rp " + Math.round(adminNominal).toLocaleString('id-ID');
        document.getElementById('resAff').innerText = "-Rp " + Math.round(affNominal).toLocaleString('id-ID');
        document.getElementById('resVch').innerText = "-Rp " + Math.round(vchNominal).toLocaleString('id-ID');
        document.getElementById('resCuan').innerText = "Rp " + Math.round(cuan).toLocaleString('id-ID');

        const coret = Math.ceil((jual * 1.3) / 100) * 100;
        document.getElementById('stratList').innerHTML = `
            <div class="strat-box">🚀 <b>Strategi Affiliate:</b> Berikan komisi menarik untuk kreator karena margin sudah aman di harga ini.</div>
            <div class="strat-box">🏷️ <b>Harga Coret:</b> Pasang harga Rp ` + coret.toLocaleString('id-ID') + ` di Seller Centre agar diskon terlihat besar.</div>
            <div class="strat-box">📦 <b>Optimasi Produk:</b> Gunakan bundle paket isi 3 untuk mengefisiensi biaya admin tetap Shopee.</div>
            <div class="strat-box">🎟️ <b>Voucher Toko:</b> Aktifkan voucher diskon ${vchRate*100}% untuk meningkatkan klik pada hasil pencarian.</div>
            <div class="strat-box">💡 <b>SEO Judul:</b> Pastikan judul mengandung kata kunci volume tinggi agar performa organik naik.</div>
        `;
    }
</script>
</body>
</html>
"""

components.html(html_full, height=1500, scrolling=True)
