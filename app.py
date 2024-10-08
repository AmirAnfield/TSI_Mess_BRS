import streamlit as st

# Fonction pour générer le message
def generate_message(ref, iban, company, case):
    if case == "Tous les relevés demandés":
        return f"""
Bonjour,

Référence : {ref}

Vous trouverez en pièce jointe le relevé bancaire sur les périodes demandées du compte {iban} de la société {company}.

Cordialement,
        """.strip()
    elif case == "Aucune transaction sur une période mais transactions sur le reste":
        return f"""
Bonjour,

Référence : {ref}

Vous trouverez en pièce jointe le relevé bancaire sur les périodes demandées du compte {iban} de la société {company}.
- Pas de transaction pour les autres périodes demandées.

Cordialement,
        """.strip()
    elif case == "Aucune transaction sur toutes les périodes demandées":
        return f"""
Bonjour,

Référence : {ref}

Aucune transaction pour les périodes demandées du compte {iban} de la société {company}.

Cordialement,
        """.strip()
    elif case == "Demande de cartons de signature à la place des relevés":
        return f"""
Bonjour,

Référence : {ref}

Vous trouverez en pièce jointe le carton de signature du compte {iban} de la société {company}.

Cordialement,
        """.strip()
    return ""

# Titre de l'application
st.title("Messages BRS")

# Champs du formulaire
reference = st.text_input("Référence :")
iban = st.text_input("IBAN :")
company = st.text_input("Société :")

# Options pour les cas avec des cases à cocher
case_tous_releves = st.checkbox("Tous les relevés demandés")
case_aucune_transaction_periode = st.checkbox("Période manquante")
case_aucune_transaction_total = st.checkbox("Aucune transaction")
case_carton_signature = st.checkbox("Cartons de signature")

# Vérification de quel cas est sélectionné
case = None
if case_tous_releves:
    case = "Tous les relevés demandés"
elif case_aucune_transaction_periode:
    case = "Aucune transaction sur une période mais transactions sur le reste"
elif case_aucune_transaction_total:
    case = "Aucune transaction sur toutes les périodes demandées"
elif case_carton_signature:
    case = "Demande de cartons de signature à la place des relevés"

# Bouton pour générer le message
if st.button("Générer le message"):
    if reference and iban and company and case:
        message = generate_message(reference, iban, company, case)
        st.text_area("Message généré :", value=message, height=300)
    else:
        st.error("Veuillez remplir tous les champs et sélectionner au moins un cas.")
