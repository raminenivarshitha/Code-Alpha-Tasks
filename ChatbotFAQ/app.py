import streamlit as st
from faq import faq

# ---------------- Page Configuration ---------------- #

st.set_page_config(
    page_title="Tech Knowledge FAQ Chatbot",
    page_icon="🤖",
    layout="wide"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>
.main{
    padding-top:1rem;
}

.stChatMessage{
    border-radius:10px;
}

.stButton>button{
    width:100%;
    border-radius:8px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Session ---------------- #

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- Sidebar ---------------- #

with st.sidebar:

    st.title("🤖 Tech FAQ Chatbot")

    st.markdown("### 📚 Available Topics")

    topics = [
        "Artificial Intelligence",
        "Machine Learning",
        "Deep Learning",
        "Generative AI",
        "Prompt Engineering",
        "Cloud Computing",
        "Python",
        "Java",
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "SQL",
        "Database",
        "Data Science",
        "Big Data",
        "Computer Vision",
        "NLP",
        "Cybersecurity",
        "Blockchain",
        "IoT",
        "API",
        "Git",
        "GitHub",
        "Linux",
        "Operating System",
        "Docker",
        "Kubernetes",
        "DevOps",
        "Neural Networks",
        "Algorithms",
        "Data Structures",
        "OOP"
    ]

    for topic in topics:
        st.markdown(f"✅ {topic}")

    st.divider()

    st.metric(
        "Questions Asked",
        len([
            msg for msg in st.session_state.messages
            if msg["role"] == "user"
        ])
    )

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ---------------- Main Page ---------------- #

st.title("💬 Tech Knowledge FAQ Chatbot")

st.write(
    """
Ask questions related to **Computer Science and Information Technology**.

Examples:
- What is AI?
- Explain Machine Learning
- What is Docker?
- What is GitHub?
- Explain APIs
- What is OOP?
"""
)

# ---------------- Chat History ---------------- #

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------- Chat Input ---------------- #

query = st.chat_input("Ask a technology question...")

if query:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    search = query.lower().strip()

    response = None

    for keyword, explanation in faq.items():

        if keyword in search:
            response = explanation
            break

    if response is None:

        response = """
❌ Sorry! I couldn't find information for that topic.

### Try asking about:

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Generative AI
- Prompt Engineering
- Cloud Computing
- Python
- Java
- HTML
- CSS
- JavaScript
- SQL
- Database
- Git & GitHub
- Docker
- Kubernetes
- DevOps
- Cybersecurity
- Blockchain
- IoT
- Computer Vision
- NLP
- Data Science
- Big Data
- OOP
- Algorithms
- Data Structures
"""

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    st.rerun()