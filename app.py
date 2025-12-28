import streamlit as st
import streamlit.components.v1 as components

# 1. Konfigurasi Halaman Dasar
st.set_page_config(
    page_title="Shopee Smart Pricing Pro 2025", 
    page_icon="🧡", 
    layout="centered"
)

# 2. CSS UNTUK MENGHILANGKAN ICON GITHUB & MENU STREAMLIT
st.markdown("""
    <style>
    /* Menghilangkan Header (Termasuk Icon GitHub) */
    header {visibility: hidden !important;}
    
    /* Menghilangkan Menu (Tiga Garis) di Kanan Atas */
    #MainMenu {visibility: hidden !important;}
    
    /* Menghilangkan Footer "Made with Streamlit" */
    footer {visibility: hidden !important;}
    
    /* Menyesuaikan jarak atas setelah header dihilangkan */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
    }

    /* Menghilangkan dekorasi link GitHub pada gambar/elemen */
    .viewerBadge_container__1QSob { display: none !important; }
    
    /* Background Body Streamlit agar selaras dengan HTML */
    .stApp {
        background-color: #f4f4f7;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. KODE HTML UTAMA (Sesuai Versi Anda)
html_code = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
        :root { --shopee-orange: #EE4D2D; --bg: #f4f4f7; --success: #26aa99; --danger: #e74c3c; }
        body { font-family: 'Inter', sans-serif; background: var(--bg); display: flex; justify-content: center; padding: 15px; margin: 0; }
        .card { background: white; width: 100%; max-width: 500px; border-radius: 24px; box-shadow: 0 15px 35px rgba(0,0,0,0.1); overflow: hidden; }
        .header { background: linear-gradient(135deg, #f53d2d, #ff6433); color: white; padding: 25px 20px; text-align: center; }
        .content { padding: 25px; }
        .grid-input { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }
        label { display: block; font-size: 11px; font-weight: 800; color: #888; margin-bottom: 8px; letter-spacing: 0.5px; text-transform: uppercase; }
        input, select { width: 100%; padding: 14px; border: 2px solid #eee; border-radius: 14px; font-size: 14px; box-sizing: border-box; transition: 0.3s; font-weight: 600; margin-bottom: 15px; }
        input:focus { border-color: var(--shopee-orange); outline: none; background: #fffaf9; }
        .btn-main { width: 100%; background: var(--shopee-orange); color: white; border: none; padding: 18px; border-radius: 14px; font-size: 16px; font-weight: 700; cursor: pointer; box-shadow: 0 4px 15px rgba(238, 77, 45, 0.3); margin-top: 10px; }
        .btn-main:active { transform: scale(0.98); }
        .result-area { display: none; margin-top: 25px; animation: fadeIn 0.5s; }
        .price-tag { text-align: center; background: #e6f7f4; padding: 20px; border-radius: 18px; margin-bottom: 20px; border: 1px solid #b3e5dc; }
        .suggested-price { display: block; font-size: 32px; font-weight: 800; color: var(--success); }
        .fee-breakdown { font-size: 12px; background: #fafafa; padding: 15px; border-radius: 12px; border: 1px solid #eee; margin-bottom: 25px; }
        .fee-row { display: flex; justify-content: space-between; margin-bottom: 6px; color: #666; }
        .strategy-section { border-top: 2px dashed #ddd; padding-top: 20px; }
        .strategy-card { background: #fff; border: 1px solid #eee; border-left: 4px solid var(--shopee-orange); padding: 15px; border-radius: 10px; font-size: 13px; line-height: 1.5; margin-bottom: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.02); }
        .strategy-card strong { color: var(--shopee-orange); display: block; margin-bottom: 4px; font-size: 14px; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body>
<div class="card">
    <div class="header">
        <h1 style="margin:0; font-size: 20px;">Shopee Pricing Assistant</h1>
        <p style="margin:5px 0 0; font-size: 11px; opacity: 0.9;">Custom Profit & Voucher Strategy 2025</p>
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
                <label>Rencana Voucher (%)</label>
                <select id="voucherPlan">
                    <option value="0">0% (Tanpa Voucher)</option>
                    <option value="0.03">3% Diskon</option>
                    <option value="0.05">5% Diskon</option>
                    <option value="0.10">10% Diskon</option>
                    <option value="0.20">20% Diskon</option>
                </select>
            </div>
        </div>
        <label>KATEGORI PRODUK (ADMIN)</label>
        <select id="kategori">
            <option value="0.08">Grup A (8.0%) - Fashion, Kecantikan</option>
            <option value="0.075">Grup B (7.5%) - Elektronik, Rumah</option>
            <option value="0.06">Grup C (6.0%) - Kamera, Hobi</option>
            <option value="0.04">Grup D (4.0%) - Makanan, Bayi</option>
        </select>
        <label>IKUT PROGRAM PROMOSI SHOPEE?</label>
        <select id="program">
            <option value="0">Tidak Ikut Program XTRA</option>
            <option value="0.04">Gratis Ongkir XTRA (4%)</option>
            <option value="0.085">Komplit (Gr. Ongkir + Cashback XTRA) (8.5%)</option>
        </select>
        <button class="btn-main" onclick="hitungHarga()">HITUNG HARGA JUAL IDEAL</button>
        <div id="resultArea" class="result-area">
            <div class="price-tag">
                <span id="labelHarga" style="font-size: 11px; color: #666; font-weight: 600; text-transform: uppercase;"></span>
                <span class="suggested-price" id="resHargaJual"></span>
            </div>
            <div class="fee-breakdown">
                <div class="fee-row"><span>Potongan Fee Shopee:</span> <span id="resFeePersen"></span></div>
                <div class="fee-row"><span>Potongan Voucher Anda:</span> <span id="resVoucherValue"></span></div>
                <div class="fee-row"><span>Biaya Proses (Fix 2025):</span> <span>Rp 1.250</span></div>
                <div class="fee-row" style="color: var(--success); font-weight: 700; border-top: 1px solid #ddd; padding-top: 5px; margin-top: 5px;">
                    <span>Profit Bersih (Masuk Kantong):</span> <span id="resCuan"></span>
                </div>
            </div>
            <div class="strategy-section">
                <label>5 STRATEGI PROMOSI UNTUK ANDA:</label>
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
        const hppRaw = document.getElementById('hppInput').value.replace(/\./g, '');
        const hpp = parseFloat(hppRaw);
        const targetProfitPersen = parseFloat(document.getElementById('targetProfit').value) / 100;
        const rateVoucher = parseFloat(document.getElementById('voucherPlan').value);
        const rateKat = parseFloat(document.getElementById('kategori').value);
        const rateProg = parseFloat(document.getElementById('program').value);
        const biayaProses = 1250;
        if (!hpp) return alert("Masukkan modal dulu!");
        const totalRatePotongan = rateKat + rateProg + rateVoucher;
        const marginUang = hpp * targetProfitPersen;
        let hargaJual = (hpp + marginUang + biayaProses) / (1 - totalRatePotongan);
        hargaJual = Math.ceil(hargaJual / 100) * 100;
        const potonganFee = hargaJual * (rateKat + rateProg);
        const potonganVoucher = hargaJual * rateVoucher;
        const cuanBersih = hargaJual - potonganFee - potonganVoucher - biayaProses - hpp;
        document.getElementById('resultArea').style.display = 'block';
        document.getElementById('labelHarga').innerText = "Harga Jual untuk Profit " + (targetProfitPersen*100) + "%";
        document.getElementById('resHargaJual').innerText = "Rp " + hargaJual.toLocaleString('id-ID');
        document.getElementById('resFeePersen').innerText = "-Rp " + Math.round(potonganFee).toLocaleString('id-ID');
        document.getElementById('resVoucherValue').innerText = "-Rp " + Math.round(potonganVoucher).toLocaleString('id-ID');
        document.getElementById('resCuan').innerText = "Rp " + Math.round(cuanBersih).toLocaleString('id-ID');
        const strategies = [
            { t: "1. Fokus SEO & Organik", d: "Gunakan harga ini sebagai harga inti tanpa diskon tambahan agar margin tetap terjaga." },
            { t: "2. Strategi Voucher " + (rateVoucher*100) + "%", d: "Budget voucher sudah masuk ke harga jual, berikan secara publik agar pembeli merasa untung." },
            { t: "3. Kombo Hemat (Grosir)", d: "Beri diskon 1-2% untuk beli 2 pcs. Karena biaya proses Rp1.250 flat, profit meningkat jika pembeli beli banyak." },
            { t: "4. Voucher Ikuti Toko", d: "Gunakan nilai Rp2.000 - Rp5.000 sebagai magnet follower." },
            { t: "5. Psikologi Harga Coret", d: "Upload produk harga Rp " + Math.round(hargaJual * 1.25 / 100)*100 + " coret menjadi Rp " + hargaJual.toLocaleString('id-ID') + "." }
        ];
        let html = "";
        strategies.forEach(s => { html += `<div class="strategy-card"><strong>${s.t}</strong>${s.d}</div>`; });
        document.getElementById('strategyContainer').innerHTML = html;
    }
</script>
</body>
</html>
"""

# 4. Tampilkan Komponen HTML
components.html(html_code, height=1400, scrolling=True)
