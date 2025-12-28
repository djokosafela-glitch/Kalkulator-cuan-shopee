import streamlit as st
import streamlit.components.v1 as components

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Shopee Smart Pricing Pro", page_icon="🧡", layout="centered")

# CSS untuk memperbaiki tampilan Login & Password
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
    
    /* Container Login yang Lebih Terang agar Konten Jelas */
    .login-box {
        background: rgba(255, 255, 255, 0.9); /* Putih hampir solid agar teks hitam terlihat */
        backdrop-filter: blur(10px);
        border-radius: 25px;
        padding: 40px 30px;
        border: 1px solid #ddd;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        text-align: center;
    }

    /* Memaksa Warna Teks Input Password menjadi Hitam */
    input {
        color: #000000 !important;
        background-color: #ffffff !important;
    }

    .slogan-text {
        color: #444;
        font-size: 14px;
        font-style: italic;
        margin-top: 20px;
        line-height: 1.5;
    }

    h1 { color: #EE4D2D !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. Logika Login
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    # Menggunakan kolom untuk memposisikan kotak login di tengah secara vertikal
    st.write("##") # Spasi atas
    col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
    
    with col2:
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        # Menampilkan Logo Shopee
        st.image("https://upload.wikimedia.org/wikipedia/commons/f/fe/Shopee.svg", width=80)
        st.markdown("<h1>Premium Access</h1>", unsafe_allow_html=True)
        
        # Input Password dengan label yang jelas
        pwd = st.text_input("MASUKKAN KODE AKSES", type="password", help="Silakan masukkan password yang diberikan Admin")
        
        if st.button("MULAI ANALISA SEKARANG", use_container_width=True):
            if pwd == "cuan2025":
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("Password Salah! Hubungi Admin.")
        
        st.markdown('<p class="slogan-text">"Makin tahu cuanmu, makin menyala peluang suksesmu!"</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# 3. APLIKASI UTAMA (Fitur Lengkap)
html_app = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
        body { font-family: 'Inter', sans-serif; background: #f4f4f7; padding: 10px; margin: 0; display: flex; justify-content: center; }
        .card { background: white; width: 100%; max-width: 450px; border-radius: 24px; box-shadow: 0 15px 35px rgba(0,0,0,0.1); overflow: hidden; }
        .header { background: linear-gradient(135deg, #f53d2d, #ff6433); color: white; padding: 25px 20px; text-align: center; }
        .content { padding: 20px; }
        .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }
        label { display: block; font-size: 10px; font-weight: 800; color: #888; margin-bottom: 8px; text-transform: uppercase; }
        input, select { width: 100%; padding: 14px; border: 2px solid #eee; border-radius: 14px; font-size: 14px; box-sizing: border-box; margin-bottom: 15px; font-weight: 600; color: #333; }
        .btn-calc { width: 100%; background: #EE4D2D; color: white; border: none; padding: 18px; border-radius: 14px; font-size: 16px; font-weight: 700; cursor: pointer; }
        .result-box { display: none; margin-top: 25px; }
        .price-display { text-align: center; background: #e6f7f4; padding: 20px; border-radius: 18px; border: 1px solid #b3e5dc; margin-bottom: 20px; }
        .price-val { display: block; font-size: 32px; font-weight: 800; color: #26aa99; }
        .fee-card { background: #fafafa; padding: 15px; border-radius: 12px; border: 1px solid #eee; font-size: 12px; }
        .fee-item { display: flex; justify-content: space-between; margin-bottom: 6px; }
        .wa-btn { position: fixed; bottom: 20px; right: 20px; background: #25D366; color: white; padding: 12px 20px; border-radius: 50px; text-decoration: none; font-weight: bold; box-shadow: 0 4px 10px rgba(0,0,0,0.3); z-index: 999; }
    </style>
</head>
<body>
<div class="card">
    <div class="header">
        <h2 style="margin:0; font-size: 20px;">Shopee Pricing Pro</h2>
        <p style="margin:5px 0 0; font-size: 11px; opacity: 0.9;">Professional Strategy 2025</p>
    </div>
    <div class="content">
        <label>Modal Produk (Rp)</label>
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
                    <option value="0.05">5%</option>
                    <option value="0.10">10%</option>
                </select>
            </div>
        </div>

        <label>Kategori Produk & Program</label>
        <select id="kat">
            <option value="0.08">Grup A (Fashion/Beauty - 8%)</option>
            <option value="0.06">Grup C (Hobby/Tools - 6%)</option>
        </select>
        <select id="prog">
            <option value="0">Tanpa Program XTRA</option>
            <option value="0.04">Gratis Ongkir XTRA (4%)</option>
            <option value="0.085">XTRA Komplit (8.5%)</option>
        </select>

        <button class="btn-calc" onclick="calculate()">HITUNG SEKARANG</button>

        <div id="result" class="result-box">
            <div class="price-display">
                <span style="font-size: 11px; color: #666;">HARGA JUAL IDEAL:</span>
                <span class="price-val" id="resPrice"></span>
            </div>
            <div class="fee-card">
                <div class="fee-item"><span>Admin Shopee:</span> <span id="resFee"></span></div>
                <div class="fee-item" style="color: #26aa99; font-weight: 700;"><span>Profit Bersih:</span> <span id="resCuan"></span></div>
            </div>
        </div>
    </div>
</div>

<a href="https://wa.me/6281553472658" class="wa-btn" target="_blank">💬 Chat Admin</a>

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
        const vch = parseFloat(document.getElementById('vch').value);
        const kat = parseFloat(document.getElementById('kat').value);
        const prog = parseFloat(document.getElementById('prog').value);
        
        if(!hpp) return;
        
        const rate = kat + prog + vch;
        let jual = (hpp + (hpp * target) + 1250) / (1 - rate);
        jual = Math.ceil(jual / 100) * 100;

        const fee = jual * (kat + prog);
        const cuan = jual - fee - (jual * vch) - 1250 - hpp;

        document.getElementById('result').style.display = 'block';
        document.getElementById('resPrice').innerText = "Rp " + jual.toLocaleString('id-ID');
        document.getElementById('resFee').innerText = "-Rp " + Math.round(fee).toLocaleString('id-ID');
        document.getElementById('resCuan').innerText = "Rp " + Math.round(cuan).toLocaleString('id-ID');
    }
</script>
</body>
</html>
"""

components.html(html_app, height=1000, scrolling=True)
                
