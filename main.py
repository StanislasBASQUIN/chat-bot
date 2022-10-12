from nltk.chat.util import Chat, reflections

# Redéfinir le dialogue.
# Définir le dialogue.

# Partie Gauche est la Question de User. Partie Droite est la réponse du Bot.
pairs = [
    ["Mon Prenom est Ucef", ["Bonjour Ucef"]]
    ["Mon Prenom est (.*)", ["Bonjour %1"]],
    ["(Bonjour|Salut|Coucou|Hello)", ["Bonjour", "Hello", "Comment puis-je vous aider?"]],
    ["Je souhaite acheter un (.*) volume (.*)", ["Daccord, je vais vous préparer les %1 Volume %2"]],
    ["(.*) (ville|adresse)", ["Paris xxxx"]]
]

chat = Chat(pairs, reflections)
