import spacy
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

spacy.load('en')

Bookshop = ChatBot('bookshopBot',
                   read_only=False,
                   logic_adapters=["chatterbot.logic.BestMatch"],
                   storage_adapter="chatterbot.storage.SQLStorageAdapter")



greet_conversation = [
    "Hello",
    "Hi there!",
    "How are you?",
    "I'm great well.",
    "what is your name?",
    "my name is book shop robot.",
    "That is good to hear",
    "Thank you.",
    "You're welcome",
    "Yes it is."

]

open_timings_conversation = [
    "What time does the Bookshop open?",
    "The Bookshop opens at 9AM.",
]

close_timings_conversation = [
    "What time does the Bookshop close?",
    "The Bookshop closes at 8PM.",
]
spec_conversation = [
    "How much type of books you have?",
    "Two thousands type of books I have .",
    "who is book is good?",
    "Holly Quran pak is a good book I have. "

]
# Initializing Trainer Object
trainer = ListTrainer(Bookshop)

# Training Bookshopbot
# training from corpus
corpus_tranier = ChatterBotCorpusTrainer(Bookshop)
corpus_tranier.train("chatterbot.corpus.english")
trainer.train(greet_conversation)
trainer.train(open_timings_conversation)
trainer.train(close_timings_conversation)
trainer.train(spec_conversation)

while True:
    user_input = input('You')
    if user_input == 'bye':
        break
    response = Bookshop.get_response(user_input)
    print(response)
