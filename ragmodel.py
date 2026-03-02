import faiss
from groq import Groq
import os
import PyPDF2
import numpy as np
import pickle

#API key setup
client = Groq(api_key=os.getenv(""))

def pdf_to_vectors(pdf_path):
    print("Reading PDF: ", pdf_path)
    with open(pdf_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        total_pages = len(pdf_reader.pages)
        #print(total_pages) 

        page_texts = []
        for page_num, page in enumerate(pdf_reader.pages):
            page_text = page.extract_text()
            page_texts.append({
                'text': page_text,
                'page_number': page_num+1
            })
        
        text = ''.join([p['text'] for p in page_texts])
    
    print("Total pages: ", total_pages)
    print("total text length: ", len(text))
    print("Average characters per page: ", len(text)//total_pages)


    chunks=[]
    chunk_metadata =[]

    for i in range(o, len(text), 400):
        chunk_text = text[i:i+500]
        


#text = pdf_to_vectors("Bevolution Audit SOP.pdf")
#print(text[:1000])
