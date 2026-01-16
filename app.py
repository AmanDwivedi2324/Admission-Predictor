import streamlit as st
import pickle

# loading the trained data 
model = pickle.load(open('model.pkl','rb'))

# creating website 
st.title("Graduate Admission Predictor")
st.write("Enter your scores to check your chance of admission.")

# creating input fields
gre = st.number_input('GRE Score (0-340)',min_value=0,max_value=340,value=300, help="Graduate Record Examination. This is a standardized test for most graduate schools in the US. A score above 300 is considered good.")
toefl = st.number_input('TOEFL Score (0-120)',min_value=0,max_value=120,value=100, help="Test of English as a Foreign Language. This measures your English proficiency. Top universities usually require a score above 100.")
rating = st.slider('University Rating (1-5)', 1,5,3, help="The ranking/prestige of the university you are APPLYING to. 1 = Average College, 5 = Top Tier University (like MIT, Stanford).")
sop = st.slider('SOP Strength (1-5)',1.0,5.0,3.0, help="Statement of Purpose. Rate the quality of your personal essay explaining why you want to join. 1 = Weak/Generic, 5 = Strong/Unique.")
lor = st.slider('LOR Strength (1-5)',1.0,5.0,3.0, help="Letter of Recommendation. How strongly do your professors or bosses recommend you? 1 = Weak support, 5 = Strong endorsement.")
cgpa = st.number_input('CGPA (0-10)', min_value=0.0,max_value=10.0,value=8.0, help="Cumulative Grade Point Average. Your average score during your undergraduate degree.")
research = st.radio('Do you have Research Experience?', ["Yes","No"], help="Select 'Yes' if you have published any research papers or worked on significant research projects. This is a major advantage.")

# converting yes/no to 1/0
research_score = 1 if research == 'Yes' else 0

# predict the logic 
if st.button("Predict Chance"):
    # prepare the data 
    input_data = [[gre,toefl,rating,sop,lor,cgpa,research_score]]
    
    # make prediction 
    prediction = model.predict(input_data)
    
    # display result 
    st.success(f'Your Chance of Admission is : {round(prediction[0]*100,2)}%')