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

   prompt= PromptTemplate.from_template(
       """
        You are a helpful assistant that answers questions based only on the YouTube video transcript.

        Context:
        {context}

        Question:
        {question}

        Instructions:
        - Answer only from the given context.
        - If the answer is not present in the context, say: "I could not find this information in the video."
        - Keep the answer clear and concise.

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