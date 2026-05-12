from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import os

load_dotenv()


def build_vectorstore(transcript_text):

  text_splitter= RecursiveCharacterTextSplitter(

    chunk_size=500,

    chunk_overlap=50
  )

  chunks= text_splitter.create_documents([transcript_text])

  embeddings= OpenAIEmbeddings()

  vectorstore=FAISS.from_documents(

    chunks,

    embeddings

  )
  return vectorstore

if __name__ == "__main__":

  sample_text="AI is transforming healthcare. " * 100

  vectorstore= build_vectorstore(sample_text)

  print(vectorstore)
