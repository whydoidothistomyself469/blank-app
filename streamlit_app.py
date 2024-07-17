import streamlit as st
from streamlit_option_menu import option_menu
import os
import json
import requests
from streamlit_lottie import st_lottie


    # lottie functions
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_lottieurl1(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_lottieurl2(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_lottieurl3(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_lottieurl4(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_lottieurl5(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_lottieurl6(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_lottieurl7(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_lottieurl8(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_lottieurl9(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    
#Asset Loading
lottie_code = load_lottieurl("https://lottie.host/955f90b2-a0a2-4647-9a7c-a12e1f04c6f9/7dOqAtKMxJ.json")
lottie_code2 = load_lottieurl1("https://lottie.host/a26b6b4e-7c3a-41ba-8ec3-0d54ae90070a/v4N8U37Cyx.json")
lottie_code3 = load_lottieurl2("https://lottie.host/39c9533b-39c2-40c6-a041-377035faab29/Sb3Or2oouS.json")
lottie_code4 = load_lottieurl3("https://lottie.host/24d25b16-55c9-4f45-906a-1ff1ba8d402c/2tdFK6rIvd.json")
lottie_code5 = load_lottieurl4("https://lottie.host/dbdc5b63-ea04-4ae5-9707-7758b65063f0/nJoSRHvluR.json")
lottie_code6 = load_lottieurl5("https://lottie.host/ab9a7b77-b0af-408b-9bf9-09bd2f0cdd41/oPztphH0VT.json")
lottie_code7 = load_lottieurl6("https://lottie.host/8fc9d936-c7f8-4a21-9e60-fa74fa5b3d84/MsZcCAmLd8.json")
lottie_code9 = load_lottieurl9("https://lottie.host/f7438fcf-55ae-4228-82c2-f6b6fe81c185/ClwXahRlZ7.json")


st.set_page_config(
        page_title="Dennis's Portfolio👋",
)

def home():
    
#About Me
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Me! 🤖")
        st.write("Born in 2008. I am a student from Compassvale Secondary School. A hobby of mine is to explore new places, tinker around with digital circuits and creating things in python. ")
        st.write("As a person who loves to tackle problems, no matter the difficulty, this has tremendously built up my critical thinking skills. These skills are crucial in Electronics and Computer Engineering, where solving problems, whether it’s debugging a program or troubleshooting circuits, is common.")
        st.write("The first instance where my interest in Electronics and Computer Engineering sparked was in Secondary School. When I first too.")
        st.write(".")
        st.write("When I was in Secondary 2, I received the PLD in the form of a laptop. This re-ignited my interest in programming. I knew already that I wanted to be apart of it in some way.")

    with right_column:
        st_lottie(lottie_code, height = 400, key = "computer")
        st_lottie(lottie_code2, height = 500, key = "phone")   

def val():
    left_column2, right_column2 = st.columns(2)
    with left_column2:
       st.write("---")
       st.header("Experiences & Values👤")
       st.write("Values are reaped from experience.")
       st.write("From my experiences so far, I learnt many values but the most important to me were resilience, responsibility and creativity.")
       st.write("I learned these values from the many competitions I participated in, especially in the IDE 2023 Competition. The Robotics CCA in my school, being a new CCA, was underfunded and we were using old models such as NXT. We even faced problems due to how outdated the models were such as the robot not being able to move straight")
       st.write("However, as the team's leader and coder, I worked tirelessly even staying back in school to fix the problem. Yet, I was unable to fix it.")
       st.write("This did not deter me, I entered the competition doing everything in my power to fix it within the time period. In the end, I manage to fix it at the cost of losing speed which ended up causing us to lose the competiton. However, I left relieved that I did not give up.")
    with right_column2:
       st_lottie(lottie_code4, height = 400, key = "idk")

def achievements():
  #Why do they make centering so hard  
    left_column3, right_column3 = st.columns((2, 3))
    with left_column3:
        st.write("---")
        st.title("Achievements🏅")
        st.write(
        """
        - Commendation Award For Temasek Poly Engineering (Sec 4, 2024)
        - Service Award, Chairperson Of Robotics (Sec 4, 2024)
        - EAGLES Edusave Award (Sec 3, 2023)
        - Top In Electronics (Sec 3, 2023)
        """)
 
        st.title("Self Enchrichment")
        st.write(
        """
        - Sec 1 Cyberwellness Quest
        - Sec 2 Cyberwellness Quest
        - Applied Learning Module: Outsmart The Hacker (At Republic Poly)
        - Industry and Skills Exposure Day
        - S1-02 Python Code Camp For Beginners (CodingLab)
        - Volunteered at Bethesda Care Old Folk's Home
        """)

    with right_column3:
        st.write("---")
        st.title("Participations 🖐")
        st.write(
        """
        - 3 Years Worth Of Robotics Competitions 
        (IDE 2021, IDE 2022, NRC 2022, IDE 2023)
        - Participated in Math Kangaroo
        - Participated in Stem-X
        """)
    with right_column3:
        st_lottie(lottie_code5, height = 400, key = "award")

def projects():
    left_column4, right_column4 = st.columns((3, 2))
    with right_column4:
        st.write("---")
        st.title("One thing I made using ICT")
        st.write(
           """
           One thing I made using ICT..
           Is this! I made it from scratch using Python!
           I started on 11/7/2024, where I downloaded the python packages I needed and watched tutorials on how to create a website.
           It took a while but I eventually got the hang of it.
           By 12/7/2024, I completed my first ever "website" with only 240 lines of code. (You can see the code through my Github Profile)
        """)
        st.write("I made this as not only did I want to challenge myself, I wanted prove to you that I am truly intrested in this course, I am passionate about coding and I am willing to always learn new things.")
        st.write("I have made other projects such as a simple Rock, Papers, Scissors and a Pascals Triangle Calculator, simple calculators but this is by far the most difficult challenge I have set and done myself and most proud to show you!")
    with left_column4:
        st_lottie(lottie_code6, height = 400, key = "waves")
        st_lottie(lottie_code9, height = 400, key ="biking")
def contacts():
    left_column4, right_column4 = st.columns((3, 2))
    with left_column4:
      st.write("---")
      st.title("Contact Me!📲🤙")
      st.subheader("Email📧: hodennis004@gmail.com")
      st.subheader("Phone Number☎: 9625 6993")

    with right_column4:
        st_lottie(lottie_code7, height= 400, key = "contact")

st.markdown(
    """
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src=f"https://www.googletagmanager.com/gtag/js?id={os.getenv('analytics_tag')}"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', os.getenv('analytics_tag'));
        </script>
    """, unsafe_allow_html=True)
print(os.getenv('analytics_tag'))


class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def NavigationBar():
        # sidebars wooo
        with st.sidebar:        
            app = option_menu(
                menu_title="Navigation",
                menu_icon='sign-turn-slight-right-fill',

                options=['About Me','Why I Chose TP', 'Experience And Values', 'Achievements','Project','Contacts'],

                icons=['person-circle','house-fill', 'filter-circle', 'trophy-fill','person-workspace','info-circle-fill'],

                default_index=0,


                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},} #this took too long to do
                
                )
# Page loader
        if app == 'About Me':
            print(home())
        if app == "Experience And Values":
            print(val())
        if app == "Achievements":
            print(achievements())        
        if app == 'Project':
            projects()
        if app == 'Contacts':
            contacts()      
                     
          
             
    NavigationBar()       
# FINALLY DONE
