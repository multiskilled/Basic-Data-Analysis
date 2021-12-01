import matplotlib.pyplot as plt  #importing matplotlib library for data visualization
import statistics                               #importing statistics for calculating median


#main function
def main():
    read_file()

def read_file():
    #locating file path for csv files
    file_path="life.csv"
    bmi_men="bmi_men.csv"
    bmi_women="bmi_women.csv"
    try:
        #reading 3 files once
        file_obj=open(file_path,"r")
        header_dic,data_dic=write_dic(file_obj) #life expectancy
        bmi_m_file=open(bmi_men,"r")
        men_head,men_data=write_dic(bmi_m_file)#men bmi
        bmi_w_file=open(bmi_women,"r")
        women_head,women_data=write_dic(bmi_w_file)#women bmi
        
        #calling functions
        world_avg=averageAndBmi(men_data,women_data)        #storing average bmi of men and women data in world average dictionary
        
        Statistics(men_head,world_avg)                                              #Calling Statistics method with  header values and world average bmi
        print("Men vs women BMI in highest population countries:")
        print("*** China ***")
        fiveYearBmi(men_data,women_data,'China')                        #calling five year bmi method for men and women data of China
        print("*** India ***")
        fiveYearBmi(men_data,women_data,'India')                        #calling five year bmi method for men and women data of India
        print("*** United States ***")
        fiveYearBmi(men_data,women_data,'United States')            #calling five year bmi method for men and women data of United states

        graphs(data_dic,men_head,world_avg)                         #calling graphs Method for plotting graphs.(data visualization)
    
    except IOError:                                 #if file location is not found or name mistyped then this executes
        print("Err: File was not found")

#Function for creating a dictionary average BMI
def averageAndBmi(men_data,women_data):

    world_avg={}                                #creating empty dictionary
    for k,v in men_data.items():
        avg_bmi=[]                              # storing average bmi in a empty list 
     
        for x in range(0,len(v)):               #runs till lenght of values in mens_data dictionary
            bmi_dic=v[x]+women_data[k][x]        #bmi dic has values from 0 to len(values)  of men data and women data with same size
            avgofAll=bmi_dic/2                 #dividing by because we have two data-men and women data
            avg_bmi.append(avgofAll)         # appending average  average bmi in a empty list 
            world_avg[k]=avg_bmi
   
    return world_avg                    #returns world neutral average dictionary with same size

#Function for five year BMI of men and women data
def fiveYearBmi(men_data,women_data,country):
    years = [24,25,26,27,28]                    #last five years
    men_v = 0                                                #initializing men_value to 0
    #five year bmi value for men  with men-data dictionary
    for k,v in men_data.items():
        if k == country :
            for y in years:
                men_v += v[y]
    men_low=men_v/5
    #five year bmi value for women  with women_data dictionary
    women_v = 0                                            #initializing women_value to 0
    for k,v in women_data.items():
        if k == country:
            for y in years:
                women_v += v[y]
    women_low=women_v/5
    print("Men:     "+str(round(men_low,2)))            #printing men bmi
    print("Women:    "+str(round(women_low,2))) #printing women bmi
    percentage=abs(float(men_low - women_low ))/(float(men_low + women_low)) * 100  #calculating percentage difference
    print("Percent difference:"+"{:.2f}".format(percentage)+"%")                            #prints the percentage difference  with 2 decimal values 


#Function for writing the file data into list and dictionaries
#which takes in csv files as a parameter
def write_dic(Csvfile):
    #Two dictionary data and one header list
    data_dic={}                                                             #initializing a empty data dictionary with country name -> float  values
    header_dic={}                                                           #initializing a empty header dictionary  with country --> years 
    header_list=[]                                                          #initializing a empty list
    
    #initializing coutner value
    c=0
    for line in Csvfile:
        list=[]                                                                 #initializing a empty list
        c+=1
        if c==1:
            record=line.rstrip('\n')                            #striping the \n from list
            record=line.split(',')                                  #splitting  the line by , in list
            key=record[0]                                               #setting record  index 0  and assigning to key
            header_list=record[1::]                                 #assigning  record with index for 1 to end to header_list
            header_dic[key]=header_list
            
        else:
            record=line.rstrip('\n')
            record=line.split(',')
            key=record[0]
            
            list=record[1::]
            #converting the values in the list from String to Float
            for k in range(0,len(list)):
                list[k] = float(list[k])            #using python inbuilt float method to convert from string to float
            data_dic[key]=list              #storing the float list in dictionary as value 
        
    
    Csvfile.close()                             #closing the csv file
    return header_dic, data_dic        #returning dictionary header and data


#Function for displaying and plotting graphs using matpotlib library
def graphs(data,year,world_avg):
    Country=input("Enter the country to visualize life expectancy data: ")

    for k,v in data.items():            #for loop for iterating in the data_dicionary and checking with user input country
        if k == Country:
            y1_data = v[-10:]          #assigning value to y1_data

    for k,v in year.items():            #for loop for iterating  the years from years data
         x_data = v[-10:]                   #assigning value to x_data

    for k,v in world_avg.items():       #for loop for iterating  the world average bmi data f
        y2_data=v[-10:]                          #assigning value to y2_data

    print("Plot for \' "+Country+" \' opens in a new window.")
    print("Correlation plot opens in a new window.")
    fig = plt.figure()
    ax1 = fig.add_subplot()
    ax1.set_xlabel('Years')
    ax1.plot(x_data, y1_data,'b*-')
    ax1.tick_params(axis='y', labelcolor='b')
    ax1.set_ylabel('Life Expectancy,', color='b')
    
    ax2 = ax1.twinx()                          
    ax2.plot(x_data, y2_data, 'ro-')
    ax2.tick_params(axis='y', labelcolor='r')
    ax2.set_ylabel('worldwide average BMI', color='r')

    plt.show()
    print("Good Bye")               #when plot graph window is closed this string prints out

      
#Function for minimum , maximum and median value calculaiton
def Statistics(men_head,world_avg):
    try:
         minMaxList = []                                        #initializing a empty list
         countries=[]                                                #initializing a empty list for storing countries
         user_year=input("select a year to find statistics(1980 to 2008): ")            #takes user input
         if int(user_year) >= 1980  and int(user_year)  <= 2008:
             for k,v in men_head.items():                                                                        #for loop to retrive the year index
                    index_v=v.index(user_year)
                                                        
             for r,s in world_avg.items():                                                                               #for retriving the values of  entered year using Year Index
                    countries.append(r)                                                                                     #appending keys to countries list
                    index_z=s[index_v]                                                                                      #assigning index value of year to index z
                    minMaxList.append(index_z)                                                                                  #appending the values to list
             minimum_country=countries[minMaxList.index(min(minMaxList)) ]                                      #caluating minium for the requested year using builtin min function
             maximum_country=countries[minMaxList.index(max(minMaxList)) ]                                       #caluating minium for the requested year using builtin max function
             MedianValue=statistics.median(minMaxList)                                                                      #calculating median value of  list using the bultin statistics library
             print("In "+ user_year +", countries with minimum and maximum BMI values were "+ minimum_country +"  and  "+maximum_country+ " respectively.\
Median BMI value in 1990 was "+ "{:.3f}".format(MedianValue))                                                                       #prints out the minimum value country, maximun vlaue country and its median value
         else:
             print("Entered year is not in range")      #if input is not in range then this else statement executes
    except ValueError:                                              #if the input value is not integer or not in range then it executes the print  statement
        print("<error>That is an invalid year.")


main()
