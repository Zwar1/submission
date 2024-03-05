import streamlit as st
import numpy as np  # Mengimpor NumPy, library yang digunakan untuk manipulasi data numerik, seperti array dan operasi matematika.
import pandas as pd  # Mengimpor pandas, library yang digunakan untuk manipulasi dan analisis data, terutama dalam bentuk DataFrame.
import matplotlib.pyplot as plt  # Mengimpor Matplotlib, library untuk visualisasi data, terutama untuk membuat grafik dan plot.

with st.sidebar:  
  st.header('Dashboard Analisis Data')
  st.text('Muhammad Lazuardi Firdaus')
  st.text('m012d4ky1568@bangkit.academy')


#streamlit dashboard
st.title("Bike Sharing Dataset Analysis")
st.write('Dataset ini berisi jumlah informasi peminjaman sepeda per jam dan harian antara tahun 2011 dan 2012 di sistem peminjaman sepeda di Ibukota dengan informasi cuaca dan musim yang berkaitanm.')

st.header("Data Visualisation")

dh = pd.read_csv("all_data.csv")
st.subheader("5 Data Teratas dari Dataset:")
st.write(dh.head())
st.subheader("5 Data paling terakhir")
st.write(dh.tail())

st.subheader('Pertanyaan 1: Kapan waktu yang baik untuk sekiranya diperlukan perbaikan alat?')
st.write('Untuk mengetahui jawaban tersebut, maka dilakukan analisis data dengan menggunakan bar plot sebagai visualisasi data.')
st.write('Bar Plot:')

plt.figure()
jam = dh['hr']   # Mengambil kolom 'hr' dari DataFrame dh dan menyimpannya ke dalam variabel jam, yang akan digunakan sebagai sumbu x dalam plot.
jumlah = dh['cnt']  # Mengambil kolom 'cnt' dari DataFrame dh dan menyimpannya ke dalam variabel jumlah, yang akan digunakan sebagai sumbu y dalam plot.

plt.bar(jam, jumlah, color='skyblue')  # Membuat plot jenis bar chart dengan menggunakan data dari variabel jam sebagai sumbu x dan data dari variabel jumlah sebagai sumbu y.

plt.title('Pengaruh Waktu terhadap Jumlah Peminjaman Sepeda')  # Menambahkan judul plot untuk memberikan konteks tentang apa yang sedang ditampilkan.
plt.xlabel('Waktu (jam)')  # Menambahkan label sumbu x untuk menjelaskan apa yang diwakilkan oleh sumbu x, dalam hal ini waktu dalam jam.
plt.ylabel('Jumlah Peminjaman')  # Menambahkan label sumbu y untuk menjelaskan apa yang diwakilkan oleh sumbu y, dalam hal ini jumlah peminjaman sepeda.

st.pyplot(plt) # menampilkan plot bar pada streamlit
with st.expander("See explanation"):
    st.write(
        """Dari hasis analisis data yang bisa dilihat dari gambar diatas, terdapat waktu dengan jumlah peminjaman yang cukup rendah pada rentang pukul 23.00-07.00. 
        Dimana jumlah peminjaman dibawah 300, dan itu bisa dimanfaatkan sebagai waktu untuk perbaikan sepeda jika diperlukan. Karena dengan peminjaman sepeda yang sedikit 
        artinya potensi terganggunya sistem peminjaman ketika ada unit yang perlu diperbaiki lebih minim.
        """
    )


st.subheader('Pertanyaan 2 : Bagaimana kita bisa mengetahui kapan dan digunakan untuk apakah peminjaman sepeda?')
st.write('Untuk mengetahui jawaban tersebut, kita akan membandingkan jumlah peminjaman sepeda tiap harinya dalam satu minggu, dan menggunakan plot bar untuk memvisualisasikan hasilnya.')
st.write('Bar Plot : ')

plt.figure()
hari = dh['weekday']  # Mengambil kolom 'weekday' dari DataFrame dh dan menyimpannya ke dalam variabel hari, yang akan digunakan sebagai sumbu x dalam plot.

plt.bar(hari, jumlah, color='skyblue')  # Membuat plot jenis bar chart dengan menggunakan data dari variabel hari sebagai sumbu x dan data dari variabel jumlah sebagai sumbu y.

plt.title('Pengaruh hari terhadap jumlah peminjaman sepeda')  # Menambahkan judul plot untuk memberikan konteks tentang apa yang sedang ditampilkan.
plt.xlabel('Hari ke-')  # Menambahkan label sumbu x untuk menjelaskan apa yang diwakilkan oleh sumbu x, dalam hal ini hari.
plt.ylabel('Jumlah Peminjaman')  # Menambahkan label sumbu y untuk menjelaskan apa yang diwakilkan oleh sumbu y, dalam hal ini jumlah.

st.pyplot(plt)  # Menampilkan plot yang telah dibuat.
with st.expander("See explanation"):
    st.write(
        """Dari gambar diatas bisa dilihat bahwa pada hari ke-0 dan hari ke-6 atau hari weekend peminjaman sepeda lebih sedikit dari hari lainnya, 
        ini sapat mengindikasikan jika biasanya peminjaman sepeda digunakan sebagai transportasi untuk kegiatan sehari-hari, seperti berangkat ke kantor 
        ataupun sekolah, dibanding dengan hari weekend yang biasanya digunakan masyarakat untuk berlibur.
        """
    )