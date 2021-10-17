import json

def konto_erstellen():
    with open("bankData.json","r+") as jdata:
        pdata=json.load(jdata)
        print(pdata)
        id=pdata['id']
        pdata['id']=id+1
        # jdata.seek(0)      
        # json.dump(pdata,jdata,indent=4)
        # jdata.truncate()
        # print(id)
        vorname= input('Wie heisen Sie mit der Vorname?\n')
        name= input('Wie heisen Sie mit der Nachname?\n')
        passwort= input('Geben Sie eine Passwort ein: ')
        id_info={'vorname': vorname, 'nachname': name, 'passwort': passwort}
        pdata[id]=id_info
        print(pdata)
        jdata.seek(0)   
        json.dump(pdata,jdata,indent=4)
        jdata.truncate()
    print (f'Ihre ID Nummer lautet: {id}\nIhre Passwort lautet: {passwort}\nBitte notieren Sie es!')
def geld_abheben ():
    
def geld_einzahlen():
    pass
def geld_ueberweisen ():
    pass
def geld_investieren ():
    pass

antwort= input('Was kann ich fuer Sie tun?\n1. Konto erstellen.\n2. Geld abheben.\n3. Geld einzahlen.\n4. Geld ueberweisen.\n5. Geld investieren.\nWaehlen Sie bitte eine Nummer: ')
if antwort=="1":
    konto_erstellen()

elif antwort=='2':
    geld_abheben()

elif antwort=='3':
    geld_einzahlen()

elif antwort=='4':
    geld_ueberweisen()

elif antwort=='5':
    geld_investieren()



