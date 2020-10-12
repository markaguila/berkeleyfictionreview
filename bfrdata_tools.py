from collections import Counter
import re

"""
Python code used to analyze BFR data.

Available BFR author and editor names along with story titles were
copied from the BFR website and pasted in a text file.

Available BFR issues were downloaded as pdf files from BFR website,
converted to text files using Zamzar, and read into Python for analysis.

Note: Not all issues of BFR were available for download.
Editor, author, and title data included from issues: 1-4, 6-9, 13, 15-21, 23-39
(Data missing from 5, 10-12, 14, 22)
Full text included from issues: 6-9, 15-21, 23-27
(Full text missing from 1-5, 10-14, 22, 28-39)

"""


"CODE TO OPEN AND READ IN TEXT FILES"

bfr_path = "C:/Users/Mark/Desktop/downloads/BFR/"

names = open(bfr_path + "name_data.txt")
name = names.read().split()

"A list of the issue numbers for which there the full text is available."
issue_numbers = [x for x in range(6, 10)] + [x for x in range(15, 22)] + [x for x in range(23, 28)]

"A list of the file paths for the corresponding issues."
issue_paths = [bfr_path + "Issue " + str(x) + ".txt" for x in issue_numbers]

"A list with the full text of each issue."
issues = [open(x).read() for x in issue_paths]

"A string containing the full text of every available issue."
master = issues[0]
for x in issues[1:]:
    master = master + x



"HELPFUL FUNCTIONS TO LOOK AT WORD COUNTS"

"Print the number of times WORD appears in master, case-sensitive."
def exact_word_count(word):
    print(word, ":", master.count(word))

"Print the number of times WORD appears with capital or lowercase letters."
def word_count(word):
    print(word.lower(), ":", master.lower().count(word.lower()))

"Print the number of times WORD appears in each issue."
def all_word_count(word):
    print(word)
    for i in range(len(issues) - 1):
        text = issues[i]
        number = issue_numbers[i]
        print("Issue", number, ":", text.lower().count(word))

"Print the word frequency (not case-sensitive) of all the words in WORD_LIST. (Counts from all issues.)"
def compare_words(word_list):
    for word in word_list:
        word_count(word)

"Print the word frequency (case-sensitive) of all the words in WORD_LIST. (Counts from all issues.)"
def compare_exact_words(word_list):
    for word in word_list:
        exact_word_count(word)



"LIST OF US STATES AND WORLD COUNTRIES"
"Countries copied and pasted from online references and split into lists"

us_states = """Alabama
Alaska
Arizona
Arkansas
California
Colorado
Connecticut
Delaware
Florida
Georgia
Hawaii
Idaho
Illinois
Indiana
Iowa
Kansas
Kentucky
Louisiana
Maine
Maryland
Massachusetts
Michigan
Minnesota
Mississippi
Missouri
Montana
Nebraska
Nevada
New Hampshire
New Jersey
New Mexico
New York
North Carolina
North Dakota
Ohio
Oklahoma
Oregon
Pennsylvania
Rhode Island
South Carolina
South Dakota
Tennessee
Texas
Utah
Vermont
Virginia
Washington
West Virginia
Wisconsin
Wyoming"""

us_list = us_states.split("\n")

all_countries = """
Afghanistan
Albania
Algeria
Andorra
Angola
Antigua and Barbuda
Argentina
Armenia
Australia
Austria
Azerbaijan
The Bahamas
Bahrain
Bangladesh
Barbados
Belarus
Belgium
Belize
Benin
Bhutan
Bolivia
Bosnia and Herzegovina
Botswana
Brazil
Brunei
Bulgaria
Burkina Faso
Burundi
Cabo Verde
Cambodia
Cameroon
Canada
Central African Republic
Chad
Chile
China
Colombia
Comoros
Congo, Democratic Republic of the
Congo, Republic of the
Costa Rica
Côte d’Ivoire
Croatia
Cuba
Cyprus
Czech Republic
Denmark
Djibouti
Dominica
Dominican Republic
East Timor (Timor-Leste)
Ecuador
Egypt
El Salvador
Equatorial Guinea
Eritrea
Estonia
Eswatini
Ethiopia
Fiji
Finland
France
Gabon
The Gambia
Georgia
Germany
Ghana
Greece
Grenada
Guatemala
Guinea
Guinea-Bissau
Guyana
Haiti
Honduras
Hungary
Iceland
India
Indonesia
Iran
Iraq
Ireland
Israel
Italy
Jamaica
Japan
Jordan
Kazakhstan
Kenya
Kiribati
Korea, North
Korea, South
Kosovo
Kuwait
Kyrgyzstan
Laos
Latvia
Lebanon
Lesotho
Liberia
Libya
Liechtenstein
Lithuania
Luxembourg
Madagascar
Malawi
Malaysia
Maldives
Mali
Malta
Marshall Islands
Mauritania
Mauritius
Mexico
Micronesia
Moldova
Monaco
Mongolia
Montenegro
Morocco
Mozambique
Myanmar
Namibia
Nauru
Nepal
Netherlands
New Zealand
Nicaragua
Niger
Nigeria
North Macedonia
Norway
Oman
Pakistan
Palau
Panama
Papua New Guinea
Paraguay
Peru
Philippines
Poland
Portugal
Qatar
Romania
Russia
Rwanda
Saint Kitts and Nevis
Saint Lucia
Saint Vincent and the Grenadines
Samoa
San Marino
Sao Tome and Principe
Saudi Arabia
Senegal
Serbia
Seychelles
Sierra Leone
Singapore
Slovakia
Slovenia
Solomon Islands
Somalia
South Africa
Spain
Sri Lanka
Sudan
South Sudan
Suriname
Sweden
Switzerland
Syria
Taiwan
Tajikistan
Tanzania
Thailand
Togo
Tonga
Trinidad and Tobago
Tunisia
Turkey
Turkmenistan
Tuvalu
Uganda
Ukraine
United Arab Emirates
United Kingdom
United States
Uruguay
Uzbekistan
Vanuatu
Vatican City
Venezuela
Vietnam
Yemen
Zambia
Zimbabwe"""

countries_list = all_countries.split("\n")

c = {}
s = {}
w = {}



"Code commented out to decease load time for program."
#c['country'] = [x for x in countries_list]
#s['state'] = [x for x in us_list]
#c['count'] = [master.count(x) for x in countries_list]
#s['count'] = [master.count(x) for x in us_list]

"Use Counter().most_common(n) to look at top entries."
