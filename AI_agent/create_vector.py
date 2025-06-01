from pinecone import Pinecone
import fitz
import google.generativeai as genai
import os
PINECONE_API_KEY= "pcsk_2PU4uY_GLFUYDozHwbtaSv64ADBkey8qYV3VGuwqmFnDEQmhttgeUUq7dGcg19eX1LxiEn"
GEMINI_API_KEy= "AIzaSyCv25pgfBSrY22niRI_eLr0pn9UbPnch3o"

def extrac_text_from_pdf(pdf_path):
    text=""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text() + "\n"
    return text
model = "models/text-embedding-004"

genai.configure(api_key=GEMINI_API_KEy)

def embed_text(text):
    response = genai.embed_content(
        model=model,
        content=text,
        task_type="retrieval_document"
    )
    return response

pinecone_client = Pinecone(api_key=PINECONE_API_KEY)

vector_index = pinecone_client.Index("student-kb")

def upsert_vector_to_pinecone(document_text):
    upsert_data = []
    for idx, (file,text) in enumerate(document_text.items()):
        vector =  embed_text(text).get("embedding", [])
        meta_data = {
            "text":text,

        }
        upsert_data.append((f"doc-{idx}", vector,meta_data))

        vector_index.upsert(upsert_data)
        print("Vectors upserted successfully.")

if __name__== "__main__":
    document_text ={}

    for file in os.listdir("documents"):
        text= extrac_text_from_pdf("documents/" + file)
        document_text[file] = text
    upsert_vector_to_pinecone(document_text)
    print("All documents processed and vectors upserted.")


