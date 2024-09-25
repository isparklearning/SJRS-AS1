import streamlit as st
import pandas as pd
import time
col1, col2 = st.columns(2)
with col1:
    st.image("001.png")
with col2:
    st.subheader("Welcome to Result Portal of St.Joseph Residential School (CBSE) - Sriperumbudur \n Assesment - 1")
d = 0
c = ""
a = st.selectbox( "Select the class?", ("GRADE - 6", "GRADE - 7", "GRADE - 8", "GRADE - 9","GRADE - 10"),)
if (a == "GRADE - 6"):
    c = "6"
elif (a == "GRADE - 7"):
    c = "7"
elif (a == "GRADE - 8"):
    c = "8"
elif (a == "GRADE - 9"):
    c = "9"
elif (a == "GRADE - 10"):
    c = "10"
else:
    d = 1
f = ".xlsx"
e = "Here is the Result of " + a
if st.button("Submit"):
    progress_text = "Searching in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    if d == 1:
        st.warning("Please Select a Valid Class")
    else:
        if d == 1:
            pass
        else:
            st.success('Found!', icon="✅")
        dataframe1 = pd.read_excel(c + f)
        st.write(e)
        st.write(dataframe1)
        with open(c+f, "rb") as template_file:
            template_byte = template_file.read()
            st.download_button(label="Click to Download File as Excel",
                        data=template_byte,
                         file_name=c+f,
                         mime='application/octet-stream')