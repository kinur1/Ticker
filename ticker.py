import streamlit as st
import pandas as pd

# Data Ticker Cryptocurrency dengan Deskripsi
crypto_data = {
    "Ticker": ["BTC-USD", "ETH-USD", "BNB-USD", "ADA-USD", "XRP-USD", "SOL-USD", 
               "DOGE-USD", "DOT-USD", "MATIC-USD", "LTC-USD", "SHIB-USD", "AVAX-USD", 
               "UNI-USD", "LINK-USD", "XLM-USD", "ATOM-USD", "TRX-USD", "ETC-USD", 
               "ICP-USD", "FIL-USD"],
    "Name": ["Bitcoin", "Ethereum", "Binance Coin", "Cardano", "XRP", "Solana", 
             "Dogecoin", "Polkadot", "Polygon", "Litecoin", "Shiba Inu", "Avalanche", 
             "Uniswap", "Chainlink", "Stellar", "Cosmos", "TRON", "Ethereum Classic", 
             "Internet Computer", "Filecoin"],
    "Description": [
        "Bitcoin: Cryptocurrency pertama dan paling terkenal, diciptakan oleh Satoshi Nakamoto, digunakan sebagai penyimpan nilai dan alat transaksi.",
        "Ethereum: Platform blockchain yang mendukung smart contracts dan aplikasi terdesentralisasi, menggunakan Ether sebagai mata uang asli.",
        "Binance Coin: Mata uang asli dari Binance Exchange yang digunakan untuk diskon biaya trading dan transaksi dalam ekosistem Binance.",
        "Cardano: Platform blockchain yang fokus pada keamanan dan skalabilitas dengan konsensus Proof of Stake, mata uangnya adalah ADA.",
        "XRP: Cryptocurrency dari Ripple Labs yang dirancang untuk transaksi lintas batas yang cepat dan biaya rendah.",
        "Solana: Blockchain yang dikenal dengan kecepatan tinggi dan biaya rendah, mendukung aplikasi terdesentralisasi dan DeFi.",
        "Dogecoin: Awalnya dibuat sebagai lelucon, kini Dogecoin adalah cryptocurrency populer dengan komunitas yang aktif.",
        "Polkadot: Platform multi-chain yang memungkinkan interoperabilitas antara blockchain yang berbeda, didesain oleh Gavin Wood.",
        "Polygon: Solusi layer-2 untuk Ethereum yang meningkatkan kecepatan dan mengurangi biaya transaksi di jaringan Ethereum.",
        "Litecoin: Dibuat sebagai versi 'ringan' dari Bitcoin, dirancang untuk transaksi yang lebih cepat dan biaya yang lebih rendah.",
        "Shiba Inu: Token berbasis komunitas yang mirip dengan Dogecoin, populer di kalangan investor cryptocurrency baru.",
        "Avalanche: Blockchain yang mendukung smart contracts dan aplikasi DeFi, terkenal dengan kecepatan transaksi yang tinggi.",
        "Uniswap: Pertukaran terdesentralisasi di Ethereum yang memungkinkan pertukaran token tanpa pihak ketiga.",
        "Chainlink: Jaringan oracle terdesentralisasi yang menyediakan data dunia nyata untuk smart contracts di blockchain.",
        "Stellar: Jaringan yang dirancang untuk pembayaran lintas batas, terutama untuk mata uang fiat dan stablecoin.",
        "Cosmos: Proyek yang bertujuan untuk menciptakan jaringan blockchain yang saling terhubung untuk skalabilitas tinggi.",
        "TRON: Platform yang memungkinkan pengembangan aplikasi hiburan berbasis blockchain dengan biaya rendah.",
        "Ethereum Classic: Versi awal Ethereum setelah hard fork pada 2016, mendukung smart contracts.",
        "Internet Computer: Platform cloud terdesentralisasi yang memungkinkan aplikasi web berjalan di blockchain.",
        "Filecoin: Jaringan penyimpanan terdesentralisasi yang memungkinkan penyimpanan dan pengambilan data dengan sistem token."
    ]
}

# Convert to DataFrame
crypto_df = pd.DataFrame(crypto_data)

# Streamlit Layout
st.title("Daftar Ticker Cryptocurrency dengan Deskripsi")
st.write("Berikut adalah beberapa cryptocurrency populer beserta deskripsi singkatnya:")

# Display DataFrame as a table in Streamlit
st.table(crypto_df)
