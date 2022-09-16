from models import Sticker

countries = [

'QAT','ECU','SEN','NED','ENG','IRN','USA','WAL','ARG','KSA','MEX','POL','FRA','AUS','DEN','TUN','ESP',
'CRC','GER','JPN','BEL','CAN','MAR','CRO','BRA','SRB','SUI','CMR','POR',
'GHA','URU','KOR'

]

id_completed = []

for country in countries:
    for i in range(1,20):
        id = country + ' ' +str(i)
        id_completed.append(id)

for i in range(1,30):
        id =  'FWC ' +str(i)
        id_completed.append(id)

print(id_completed)

for figurita in id_completed:
        objecto = Sticker(id_complete=figurita)
        objecto.save()