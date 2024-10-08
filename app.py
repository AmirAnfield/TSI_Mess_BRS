import streamlit as st

# Fonction pour générer le message
def generate_message(ref, iban, company, case):
    if case == "Tous les relevés demandés":
        return f"""
        Bonjour,
        Référence : {ref}
        Vous trouverez en pièce jointe le relevé bancaire sur les périodes demandées du compte {iban} de la société {company}.
        Cordialement,
        """
    elif case == "Aucune transaction sur une période mais transactions sur le reste":
        return f"""
        Bonjour,
        Référence : {ref}
        Vous trouverez en pièce jointe le relevé bancaire sur les périodes demandées du compte {iban} de la société {company}.
        - Pas de transaction pour les autres périodes demandées.
        Cordialement,
        """
    elif case == "Aucune transaction sur toutes les périodes demandées":
        return f"""
        Bonjour,
        Référence : {ref}
        Aucune transaction pour les périodes demandées du compte {iban} de la société {company}.
        Cordialement,
        """
    elif case == "Demande de cartons de signature à la place des relevés":
        return f"""
        Bonjour,
        Notre équipe vous remercie pour votre mail sur requisitions@qonto.com.
        Référence : {ref}
        Vous trouverez en pièce jointe le carton de signature du compte {iban} de la société {company}.
        Cordialement,
        """
    return ""

# Titre de l'application
st.title("Générateur de Messages")

# Champs du formulaire
reference = st.text_input("Référence :")
iban = st.text_input("IBAN :")
company = st.text_input("Nom de la société :")

# Options pour le cas
case_options = [
    "Tous les relevés demandés",
    "Aucune transaction sur une période mais transactions sur le reste",
    "Aucune transaction sur toutes les périodes demandées",
    "Demande de cartons de signature à la place des relevés"
]

case = st.selectbox("Sélectionnez un cas :", case_options)

# Bouton pour générer le message
if st.button("Générer le message"):
    if reference and iban and company:
        message = generate_message(reference, iban, company, case)
        st.text_area("Message généré :", value=message, height=300)
    else:
        st.error("Veuillez remplir tous les champs.")
