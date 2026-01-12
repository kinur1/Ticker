import streamlit as st
import pandas as pd
import datetime as dt

st.set_page_config(page_title="Ticker Crypto", layout="wide")

@st.cache_data(ttl=60*60)  # cache 1 jam
def fetch_yahoo_crypto_table():
    url = "https://finance.yahoo.com/crypto"
    tables = pd.read_html(url)          # ambil tabel dari halaman
    df = tables[0]                      # biasanya tabel pertama adalah daftar crypto
    # Standarisasi nama kolom (kadang Yahoo berubah format)
    df.columns = [str(c).strip() for c in df.columns]

    # Pastikan kolom minimal ada (umum: Symbol, Name, Price, Change, % Change, Volume, Market Cap)
    # Kalau kolom sedikit beda, tetap tampilkan semua yang ada.
    return df

def safe_fetch():
    try:
        return fetch_yahoo_crypto_table(), None
    except Exception as e:
        return None, str(e)

st.title("📌 Daftar Ticker Crypto (Yahoo Finance)")

# Tombol refresh (clear cache)
colA, colB, colC = st.columns([1, 1, 3])
with colA:
    if st.button("🔄 Refresh Data"):
        st.cache_data.clear()
with colB:
    st.caption(f"Update: {dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

df, err = safe_fetch()

if err:
    st.error("Gagal mengambil data dari Yahoo Finance. Pastikan ada internet.")
    st.code(err)
    st.stop()

# --- Kontrol filter / pencarian ---
c1, c2, c3 = st.columns([2, 1, 1])
with c1:
    q = st.text_input("🔎 Cari (symbol / nama)", "")
with c2:
    only_usd = st.checkbox("Hanya pair -USD", value=True)
with c3:
    view_mode = st.selectbox("Mode tampilan", ["Tabel", "Kartu"])

# --- Filter data ---
df_show = df.copy()

# Kolom yang umum dipakai
symbol_col = "Symbol" if "Symbol" in df_show.columns else df_show.columns[0]
name_col = "Name" if "Name" in df_show.columns else None

if only_usd:
    df_show = df_show[df_show[symbol_col].astype(str).str.endswith("-USD", na=False)]

if q.strip():
    q_low = q.strip().lower()
    mask_symbol = df_show[symbol_col].astype(str).str.lower().str.contains(q_low, na=False)
    if name_col:
        mask_name = df_show[name_col].astype(str).str.lower().str.contains(q_low, na=False)
        df_show = df_show[mask_symbol | mask_name]
    else:
        df_show = df_show[mask_symbol]

st.caption(f"Total tampil: **{len(df_show)}** ticker")

# --- Tampilkan ---
if view_mode == "Tabel":
    st.dataframe(df_show, use_container_width=True, hide_index=True)
else:
    # Mode kartu sederhana (mirip list)
    cols = df_show.columns.tolist()
    for _, row in df_show.head(200).iterrows():  # batasi biar ringan
        sym = row.get(symbol_col, "")
        nm = row.get(name_col, "") if name_col else ""
        price = row.get("Price (Intraday)", row.get("Price", ""))
        chg = row.get("Change", "")
        pct = row.get("% Change", row.get("Change %", ""))
        mcap = row.get("Market Cap", "")
        vol = row.get("Volume in Currency (Since 0:00 UTC)", row.get("Volume", ""))

        st.markdown(
            f"""
            <div style="padding:12px;border:1px solid #ddd;border-radius:12px;margin-bottom:10px;">
              <div style="font-size:18px;font-weight:700;">{sym} <span style="font-weight:400;color:#666;">{nm}</span></div>
              <div style="margin-top:6px;">
                <b>Price:</b> {price} &nbsp; | &nbsp;
                <b>Change:</b> {chg} ({pct}) &nbsp; | &nbsp;
                <b>Vol:</b> {vol} &nbsp; | &nbsp;
                <b>MCAP:</b> {mcap}
              </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.info("Mode kartu dibatasi 200 item pertama supaya tidak berat.")
