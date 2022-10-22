import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
import pandas as pd

icon = Image.open('imag.png')
st.set_page_config(layout = 'wide', page_title="Self-Development",page_icon= icon)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_shops = load_lottieurl('https://assets7.lottiefiles.com/packages/lf20_j2rjqphu.json')
st_lottie(lottie_shops, height=200)
st.header('Study Interface')
# col1, col2, col3, = st.columns([0.5, 1, 0.5])
# with col1:
#     logo = Image.open('tinu.jpg')
#     st.image(logo,width=200,caption= '')

col1, col2 = st.columns(2)
       
col1_expander = col1.expander("Section 1: Background")
with col1_expander:
    struc = st.radio(label = 'Select a Topic', options = ['Hold',
                                                            'Profile',
                                                            "Strenght/Weakness",
                                                            "Agile-Scrum vs. Traditional Waterfall"
                                                            ])

    # st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    st.write('---')


    if struc == 'Profile':
        logo = Image.open('tinu.jpg')
        st.image(logo,width= 150,caption = 'Profile Picture')
        st.write('''Atinuke Aminat has her first degree in Economics and a Master's Degree in Project 
        Managenment from the University of Salford Manchester. She has over 15 years experience working 
        as a project manager and health support manager in Nigeria and the United Kingdom.''')

    if struc == "Strenght/Weakness":
        st.write('''**This is an my assessement of your strength and weaknesses**  
**Strength**
1. You understand people. This it is a unique part of people's skill, this helps you as a leader or a manager.
2. You carry a measure of goodwill around you all the time
3. You are Deligient, hardworking, and you pay so much attention to details
4. You dont accept failure as an option, you always go for the best
**Weakness**  
You have only one weakness which is:  
You dont believe in yourself, you doubt yourself a lot and it erases all your strenghts
If you can belive a little more about yourself, the sky is the limit. We need to talk about this.
Also I will expect you to talk about my weaknesses too.  
''')

    if struc == "Agile-Scrum vs. Traditional Waterfall":
        st.write('**Scrum vs. Traditional Waterfall**')
        st.write('Introduction')
        st.write('''Which of the above project management methodologies is more compatible to reality especially
        in a globalizing world? Do you strive to continually provide a better output? Do you look to be competitive in the 
        in your industry by continually raising the bar? Do you strive to continually be a better version of yourself?
        Do we continually put measures in place to get the best from our governments and leaders? If the answer to
        all these is yes then you understand the difference between the traditional waterfall project management
        method and the Agile methodologies. When water falls it does not come back up again.''')

        logo = Image.open('trad.png')
        st.image(logo,use_column_width=True,caption = 'Scrum vs. Traditiona 1')

        st.write('''Fixated, rigid, deterministic, sequential, top-down etc. are some of the words that describe the 
        the traditional method. You plan everything before hand and not empirically. Requirements are fixed, and 
        budget and time get agreed on earlier, to this end, teams often face budget and timeline constraints with 
        this approach. In the above diagramatic illustration the traditional approach is above the Agile-Scrum approach
        You can see that the Scrum appraoch has different outcomes as opposed to the traditional appraoch 
        with just one outcome. Agile project management focuses more on implementing the client’s feedback
        and reviewing the product periodically. Customer collaboration is a vital factor in agile. 
        It doesn’t follow a plan blindly and responses to changes quickly. You allow for periodic refinement and 
        changing of project scope based on many factors like:  
- Clients and stakeholders input
- Technological Changes
- Financial and budgetary constraints
- Timelines Constraints etc.
Actually you continue to improve on the initial plan until you arrive at version that is most suitable and 
compatible with desires of the clients and the current state of things. This is illustrated in the diagram below.
''')
        
        logo = Image.open('Agile1.jpg')
        st.image(logo,use_column_width=True,caption = 'Scrum vs. Traditiona 2')

        st.write('''**Advantages of the Agile-Scrum Approach**''')
        st.write('''1. Enhanced Flexibility
2. Transparency
3. Effective Collaboration
4. Efficient Problem Solving
5. Reduced Complexities
6. Customer Satisfaction
7. Ownership and Accountability
''')
        
        st.write(' ')
        st.write('**Characteristics of Scrum vs. Traditional Aproaches**')
        Ad = pd.read_csv('AgileS.csv')
        Ad

        st.write('''**Assignment**  
1. Using case studies, discuss the advantages of the Scrum over the traditional approach showing clearly why you think they are advantageous
2. Discuss the characteristics of the scrum and traditional aproaches using case studies''')
        



        


    




