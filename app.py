import streamlit as st
import streamlit.components.v1 as components

# 1. Konfigurasi Dasar
st.set_page_config(page_title="Shopee Smart Pricing Pro", page_icon="🧡", layout="centered")

# CSS untuk menyembunyikan elemen Streamlit dan mendesain Halaman Login
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Background Login dengan Gambar & Efek Kabut */
    .stApp {
        background: url("https://images.unsplash.com/photo-1614850523296-d8c1af93d400?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80");
        background-size: cover;
    }
    
    .login-box {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(15px);
        border-radius: 30px;
        padding: 40px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        text-align: center;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-top: 50px;
    }
    
    .slogan {
        color: white;
        font-size: 16px;
        font-style: italic;
        margin-top: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    /* Tombol Login Elegan */
    div.stButton > button {
        background-color: #EE4D2D;
        color: white;
        border-radius: 12px;
        border: none;
        padding: 10px 30px;
        font-weight: bold;
        transition: 0.3s;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Logika Login
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    col1, col2, col3 = st.columns([1,4,1])
    with col2:
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.image("https://upload.wikimedia.org/wikipedia/commons/f/fe/Shopee.svg", width=80)
        st.markdown("<h2 style='color:white;'>Premium Access</h2>", unsafe_allow_html=True)
        
        pwd_input = st.text_input("Password", type="password", placeholder="Masukkan kode akses...")
        
        if st.button("MULAI ANALISA CUAN"):
            if pwd_input == "cuan2025":
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("Akses Ditolak!")
        
        st.markdown('<p class="slogan">"Makin tahu cuanmu, makin menyala peluang suksesmu!"</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# 3. KODE UTAMA (Fitur Lengkap Kembali)
html_code = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
        :root { --shopee-orange: #EE4D2D; --bg: #f4f4f7; --success: #26aa99; }
        body { font-family: 'Inter', sans-serif; background: #f4f4f7; display: flex; justify-content: center; padding: 10px; margin: 0; }
        .card { background: white; width: 100%; max-width: 480px; border-radius: 24px; box-shadow: 0 15px 35px rgba(0,0,0,0.1); overflow: hidden; }
        .header { background: linear-gradient(135deg, #f53d2d, #ff6433); color: white; padding: 25px 20px; text-align: center; }
        .content { padding: 20px; }
        .grid-input { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }
        label { display: block; font-size: 10px; font-weight: 800; color: #888; margin-bottom: 8px; text-transform: uppercase; }
        input, select { width: 100%; padding: 14px; border: 2px solid #eee; border-radius: 14px; font-size: 14px; box-sizing: border-box; margin-bottom: 15px; font-weight: 600; }
        .btn-main { width: 100%; background: var(--shopee-orange); color: white; border: none; padding: 18px; border-radius: 14px; font-size: 16px; font-weight: 700; cursor: pointer; }
        .result-area { display: none; margin-top: 25px; animation: fadeIn 0.5s; }
        .price-tag { text-align: center; background: #e6f7f4; padding: 20px; border-radius: 18px; margin-bottom: 20px; border: 1px solid #b3e5dc; }
        .suggested-price { display: block; font-size: 32px; font-weight: 800; color: var(--success); }
        .fee-breakdown { font-size: 12px; background: #fafafa; padding: 15px; border-radius: 12px; border: 1px solid #eee; margin-bottom: 20px; }
        .fee-row { display: flex; justify-content: space-between; margin-bottom: 6px; }
        .strategy-card { background: #fff; border-left: 4px solid var(--shopee-orange); padding: 12px; border-radius: 8px; font-size: 12px; margin-bottom: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
        .wa-float { position: fixed; bottom: 20px; right: 20px; background: #25D366; color: white; padding: 12px 20px; border-radius: 50px; text-decoration: none; font-weight: bold; box-shadow: 0 4px 10px rgba(0,0,0,0.3); z-index: 1000; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body>
<div class="card">
    <div class="header">
        <h1 style="margin:0; font-size: 20px;">Shopee Pricing Assistant</h1>
        <p style="margin:5px 0 0; font-size: 11px; opacity: 0.9;">Professional Profit Strategy 2025</p>
    </div>
    <div class="content">
        <label>MODAL PRODUK / HPP (RP)</label>
        <input type="text" id="hppInput" placeholder="Contoh: 50.000" oninput="formatRupiah(this)">
        
        <div class="grid-input">
            <div>
                <label>Target Profit (%)</label>
                <input type="number" id="targetProfit" value="20">
            </div>
            <div>
                <label>Voucher Toko (%)</label>
                <select id="voucherPlan">
                    <option value="0">0%</option>
                    <option value="0.05">5%</option>
                    <option value="0.10">10%</option>
                </select>
            </div>
        </div>

        <label>KATEGORI ADMIN & PROGRAM</label>
        <select id="kategori">
            <option value="0.08">Grup A (8.0%)</option>
            <option value="0.06">Grup C (6.0%)</option>
        </select>
        <select id="program">
            <option value="0">Tanpa Program XTRA</option>
            <option value="0.04">Gratis Ongkir XTRA (4%)</option>
            <option value="0.085">Komplit XTRA (8.5%)</option>
        </select>

        <button class="btn-main" onclick="hitungHarga()">HITUNG HARGA IDEAL</button>

        <div id="resultArea" class="result-area">
            <div class="price-tag">
                <span id="labelHarga" style="font-size: 11px; color: #666; font-weight: 800;">HARGA JUAL REKOMENDASI</span>
                <span class="suggested-price" id="resHargaJual"></span>
            </div>
            <div class="fee-breakdown">
                <div class="fee-row"><span>Potongan Fee Shopee:</span> <span id="resFee"></span></div>
                <div class="fee-row"><span>Biaya Proses Fix:</span> <span>Rp 1.250</span></div>
                <div class="fee-row" style="color:var(--success); font-weight:700; border-top:1px solid #eee; margin-top:5px; padding-top:5px;">
                    <span>Profit Bersih:</span> <span id="resCuan"></span>
                </div>
            </div>
            <div id="stratContainer"></div>
        </div>
    </div>
</div>

<a href="https://wa.me/6281553472658" class="wa-float" target="_blank">💬 Chat Admin</a>

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
        const hpp = parseFloat(document.getElementById('hppInput').value.replace(/\./g, ''));
        const target = parseFloat(document.getElementById('targetProfit').value) / 100;
        const vch = parseFloat(document.getElementById('voucherPlan').value);
        const kat = parseFloat(document.getElementById('kategori').value);
        const prg = parseFloat(document.getElementById('program').value);
        
        if(!hpp) return;
        
        const rate = kat + prg + vch;
        let harga = (hpp + (hpp * target) + 1250) / (1 - rate);
        harga = Math.ceil(harga / 100) * 100;
        
        const fee = harga * (kat + prg);
        const cuan = harga - fee - (harga * vch) - 1250 - hpp;

        document.getElementById('resultArea').style.display = 'block';
        document.getElementById('resHargaJual').innerText = "Rp " + harga.toLocaleString('id-ID');
        document.getElementById('resFee').innerText = "-Rp " + Math.round(fee).toLocaleString('id-ID');
        document.getElementById('resCuan').innerText = "Rp " + Math.round(cuan).toLocaleString('id-ID');
        
        document.getElementById('stratContainer').innerHTML = `
            <div class="strategy-card"><strong>Psikologi Harga:</strong> Set harga coret di Rp ${(Math.round(harga*1.2/100)*100).toLocaleString('id-ID')}</div>
            <div class="strategy-card"><strong>Profit Margin:</strong> Target ${(target*100)}% tercapai dengan aman.</div>
        `;
    }
</script>
</body>
</html>
"""

components.html(html_code, height=1200, scrolling=True)
