import streamlit as st
import google.generativeai as genai

api_key=st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

col1,col2=st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Furkan Ayakdas")
with col2:
    st.image("Images/me6.png")

st.title(" ")
persona=""" You are Furkan AI bot. You help people answer questions about your self (i.e Furkan) Answer as if you are responding . dont answer in second or third person.
If you don't know they answer you simply say "That's a secretHere is more info about Furkan:
I am a senior student in the computer engineering department. Advanced Python, Flask, Tensorflow, 
OpenCV, C, C ++, C#, Asp .NET, .NET MAUI, JavaScript, Java, JSP, Spring, Mongodb, Postgresql, SQL Server. 
My Project participated in the smart transportation competition as the last project in Teknofest 2022. My 
project was published in 5th ICONSEC transactions. Another project I developed with IoT-based 
autonomous systems received support from TUBITAK 2209-A in 2023. I'm trying to improve myself. I 
have a compulsory summer internship this year and then I have a long -term internship. I believe that I 
can improve myself more and contribute to you during my internship."""
st.title("Furkan's AI Bot")
user_question=st.text_input("Ask anything about me")
if st.button("ASK",use_container_width=400):
    prompt=persona+"Here is the question that the user asked: "+user_question
    response=model.generate_content(prompt)
    st.write(response.text)

col1,col2=st.columns(2)
with col1:
    st.subheader("Youtube Channel")
    st.write("- Largest network channel")
    st.write("- 1k Subscribers")

with col2:
    st.video("https://youtu.be/iaAWMAVsYQM?si=-fPemDSOlSHoK670")

#st.title(" ")
#st.title("My Achievements")
#st.image("Images/me4.png")

st.write(" ")
st.title("My Achievements")
col1,col2,col3=st.columns(3)
with col1:
    st.image("Images/cef1.png")
    st.image("Images/cef2.png")
    st.image("Images/cef3.png")
with col2:
    st.image("Images/cef4.png")
    st.image("Images/cef5.png")
    #st.image("Images/me4.png")
#with col3:
 #   st.image("Images/me4.png")
  #  st.image("Images/me2.png")
   # st.image("Images/me5.png")

st.write(" ")
st.title("My Skills")
st.slider("Python",0,100,90)
st.slider("Flask",0,100,90)
st.slider("Tensorflow",0,100,60)
st.slider("OpenCV",0,100,70)
st.slider("Machine Learning",0,100,70)
st.slider("Data Science",0,100,70)
st.slider("Computer Vision",0,100,60)
st.slider("ASP.NET",0,100,90)
st.slider("Java",0,100,90)
st.slider("JSP",0,100,90)
st.slider("Postgresql",0,100,90)
st.slider("Tensorflow",0,100,90)
st.slider("Mongodb",0,100,50)
st.slider("PL-SQL",0,100,65)

# st.file_uploader("Upload a file")

st.subheader(" ")
st.title("CONTACT")
st.write("furkan.ayakdas20@gmail.com")
st.write("https://www.linkedin.com/in/furkan-ayakda%C5%9F-4001771b8/")
st.write("https://github.com/furkan0920")
