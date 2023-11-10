import pandas as pd

# Baca data dari file CSV
data = pd.read_csv("pizza.csv")

# Konversi kolom "order_date" ke datetime
data['order_date'] = pd.to_datetime(data['order_date'])

# Ekstrak bulan dari kolom "order_date"
data['bulan'] = data['order_date'].dt.strftime('%Y-%m')

# Kelompokkan data per bulan dan hitung total penjualan pizza untuk setiap jenis pizza
monthly_sales = data.groupby(['bulan', 'pizza_name'])['quantity'].sum().reset_index()

# Hitung rata-rata penjualan pizza untuk setiap jenis pizza dalam 12 bulan terakhir
monthly_sales['12bulan_moving_avg'] = monthly_sales.groupby('pizza_name')['quantity'].rolling(12).mean().reset_index(level=0, drop=True)

# Ambil data penjualan untuk bulan terakhir dalam data
last_month_data = monthly_sales[monthly_sales['bulan'] == monthly_sales['bulan'].max()]

# Prediksi penjualan untuk bulan depan berdasarkan rata-rata penjualan 12 bulan terakhir
predictions = last_month_data[['pizza_name', '12bulan_moving_avg']]

# Urutkan hasil prediksi dari yang terbesar ke yang terkecil
predictions_sorted = predictions.sort_values(by='12bulan_moving_avg', ascending=False)

# Tampilkan hasil prediksi yang sudah diurutkan
print("Prediksi Penjualan Pizza untuk Bulan Depan (berdasarkan 12 bulan terakhir) - Diurutkan:")
print(predictions_sorted)
