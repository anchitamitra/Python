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
    elif State == "HAMPSHIRE UNITED KINGDOM":
        return "UK"
    elif "Not Found" in State:
        return "N/A"
    elif "Ontario" in State:
        return "ON"
    elif "Florida" in State:
        return "FL"
    elif State == "VICTORIA":
        return "Victoria"
    elif "New York" in State:
        return "NY"
    elif "NEW JERSEY" in State:
        return "NJ"
    elif "New South Wales" in State:
        return "NSW"
    elif "New Territories" in State:
        return "NT"
    elif "Newcastle Upon Tyne" in State:
        return "NUT"
    elif State == "NEW JERSEY":
        return "NJ"
    elif State == "NEW SOUTH WALES":
        return "NSW"
    elif "New Brunswick" in State:
        return "NB"
    elif "Newtownabbey" in State:
        return "NTA"
    elif "Gt Lon" in State:
        return "London"
    elif "Maharashtra" in State:
        return "Maharashtra"
    elif "AZ" in State :
        return "AZ"
    elif "Al Madinah Province" in State:
        return "AL"
    elif "Andhra Pradesh" in State:
        return "AP"
    elif State == "Australian Capital Territory":
        return "AU"
    elif "Argentina" in State:
        return "AR"
    elif "Australia" in State:
        return "AU"
    elif "Abu Dhabi" in State:
        return "AD"
    elif "Al Kuwayt" in State:
        return "Kuwayt"
    elif State == "Autonomous City of Buenos Aires":
        return "Buenos Aires"
    elif "British Columbia" in State :
        return "BC"
    elif "Greater London" in State :
        return "London"
    elif "North Somerset" in State :
        return "NS"
    elif "D.F." in State :
        return "DF"
    elif "West Sussex" in State :
        return "WS"
    elif "ks" in State :
        return "KS"
    elif "California" in State :
        return "CA"
    elif "Northern Ireland" in State :
        return "NI"
    elif "London" in State :
        return "London"
    elif "Western Australia" in State:
        return "WA"
    elif "QROO" in State :
        return "QR"
    elif "Bristol" in State :
        return "Bristol"
    elif "Dorset County" in State :
        return "DC"
    elif "Singapore" in State :
        return "Singapore"
    elif "West Mids" in State :
        return "WM"
    elif "South York" in State :
        return "SY"
    elif "Western Cape" in State :
        return "WC"
    elif "Brighton" in State :
        return "Brighton"
    elif State == "NEW JERSEY":
        return "NJ"
    elif "Grande Casablanca" in State :
        return "GC"
    elif "Brussel" in State :
        return "Brussel"
    elif "Manchester" in State:
        return "Manchester"
    elif "Accra" in State :
        return "Accra"
    elif "Distrito Federal" in State :
        return "DF"
    elif "Yorkshire" in State :
        return "North Yorkshire"
    elif "Columbia" in State :
        return "Columbia"
    elif "Westminster" in State :
        return "Westminster"
    elif "Madhya Pradesh" in State:
        return "MP"
    elif "Denmark" in State :
        return "Denmark"
    elif "Edinburgh" in State :
        return "Edinburgh"
    elif "West Lothian" in State :
        return "WL"
    elif "York" in State:
        return "York"
    elif "France" in State :
        return "FR"
    elif "Lumpur" in State :
        return "Kuala Lumpur"
    elif State == "SÃ£o Paulo":
        return "Sao Paulo"
    elif "Finland" in State :
        return "Finland"
    elif State == "FLORIDA 32901":
        return "FL"
    elif State == "OH.":
        return "OH"
    elif "Spain" in State:
        return "Spain"
    elif "Illinois" in State:
        return  "IL"
    elif State == "State / Province / Region":
        return "N/A"
    elif State == "South East Upper Bavaria / SÃ¼dostoberbayern":
        return "Bavaria"
    elif "Tamil Nadu" in State:
        return "TN"
    elif "Kingston" in State:
        return "Kingston"
    elif State == "CALIFORNA":
        return "CL"
    elif State == "JERSEY":
        return  "NJ"
    elif State == "MÃ©xico":
        return "Mexico"
    elif State == "W.A.":
        return "WA"
    elif State == "na":
        return "N/A"
    elif State == "2300":
        return "N/A"
    elif State == "BogotÃ¡, D.C.":
        return "DC"
    elif State == "-":
        return "N/A"
    elif "Dublin" in State:
        return "Dublin"
    elif State == "IL 60025":
        return "IL"
    elif State == "West Susx":
        return "WS"
    elif State == "Bath And North East Somerset":
        return "Somerset"
    elif State == " California":
        return "CL"
    elif State == "ONTARIO CANADA":
        return "ON"
    elif State == "#NAME?":
        return  "N/A"
    elif State == "FLORIDA 32901":
        return "FL"
    else:
        return State
def change_name_ZipCode(row):
    ZipCode = str(row['ZipCode'])
    if ZipCode == "Zip/Postal":
        return "N/A"
    elif ZipCode == "Zip / Postal Code":
        return "N/A"
    elif ZipCode == "0":
        return "N/A"
    elif ZipCode == "42100 FRANCE":
        return 42100
    elif ZipCode == "Powell, Ohio 43065":
        return 43065
    elif ZipCode == "flFL":
        return "N/A"
    elif ZipCode == "6090 â€Ž":
        return 6090
    elif ZipCode == "BN1 1GEâ€Ž":
        return "BN1 1GE"
    elif "Dublin" in ZipCode:
        return "N/A"
    elif ZipCode == "Z19139ip/Pos":
        return "N/a"
    elif ZipCode == "Australia":
        return "N/A"
    elif ZipCode == "bn1 1we" :
        return "BN1 1WE"
    elif ZipCode == "VA":
        return "N/A"
    elif ZipCode == "NH":
        return "N/A"
    elif ZipCode == "IL":
        return "N/A"
    elif ZipCode == "ex6 7aj":
        return "EX6 7AJ"
    elif ZipCode == "E1":
        return "N/A"
    elif ZipCode == "se11 4ld":
        return "SE11 4LD"
    elif ZipCode == "nj":
        return "N/A"
    elif ZipCode == "Postal Code":
        return  "N/A"
    elif ZipCode == "Postcode":
        return "N/A"
    elif ZipCode == "TX":
        return "N/A"
    elif ZipCode == "British Columbia":
        return "N/A"
    elif ZipCode == "91316/ 91335":
        return 91316
    elif ZipCode == "Florida":
        return "N/A"
    elif ZipCode == "413 01 GÃ¶teborg":
        return "413 01 GA"
    elif ZipCode == "Singapore":
        return "N/A"
    elif ZipCode == "ki":
        return "N/A"
    elif ZipCode == " 400 Glenwoo":
        return "400 Gl"
    elif ZipCode == "TN25 4AJ. (For SatNav please use TN24 9JZ)":
        return "N/A"
    elif ZipCode == "D2":
        return "N/A"
    elif ZipCode == "PA":
        return "N/A"
    elif ZipCode == "NY":
        return "N/A"
    elif ZipCode == "E2":
        return "N/A"
    elif ZipCode == "W1":
        return "N/A"
    elif ZipCode == "NC":
        return "N/A"
    elif ZipCode == "SC":
        return "N/A"
    elif ZipCode == "S75v 1JL":
        return "S75V 1JL"
    elif ZipCode == "t0c 2p0":
        return "T0C 2P0"
    elif ZipCode == "k1y 0y1":
        return "K1Y 0Y1"
    elif ZipCode == "NV":
        return "N/A"
    elif ZipCode == "SEEKONK, MA.":
        return "N/A"
    elif ZipCode == "DC":
        return "N/A"
    elif ZipCode == "T0P":
        return "N/A"
    elif ZipCode == "Cambridge, MA":
        return "N/A"
    elif ZipCode == "Nevada":
        return "N/A"
    elif ZipCode == "Kingston 12":
        return "N/A"
    elif ZipCode == "E14 4DHâ€Ž":
        return "E14 4DH"
    elif ZipCode == "WA":
        return "N/A"












    else:
        return ZipCode


df = pd.read_csv('LocationDataSample.csv')
print(df)
df.fillna({'City': 'Not found', 'State': 'Not Found', 'ZipCode': 0, 'Country': 'Not Available'}, inplace=True)
df['change_name_City'] = df.apply(lambda row: change_name_City(row), axis=1)
df['change_name_State'] = df.apply(lambda row: change_name_State(row), axis=1)
df['change_name_ZipCode'] = df.apply(lambda row: change_name_ZipCode(row), axis=1)

df.to_csv('New.csv', index=False)
