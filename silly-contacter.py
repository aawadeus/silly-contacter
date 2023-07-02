import requests
import random
import time


def randFirstLast():
    with open("first-names.txt", "r") as file1:
        allText1 = file1.read()
        word1 = list(map(str, allText1.split()))
    
    with open("last-names.txt", "r") as file2:
        allText2 = file2.read()
        word2 = list(map(str, allText2.split()))
    
    return random.choice(word1) + " " + random.choice(word2) 


def seqEmail():
    with open("emails.txt", "r") as file3:
        allText3 = file3.read()
        word3 = list(map(str, allText3.split()))
    
        for i in range(len(word3)):
            yield word3[i]


def sign_up(url, name, email, message):
    form_data = {
        'Name': name,
        'Email': email,
        'Message': message
    }
    
    response = requests.post(url, data=form_data)

    if response.status_code == 200:
        print("Code 200 - OK")
    else:
        print("ERROR")


url = 'https://random-site.com/contact'
name = randFirstLast
emails = []
message = '*Your silly message here*'


for email in seqEmail():
    emails.append(email)


index = 0
while True:
    sign_up(url, name(), emails[index], message)
    #print(url, name(), emails[index], message) # use this to text that your provided lists work, comment it out when wanting to use it.
    index = (index + 1) % len(emails)
    print("Signups Completed:", index)
    time.sleep(5)


