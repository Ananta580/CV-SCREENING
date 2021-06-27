import re
import datetime

def ExperienceCalculator(Date="2016  – present"):
    Date =re.sub('(\d+(\.\d+)?)', r' \1 ', Date).strip() 
    Date =  re.sub('[^A-Za-z0-9\- –]','',Date)
    seperator = ['-','to','–']
    present = ['present','till','tillnow','current','currently']
    date = []
    tester=True
    for seperate in seperator:
        if seperate in Date:
            tester = False
            date = Date.split(seperate)
            break
    if tester:
        date.append(Date)
    if len(date) == 1:
        return ExtractExperianceWithPresent(date[0])
    elif re.sub('[^A-Za-z]','',date[1]).lower() in present:
        return ExtractExperianceWithPresent(date[0])
    else:
        return ExtrachExperienceWithPastDate(date[0],date[1])
def ExtrachExperienceWithPastDate(past,future):
    today = datetime.datetime.now() 
    pd1 = past.split()
    pd2 = future.split()
    preMonth1 = -1
    preMonth2 = -1
    preYear1 = -1 
    preYear2 = -1 
    for p in pd1:
        if not p.isnumeric():
            preMonth1= ConvertStringMonthToNumber(p)
        else: preYear1 =int(p)
    if(preYear1==-1):
        return 0
    if(preMonth1!=-1):
        pastDate = datetime.datetime(preYear1,preMonth1,today.day)
    else:
        pastDate = datetime.datetime(preYear1,today.month,today.day)

    itemListCount = 0
    for p in pd2:
        if(itemListCount<2):
            if not p.isnumeric():
                preMonth2= ConvertStringMonthToNumber(p)
            else: preYear2 =int(p)
        itemListCount +=1
    if(preYear2==-1):
        return 0
    if(preMonth2!=-1):
        futureDate = datetime.datetime(preYear2,preMonth2,today.day)
    else:
        futureDate = datetime.datetime(preYear2,today.month,today.day)

    exp = round((futureDate-pastDate).days/365,1)
    return exp

def ExtractExperianceWithPresent(previousDate):
    today = datetime.datetime.now() 
    pd = previousDate.split()
    preMonth = -1
    preYear = -1 
    for p in pd:
        if not p.isnumeric():
            preMonth= ConvertStringMonthToNumber(p)
        else: preYear =int(p)
    if(preYear==-1):
        return 0
    if(len(str(preYear))==2):
        preYear=preYear+2000
    if(preMonth!=-1):
        preDate = datetime.datetime(preYear,preMonth,today.day)
    else:
        preDate = datetime.datetime(preYear,today.month,today.day)

    exp = round((today-preDate).days/365,1)
    return exp

def ConvertStringMonthToNumber(month):
    longMonth = [ 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december' ] 
    shortMonth = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    month = month.lower()
    month = re.sub('[^A-Za-z]','',month)
    num=-1
    if month in longMonth:
        num = longMonth.index(month) + 1
    if month in shortMonth:
        num = shortMonth.index(month) + 1
    return num
    
ExperienceCalculator()
