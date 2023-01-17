import json
with open ('precipitation.json') as file:
    precipitation_data=json.load(file)

seattle_data=[]
for data in precipitation_data:
    if data['station']=="GHCND:USW00093814":
        seattle_data.append(data)
        #precipitation_data
#seattle information is put into seattle_data                

#print(seattle_data)

sum=0
total_monthly_precipitation=[0]*12
for data in seattle_data:
    date=data['date']
    date=date.split("-")
    value=data['value']
    total_monthly_precipitation[int(date[1])-1]+=value
    
with open('result.json', 'w') as file:
    json.dump({
        "Seattle":{
            "station": "GHCND:USW00093814",
            "State": "Washington",
            "total_monthly_precipitation": [total_monthly_precipitation]
        }
    }, file, indent=4, sort_keys=True) 
        #total_monthly_precipitation, file, indent=4, sort_keys=True)

#part 2
sum=0
for data in total_monthly_precipitation:
    sum+=data
total_yearly_precipation=sum

with open('result.json', 'w') as file:
    json.dump({
        "Seattle":{
            "station": "GHCND:USW00093814",
            "State": "Washington",
            "total_monthly_precipitation": [total_monthly_precipitation],
            "total_yearly_precipitation": [total_yearly_precipation]
        }
    }, file, indent=4, sort_keys=True) 

relative_monthly_precipitation_list=[]
for data in total_monthly_precipitation:
    relative_monthly_precipitation=data/total_yearly_precipation
    relative_monthly_precipitation_list.append(relative_monthly_precipitation)
print(relative_monthly_precipitation_list)


with open('result.json', 'w') as file:
    json.dump({
        "Seattle":{
            "station": "GHCND:USW00093814",
            "State": "Washington",
            "total_monthly_precipitation": [total_monthly_precipitation],
            "total_yearly_precipitation": [total_yearly_precipation],
            "relative_monthly_precipitation": [relative_monthly_precipitation_list]
        }
    }, file, indent=4, sort_keys=True) 


#relative_monthly_precipitation= total_monthly_precipitation/total_yearly_precipation

#total_yearly_precipitation=total_monthly_precipitation)
#print(total_monthly_precipitation)
    


    #if date[1]==
     #   sum+=value
    #total_monthly_precipitation.append(sum)


   #if date[1]=='01':
    #    sum+=value
    

