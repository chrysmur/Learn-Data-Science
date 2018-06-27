#Reading the gun data from guns.csv
import csv
import datetime
f = open("guns.csv","r")
gun_data = list(csv.reader(f))
headers = gun_data[0]
gun_data = gun_data[1:]

#Reading the 2010 census data from census.csv
f = open("census.csv","r")
census = list(csv.reader(f))
census = census[1]
total_per_race = {}
total_per_race["White"] = census[10]
total_per_race["Hispanic"]=census[11]
total_per_race["Black"] = census [12]
total_per_race["Native American/Native Alaskan"]=census[13]
total_per_race["Asian/Pacific Islander"] = census[14]+ census[15]

#count how many deaths occured in each year
def count_yearly_deaths(data):
    years = [row[1] for row in data]
    year_counts = {}
    for year in years:
        if year in year_counts:
            year_counts[year] += 1
        else:
            year_counts[year] = 1
    return year_counts

#count per month, by creating a datetime object 
def count_monthly_deaths(data):
    dates = [datetime.datetime(year = int(row[1]), month=int(row[2]), day=1) for row in data]
    date_counts = {}
    for date in dates:
        if date.month in date_counts:
            date_counts[date.month] +=1
        else:
            date_counts[date.month] =1
    return date_counts

#count per sex
def count_gender(data):
    sex_counts ={}
    sex_data = [row[5] for row in data]
    for sex in sex_data:
        if sex in sex_counts:
            sex_counts[sex ] +=1
        else:
            sex_counts[sex]=1
    return sex_counts

def count_race(data):
    race_counts = {}
    race_data = [row[7] for row in data]
    for race in race_data:
        if race in race_counts:
            race_counts[race]+=1
        else:
            race_counts[race]=1
    return race_counts

def count_race_per_hundrendk(race_counts):
    race_per_hundrendk = {}
    for race in race_counts:
        race_per_hundrendk[race] = (int(race_counts[race]) / int(total_per_race[race]))*100000
    return race_per_hundrendk

#modify this to take any intent and create the dictionary
def count_by_homicide(data):
    #extract the intent column
    intents = [row[3] for row in data]
    races = [row[7] for row in data]
    homicide_race_counts = {}
    for i,race in enumerate(races):
        if intents[i] == "Homicide":
            if race in homicide_race_counts:
                homicide_race_counts[race] +=1
            else:
                homicide_race_counts[race]=1
    return homicide_race_counts

def count_by_police(data):
    police = [row[4] for row in data]
    races = [row[7] for row in data]
    police_involved = {}
    for i,race in enumerate(races):
        if police[i]=="1":
            if race in police_involved:
                police_involved[race] +=1
            else:
                police_involved[race] = 1
    return police_involved

#Find the most rampant intent 
def ranking_the_intents(data):
    intents_rank = {}
    intents = [row[3] for row in data]
    for intent in intents:
        if intent in intents_rank:
            intents_rank[intent] = intents_rank[intent]+1
        else:
            intents_rank[intent] =1
    #percentage
    total=0
    for key in intents_rank:
        total += intents_rank[key]
    intents_rank_rate = {}
    for intent in intents_rank:
        intents_rank_rate[intent] =  int(intents_rank[intent])/int(total) * 100
        
    return intents_rank_rate
#intent rate per month
def intent_rel_month(data,cause):
    months = [row[2] for row in data]
    intents = [row[3] for row in data]
    cause_per_month={}
    for i,row in enumerate(intents):
        if row == cause:
            if months[i] in cause_per_month:
                cause_per_month[months[i]] +=1
            else:
                cause_per_month[months[i]] = 1
    return cause_per_month
#intent by gender
def intent_rel_gender(data,cause):
    sex = [row[5] for row in data]
    intents = [row[3] for row in data]
    cause_per_sex={}
    for i,row in enumerate(intents):
        if row == cause:
            if sex[i] in cause_per_sex:
                cause_per_sex[sex[i]] +=1
            else:
                cause_per_sex[sex[i]] = 1
    return cause_per_sex


