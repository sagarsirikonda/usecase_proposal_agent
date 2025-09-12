import streamlit as st
from proposal_crew.crew import run_proposal_crew

# --- CUSTOM STYLING (CSS) ---
# This CSS will be injected into the Streamlit app for a custom look and feel.
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Create a 'style.css' file in the same directory with the content below
# Or, for simplicity, we can define the style directly in the Python script.
st.markdown("""
<style>
    /* Main app background */
    .stApp {
        background-color: #0d1b2a; /* A dark navy blue */
        color: #e0e1dd; /* Off-white text */
    }

    /* Sidebar styling */
    .st-emotion-cache-16txtl3 {
        background-color: #1b263b; /* A slightly lighter navy */
    }

    /* Input box styling */
    .stTextInput>div>div>input {
        background-color: #415a77;
        color: #e0e1dd;
        border-radius: 10px;
    }

    /* Button styling */
    .stButton>button {
        background-color: #0077b6; /* Vibrant blue */
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #0096c7; /* Lighter blue on hover */
        color: white;
    }

    /* Headers */
    h1, h2, h3 {
        color: #ade8f4; /* Light vibrant blue for headers */
    }

    /* Markdown output styling */
    .stMarkdown {
        background-color: #1b263b;
        padding: 20px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.title("🤖 Control Panel")
st.sidebar.image("https://www.gstatic.com/lamda/images/gemini/google_gemini_3_1920x1080_0a2c035f29d1012e105342a17058a98f.jpg")
st.sidebar.info("Enter a company or industry below and click 'Generate Proposal' to start.")

company_input = st.sidebar.text_input(
    "Company or Industry Name:",
    placeholder="e.g., 'NVIDIA'"
)

# --- MAIN PAGE ---
st.title("🤖 GenAI Use Case Generator")

if st.sidebar.button("Generate Proposal"):
    if not company_input:
        st.sidebar.warning("Please enter a company or industry name.")
    else:
        st.info(f"🚀 Kicking off the analysis for: **{company_input}**")
        
        with st.spinner("The AI Crew is assembling and beginning its mission... This may take a few minutes."):
            # Run the crew
            proposal_result = run_proposal_crew(company_input)

        st.success("Proposal Generated Successfully!")
        
        st.subheader("Your AI-Generated Proposal:")
        st.markdown(proposal_result)

        # Download button
        file_name = f"{company_input.replace(' ', '_').lower()}_ai_proposal.md"
        st.sidebar.download_button(
            label="⬇️ Download Proposal",
            data=proposal_result,
            file_name=file_name,
            mime="text/markdown",
        )
else:
    st.info("Your generated proposal will appear here once the analysis is complete.")