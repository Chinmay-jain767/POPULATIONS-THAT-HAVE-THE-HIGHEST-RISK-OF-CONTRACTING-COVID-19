import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

#from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("finalized_model.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
       
def predict_note_authentication(Breathing_Problem,Fever,Dry_Cough,Sore_throat,Hyper_Tension,Abroad_travel,Contact,Attended,Visited,Family):
    
   
    X=np.array([[Breathing_Problem,Fever,Dry_Cough,Sore_throat,Hyper_Tension,Abroad_travel,Contact,Attended,Visited,Family]])
    X[X=='yes'] = 1
    X[X=='no'] = 0
    prediction=classifier.predict(X)
    if prediction==1:
      prediction="Our AI model feels after analyzing your symptoms , that you can be a potential covid patient , please contact your nearest medical care centre. "
    else:
      prediction="Our AI model feels after analyzing your symptoms, that you are safe, so be safe and wear mask."
    print(prediction)
    return prediction



def main():
    st.title("POPULATIONS THAT HAVE THE ​HIGHEST RISK OF ​CONTRACTING COVID-19")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Type "yes" if you it is true otherwise type "no" </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Breathing_Problem = st.text_input("Breathing Problem","Type Here")
    Fever = st.text_input("Fever","Type Here")
    Dry_Cough = st.text_input("Dry Cough","Type Here")
    Sore_throat = st.text_input("Sore throat","Type Here")
    Hyper_Tension = st.text_input("Hyper Tension","Type Here")
    Abroad_travel = st.text_input("Abroad travel","Type Here")
    Contact = st.text_input("Contact with COVID Patient","Type Here")
    Attended = st.text_input("Attended Large Gathering","Type Here")
    Visited = st.text_input("Visited Public Exposed Places","Type Here")
    Family = st.text_input("Family working in Public Exposed Places","Type Here")
    
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Breathing_Problem,Fever,Dry_Cough,Sore_throat,Hyper_Tension,Abroad_travel,Contact,Attended,Visited,Family)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("More solution ")
        st.text("Comming soon")

if __name__=='__main__':
    main()