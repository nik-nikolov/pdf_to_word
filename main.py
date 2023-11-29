import os
import streamlit as st
from pdf2docx import Converter
import tempfile

temp_dir = tempfile.TemporaryDirectory()
st.write(temp_dir.name)


def pdf_to_word(pdf_file_path):
    # Convert PDF to DOCX using pdf2docx
    docx_file_path = pdf_file_path.replace('.pdf', '.docx')
    cv = Converter(pdf_file_path)
    cv.convert(docx_file_path)
    cv.close()
    return docx_file_path


st.title("PDF to Word Converter with OCR")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
if uploaded_file is not None:
    st.write("Converting... Please wait.")
    with open(os.path.join(temp_dir.name, uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("Saved File")
    uploaded_file_path = os.path.join(temp_dir.name, uploaded_file.name)
    docx_file_name = uploaded_file.name.replace('.pdf', '.docx')
    converted_docx = pdf_to_word(uploaded_file_path)
    st.write("Conversion complete!")

    # Offer download link for the converted Word file
    with open(converted_docx, 'rb') as f:
        st.download_button(
            label="Download Converted Word File",
            file_name=docx_file_name,
            data=f,
            key="word_file",
            help="Click to download the converted Word file.",
        )
