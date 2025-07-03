f1_text = """
Formula One, or F1, is the top level of car racing for single-seat cars.
The first F1 World Championship race happened in 1950 at Silverstone.
Lewis Hamilton and Michael Schumacher both have seven world titles.
Max Verstappen won the 2023 F1 championship driving for Red Bull.
The Monaco Grand Prix is famous for being raced on tight city streets.
F1 cars can go from 0 to 100 km/h in about 2.5 seconds.
Races are held every weekend and include practice, qualifying, and the race.
The FIA (Fédération Internationale de l'Automobile) manages F1.
Tire strategy is important and includes soft, medium, and hard compounds.
The Drag Reduction System (DRS) helps drivers overtake by reducing drag.
"""

with open("formula1.txt", "w") as f:
    f.write(f1_text)

import streamlit as st

# Load sentences from file
with open("formula1.txt", "r") as f:
    sentences = [s.strip() for s in f.read().split(".") if s.strip()]

# Preprocessing (basic lowercase + punctuation removal)
def clean(text):
    return text.lower().replace(",", "").replace(".", "")

# Jaccard Similarity
def get_best_match(query):
    query_set = set(clean(query).split())
    best_score = 0
    best_sentence = "Sorry, I don't know the answer to that."
    for sentence in sentences:
        sentence_set = set(clean(sentence).split())
        score = len(query_set & sentence_set) / len(query_set | sentence_set)
        if score > best_score:
            best_score = score
            best_sentence = sentence
    return best_sentence

# Streamlit Interface
def main():
    st.title("F1 Chatbot (No NLTK)")
    st.write("Ask me anything about Formula One racing!")
    user_input = st.text_input("You:")
    if st.button("Submit"):
        response = get_best_match(user_input)
        st.write("Chatbot: " + response)

if __name__ == "__main__":
    main()
