import pandas as pd

baseUrl = "https://apps.alleghenycounty.us/website/millsd.asp?Year={}"

fromYear = 2001
toYear = 2019

allTables = []

for year in range(fromYear, toYear + 1):
    url = baseUrl.format(year)
    
    table = pd.read_html(url)[0]

    table.insert(4, "Year", year)

    allTables.append(table)

allDfs = pd.concat(allTables)

filename = "sd_millages.xlsx"

allDfs.to_excel(filename)

print("Output School District millages to {}".format(filename))
