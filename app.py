import streamlit as st

st.header('Calculator App')

st.write('This is a calculator application developed in using Streamlit')

#btn=st.button('Click Me')
#if btn:
    #st.balloons()

num1=st.number_input('Enter the first number')  
option=st.selectbox('Select the operation',("+","-","*","/"))
num2=st.number_input('Enter the second number')  
btn2=st.button('Calculate')
if btn2:
    if option=="+":
        st.subheader(f'Added result is {num1+num2}')
    elif option=="-":
        st.subheader(f'Subtracted result is {num1-num2}')  
    elif option=="*":
        st.subheader(f'Multiplied result is {num1*num2}')   
    elif option=="/":
        st.subheader(f'Devision result is {num1/num2}')