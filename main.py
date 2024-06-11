import streamlit as st
import pandas as pd

st.title("Test streamlit")
st.write("Test")

st.markdown("## my markdown")
code = '''def hello():
    print("Hello, Streamlit!")'''

show_btn = st.button("show code")
if show_btn: 
    st.code(code, language='python')

cols = st.columns(2)
with cols[0]:
    age_inp = st.number_input("Input your age")
    st.markdown(f"Your age is{age_inp}")


#st.markdown("# NLP task")
with cols[1]:
    text_inp = st.text_input("Input your text")
    word_tokenize = "|".join(text_inp.split())
    st.markdown(f"{word_tokenize}")


df = pd.DataFrame({
   'first column': [1,2,3,4],
   'second column': [10,20,30,40]
})
st.dataframe(df)
show_chart_btn = st.button("Show Chart")
if show_chart_btn:
    st.line_chart(df,x='first column' , y='second column' )