import pandas
import pandas as pd
import numpy as np

def change_name_City(row):
 City = str(row['City'])
 if City == " South San Francisco":
     return "San Francisco"
 elif  City == "So. San Francisco":
     return "San Francisco"
 elif "San Fr" in City:
     return "San Francisco"
 elif City == "Not found":
     return "N/A"
 elif City == "London Borough of Hackney":
     return "London"
 elif City == "Londonderry":
     return "London"
 elif City == "London Borough of Islington":
     return "London"
 elif City == "London London ":
     return "London"
 elif City == "London, ":
     return "London"
 elif   City == "East London":
     return "London"
 elif City == "Central London":
     return "London"
 elif City == "City of London":
     return "London"
 elif City == "Chicago Illinois":
     return "Chicago"
 elif City == "Chicago Heights":
     return "Chicago"
 elif City == "281-334-1000":
     return "N/A"
 elif City == "4150-702":
     return "N/A"
 elif City == "Ä°stanbul":
     return "Istanbul"
 elif City == "Â· Jaipur":
     return "Jaipur"
 elif City == "Accra,":
     return "Accra"
 elif City == "Albuquerque":
     return "Alburquerque"
 elif City == "alert(1)":
     return "N/A"
 elif City == "All Over":
     return "N/A"
 elif City == "Amsterdam Zuidoost":
     return "Amsterdam"
 elif City == "Ann Abor":
     return "Ann Arbor"
 elif City == "Atlanta<ga":
     return "Atlanta "
 elif City == "Barcelone":
     return "Barcelona"
 elif City == "Barre":
     return "Barrie"
 elif City == "Bath And North East Somerset":
     return "Bath"
 elif City == "Battle Creek":
     return "Battle"
 elif City == "Battle Ground":
     return "Battle"
 elif City == "Bellevue ,WA":
     return "Bellevue"
 elif  City == "Ben Lomons":
     return "Ben Lomond"
 elif City == "Bengaluru":
     return "Bangalore"
 elif City == "Bethel Park":
     return "Bethel"
 elif City == "Beverly Hills":
     return "Beverley"
 elif City == "Boca Chica":
     return "Boca Raton"
 elif City == "BogotÃ¡":
     return "Bogota"
 elif City == "Bondi Beach":
     return "Bondi"
 elif City == "Bondi Junction":
     return "Bondi"
 elif City == "Boulder Hill":
     return "Boulder"
 elif City == "Bowie Mill Park":
     return "Bowie"
 elif City == "Bridgeton":
     return "Bridgetown"
 elif City == "Brighton And Hove":
     return "Brighton"
 elif City == "Brisbane Australia":
     return "Brisbane"
 elif City == "Bristow":
     return "Bristol"
 elif City == "Bronx":
     return "Bronxville"
 elif City == "Brookline":
     return "Brooklyn"
 elif City == "Brooklyn Heights":
     return "Brooklyn"
 elif City == "Brooklyn New York":
     return "Brooklyn"
 elif City == "Brooklyn Park":
     return "Brooklyn"
 elif City == "Buc":
     return "Bucharest"
 elif City == "Brookville":
     return "Brownsville"
 elif City == "Brussels":
     return "Brussel"
 elif City == "Buena Park":
     return "Buena"
 elif City == "Buena Vista":
     return "Buena"
 elif City == "Calgary  Alberta":
     return "Calgary"
 elif City == "cali":
     return "California"
 elif City == "Cambridge Ma":
     return "Cambridge"
 elif City == "Cardiff By The Sea":
     return "Cardiff"
 elif City == "Carmel-by-the-Sea":
     return "Carmel"
 elif City == "Carrboro":
     return "Carroboro"
 elif City == "Castlegar":
     return "Castle Rock"
 elif City == "Cedar Hill":
     return "Cedar"
 elif City == "Cedar Park":
     return "Cedar"
 elif City == "Cedar Rapids":
     return "Cedar"
 elif City == "Crown Center Amphitheatre, Independence":
     return "Centerville"
 elif City == "Charlotte N":
     return "Charlotte"
 elif City == "Chatham-Kent":
     return "Chatham"
 elif City == "Cherry Lane West Drayton Junction 4m4 Ub7 9hb Heathrow United Kingdom Tel (+44)1895/431431 Fax (+44)1895/431221":
     return "Cherry Hill"
 elif City == "Chesapeake Beach":
     return "Chesapeake"
 elif City == "Ciudad de Buenos Aires":
     return "Ciudad"
 elif City == "Ciudad de MÃ©xico":
     return "Ciudad"
 elif City == "Ciudad ObregÃ³n":
     return "Ciudad"
 elif City == "Claremore":
     return "Claremont"
 elif City == "Cocoa Beach":
     return "Cocoa"
 elif City == "College Green":
     return "College Park"
 elif City == "Columbus, OH":
     return "Columbus"
 elif City == "Conwy":
     return "Conway"
 elif City == "Corona":
     return "Coronado"
 elif City == "DÃ¼sseldorf":
     return "Düsseldorf"
 elif City == "Daytona Beach":
     return "Daytona"
 elif City == "Dayton":
     return "Daytona"
 elif City == "Daytona Beach Shores":
     return "Daytona"
 elif City == "Dearborn Heights":
     return "Dearborn"
 elif City == "Decatur":
     return "Decateur"
 elif City == "Deerfield Beach":
     return "Deerfield"
 elif City == "Deptford Township":
     return "Deptford"
 elif City == "Doncaster East":
     return "Donacaster"
 elif City == "Doncaster":
     return "Donacaster"
 elif City == "Douglasville":
     return "Douglas"
 elif City == "Dublin 12":
     return "Dublin"
 elif City == "Dublin 3":
     return "Dublin"
 elif City == "Duncan Falls":
     return "Duncan"
 elif City == "Duncanville":
     return "Duncan"
 elif City == "Eagle River":
     return "Eagle"
 elif City == "Edinburg":
     return "Edinburgh"
 elif City == "Edisto Beach":
     return "Edison"
 elif City == "Edmond":
     return "Edmonton"
 elif City == "Egg Harbor Township,":
     return "Egg Harbor Township"
 elif City == "Elizabeth City":
     return "Elizabeth"
 elif City == "Elizabethtown":
     return "Elizabeth"
 elif City == "Farmington Hills":
     return "Farmington"
 elif City == "Fitzroy North":
     return "Fitzroy"
 elif City == "Fitzroy Vic ":
     return "Fitzroy"
 elif City == "Forest Park":
     return "Forest"
 elif City == "Forest Glen":
     return "Forest"
 elif City == "Forest Hill":
     return "Forest"
 elif City == "Fort Bliss":
     return "Fort Worth"
 elif City == "Fort Lauderdale":
     return "Fort Myers"
 elif City == "Fort Pierce":
     return "Fort Myers"
 elif City == "Freehold Township":
     return "Freehold"
 elif City == "Freemason's Hall, Dublin 2":
     return "Dublin"




 else:
     return City


df = pd.read_csv('LocationDataSample.csv')
print(df)
df.fillna({'City': 'Not found', 'State': 'Not Found', 'ZipCode': 0, 'Country': 'Not Available'}, inplace=True)
df['change_name_City'] = df.apply(lambda row:change_name_City(row), axis=1)

df.to_csv('New.csv',index=False)




