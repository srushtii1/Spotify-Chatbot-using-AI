# importing the required modules
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
 
# creating a chatbot
myBot = ChatBot(
 name = 'Sakura',
 read_only = True,
 logic_adapters = [
'chatterbot.logic.MathematicalEvaluation',
'chatterbot.logic.BestMatch'
]
)
 


 
quest_1 = [
'What is Spotify?',
'Spotify is a digital music, podcast, and video service that gives you access to millions of songs and other content from creators all over the world.'
 ]
quest_2 = [
'Hi... how can I help you?',
'I need to delete a song from my playlist.'
 ]
quest_3 = [
'Can you confirm you wish to delete a song from a playlist?',
'Yes.'
 ]
quest_4 = [
'Sure! which playlist are you referring to?',
'The one with songs from the Beach Boys.'
 ]
quest_5 = [
'Oh, I see. I think you have three playlists with songs from the Beach Boys. They are "Fun in the car," "Lounging at home," and "Party at Andy".',
'Fun in the car.'
 ]
quest_6 = [
'OK, which song do you want to delete?',
'The one from the Monkeys.'
 ]
quest_7 = [
'You have a song entitled, "Shock the Money," and you have songs from the artist, "The Monkeys." Are you referring to the song or the artist?',
'The artist.'
 ]
quest_8 = [
'Which song by "The Monkeys" do you want to delete?',
'I’m a Believer'
 ]
quest_9 = [
'I’m a Believer song deleted successfully',
'Ok']
quest_10 = [
'Any further questions?',
"No"
 ]

# using the ListTrainer class  
list_trainee = ListTrainer(myBot)
for i in (quest_1, quest_2, quest_3, quest_4, quest_5,
 quest_6, quest_7, quest_8, quest_9, quest_10,):
 list_trainee.train(i)
 
# using the ChatterBotCorpusTrainer class
corpus_trainee = ChatterBotCorpusTrainer(myBot)
corpus_trainee.train('chatterbot.corpus.english')

