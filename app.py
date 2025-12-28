import streamlit as st
import streamlit.components.v1 as components

# 1. Konfigurasi Halaman Dasar
st.set_page_config(
    page_title="Shopee Smart Pricing Pro 2025", 
    page_icon="🧡", 
    layout="centered"
)

# 2. CSS Global untuk Streamlit UI (Font Poppins & Rapi)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');

    header {visibility: hidden !important;}
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    
    .block-container {
        padding-top: 5rem !important;
        background-color: #f4f4f7;
    }

    html, body, [class*="st-"] {
        font-family: 'Poppins', sans-serif !important;
    }
    
    .login-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 100%;
    }
    
    .login-header {
        font-weight: 800;
        font-size: 32px;
        color: #EE4D2D;
        margin-bottom: 8px;
        letter-spacing: -0.5px;
    }
    
    .login-sub {
        font-size: 15px;
        color: #555;
        margin-bottom: 35px;
        font-weight: 400;
    }

    /* Menyamakan Lebar Kotak Password dan Tombol (Proporsional) */
    [data-testid="stTextInput"], [data-testid="stButton"] {
        width: 320px !important;
        margin: 0 auto;
    }

    /* Styling Tombol Login agar Elegan */
    div.stButton > button:first-child {
        background-color: #EE4D2D;
        color: white;
        border-radius: 12px;
        width: 100%;
        border: none;
        height: 52px;
        font-weight: 600;
        font-size: 16px;
        font-family: 'Poppins', sans-serif;
        transition: all 0.3s ease;
        margin-top: 5px;
    }
    
    div.stButton > button:hover {
        background-color: #d73211;
        box-shadow: 0 6px 15px rgba(238, 77, 45, 0.25);
        transform: translateY(-1px);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Logika Autentikasi
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if not st.session_state['authenticated']:
    st.markdown('<div class="login-wrapper">', unsafe_allow_html=True)
    st.markdown('<div class="login-header">Hitung Cerdas untuk<br>Jualan Berkualitas</div>', unsafe_allow_html=True)
    st.markdown('<div class="login-sub">Silakan masukkan kata sandi akses premium</div>', unsafe_allow_html=True)
    
    password = st.text_input("Password", type="password", placeholder="Kata Sandi", label_visibility="collapsed")
    
    if st.button("Buka Kalkulator Sekarang"):
        if password == "cuan2025":
            st.session_state['authenticated'] = True
            st.rerun()
        else:
            st.error("Akses ditolak. Kata sandi salah.")
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop() 

# 4. KODE HTML UTAMA (Kalkulator & 5 Strategi)
html_code = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');
        :root { --shopee-orange: #EE4D2D; --bg: #f4f4f7; --success: #26aa99; --dark: #333; }
        body { font-family: 'Poppins', sans-serif; background: var(--bg); display: flex; justify-content: center; padding: 15px; margin: 0; }
        .card { background: white; width: 100%; max-width: 500px; border-radius: 24px; box-shadow: 0 15px 35px rgba(0,0,0,0.1); overflow: hidden; }
        .header { background: linear-gradient(135deg, #f53d2d, #ff6433); color: white; padding: 30px 20px; text-align: center; }
        .content { padding: 25px; }
        
        .grid-input { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }
        label { display: block; font-size: 11px; font-weight: 700; color: #888; margin-bottom: 8px; letter-spacing: 0.5px; text-transform: uppercase; }
        
        input, select { width: 100%; padding: 14px; border: 2px solid #eee; border-radius: 14px; font-size: 14px; box-sizing: border-box; transition: 0.3s; font-weight: 600; margin-bottom: 15px; font-family: 'Poppins', sans-serif; }
        input:focus { border-color: var(--shopee-orange); outline: none; background: #fffaf9; }
        
        .btn-main { width: 100%; background: var(--shopee-orange); color: white; border: none; padding: 18px; border-radius: 14px; font-size: 16px; font-weight: 700; cursor: pointer; font-family: 'Poppins', sans-serif; box-shadow: 0 4px 15px rgba(238, 77, 45, 0.3); margin-top: 10px; }
        
        .result-area { display: none; margin-top: 25px; animation: fadeIn 0.5s forwards; }
        .price-tag { text-align: center; background: #fff9f0; padding: 20px; border-radius: 18px; margin-bottom: 20px; border: 2px solid #ffe8cc; }
        .suggested-price { display: block; font-size: 34px; font-weight: 800; color: var(--shopee-orange); }
        
        .fee-breakdown { font-size: 12px; background: #fafafa; padding: 18px; border-radius: 15px; border: 1px solid #eee; margin-bottom: 25px; }
        .fee-row { display: flex; justify-content: space-between; margin-bottom: 8px; color: #555; }
        .total-cuan { color: var(--success); font-size: 15px; font-weight: 800; border-top: 1px solid #ddd; padding-top: 10px; margin-top: 10px; }
        
        .strategy-title { font-size: 14px; font-weight: 800; color: #444; margin-bottom: 15px; display: block; }
        .strategy-card { background: #fff; border: 1px solid #f0f0f0; border-left: 5px solid var(--shopee-orange); padding: 15px; border-radius: 12px; font-size: 13px; line-height: 1.6; margin-bottom: 12px; display: flex; align-items: flex-start; gap: 12px; }
        .strat-icon { font-size: 20px; }
        .strat-text strong { color: var(--dark); display: block; margin-bottom: 2px; font-size: 14px; }

        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body>

<div class="card">
    <div class="header">
        <h1 style="margin:0; font-size: 20px; font-weight: 800;">Shopee Pricing Assistant</h1>
        <p style="margin:5px 0 0; font-size: 11px; opacity: 0.9;">Professional Profit Strategy 2025</p>
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
        <input type="number" id="affiliateRate" value="5">

        <label>KATEGORI PRODUK (ADMIN)</label>
        <select id="kategori">
            <option value="0.08">Grup A (8.0%) - Fashion, Kecantikan, Aksesoris</option>
            <option value="0.075">Grup B (7.5%) - Elektronik, Rumah Tangga</option>
            <option value="0.06">Grup C (6.0%) - Kamera, Olahraga, Mainan</option>
            <option value="0.04">Grup D (4.0%) - Makanan, Minuman, Bayi</option>
            <option value="0.025">Grup E (2.5%) - Sembako, Produk Segar</option>
        </select>

        <label>PROGRAM PROMOSI SHOPEE</label>
        <select id="program">
            <option value="0.085">Gratis Ongkir XTRA + Cashback XTRA (8.5%)</option>
            <option value="0.04">Hanya Gratis Ongkir XTRA (4.0%)</option>
            <option value="0">Tanpa Program XTRA (0%)</option>
        </select>

        <button class="btn-main" onclick="hitungHarga()">HITUNG REKOMENDASI</button>

        <div id="resultArea" class="result-area">
            <div class="price-tag">
                <span style="font-size: 11px; color: #888; font-weight: 700;">HARGA JUAL REKOMENDASI</span>
                <span class="suggested-price" id="resHargaJual"></span>
            </div>

            <div class="fee-breakdown">
                <div class="fee-row"><span>Admin & Program:</span> <span id="resAdminValue"></span></div>
                <div class="fee-row"><span>Affiliate + PPN 11%:</span> <span id="resAffValue"></span></div>
                <div class="fee-row"><span>Alokasi Voucher:</span> <span id="resVoucherValue"></span></div>
                <div class="fee-row"><span>Biaya Proses:</span> <span>Rp 1.250</span></div>
                <div class="fee-row total-cuan">
                    <span>NET PROFIT:</span> <span id="resCuan"></span>
                </div>
            </div>
            
            <span class="strategy-title">🚀 5 STRATEGI PENJUALAN UNTUK ANDA:</span>
            <div id="strategyContainer"></div>
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

        // DAFTAR 5 STRATEGI LENGKAP
        const strategies = [
            { i: "🎯", t: "Skema Affiliate", d: "Tawarkan komisi tambahan 1-3% khusus untuk Top Creator agar produk Anda direview dan viral lebih cepat." },
            { i: "🏷️", t: "Psikologi Harga Coret", d: "Gunakan fitur diskon seller untuk mencoret harga Rp " + (Math.ceil((jual * 1.3)/100)*100).toLocaleString('id-ID') + " ke harga hitungan ini." },
            { i: "📦", t: "Kombo Hemat", d: "Karena biaya proses flat Rp 1.250, buatlah paket beli 2 diskon 2% untuk memaksimalkan profit per resi." },
            { i: "⚡", t: "Flash Sale Internal", d: "Gunakan harga ini sebagai harga 'Flash Sale Toko' di jam sibuk (12.00 / 20.00) untuk memicu impulse buying." },
            { i: "🔥", t: "Voucher Ikuti Toko", d: "Berikan voucher khusus Rp 2.000 untuk pengikut baru guna membangun database pelanggan jangka panjang." }
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

components.html(html_code, height=1700, scrolling=True)
