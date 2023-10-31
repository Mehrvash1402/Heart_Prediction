## import the libraries
import streamlit as st
import keras
from PIL import Image
import numpy as np


### Load the ANN model
model =keras.models.load_model("heart_disease.h5")

# 
## creat a function for prediction--
def heart_prediction(input):
    input_array = np.asarray(input)
    input_reshape = input_array.reshape(1, -1)         ##change it into 2 dimensional array to be possible work with
    prediction = model.predict(input_reshape)
    print(prediction)     ##it prediction will be just 0 and 1 but we want output to be try to be specify then the next code tell
    
    
    if (prediction [0] == 0):   ##if it is equal to 0 then means you not die from the disease, we need to map which model predict 0 which predict 1
        return 'You are likely to die from heart failure given your health condition'
    else:
        return 'You are not likely to die from heart failure given your health conditions'
    
 ## creating another function, to page congiguaration, how the page looks like- use the streamlit documentation(docs.streamlit.io/library/cheatsheet)
def main():
    st.set_page_config(page_title="Heart Failure Prediction", layout= 'wide')
        
    ## add image
    image = Image.open('heart.png')
    st.image(image, use_column_width=False)
    
     ##set title and content
    st.title('Heart Failure Predictor using Artificial Neural Network')
    st.write('Enter your personal data to get your heart risk evaluation')
    
    ##specify the variable from the user (get input from the user)
    age = st.number_input('Age of the patient:', min_value=0, step=1)
    anaemia = st.number_input('Anemia| Yes or No |yes = 1 and no = 0', min_value=0 , step=1)
    creatinine_phosphokinase = st.number_input('Level of CPK enzyme in the blood (mcg/L)', min_value=0 , step=1)
    diabetes = st.number_input('Diabetes| Yes or No |yes = 1 and no = 0', min_value=0 , step=1)
    ejection_fraction = st.number_input('Percentage of blood leaving the heart', min_value=0 , step=1)
    high_blood_pressure = st.number_input('Hypertensive| Yes or No |yes = 1 and no = 0', min_value=0, step=1)
    platelets = st.number_input('Platelet count of blood(kiloplatelets/ml)', min_value=0, step=1)
    serum_creatinine = st.number_input('Level of Serum_cereatinine in the  blood(mg/dl)', min_value=0, step=0.01)
    serum_sodium = st.number_input('Level of Serum Sodium in the blood(mEq/L)', min_value=0, step=1)
    sex = st.number_input('Sex| Male or Female| Female = 1 and Male = 0', min_value=0, step=1)
    smoking = st.number_input('Smoke habit| Yes or No| Yes = 1 and No = 0', min_value=0, step=1)
    time = st.number_input('Follow up Period (days):' , min_value=0, step=1)
    
    ##code for prediction
    predict = ''
    ## Button for prediction
    if st.button('Predict'):
        predict = heart_prediction([age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking,time ])
    st.success(predict)
    
if __name__ == '__main__':
    main()
       
    ##  if __name__ == "__main__":
    ##  main()
    ##run in terminal
    ##streamlit run heart-model.py
    ##python -m streamlit run heart-model.py