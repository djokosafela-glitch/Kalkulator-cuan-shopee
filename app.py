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
        background: linear-gradient(135deg, #FF9900 0%, #FF4D00 100%);
        background-size: cover;
    }
    
    /* Login Box Solid & Center */
    .login-card {
        background: #ffffff;
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        text-align: center;
        max-width: 400px;
        margin: auto;
    }

    /* Ikon Profil Bulat Solid */
    .user-icon {
        width: 80px;
        height: 80px;
        background: #333;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: -80px auto 20px auto;
        border: 5px solid #FF9900;
    }

    /* Input Password Hitam di Putih */
    div[data-baseweb="input"] input {
        color: #000 !important;
        text-align: center;
        font-size: 18px;
    }
    
    .login-title {
        font-weight: 800;
        color: #333;
        margin-bottom: 10px;
        font-size: 22px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Logika Login
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.write("##")
    st.write("##")
    col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
    with col2:
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        st.markdown('<div class="user-icon"><svg width="40" height="40" viewBox="0 0 24 24" fill="white"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg></div>', unsafe_allow_html=True)
        st.markdown('<div class="login-title">PRICING CALCULATOR</div>', unsafe_allow_html=True)
        st.markdown('<p style="color:#666; font-size:14px; margin-bottom:20px;">Silakan masukkan kode akses untuk memulai analisa profit Anda.</p>', unsafe_allow_html=True)
        
        pwd = st.text_input("", type="password", placeholder="PASSWORD")
        
        if st.button("LOGIN SEKARANG", use_container_width=True):
            if pwd == "cuan2025":
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("Akses Ditolak!")
        
        st.markdown('<p style="font-size:12px; color:#FF4D00; font-weight:bold; margin-top:20px;">"Makin tahu cuanmu, makin menyala peluang suksesmu!"</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# 3. KODE DASHBOARD UTAMA (VERSI HTML LENGKAP)
html_full = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
        body { font-family: 'Inter', sans-serif; background: #f4f4f7; padding: 15px; margin: 0; display: flex; justify-content: center; }
        .card { background: white; width: 100%; max-width: 480px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); overflow: hidden; }
        .header { background: linear-gradient(135deg, #FF9900, #FF4D00); color: white; padding: 25px; text-align: center; }
        .content { padding: 20px; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
        label { display: block; font-size: 10px; font-weight: 800; color: #999; margin-bottom: 6px; text-transform: uppercase; }
        input, select { width: 100%; padding: 12px; border: 1.5px solid #eee; border-radius: 12px; font-size: 14px; margin-bottom: 15px; box-sizing: border-box; font-weight: 600; color: #333; }
        .btn-calc { width: 100%; background: #FF4D00; color: white; border: none; padding: 16px; border-radius: 12px; font-size: 15px; font-weight: 800; cursor: pointer; box-shadow: 0 5px 15px rgba(255, 77, 0, 0.3); }
        
        .result-area { display: none; margin-top: 25px; }
        .price-box { background: #fff9f0; border: 1px solid #ffe8cc; border-radius: 15px; padding: 20px; text-align: center; margin-bottom: 15px; }
        .price-val { font-size: 32px; font-weight: 800; color: #FF4D00; }
        .detail-card { background: #fafafa; border-radius: 12px; padding: 15px; border: 1px solid #eee; margin-bottom: 20px; }
        .detail-row { display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 8px; }
        .strat-box { background: white; border-left: 4px solid #FF9900; padding: 12px; border-radius: 8px; font-size: 12px; margin-bottom: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
        .wa-float { position: fixed; bottom: 20px; right: 20px; background: #25D366; color: white; padding: 12px 20px; border-radius: 50px; text-decoration: none; font-weight: 700; box-shadow: 0 4px 15px rgba(0,0,0,0.2); z-index: 999; }
    </style>
</head>
<body>
<div class="card">
    <div class="header">
        <h2 style="margin:0; font-size: 18px;">Shopee Pricing Assistant</h2>
        <p style="margin:5px 0 0; font-size: 10px; opacity: 0.9;">Update Kebijakan & Biaya Admin 2025</p>
    </div>
    <div class="content">
        <label>Modal Produk / HPP (RP)</label>
        <input type="text" id="hpp" placeholder="Contoh: 50.000" oninput="formatRp(this)">
        
        <div class="grid">
            <div><label>Target Profit (%)</label><input type="number" id="profit" value="20"></div>
            <div><label>Affiliate (%)</label><input type="number" id="aff" value="5"></div>
        </div>

        <label>Rencana Voucher Toko</label>
        <select id="vch">
            <option value="0">Tanpa Voucher (0%)</option>
            <option value="0.05">Voucher Diskon 5%</option>
            <option value="0.10">Voucher Diskon 10%</option>
        </select>

        <label>Kategori Produk</label>
        <select id="kat">
            <option value="0.08">Grup A (Fashion, Kecantikan - 8%)</option>
            <option value="0.075">Grup B (Elektronik - 7.5%)</option>
            <option value="0.06">Grup C (Hobi, Alat Musik - 6%)</option>
            <option value="0.04">Grup D (FMCG, Makanan - 4%)</option>
        </select>

        <label>Program Promosi Shopee</label>
        <select id="prog">
            <option value="0.085">Gratis Ongkir XTRA + Cashback XTRA (8.5%)</option>
            <option value="0.04">Hanya Gratis Ongkir XTRA (4%)</option>
            <option value="0">Tidak Ikut Program (0%)</option>
        </select>

        <button class="btn-calc" onclick="hitung()">LIHAT REKOMENDASI HARGA</button>

        <div id="result" class="result-area">
            <div class="price-box">
                <div style="font-size: 10px; font-weight: 700; color: #666; margin-bottom: 5px;">REKOMENDASI HARGA JUAL</div>
                <div class="price-val" id="resPrice"></div>
            </div>
            <div class="detail-card">
                <div class="detail-row"><span>Potongan Admin + XTRA:</span><span id="resAdmin"></span></div>
                <div class="detail-row"><span>Biaya Affiliate (+PPN 11%):</span><span id="resAff"></span></div>
                <div class="detail-row"><span>Alokasi Voucher Toko:</span><span id="resVch"></span></div>
                <div class="detail-row"><span>Biaya Proses Fix:</span><span>-Rp 1.250</span></div>
                <div class="detail-row" style="border-top: 1px solid #eee; padding-top: 8px; margin-top: 8px; font-weight: 800; color: #FF4D00;">
                    <span>Profit Bersih Anda:</span><span id="resCuan"></span>
                </div>
            </div>
            <div id="stratList"></div>
        </div>
    </div>
</div>

<a href="https://wa.me/6281553472658" class="wa-float" target="_blank">💬 Chat Admin</a>

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
        if(!hpp) return;
        const target = parseFloat(document.getElementById('profit').value) / 100;
        const affRate = (parseFloat(document.getElementById('aff').value) / 100) * 1.11;
        const vchRate = parseFloat(document.getElementById('vch').value);
        const katRate = parseFloat(document.getElementById('kat').value);
        const progRate = parseFloat(document.getElementById('prog').value);
        
        const totalPotongan = katRate + progRate + vchRate + affRate;
        let jual = (hpp + (hpp * target) + 1250) / (1 - totalPotongan);
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
            <div class="strat-box">🚀 <b>Strategi Affiliate:</b> Berikan komisi ${document.getElementById('aff').value}% untuk menarik influencer.</div>
            <div class="strat-box">🏷️ <b>Harga Coret:</b> Pasang harga Rp ${coret.toLocaleString('id-ID')} lalu coret ke harga rekomendasi.</div>
            <div class="strat-box">📦 <b>Paket Hemat:</b> Jual bundle isi 2 untuk menghemat biaya fix Rp 1.250.</div>
            <div class="strat-box">🎟️ <b>Voucher:</b> Aktifkan voucher toko saat ada event 2.2, 3.3 untuk naikkan konversi.</div>
            <div class="strat-box">💡 <b>Optimasi:</b> Gunakan kata kunci SEO yang tepat di judul produk Anda.</div>
        `;
    }
</script>
</body>
</html>
"""

components.html(html_full, height=1400, scrolling=True)
