provinces={'ADANA':[37.0,35.3213333],'ADIYAMAN':[37.7641667,38.2761667],'AFYONKARAHISAR':[38.76376,30.54034],'AGRI':[39.7216667,43.0566667],'AMASYA':[40.65,35.8333333],'ANKARA':[39.92077,32.85411],'ANTALYA':[36.88414,30.70563],'ARTVIN':[41.1833333,41.8166667],'AYDIN':[37.8444,27.8458],'BALIKESIR':[39.648369,27.88261],'BILECIK':[40.150131,29.983061],'BINGOL':[38.885349,40.498291],'BITLIS':[38.4,42.1166667],'BOLU':[40.739479,31.611561],'BURDUR':[37.726909,30.288876],'BURSA':[40.18257,29.06687],'CANAKKALE':[40.155312,26.41416],'CANKIRI':[40.6,33.6166667],'CORUM':[40.5505556,34.9555556],'DENIZLI':[37.77652,29.08639],'DIYARBAKIR':[37.91441,40.230629],'EDIRNE':[41.6666667,26.5666667],'ELAZIG':[38.680969,39.226398],'ERZINCAN':[39.75,39.5],'ERZURUM':[39.9043189,41.2678853],'ESKISEHIR':[39.784302,30.51922],'GAZIANTEP':[37.06622,37.38332],'GIRESUN':[40.912811,38.38953],'GUMUSHANE':[40.4602778,39.4813889],'HAKKARI':[37.5833333,43.7333333],'HATAY':[36.4018488,36.3498097],'ISPARTA':[37.7666667,30.55],'MERSIN':[36.8,34.6333333],'ISTANBUL':[41.00527,28.97696],'IZMIR':[38.41885,27.12872],'KARS':[40.59267,43.077831],'KASTAMONU':[41.38871,33.78273],'KAYSERI':[38.7333333,35.4833333],'KIRKLARELI':[41.7333333,27.2166667],'KIRSEHIR':[39.15,34.1666667],'KOCAELI':[40.8532704,29.8815203],'KONYA':[37.8666667,32.4833333],'KUTAHYA':[39.4166667,29.9833333],'MALATYA':[38.35519,38.30946],'MANISA':[38.619099,27.428921],'KAHRAMANMARAS':[37.5833333,36.9333333],'MARDIN':[37.3122361,40.735112],'MUGLA':[37.2152778,28.3636111],'MUS':[38.7432926,41.5064823],'NEVSEHIR':[38.62442,34.723969],'NIGDE':[37.9666667,34.6833333],'ORDU':[40.9833333,37.8833333],'RIZE':[41.02005,40.523449],'SAKARYA':[40.7568793,30.378138],'SAMSUN':[41.292782,36.33128],'SIIRT':[37.94429,41.93288],'SINOP':[42.0264222,35.1550745],'SIVAS':[39.747662,37.017879],'TEKIRDAG':[40.9833333,27.5166667],'TOKAT':[40.3166667,36.55],'TRABZON':[41.0,39.7333333],'TUNCELI':[39.1079868,39.5401672],'SANLIURFA':[37.15,38.8],'USAK':[38.682301,29.40819],'VAN':[38.4941667,43.38],'YOZGAT':[39.82,34.8044444],'ZONGULDAK':[41.456409,31.798731],'AKSARAY':[38.36869,34.03698],'BAYBURT':[40.255169,40.22488],'KARAMAN':[37.17593,33.228748],'KIRIKKALE':[39.846821,33.515251],'BATMAN':[37.881168,41.13509],'SIRNAK':[37.5163889,42.4611111],'BARTIN':[41.6344444,32.3375],'ARDAHAN':[41.110481,42.702171],'IGDIR':[39.9166667,44.0333333],'YALOVA':[40.65,29.2666667],'KARABUK':[41.2,32.6333333],'KILIS':[36.718399,37.12122],'OSMANIYE':[37.06805,36.261589],'DUZCE':[40.843849,31.15654]}

departure=input("Departure province:\n")


departure=departure.upper()


provinces=dict(sorted(provinces.items()))


counter=0
province_counter=0

while departure not in provinces.keys():
  string_departure=str()
  for i in provinces.keys():
    counter+=1 
    if i[:len(departure)]==departure:
      string_departure+=i+','
      province_counter+=1
    elif counter==81 :
      length_departures=len(string_departure)
      if string_departure=="":
        print("Province not found!")
        departure=input("Departure province:\n")
        departure=departure.upper()
        if departure not in provinces.keys():
          counter=0
      elif string_departure!="":
        print("Province not found!")
        if province_counter==1:
          print("Possible province:"+string_departure[:length_departures-1])
          departure=input("Departure province:\n")
          departure=departure.upper()
        elif province_counter>=1:
          print("Possible provinces:"+string_departure[:length_departures-1])
          departure=input("Departure province:\n")
          departure=departure.upper()
        if departure not in provinces.keys():
          counter=0
          province_counter=0

d_x=provinces[departure][0]
d_y=provinces[departure][1]

counter=0
province_counter=0

arrival=input("Arrival province:\n")
arrival=arrival.upper()


while arrival not in provinces.keys() or arrival==departure:
  string_arrival=str()
  while arrival==departure:
    print("Enter a different province!")
    arrival=input("Arrival province:\n")
    arrival=arrival.upper()
  for i in provinces.keys():
    counter+=1 
    if i[:len(arrival)]==arrival:
      string_arrival+=i+','
      province_counter+=1
    elif counter==81 :
      length_arrivals=len(string_arrival)
      if string_arrival=="":
        print("Province not found!")
        arrival=input("Arrival province:\n")
        arrival=arrival.upper()
        if arrival not in provinces.keys():
          counter=0
          province_counter=0
      elif string_arrival!="":
        if province_counter==1:
          if arrival in provinces.keys():
            break
          print("Province not found!")
          print("Possible province:"+string_arrival[:length_arrivals-1])
          arrival=input("Arrival province:\n")
          arrival=arrival.upper()
        elif province_counter>=1:
          print("Province not found!")
          print("Possible provinces:"+string_arrival[:length_arrivals-1])
          arrival=input("Arrival province:\n")
          arrival=arrival.upper()
        if arrival not in provinces.keys():
          counter=0
          province_counter=0

provinces[departure]=[d_x,d_y]

a_x=provinces[arrival][0]
a_y=provinces[arrival][1]

vehicle_types={"CAR":90,"MOTORCYCLE":80,"BICYCLE":25}

distance=((((a_x-d_x)**2+(a_y-d_y)**2))**(1/2))*100
distance_rounded=(distance-int(distance))*100

distance_rounded=round(distance_rounded)

travel_type=input("Enter travel type:\n")
travel_type=travel_type.upper()
while travel_type not in vehicle_types.keys():
  travel_type=input("Enter travel type:\n")
  travel_type=travel_type.upper()

print("\nI am calculating the distance between "+departure+" and "+arrival+" ...\n")

time_=distance/vehicle_types[travel_type]

time_minutes=(time_-int(time_))*60

print("Distance: "+str(int(distance))+"."+str(distance_rounded)+" km")
print("Approximate travel time with "+str(travel_type)+": "+str(int(time_))+" hours "+str(int(time_minutes))+" minutes")

provinces.pop(departure)
for x in provinces.keys():
  provinces[x]=((d_x-provinces[x][0])**2+(d_y-provinces[x][1])**2)**1/2
  
sorted_locations = sorted(provinces.values()) 
sorted_provinces = {}
for i in sorted_locations:
    for n in provinces.keys():
        if provinces[n] == i:
            sorted_provinces[n] = provinces[n]
            break


recommended_provinces=list()
counter=0
for i in sorted_provinces.keys():
  recommended_provinces.append(i)
  counter+=1
  if counter==3:
    break

recommended_provinces=sorted(recommended_provinces)

recommended_provinces_string=str()
for i in recommended_provinces:
  recommended_provinces_string+=i+","

print("Recommended places close to "+departure+":"+recommended_provinces_string[:len(recommended_provinces_string)-1])