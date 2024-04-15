# import library
import streamlit as st
from PIL import Image

#membuat function untuk nantinya dipanggil di app.py
def run():
    st.title('Welcome to Explaration Data Analysis')

    # menampilakn berbagai jenis gambar motor dan mobil
    st.subheader('GAMBAR SETIAP KELAS')
    image = Image.open('jenis_mobil_motor.png')
    st.image(image, caption='Berbagai jenis motor')
    image2 = Image.open('jenis_mobil.png')
    st.image(image2, caption='Berbagai jenis mobil')
    # menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('Gambar diatas merupakan beberapa contoh visualisasi motor dan mobil dari berbagai arah, bentuk, dan warna yang menunjukkan variasi dari gambar agar model dapat memprediksi lebih baik.')
        
    # menampilkan sampel 
    st.subheader('SAMPLE BIKE VS CAR')
    image3 = Image.open('sample_motor.png')
    image4 = Image.open('sample_mobil.png')
    st.image(image3, caption='Sample Bike')
    st.image(image4, caption='Sample Car')
    # menampilkan penjelasan
    with st.expander('Explanation'):
        st.caption('Gambar motor memiliki tinggi 100 pixel, lebar 100 pixel, dan terdiri dari 3 saluran warna (RGB). Sedangkan Gambar mobil memiliki tinggi 164 pixel, lebar 306 pixel, dan terdiri dari 3 saluran warna (RGB). Kedua sampel tersebut sama-sama memiliki warna RGB, namun untuk gambar mobil pixelnya lebih tinggi sehingga lebih jelas.')
    
    # menampilkan perbandingan rasio dari gambar sampel
    st.subheader('PERBANDINGAN RASIO GAMBAR SAMPLE')
    image5 = Image.open('perbandingan_rasio.png')
    st.image(image5, caption='Rasio dua gambar sample')
    # menampilkan penjelasan
    with st.expander('Explanation'):
        st.caption('Dari visualisasi aspect ratio comparison antara bike dan car menunjukkan bahwa nilai yang lebih tinggi tersebut lebih panjang atau lebih melebar dalam satu dimensi tertentu. Hal tersebut dapat dilihat sebelumnya bahwa memang gambar mobil terlihat lebih besar dari gambar motor. Jika dilihat secara kualitas, gambar mobil juga terlihat lebih jelas dan tidak buram.')
    
    # menampilkan perbandingan rasio dari gambar sampel
    st.subheader('PERBANDINGAN HOG GAMBAR SAMPLE')
    image6 = Image.open('HOG.png')
    st.image(image6, caption='HOG sample')
    # menampilkan penjelasan
    with st.expander('Explanation'):
        st.caption('Visualisasi HOG ini dapat memberikan ciri-ciri visual yang membedakan antara motor dan mobil agar dapat mengklasifikasi dengan baik.')

    # menampilkan perbandingan rasio dari gambar sampel
    st.subheader('PERBANDINGAN RATA-RATA INTENSITAS WARNA PADA GAMBAR SAMPLE')
    image7 = Image.open('mean_color.png')
    image8 = Image.open('mean_color_car.png')
    st.image(image7, caption='Warna pada bike')
    st.image(image8, caption='Warna pada car')
    # menampilkan penjelasan
    with st.expander('Explanation'):
        st.caption('Berikut adalah rata-rata setiap warna dari car dan bike. Terlihat dari visualisasi sample gambar keduanya memiliki proporsi warna yang hampir seimbang, namun perbedaannya pada gambar sampel mobil intensitas warnanya lebih tinggi dibandingkan gambar sampel motor.')

# Jalankan eda
if __name__ == '__main__':
    run()