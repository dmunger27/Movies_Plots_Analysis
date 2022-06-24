import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'plot': "Lenny Parker, a mysterious stranger becomes the landlord of a local pub. A ruthless gang who work for local businessman Ray Gleeson decide they want to take over the pub, spurred on by the fact that Lenny's barmaid Terri is the ex of Ray's psychotic son Dominic Gleeson. Dominic is out for revenge after being neglected by Terri, Lenny is the only obstacle standing in his way as Terri and her daughter Peewee find themselves drawn to Lenny. When Dominic and the gang go too far and attack Terri, Lenny is forced to face his darkest fears and go back to his old ways to protect his pub and newfound family - but how far will he go?"})

print(r.json())