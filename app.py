import streamlit as st
st.title('Max of Three Numbers')

a = st.number_input('Enter First number')
st.write('The first number is ', a)

b = st.number_input('Enter Second number')
st.write('The second number is ', b)

c = st.number_input('Enter Third number')
st.write('The third number is ', c)

def max(a,b,c):
    if a>b:
        if a>c :
            return a
        else:
            return c
    else:
        if b>c :
            return b
        else:
            return c
st.subheader('The Maximum of Three is ', max(10,6,4))

