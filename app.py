import streamlit as st

from utils.transcript import get_transcript
from utils.embedder import build_vectorstore
from utils.qa_chain import get_answer


st.set_page_config(
    page_title="YouTube Q&A Bot",
    layout="centered"
)

st.title("🎥 YouTube Video Q&A Bot")

st.write(
    "Paste a YouTube video URL, process the transcript, and ask questions about the video."
)


if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "video_url" not in st.session_state:
    st.session_state.video_url = ""


youtube_url = st.text_input(
    "Paste YouTube URL here"
)

process_button = st.button(
    "Process Video"
)

if process_button:

    with st.spinner(
        "Extracting transcript and building knowledge base..."
    ):

        transcript_text=get_transcript(youtube_url)

        if transcript_text.startswith("Error:") or transcript_text== "Invalid YouTube URL":

            st.error(transcript_text)

            st.session_state.vectorstore=None
        
        else:
             vectorstore= build_vectorstore(transcript_text)

             st.session_state.vectorstore= vectorstore

             st.session_state.video_url= youtube_url

             st.success("Video processed successfully!")


    


# ✅ Q&A SECTION process_button ke bahar hona chahiye
st.divider()

st.subheader("Ask Questions")

question = st.text_input(
    "Ask anything about this video"
)

ask_button = st.button(
    "Ask Question"
)

if ask_button:

    if question.strip() == "":
        st.warning("Please enter a question.")

    elif st.session_state.vectorstore is None:
        st.warning("Please process a YouTube video first.")

    else:

        with st.spinner("Generating answer..."):

            answer = get_answer(
                question,
                st.session_state.vectorstore
            )

        st.markdown("### 🤖 Answer")

        st.info(answer)