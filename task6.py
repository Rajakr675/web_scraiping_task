

#the code

import json


with open("task4.json","r") as f:
    data= json.load(f)

    Hindi=0
    English=0
    Malayalam=0
    Tamil=0
    Marathi=0
    Telugu=0
    kannada=0
    Bengali=0
    Spanish=0
    dic={}
    for i in data:
        for j in i["language"]:
            if "Hindi" ==j:
                Hindi+=1
                
            elif "English" ==j:
                English+=1
                
            elif "Malayalam" ==j:
                Malayalam +=1
                
            elif "Tamil" ==j:

                Tamil+=1 
            elif "Marathi"==j:
                Marathi+=1

            elif "Telugu"==j:
                Telugu+=1
            
            elif "Kannada"==j:
                kannada+=1

            elif "Bengali" ==j:
                Bengali+=1

            elif "Spanish" ==j:
                Spanish+=1
dic["Hindi"]=Hindi
dic["English"]=English
dic["Malayalam"]=Malayalam
dic["Tamil"]=Tamil
dic["Marathi"]=Marathi
dic["Telugu"]=Telugu
dic["kannada"]=kannada
dic["Bengali"]=Bengali

print(dic)




# print("Hindi",Hindi)
# print("English",English)
# print("Malyalam",Malayalam)
# print("Tamil",Tamil)
# print(j)
























