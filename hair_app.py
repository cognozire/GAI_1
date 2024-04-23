import streamlit as st
import pandas as pd
import joblib

def hair_health_main():

    st.title('Hair Health Prediction')

    # loading the model
    model = joblib.load('hair_health_prediction_model.pkl')

    # loading the encoder
    encoder = joblib.load('encoder.pkl')

    categorical_columns = [
        'Genetics', 'Hormonal Changes', 'Medical Conditions',
        'Medications & Treatments', 'Nutritional Deficiencies ', 'Stress', 'Poor Hair Care Habits ', 'Environmental Factors', 'Smoking',
        'Weight Loss '
    ]

    # taking user input
    age = st.text_input('Enter your age:')

    genetics = st.selectbox("Do you have a genetic condition?", [" ", "Yes", "No"])

    hormonal_changes = st.selectbox("Do you have abnormal hormonal changes?", [" ", "Yes", "No"])

    medical_cond = st.selectbox("Do you have any of these medical conditions?", [" ", 'No Data', 'Eczema', 'Dermatosis', 'Ringworm', 'Psoriasis', 'Alopecia Areata ', 'Scalp Infection', 'Seborrheic Dermatitis', 'Dermatitis', 'Thyroid Problems', 'Androgenetic Alopecia'])

    medications_and_treatments = st.selectbox("Do you take any of these medications or treatments?", [" ", 'No Data', 'Antibiotics', 'Antifungal Cream', 'Accutane', 'Chemotherapy', 'Steroids', 'Rogaine', 'Blood Pressure Medication', 'Immunomodulators', 'Antidepressants ', 'Heart Medication '])

    defc = st.selectbox("Do you have any of these deficiencies?", [" ", 'Magnesium deficiency', 'Protein deficiency', 'Biotin Deficiency ', 'Iron deficiency', 'Selenium deficiency', 'Omega-3 fatty acids', 'Zinc Deficiency', 'Vitamin A Deficiency', 'Vitamin D Deficiency', 'No Data', 'Vitamin E deficiency'])

    stress = st.selectbox("How are your stress levels?", [" ", 'Moderate', 'High', 'Low'])

    hair_habits = st.selectbox("Do you have poor hair care habits?", [" ", "Yes", "No"])

    env_factors = st.selectbox("Could environmental factors be affecting your hair health?", [" ", "Yes", "No"])

    smoking = st.selectbox("Do you smoke?", [" ", "Yes", "No"])

    weight_loss = st.selectbox("Are you experiencing weight loss?", [" ", "Yes", "No"])

    if st.button('Submit'): 
        if genetics!= " " and hormonal_changes!= " " and medical_cond!= " " and medications_and_treatments!= " " and defc!= " " and stress!= " " and hair_habits!= " " and env_factors!= " " and smoking!= " " and weight_loss!= " ":
            
            # Collect user input for each categorical column
            data = {'Genetics': [genetics],
            'Hormonal Changes': [hormonal_changes],
            'Medical Conditions': [medical_cond],
            'Medications & Treatments': [medications_and_treatments],
            'Nutritional Deficiencies ': [defc],
            'Stress': [stress],
            'Poor Hair Care Habits ': [hair_habits],
            'Environmental Factors': [env_factors],
            'Smoking': [smoking],
            'Weight Loss ': [weight_loss]}

            # Create DataFrame from user input
            new_data = pd.DataFrame(data)

            # Apply one-hot encoding to the categorical columns
            one_hot_encoded = encoder.transform(new_data)

            # Create DataFrame from one-hot encoded data
            one_hot_encoded_df = pd.DataFrame(one_hot_encoded, columns=encoder.get_feature_names_out(new_data.columns))

            one_hot_encoded_df.insert(0, 'Age', int(age))

            prediction = model.predict(one_hot_encoded_df)
            if prediction[0] == 0:
                st.success('Less likely to have hairfall.')  
            else: 
                st.error('More likely to have hairfall.')
        
        else:
            st.warning('Kindly answer all the questions.')

if __name__ == "__main__":
    hair_health_main()