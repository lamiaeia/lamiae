
import streamlit as st
import numpy as np
import pickle
import os

# Charger le modèle
model = pickle.load(open("appli/model.pkl", "rb"))

# Titre de l'application
st.title(" Faire de Prédiction")

# Formulaire pour saisir les entrées utilisateur
st.header("Compléter les informations suivantes:")

# Entrée utilisateur:
credit_score = st.number_input('Score de crédit', min_value=0, max_value=1000)
age = st.number_input('Âge', min_value=0, max_value=120)
tenure = st.number_input("Ancienneté (années)", min_value=0, max_value=20)
balance = st.number_input("Solde du compte")
num_products = st.number_input("Nombre de produits", min_value=0, max_value=10)
has_card = st.selectbox("Possède une carte de crédit ?", ["Oui", "Non"])
is_active = st.selectbox("Client actif ?", ["Oui", "Non"])
estimated_salary = st.number_input("Salaire estimé")
gender = st.selectbox("Sexe", ["Male", "Female"])
geo = st.selectbox("Géographie", ["France", "Germany", "Spain"])


# Encodage manuel
gender = 0 if gender == "Male" else 1

# Encodage de la géographie
geo = {"France": 0, "Spain": 1, "Germany": 2}[geo]
has_card = 1 if has_card == "Oui" else 0
is_active = 1 if is_active == "Oui" else 0



# Mise en forme des données pour le modèle
features = np.array([[credit_score, age, tenure, balance, num_products,
                        has_card, is_active, estimated_salary,
                        gender, geo]])
# Prédiction
if st.button("Prédire"):
    prediction = model.predict(features)
    st.success(f"Résultat de la prédiction : {int(prediction[0])}")
else:
    st.info("Appuyez sur le bouton pour lancer la prédiction.")