PINECONE_API_KEY= "pcsk_2PU4uY_GLFUYDozHwbtaSv64ADBkey8qYV3VGuwqmFnDEQmhttgeUUq7dGcg19eX1LxiEn"
GEMINI_API_KEy= "AIzaSyCv25pgfBSrY22niRI_eLr0pn9UbPnch3o"
GROQ_APT_KEY= "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"

from pinecone import Pinecone
from create_vector import embed_text
from groq import Groq
import streamlit as st

groq_client = Groq(api_key=GROQ_APT_KEY)
pinecone_client = Pinecone(api_key = PINECONE_API_KEY)
vector_index = pinecone_client.Index("student-kb")
st.title("A cool RAG App ")
st.write("This is a simple RAG app that uses Pinecone and Groq")
query =st.text_input("Enter your question please: ")

if query:
    vector = embed_text(query).get("embedding", [])
    response = vector_index.query(vector=vector, top_k=1, include_metadata=True)
    similar_document = response["matches"][0]["metadata"]["text"]
    print("simliar document: ", similar_document)

    prompt = [
        {
            "role":"user",
            "content": f"""You are provided with some document sample which is expected to be most similar document which can be used to answer user query
            Similar Document also take data from worldwide " :
            {similar_document}
            User query: {query}
            """
        }
    ]

    print("prompt ",prompt)
    llm_response= groq_client.chat.completions.create(
        model="llama3-70b-8192",
        messages=prompt,
        max_tokens=500,
        temperature=0.7,

    )
    llm_answer= llm_response.choices[0].message.content
    st.write("Answer: "),llm_answer