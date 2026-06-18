import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import streamlit as st
from yourrights.crew import Yourrights

st.set_page_config(
    page_title="YourRights",
    layout="wide"
)

st.title("YourRights")
st.subheader("Know Your Pakistani Legal Rights")
st.markdown("Describe your situation in plain language and get clear guidance on your legal rights.")
st.divider()

left_col, right_col = st.columns([1, 1])

with left_col:
    st.markdown("### Your Situation")
    situation = st.text_area(
        "Describe your situation:",
        placeholder="Example: My landlord locked my room without a court order because I was late on rent...",
        height=300,
        label_visibility="collapsed"
    )
    submit = st.button("Know My Rights", type="primary", use_container_width=True)

with right_col:
    st.markdown("### Your Rights")
    if submit:
        if not situation.strip():
            st.warning("Please describe your situation first.")
        else:
            with st.spinner("Analyzing your situation and searching Pakistani laws..."):
                try:
                    inputs = {"situation": situation}
                    result = Yourrights().crew().kickoff(inputs=inputs)
                    st.markdown(str(result))
                    st.divider()
                    st.caption("This is for informational purposes only, not legal advice.")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
    else:
        st.info("Your legal rights analysis will appear here after you describe your situation.")