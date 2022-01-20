import pandas
import pandas as pd
import numpy as np


def change_name_City(row):
    City = str(row['City'])
    if City == " South San Francisco":
        return "San Francisco"
    elif City == "So. San Francisco":
        return "San Francisco"
    elif "San Fr" in City:
        return "San Francisco"
    elif City == "Not found":
        return "N/A"
    elif "Lond" in City:
        return "London"
    elif "Chicago" in City:
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
    elif "Battle" in City:
        return "Battle"
    elif City == "Bellevue ,WA":
        return "Bellevue"
    elif City == "Ben Lomons":
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
    elif "Bondi" in City:
        return "Bondi"
    elif City == "Boulder Hill":
        return "Boulder"
    elif City == "Bowie Mill Park":
        return "Bowie"
    elif "Bridgeton" in City:
        return "Bridgetown"
    elif City == "Brisbane Australia":
        return "Brisbane"
    elif City == "Bristow":
        return "Bristol"
    elif City == "Bronx":
        return "Bronxville"
    elif  "Brookl" in City:
        return "Brooklyn"
    elif City == "Buc":
        return "Bucharest"
    elif City == "Brookville":
        return "Brownsville"
    elif City == "Brussels":
        return "Brussel"
    elif "Buena" in City:
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
    elif "Cedar" in City:
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
    elif "Daytona" in City:
        return "Daytona"
    elif City == "Dearborn Heights":
        return "Dearborn"
    elif City == "Decatur":
        return "Decateur"
    elif City == "Deerfield Beach":
        return "Deerfield"
    elif City == "Deptford Township":
        return "Deptford"
    elif "Doncaster" in City:
        return "Donacaster"
    elif City == "Douglasville":
        return "Douglas"
    elif "Dublin" in City:
        return "Dublin"
    elif "Duncan" in City:
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
    elif "Elizabeth" in City:
        return "Elizabeth"

    elif City == "Farmington Hills":
        return "Farmington"
    elif City == "Fitzroy North":
        return "Fitzroy"
    elif City == "Fitzroy Vic ":
        return "Fitzroy"
    elif "Forest" in City:
        return "Forest"
    elif City == "Fort Bliss":
        return "Fort Worth"
    elif "Lauderdale" in City:
        return "Fort Myers"
    elif "Fort Myers" in City:
        return "Fort Myers"
    elif City == "Fort Pierce":
        return "Fort Myers"
    elif City == "Freehold Township":
        return "Freehold"
    elif "Farmington" in City:
        return "Farmington"
    elif "Fayette" in City:
        return "Fayette"
    elif "Fitzroy" in City:
        return "Fitzroy"
    elif "Flint" in City:
        return "Flint"
    elif City == "Garberville":
        return "Gardnerville"
    elif City == "Geelong West":
        return "Geelong"
    elif City == "Glendora":
        return "Glendale"
    elif "Golden" in City :
        return "Golden"
    elif City == "Grandville":
        return "Grand Rapids"
    elif City == "Greenville Sc":
        return "Greenville"
    elif City == "Greenwood Village":
        return "Greenwood"
    elif City == "Guilford":
        return "Guildford"
    elif City == "Hallandale Beach":
        return "Hallandale"
    elif City == "Hanover":
        return "Hannover"
    elif City == "Harrisburg":
        return "Harrisonburg"
    elif City == "Hong Kong Island":
        return "Hong Kong"
    elif City == "Houston Texas":
        return "Houston"
    elif City == "HIGHLAND":
        return "Highland"
    elif City == "Holly":
        return "Hollywood"
    elif "Houston" in City:
        return "Houston"
    elif "Hunting" in City:
        return "Huntington"
    elif "Irvin" in City :
        return "Irvington"
    elif "Jackson" in City:
        return "Jackson"
    elif "Jefferson" in City:
        return "Jefferson"
    elif "Jersey" in City:
        return "Jersey"
    elif City == "Johnston":
        return "Johnstown"
    elif City == "Kamarkundu":
        return "Kampala"
    elif City == "Cherry Lane West Drayton Junction 4m4 Ub7 9hb Heathrow United Kingdom Tel (+44)1895/431431 Fax (+44)1895/431221":
        return "United Kingdom"
    elif City == "Buckinghamshire, High Wycombe":
        return "Buckinghamshire"
    elif City == "King Of Prussia":
        return "Kingston"
    elif "Kota" in City :
        return "Kota Kemuning"
    elif "Laguna" in City :
        return "Laguna"
    elif City == "Lakeside":
        return "Lake Forest"
    elif City == "Canyon Lake":
        return "Lake Forest"
    elif City == "Lakewood Ranch":
        return "Lake Mary"
    elif City == "Lake Buena Vista":
        return "Lake Mary"
    elif City == "Lake Worth":
        return "Lake Mary"
    elif City == "Lakeland":
        return "Lake Mary"
    elif City == "Lady Lake":
        return "Lake Mary"
    elif City == "Lakeland":
        return "Lake Mary"
    elif City == "Lake in the Hills":
        return "Crystal Lake"
    elif City == "Lakehurst":
        return "Spring Lake"
    elif City == "Lakewood":
        return "Westlake"
    elif City == "Lakeside Marblehead":
        return "Westlake"
    elif City == "Mawson Lakes":
        return "Salt Lake City"
    elif City == "Bonney Lake":
        return "Lakewood"
    elif City == "Lansdowne Park":
        return "Lansdowne"
    elif City == "Lansing Charter Township":
        return "Lansing"
    elif "Las" in City :
        return "Las Vegas"
    elif City == "Lee&#039;s Summit":
        return "Lees Summit"
    elif City == "Lee's Summit":
        return "Lees Summit"
    elif City == "Leeds":
        return  "Leederville"
    elif City == "Leh":
        return "Lehman"
    elif City == "Lexington Fayette":
        return "Lexington"
    elif City == "Linthicum Heights":
        return "Linthicum"
    elif City == "Lismore, Newcastle, Orange and Wollongong":
        return "Lismore"
    elif City == "North Little Rock":
        return "Little Rock"
    elif City == "Livermore":
        return "Liverpool"
    elif City == "West Long Branch":
        return "Long Branch"
    elif City == "Long Island City":
        return "Long Beach"
    elif City == "Longlea":
        return "Geelong"
    elif City == "Geelong West":
        return "Geelong"
    elif "Los" in City:
        return "Los Angeles"
    elif City == "Loughborough University":
        return "Loughborough"
    elif City == "Lowell Township":
        return "Lowell"
    elif City == "Lyons":
        return "Lyon"
    elif City == "MÃ©xico":
        return "Mexico"
    elif City == "Mobile":
        return "Montgomery"
    elif City == "Millbrook":
        return "Montgomery"
    elif City == "Marana":
        return "Mesa"
    elif City == "MÃ¼nchen":
        return "Munich"
    elif City == "Majadahonda":
        return "Madrid"
    elif City == "Mexico City":
        return "Mexico"
    elif City == "Milford":
        return "Middletown"
    elif City == "Macclesfield":
        return "Manchester"
    elif City == "MediaCityUK":
        return "Manchester"
    elif "Miami" in City :
        return "Miami"
    elif City == "Mcdonough":
        return "McDonough"
    elif City == "New York City":
        return "New York"
    elif City == "NY":
        return "New York"
    elif City == "Newcastle Upon Tyne":
        return "Newcastle"
    elif "Niagara" in City:
        return "Niagara"
    elif "Delhi" in City:
        return "New Delhi"
    elif "New Orleans" in City:
        return "New Orleans"
    elif "Newark" in City:
        return "Newark"
    elif "Newport" in City:
        return "Newport"
    elif City == "Newton":
        return "Newtown"
    elif City == "Newton-le-Willows":
        return "Newtown"
    elif City == "Newburg":
        return "Newburgh"
    elif "oxford" in City:
        return "Oxford"
    elif City == "Orange,":
        return "Orange"
    elif City == "Orange Couty":
        return "Orange"
    elif City == "Orange County":
        return "Orange"
    elif City == "Lismore, Newcastle, Orange and Wollongong":
        return "Orange"
    elif City == "Ottawa,":
        return "Ottawa"
    elif City == "Ocoee":
        return "Ooty"
    elif City == "Thousand Oaks":
        return "Oakland"
    elif City == "Sherman Oaks":
        return "Oakland"
    elif "Ontario" in City :
        return "Ontario"
    elif City == "Palaiseau":
        return "Paris"
    elif City == "Penticton":
        return "Port Coquitlam"
    elif City == "QuÃ©bec":
        return "Quebec"
    elif City == "STUDIO CITY":
        return "Studio City"
    elif "Santiago" in City:
        return "Santiago"
    elif City == "Technology Commercialization Office, Columbus":
        return "N/A"
    elif City == "ThessalonÃ­ki":
        return "Thessaloniki"
    elif City == "test":
        return "N/A"
    elif City == "Union":
        return "Union City"
    elif City == "V6M 2V9":
        return "N/A"
    elif City == "Redwood City":
        return "Woodside"
    elif "Washington" in City:
        return "Washington"
    elif "ZÃ¼rich" in City:
        return "Zurich"
    else:
        return City

def change_name_State(row):
    State = str(row['State'])
    if "United" in State:
        return "UK"
    elif State == "HAMPSHIRE UNITED KINGDOM"
        return "UK"
    elif "Not Found" in State:
        return "N/A"
    elif "Ontario" in State:
        return "ON"
    elif "Florida" in State:
        return "FL"
    elif State == "VICTORIA"
        return "Victoria"

    else:
        return State


df = pd.read_csv('LocationDataSample.csv')
print(df)
df.fillna({'City': 'Not found', 'State': 'Not Found', 'ZipCode': 0, 'Country': 'Not Available'}, inplace=True)
df['change_name_City'] = df.apply(lambda row: change_name_City(row), axis=1)
df['change_name_State'] = df.apply(lambda row: change_name_State(row), axis=1)

df.to_csv('New.csv', index=False)
