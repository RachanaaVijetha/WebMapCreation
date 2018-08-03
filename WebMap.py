# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 08:42:11 2018

@author: UX011785
"""

import folium
import pandas
my_map=map
data=pandas.read_csv("TopColleges.csv")
lon=list(data["Longitude"])
lat=list(data["Latitude"])
name=list(data["Name"])
address=list(data["Address"])
my_map=folium.Map(location=[13.000625,77.527695], zoom_start=6, tiles="MapBox Bright")
fgColg=folium.FeatureGroup(name="Top Colleges")
for long,lati,nam,addr in zip(lon,lat,name,address):
    fgColg.add_child(folium.Marker(location=[lati,long],popup=nam+addr))
my_map.add_child(fgColg)

fgKar=folium.FeatureGroup(name="Karnataka")
fgKar.add_child(folium.GeoJson(data=open('district_Output.JSON','r',
encoding='utf-8-sig').read()))
my_map.add_child(fgKar)

belg_div=['BAGALKOT','BELGAUM','BIJAPUR','DHARWAD','GADAG''UTTAR KANNAD','HAVERI']
beng_div=['BANGALORE RURAL','BANGALORE URBAN','CHITRADURGA','SHIMOGA','TUMKUR','KOLAR','DAVANGERE']
gulb_div=['BELLARY','BIDAR','GULBARGA','KOPPAL','RAICHUR']
mys_div=['CHAMRAJNAGAR','DAKSHIN KANNAD','UDUPI','MYSORE','MANDYA','CHIKMAGALUR','HASSAN','KODAGU']

fgMys=folium.FeatureGroup(name="Mysuru Division")
fgMys.add_child(folium.GeoJson(data=open('district_Output.JSON','r',
encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'Red' if x['properties']['DIST'] in mys_div else '#FFD700' }))
my_map.add_child(fgMys)
 
fgBeng=folium.FeatureGroup(name="Bengaluru Division")
fgBeng.add_child(folium.GeoJson(data=open('district_Output.JSON','r',
encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'#DC143C' if x['properties']['DIST'] in beng_div else '#FFD700' }))
my_map.add_child(fgBeng)
 
fgBelg=folium.FeatureGroup(name="Belagavi Division")
fgBelg.add_child(folium.GeoJson(data=open('district_Output.JSON','r',
encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'#DC143C' if x['properties']['DIST'] in belg_div else '#FFD700' }))
my_map.add_child(fgBelg)

fgGulb=folium.FeatureGroup(name="Kalaburgi Division")
fgGulb.add_child(folium.GeoJson(data=open('district_Output.JSON','r',
encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'#DC143C' if x['properties']['DIST'] in gulb_div else '#FFD700' }))
my_map.add_child(fgGulb)
 
folium.LayerControl().add_to(my_map)
my_map.save("Karnataka.html") 

#district_data=json.load(open("district_Output.json",'r'))



#def district_division():   
#    districts_list=[]
#    for i in range(0,52):
#        district=district_data["features"][i]['properties']['DIST']
#        districts_list.append(district)
#    districts_list=set(districts_list)
#def district_division_color(districts_list):   
#    for dist in districts_list:
#        return {'color': dist_to_color[dist]}
        

 
 

                            

