import sys
from pathlib import Path

# Add the 'src' directory to the Python path
src_path = str(Path(__file__).parent.parent)
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# Your original imports remain below
from yourrights.crew import Yourrights
import streamlit as st


st.set_page_config(
    page_title="YourRights",
    layout="centered"
)

st.title("YourRights")
st.subheader("Know Your Pakistani Legal Rights")
st.markdown("Describe your situation in plain language and get clear guidance on your legal rights.")

st.divider()

situation = st.text_area(
    "Describe your situation:",
    placeholder="Example: My landlord locked my room without a court order because I was late on rent...",
    height=150
)

if st.button("Know My Rights", type="primary"):
    if not situation.strip():
        st.warning("Please describe your situation first.")
    else:
        with st.spinner("Analyzing your situation and searching Pakistani laws..."):
            try:
                inputs = {"situation": situation}
                result = Yourrights().crew().kickoff(inputs=inputs)
                st.divider()
                st.markdown("## Your Rights")
                st.markdown(str(result))
                st.divider()
                st.caption("This is for informational purposes only, not legal advice.")
            except Exception as e:
                st.error(f"An error occurred: {e}")