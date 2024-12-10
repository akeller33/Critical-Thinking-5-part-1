# Andrew Keller
# 12/7/2024

rainfall = []
years = input('Enter the number of years we are analyzing. ')
while isinstance(years, str):
    if years.isdigit():
        years = int(years)
    else:
        years = input('Must be a whole number. Enter the number of years we are analyzing.')
    
months = ['January','Febuary', 'March','April','May','June','July','August','September','October','November','December']
for year in range(years):
    row = []
    for month in range(len(months)):
        rain = input(f'How much rain fell in the month of {months[month]} of year {year+1}. ')
        while isinstance(rain, str):
            if rain.replace('.','').isdigit():
                rain = float(rain)
            else:
                rain = input(f'Must be a number. How much rain fell in the month of {months[month]} of year {year+1}. ') 
        row.append(rain)
    rainfall.append(row)

total_months = years * 12
total_rain = 0
for year in rainfall:
    for month in year:
        total_rain += month
avg_rain = total_rain / total_months



print(rainfall)
print(f'The total rainfall for the {total_months} months in question was {total_rain}.')
print(f'Giving us an average rainfall of {avg_rain:.2f} inches per month.')
                   
            
