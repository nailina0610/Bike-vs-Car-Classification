# import library
import streamlit as st
import eda
import prediction

# membuat pilihan halaman
page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Prediction Model'])

if page == 'Home Page':
    st.header('Welcome Page') 
    st.image('bikeVScar.jpeg')
    st.write('')
    st.write('')
    st.write('Graded Challenge 7')
    st.write('Nama      : Nailina Farah')
    st.write('Batch     : RMT-028')
    st.write('Tujuan    : Program ini dibuat untuk memprediksi antara gambar motor atau mobil')
    st.write('')
    st.caption('Silahkan pilih menu lain di Select Page pada sebelah kiri layar anda untuk melihat EDA dan prediksi gambar!')
    st.write('')
    st.write('')
    with st.expander("Latar Belakang"):
        st.caption('Tugas Graded Challenge 7 untuk membuat model ANN Computer Vision yang dapat memprediksi gambar. Pengembangan sistem klasifikasi gambar untuk membedakan antara motor dan mobil dalam computer vision memungkinkan penerapan praktis dalam pemantauan lalu lintas dan peningkatan keamanan jalan raya.')

    with st.expander("Problem Statement"):
            st.caption('Mengembangkan sebuah model klasifikasi menggunakan deep learning dan teknik computer vision untuk membedakan antara gambar mobil dan motor dalam dataset Car vs Bike Classification, dengan tujuan mencapai tingkat akurasi minimal 80% dalam waktu 1 minggu, yang relevan untuk mengoptimalkan pengenalan objek pada sistem otomatisasi untuk meningkatkan keamanan transportasi dan pengembangan teknologi otonom.')

    with st.expander("Kesimpulan"):
        st.caption('Menggunakan deep learning dan teknik computer vision, telah dikembangkan sebuah model untuk membedakan antara gambar mobil dan motor dalam dataset Car vs Bike Classification. Namun, meskipun akurasi sudah diatas 80%, model belum bisa mengklasifikasi motor dan mobil secara sempurna.')
elif page == 'Exploration Data Analysis':
    eda.run()
else:
    prediction .run()