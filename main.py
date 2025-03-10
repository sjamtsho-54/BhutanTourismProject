import streamlit as st

pages = [
    st.Page("home.py", title="Home"),
    st.Page("graphs.py", title="Project Details"),
    st.Page("prediction.py", title="Prediction")
]

pg = st.navigation(pages)
pg.run()
        