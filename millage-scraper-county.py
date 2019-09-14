import pandas as pd

baseUrl = "https://apps.alleghenycounty.us/website/MillMuni.asp?Year={}"

fromYear = 2001
toYear = 2019

allTables = []

for year in range(fromYear, toYear + 1):
    url = baseUrl.format(year)

    table = pd.read_html(url)[0]

    table.insert(5, "Year", year)

    allTables.append(table)

allDfs = pd.concat(allTables)

filename = "co_millages.xlsx"

allDfs.to_excel(filename)

print("Output to {}".format(filename))
