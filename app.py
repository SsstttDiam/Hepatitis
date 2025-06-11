import streamlit as st
import numpy as np
import joblib

# Memuat model yang sudah dilatih
model = joblib.load('hepatitis_model.pkl')

st.title("Prediksi Status Pendonor Darah")

# Form input untuk data pengguna
with st.form("Form_hepatitis"):
    st.header("Masukkan Data Pasien:")
    
    # Input field sesuai dengan fitur di dataset HepatitisCdata.csv
    age = st.number_input('Usia', min_value=1, max_value=120)
    sex = st.selectbox('Jenis Kelamin', ['female', 'male'])
    alb = st.number_input('Albumin (ALB)', min_value=0.0, format="%.2f")
    alp = st.number_input('Alkaline Phosphatase (ALP)', min_value=0.0, format="%.2f")
    alt = st.number_input('Alanine Aminotransferase (ALT)', min_value=0.0, format="%.2f")
    ast = st.number_input('Aspartate Aminotransferase (AST)', min_value=0.0, format="%.2f")
    bil = st.number_input('Bilirubin (BIL)', min_value=0.0, format="%.2f")
    che = st.number_input('Cholinesterase (CHE)', min_value=0.0, format="%.2f")
    chol = st.number_input('Cholesterol (CHOL)', min_value=0.0, format="%.2f")
    crea = st.number_input('Creatinine (CREA)', min_value=0.0, format="%.2f")
    ggt = st.number_input('Gamma Glutamyl Transferase (GGT)', min_value=0.0, format="%.2f")
    prot = st.number_input('Protein Total (PROT)', min_value=0.0, format="%.2f")
    
    submit = st.form_submit_button("Proses")

# Ketika tombol submit ditekan
if submit:
    # Encode jenis kelamin: female=0, male=1
    sex_encoded = 0 if sex == 'female' else 1

    # Susun fitur sesuai urutan model
    features = np.array([[age, sex_encoded, alb, alp, alt, ast, bil, che, chol, crea, ggt, prot]])

    # Lakukan prediksi
    prediction = model.predict(features)[0]

    st.header("Hasil Prediksi")
    if prediction == 0:
        st.success("Hasil: Pasien adalah Pendonor Darah")
    else:
        st.error("Hasil: Pasien BUKAN Pendonor Darah (mungkin Hepatitis / Risiko Lain)")
