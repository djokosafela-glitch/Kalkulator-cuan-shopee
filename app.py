import streamlit as st
import streamlit.components.v1 as components

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Shopee Smart Pricing 2025", page_icon="🧡", layout="centered")

# CSS UNTUK LOGIN & UI
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Background Login Mewah */
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), 
                    url("https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=2026&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
    }
    
    /* Login Box - Glassmorphism Putih Solid agar Teks Terlihat */
    .login-box {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 25px;
        padding: 40px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.5);
        text-align: center;
        margin-top: 20px;
    }

    /* Memastikan Teks Input Password Berwarna Hitam */
    div[data-baseweb="input"] input {
        color: #000000 !important;
        background-color: #ffffff !important;
    }

    .slogan {
        color: #555;
        font-size: 14px;
        font-style: italic;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Logika Login
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    _, col2, _ = st.columns([0.1, 0.8, 0.1])
    with col2:
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.image("https://upload.wikimedia.org/wikipedia/commons/f/fe/Shopee.svg", width=70)
        st.markdown("<h2 style='color:#EE4D2D; margin-top:10px;'>Premium Access</h2>", unsafe_allow_html=True)
        
        pwd = st.text_input("PASSWORD", type="password", placeholder="Ketik password di sini...")
        
        if st.button("MULAI ANALISA SEKARANG", use_container_width=True):
            if pwd == "cuan2025":
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("Password salah!")
        
        st.markdown('<p class="slogan">"Makin tahu cuanmu, makin menyala peluang suksesmu!"</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# 3. APLIKASI UTAMA (Sesuai Persis dengan Gambar 4856.jpg & 4861.jpg)
html_app = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
        body { font-family: 'Inter', sans-serif; background: #f8f9fa; margin: 0; padding: 10px; display: flex; justify-content: center; }
        .card { background: white; width: 100%; max-width: 480px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); overflow: hidden; }
        .header { background: linear-gradient(135deg, #f53d2d, #ff6433); color: white; padding: 25px; text-align: center; }
        .content { padding: 20px; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
        label { display: block; font-size: 10px; font-weight: 800; color: #999; margin-bottom: 6px; text-transform: uppercase; }
        input, select { width: 100%; padding: 12px; border: 1.5px solid #eee; border-radius: 12px; font-size: 14px; margin-bottom: 15px; box-sizing: border-box; font-weight: 600; }
        .btn-calc { width: 100%; background: #EE4D2D; color: white; border: none; padding: 16px; border-radius: 12px; font-size: 15px; font-weight: 800; cursor: pointer; text-transform: uppercase; margin-top: 10px; }
        
        /* Area Hasil Sesuai Gambar */
        .result-area { display: none; margin-top: 20px; animation: fadeIn 0.4s; }
        .price-box { background: #e6f7f4; border: 1px solid #b3e5dc; border-radius: 15px; padding: 20px; text-align: center; margin-bottom: 15px; }
        .price-val { font-size: 32px; font-weight: 800; color: #26aa99; }
        .detail-card { background: #fff; border: 1px solid #eee; border-radius: 12px; padding: 15px; margin-bottom: 20px; }
        .detail-row { display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 8px; color: #444; }
        
        /* Strategi Promosi Sesuai Gambar */
        .strat-item { background: #fff; border: 1px solid #eee; border-radius: 10px; padding: 12px; margin-bottom: 10px; font-size: 12px; display: flex; align-items: flex-start; gap: 10px; }
        .wa-float { position: fixed; bottom: 20px; right: 20px; background: #25D366; color: white; padding: 12px 20px; border-radius: 50px; text-decoration: none; font-weight: 700; box-shadow: 0 4px 15px rgba(0,0,0,0.2); font-size: 13px; z-index: 100; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body>
<div class="card">
    <div class="header">
        <h2 style="margin:0; font-size: 18px;">Shopee Smart Pricing 2025</h2>
        <p style="margin:5px 0 0; font-size: 10px; opacity: 0.9;">Detail Kategori & Affiliate Terintegrasi</p>
    </div>
    <div class="content">
        <label>Modal Produk / HPP (RP)</label>
        <input type="text" id="hpp" placeholder="Contoh: 50.000" oninput="formatRp(this)">
        
        <div class="grid">
            <div>
                <label>Target Profit (%)</label>
                <input type="number" id="profit" value="20">
            </div>
            <div>
                <label>Komisi Affiliate (%)</label>
                <input type="number" id="affiliate" value="5">
            </div>
        </div>

        <label>Rencana Voucher Toko</label>
        <select id="vch">
            <option value="0">0% (Tanpa Voucher)</option>
            <option value="0.03">3%</option>
            <option value="0.05">5%</option>
            <option value="0.10">10%</option>
        </select>

        <label>Pilih Jenis Barang (Kategori)</label>
        <select id="kat">
            <option value="0.08">Grup A (Fashion, Kecantikan, Aksesoris HP - 8%)</option>
            <option value="0.075">Grup B (Elektronik, Otomotif - 7.5%)</option>
            <option value="0.06">Grup C (Kamera, Hobi, Olahraga - 6%)</option>
            <option value="0.04">Grup D (FMCG, Makanan - 4%)</option>
        </select>

        <label>Ikut Program Promosi Shopee?</label>
        <select id="prog">
            <option value="0.085">Gratis Ongkir XTRA + Cashback XTRA (8.5%)</option>
            <option value="0.04">Hanya Gratis Ongkir XTRA (4%)</option>
            <option value="0">Tidak Ikut (0%)</option>
        </select>

        <button class="btn-calc" onclick="hitung()">Rekomendasikan Harga</button>

        <div id="result" class="result-area">
            <div class="price-box">
                <div style="font-size: 10px; font-weight: 700; color: #666; margin-bottom: 5px;">HARGA JUAL TARGET PROFIT</div>
                <div class="price-val" id="resPrice"></div>
            </div>

            <div class="detail-card">
                <div class="detail-row"><span>Biaya Admin & XTRA:</span><span id="resAdmin"></span></div>
                <div class="detail-row"><span>Affiliate (+PPN 11%):</span><span id="resAff"></span></div>
                <div class="detail-row"><span>Potongan Voucher:</span><span id="resVch"></span></div>
                <div class="detail-row"><span>Biaya Proses (Fix 2025):</span><span>-Rp 1.250</span></div>
                <div class="detail-row" style="border-top: 1px solid #eee; padding-top: 8px; margin-top: 8px; font-weight: 800; color: #26aa99;">
                    <span>Profit Bersih Final:</span><span id="resCuan"></span>
                </div>
            </div>

            <div style="font-size: 11px; font-weight: 800; color: #777; margin-bottom: 10px;">5 STRATEGI PROMOSI ANDA:</div>
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
        if(!hpp) { alert("Masukkan modal dulu!"); return; }
        
        const target = parseFloat(document.getElementById('profit').value) / 100;
        const affRate = (parseFloat(document.getElementById('affiliate').value) / 100) * 1.11; // Include PPN 11%
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
            <div class="strat-item">🚀 <b>Push Affiliate</b> Komisi sudah aman di harga jual. Segera hubungi kreator!</div>
            <div class="strat-item">🎟️ <b>Voucher Toko</b> Gunakan voucher ${vchRate*100}% secara agresif untuk tarik pembeli.</div>
            <div class="strat-item">📈 <b>Harga Coret</b> Upload di harga Rp ${coret.toLocaleString('id-ID')} lalu diskon ke harga ini.</div>
            <div class="strat-item">📦 <b>Paket Hemat</b> Biaya Rp 1.250 tetap per pesanan. Jual paket isi 3 agar lebih cuan!</div>
            <div class="strat-item">💡 <b>Fokus SEO</b> Gunakan kata kunci populer agar produk muncul secara organik.</div>
        `;
    }
</script>
</body>
</html>
"""

components.html(html_app, height=1400, scrolling=True)
