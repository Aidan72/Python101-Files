##Author Aidan Lewis
##Date: 4/5/2024
##Assignment: City temperatures python code
##Description: This program will input a file the proceed to read until the end of file delimiter while keeping track of all the data.
##    It will then calculate statistics on the data


def main():
    cityname = input('Enter the name of the city temperature file:')
    mintemp = float(200)
    # Set variables equal to zero
    counter = 0
    days = 0
    total = 0
      # With and while expression to put place of "While NOT eof(cityname)"
    with open(cityname, 'r') as data:
      while True: 
        temps = data.readline().strip() 
        # looking for the end of data then breaking the loop
        if temps == '':  
            break
     # Changing string to float     
        temperatures = float(temps)
     # Find Calculations
        days = days + 1
        total = total + temperatures
        if temperatures < mintemp:
           mintemp = temperatures
    # find average
    avg = total / days
    # Display data
    print('Number of days monitored=', days )
    print('Minimum temperature in monitored period=', mintemp)
    print('Average temperature during monitored period=', avg)

main()
#### **********SAMPLE OUTPUT******************* 
## Enter the name of the city temperature file:WestChicago.dat
##Number of days monitored= 119
##Minimum temperature in monitored period= -29.843265070500404
##Average temperature during monitored period= 11.359720937075132   
