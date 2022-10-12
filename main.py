# pip install nltk
# Developpement du ChatBot.

from nltk.chat.util import Chat, reflections

# Redéfinir le dialogue.
pairs = [
    ["Mon Prenom est Ucef", ["Bonjour Ucef"]]
]

chat = Chat(pairs, reflections)
chat.converse()


