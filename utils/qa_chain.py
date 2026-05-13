from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


def format_docs(docs):
  return "\n\n".join(doc.page_content for doc in docs)


def get_answer(question, vectorstore):
   """
    Takes user question and FAISS vectorstore.
    Retrieves relevant transcript chunks.
    Generates answer using modern LCEL chain.
    """
   retriever= vectorstore.as_retriever(
      
      search_kwargs={"k": 4}
   )

   docs=retriever.invoke(question)
   
   context= format_docs(docs)

  #  print("\nRETRIEVED CONTEXT:\n")
  #  print(context[:1000])




   prompt= PromptTemplate.from_template(
       """
You are an AI assistant answering questions strictly from a YouTube video transcript.

Transcript Context:
{context}

User Question:
{question}

Answering Rules:
- Use only the transcript context provided above.
- Give a clear and direct answer.
- If the question asks for a summary, summarize the main points from the transcript.
- If the answer is not available in the transcript context, say:
  "I could not find this information in the video."
- Do not make up facts.
- Keep the answer simple and helpful.

Answer:
"""
   )

   llm= ChatOpenAI(model="gpt-4o-mini")

   chain=prompt | llm | StrOutputParser()

   answer= chain.invoke(
      {
         "context":context,
         "question":question
      }
   )

   return answer

