# Beispielproggram. Dieses Program wurde von einem Drittanbieter erstellt.
# Chatbot
# -*- coding: utf-8 -*-
# Beispiel aus Raspberry Pi für Dummies

import random

random_replies=[
  "Oh, wirklich?",
  "Sind Sie sich dessen sicher?",
  "Hmmmmm.",
  "Interessant ...",
  "Ich weiß nicht recht, ob ich da Ihrer Meinung bin ...",
  "Definitiv!",
  "Vielleicht!",
  "Und was genau wollen Sie damit sagen",
  "Und das heißt was?",
  "Stimmt wohl.",
  "Unsinn! Völliger Unsinn!",
  "Und, was haben Sie morgen vor?",
  "Ich habe gerade genau dasselbe gedacht.",
  "Das ist wohl eine verbreitete Meinung.",
  "Das habe ich schon oft gehört.",
  "Wunderbar!",
  "Das könnte ein wenig peinlich werden!",
  "Glauben Sie das wirklich?",
  "Tatsächlich ...",
  "Genau was ich sage!",
  "Ich verstehe ..."]

chat_dictry = {
  "glücklich":"Ich bin heute auch gut drauf!",
  "traurig":"Kopf hoch, Genosse!",
  "himbeere":"Lecker! Ich mag Himbeeren!",
  "computer":"Rechner an die Macht! Sie sprechen schon mit einem.",
  "musik":"Haben Sie das neue Album von Lana Del Rey gehört?",
  "kunst":"Mal ehrlich, was ist den Kunst überhaupt?",
  "witz":"Treffen sich zwei Jäger im Wald.",
  "python":"Ich hasse Schlangen!",
  "dummkopf":"Du nennst mich Dummkopf, Matschbirne?",
  "wetter":" Ich frage mich, ob es Samstag sonnig wird?",
  "sie":"Halten Sie mich da raus!",
  "sicher":"Wie können Sie sich dessen so sicher sein?",
  "reden":"Immer nur labern! Handeln!",
  "denken":"Sie können das ja mal überschlafen.",
  "hallo":"Hallo! Alles klar in Sansibar?",
  "kosten":"Nichts ist kostenlos. Selbst der Tod kostet das Leben."}

def dictionary_check(message):
    message=message.lower()
    playerwords=message.split()
    smart_replies=[]
    for eachword in playerwords:
        if eachword in chat_dictry:
            answer=chat_dictry[eachword]
            smart_replies.append(answer)
    if smart_replies:
        reply_chosen=random.randint(1,len(smart_replies))-1
        return smart_replies[reply_chosen]
    return ""

print ("Worüber würden Sie heute gerne reden?")

user_says=""

while user_says != "Bye":
  
    user_says = ""
    while user_says == "":
        user_says = input("Reden Sie mit mir: ")

    smart_response=dictionary_check(user_says)
    if smart_response:
        print (smart_response)
    else:
        reply_chosen=random.randint(1, len(random_replies))-1
        print (random_replies[reply_chosen])
        random_replies[reply_chosen]=user_says

print ("Tschüss. Danke für das Gespräch. Jederzeit wieder!")
