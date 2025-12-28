import streamlit as st
import streamlit.components.v1 as components

# 1. Konfigurasi Halaman Dasar
st.set_page_config(
    page_title="Shopee Smart Pricing Pro 2025", 
    page_icon="🧡", 
    layout="centered"
)

# 2. CSS Global untuk Streamlit UI (Hapus elemen standar & styling Login)
st.markdown("""
    <style>
    header {visibility: hidden !important;}
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 0rem !important;
    }
    .stApp {
        background-color: #f4f4f7;
    }
    
    /* Animasi Muncul dari Bawah */
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(50px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .login-container {
        animation: slideUp 0.8s ease-out;
        text-align: center;
        padding: 40px;
        background: white;
        border-radius: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        margin-top: 50px;
    }
    
    .login-header {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        font-size: 28px;
        color: #EE4D2D;
        margin-bottom: 10px;
        line-height: 1.2;
    }
    
    .login-sub {
        font-size: 14px;
        color: #666;
        margin-bottom: 30px;
    }

    /* Styling tombol login streamlit agar senada */
    div.stButton > button:first-child {
        background-color: #EE4D2D;
        color: white;
        border-radius: 12px;
        width: 100%;
        border: none;
        height: 50px;
        font-weight: 700;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Logika Autentikasi
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if not st.session_state['authenticated']:
    # Tampilan Halaman Login
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    st.markdown('<div class="login-header">Hitung Cerdas untuk<br>Jualan Berkualitas</div>', unsafe_allow_html=True)
    st.markdown('<div class="login-sub">Masukkan kata sandi akses premium Anda</div>', unsafe_allow_html=True)
    
    password = st.text_input("Kata Sandi", type="password", placeholder="Ketik di sini...", label_visibility="collapsed")
    
    if st.button("Masuk Sekarang"):
        if password == "cuan2025":
            st.session_state['authenticated'] = True
            st.rerun()
        else:
            st.error("Kata sandi salah. Silakan coba lagi.")
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop() # Hentikan eksekusi kode di bawah jika belum login

# 4. KODE HTML UTAMA (Hanya tampil jika sudah login)
html_code = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
        :root { --shopee-orange: #EE4D2D; --bg: #f4f4f7; --success: #26aa99; --dark: #333; }
        body { font-family: 'Inter', sans-serif; background: var(--bg); display: flex; justify-content: center; padding: 15px; margin: 0; }
        .card { background: white; width: 100%; max-width: 500px; border-radius: 24px; box-shadow: 0 15px 35px rgba(0,0,0,0.1); overflow: hidden; animation: fadeIn 0.5s ease-out; }
        .header { background: linear-gradient(135deg, #f53d2d, #ff6433); color: white; padding: 30px 20px; text-align: center; }
        .content { padding: 25px; }
        
        .grid-input { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }
        label { display: block; font-size: 11px; font-weight: 800; color: #888; margin-bottom: 8px; letter-spacing: 0.5px; text-transform: uppercase; }
        
        input, select { width: 100%; padding: 14px; border: 2px solid #eee; border-radius: 14px; font-size: 14px; box-sizing: border-box; transition: 0.3s; font-weight: 600; margin-bottom: 15px; }
        input:focus { border-color: var(--shopee-orange); outline: none; background: #fffaf9; }
        
        .btn-main { width: 100%; background: var(--shopee-orange); color: white; border: none; padding: 18px; border-radius: 14px; font-size: 16px; font-weight: 700; cursor: pointer; box-shadow: 0 4px 15px rgba(238, 77, 45, 0.3); margin-top: 10px; }
        
        .result-area { display: none; margin-top: 25px; animation: fadeIn 0.5s; }
        .price-tag { text-align: center; background: #fff9f0; padding: 20px; border-radius: 18px; margin-bottom: 20px; border: 2px solid #ffe8cc; }
        .suggested-price { display: block; font-size: 36px; font-weight: 800; color: var(--shopee-orange); }
        
        .fee-breakdown { font-size: 12px; background: #fafafa; padding: 18px; border-radius: 15px; border: 1px solid #eee; margin-bottom: 25px; }
        .fee-row { display: flex; justify-content: space-between; margin-bottom: 8px; color: #555; font-weight: 500; }
        .total-cuan { color: var(--success); font-size: 15px; font-weight: 800; border-top: 1px solid #ddd; padding-top: 10px; margin-top: 10px; }
        
        .strategy-section { border-top: 2px dashed #eee; padding-top: 20px; }
        .strategy-card { background: #fff; border: 1px solid #f0f0f0; border-left: 5px solid var(--shopee-orange); padding: 15px; border-radius: 12px; font-size: 13px; line-height: 1.6; margin-bottom: 12px; display: flex; align-items: flex-start; gap: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); }
        .strat-icon { font-size: 20px; }
        .strat-text strong { color: var(--dark); display: block; margin-bottom: 2px; font-size: 14px; }

        @keyframes fadeIn { from { opacity: 0; transform: translateY(15px); } to { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body>

<div class="card">
    <div class="header">
        <h1 style="margin:0; font-size: 22px; letter-spacing: -0.5px;">Shopee Smart Pricing 2025</h1>
        <p style="margin:5px 0 0; font-size: 11px; opacity: 0.9; font-weight: 600;">Akses Premium: Admin A-E & Affiliate Tax</p>
    </div>

    <div class="content">
        <label>MODAL PRODUK / HPP (RP)</label>
        <input type="text" id="hppInput" placeholder="Contoh: 100.000" oninput="formatRupiah(this)">

        <div class="grid-input">
            <div>
                <label>Target Profit (%)</label>
                <input type="number" id="targetProfit" value="20">
            </div>
            <div>
                <label>Voucher Toko (%)</label>
                <input type="number" id="voucherRate" value="0">
            </div>
        </div>

        <label>KOMISI AFFILIATE (%) <small style="color:red">*PPN 11% Otomatis</small></label>
        <input type="number" id="affiliateRate" value="5" placeholder="Contoh: 5">

        <label>KATEGORI PRODUK (ADMIN)</label>
        <select id="kategori">
            <option value="0.08">Grup A (8.0%) - Fashion, Kecantikan, Aksesoris</option>
            <option value="0.075">Grup B (7.5%) - Elektronik, Rumah Tangga, Otomotif</option>
            <option value="0.06">Grup C (6.0%) - Kamera, Hobi, Olahraga, Mainan</option>
            <option value="0.04">Grup D (4.0%) - Makanan, Minuman, Produk Bayi</option>
            <option value="0.025">Grup E (2.5%) - Sembako, Susu Bayi, Produk Segar</option>
        </select>

        <label>PROGRAM PROMOSI SHOPEE</label>
        <select id="program">
            <option value="0.085">Gratis Ongkir XTRA + Cashback XTRA (8.5%)</option>
            <option value="0.04">Hanya Gratis Ongkir XTRA (4.0%)</option>
            <option value="0">Tanpa Program XTRA (0%)</option>
        </select>

        <button class="btn-main" onclick="hitungHarga()">REKOMENDASIKAN HARGA</button>

        <div id="resultArea" class="result-area">
            <div class="price-tag">
                <span style="font-size: 11px; color: #888; font-weight: 700;">HARGA JUAL REKOMENDASI</span>
                <span class="suggested-price" id="resHargaJual"></span>
            </div>

            <div class="fee-breakdown">
                <div class="fee-row"><span>Fee Admin & Program:</span> <span id="resAdminValue"></span></div>
                <div class="fee-row"><span>Affiliate + PPN 11%:</span> <span id="resAffValue"></span></div>
                <div class="fee-row"><span>Alokasi Voucher:</span> <span id="resVoucherValue"></span></div>
                <div class="fee-row"><span>Biaya Proses Fix:</span> <span>Rp 1.250</span></div>
                <div class="fee-row total-cuan">
                    <span>NET PROFIT:</span> <span id="resCuan"></span>
                </div>
            </div>

            <div class="strategy-section">
                <label>🚀 STRATEGI OPTIMASI PENJUALAN:</label>
                <div id="strategyContainer"></div>
            </div>
        </div>
    </div>
</div>

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
        const hpp = parseFloat(document.getElementById('hppInput').value.replace(/\./g, '')) || 0;
        const profitPct = parseFloat(document.getElementById('targetProfit').value) / 100;
        const vchPct = parseFloat(document.getElementById('voucherRate').value) / 100;
        const affPct = parseFloat(document.getElementById('affiliateRate').value) / 100;
        const katPct = parseFloat(document.getElementById('kategori').value);
        const progPct = parseFloat(document.getElementById('program').value);
        
        if (hpp <= 0) return alert("Masukkan HPP Produk!");

        const effectiveAffRate = affPct * 1.11;
        const totalTaxRate = katPct + progPct + vchPct + effectiveAffRate;
        const fixFee = 1250;

        let jual = (hpp + (hpp * profitPct) + fixFee) / (1 - totalTaxRate);
        jual = Math.ceil(jual / 100) * 100;

        const valAdmin = jual * (katPct + progPct);
        const valAff = jual * effectiveAffRate;
        const valVch = jual * vchPct;
        const netCuan = jual - valAdmin - valAff - valVch - fixFee - hpp;

        document.getElementById('resultArea').style.display = 'block';
        document.getElementById('resHargaJual').innerText = "Rp " + jual.toLocaleString('id-ID');
        document.getElementById('resAdminValue').innerText = "-Rp " + Math.round(valAdmin).toLocaleString('id-ID');
        document.getElementById('resAffValue').innerText = "-Rp " + Math.round(valAff).toLocaleString('id-ID');
        document.getElementById('resVoucherValue').innerText = "-Rp " + Math.round(valVch).toLocaleString('id-ID');
        document.getElementById('resCuan').innerText = "Rp " + Math.round(netCuan).toLocaleString('id-ID');

        const strategies = [
            { i: "🎯", t: "Targeting Affiliate", d: "Aktifkan 'Komisi Tambahan' minimal 1% di Shopee Affiliate agar produk diprioritaskan oleh para kolaborator." },
            { i: "🏷️", t: "Psikologi Harga Coret", d: "Set harga coret di Seller Centre sebesar Rp " + (Math.ceil((jual * 1.25)/100)*100).toLocaleString('id-ID') + " untuk diskon 20% yang menarik mata." },
            { i: "📦", t: "Efisiensi Biaya Fix", d: "Karena ada biaya fix Rp 1.250/order, dorong 'Kombo Hemat' agar pembeli beli lebih dari 1 barang per resi." },
            { i: "⚡", t: "Flash Sale Internal", d: "Gunakan harga Rp " + jual.toLocaleString('id-ID') + " sebagai harga promosi Flash Sale Toko untuk menaikkan skor popularitas." },
            { i: "🔍", t: "Optimasi Judul SEO", d: "Sertakan kata kunci volume tinggi dan fitur utama di 20 karakter pertama agar konversi klik (CTR) tinggi." }
        ];

        let stratHtml = "";
        strategies.forEach(s => { 
            stratHtml += `
            <div class="strategy-card">
                <div class="strat-icon">${s.i}</div>
                <div class="strat-text"><strong>${s.t}</strong>${s.d}</div>
            </div>`; 
        });
        document.getElementById('strategyContainer').innerHTML = stratHtml;
    }
</script>

</body>
</html>
"""

components.html(html_code, height=1550, scrolling=True)
