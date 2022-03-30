### read_annual function definition
def read_annual(file_name,report):
    # The function is defined to read data from the csv file
    
    try:      # to handle exception while opening file
        f = open(file_name, 'r') #to open the file
    except:
        return "File Not Fount"
    
    for line in f:  # to read line by line from the csv file 
        mod_line = line.replace('","',';') #to replace "," by ;
        mod_line = mod_line.replace(',','') #to remove 1000 seperator
        mod_line = mod_line.replace(mod_line[0],'') #to remove the first and last double quote
        mod_line = mod_line.replace(mod_line[0],'') #to remove the dot
        
        line_list=mod_line.split(";")  # to split the line into strings(words) based on ;
        key=line_list[0] # key for dictionary
        value = line_list[3].replace('\n','') #to replace new line by empty char
        report.setdefault(key, []).append(value)
        #report.append(value) #to push data into the report dictionary
    f.close()
    
    return report

### build_rate function definition
def build_rate(report):
    rate = { }
    for key in report: #iterate over report dictionary
        rate[key] = (float(report[key][3])-float(report[key][0]))/float(report[key][0])
        #float function converts string to float value
    return rate  #returns a report dictionary

## build statistics function definition
def build_statistics(report, rate):
    statistics = { } #creates a empty dictionary
    total_increase = 0
    most_populus = " "
    highest_population = 0
    least_populus = " "
    largest_increase = 0
    largest_increasing_city = " " 
    fastest_growing_city = " "
    fastest_growing = 0

    #to calcutate total increase of population
    
            

#write_report function definition
def write_report(r, filename):
    try:
        f = open(filename, "w")
    except:
        return "File Write Error"
    l = []
    f.write(str("State")+','+str("2010")+","+"2011"+","+"2012"+","+"2013"+"\n")
    for k, v in sorted(r.items()):
        l.append("\"%s\"" % (str(k)))
        for t in v: #iterate over list values
            l.append("\"%s\"" %(str(t))) #value is converted into string
        f.write(','.join(l)) #list is converted into string
        f.write('\n')  #this is used to write on a next line
        l = []
    

#write_statistics function definition
def write_statistics(stats, filename):
    try:
        f = open(filename, "w")
    except:
        return "File Write Error"
    f = open(filename, "w")
    l = []
    f.write('Statistic'+','+'Value'+'\n')
    for k, v in sorted(stats.items()):
        l.append('%s' % (str(k)))
        l.append('%s' %(str(v))) #value is converted into string
        f.write(','.join(l)) #list is converted into string
        f.write('\n')
        l = []

if __name__ == '__main__':
    report = { }
    rate = { }
    read_annual("2010.csv",report)

    read_annual("2011.csv",report)
    
    read_annual("2012.csv",report)

    read_annual("2013.csv",report)

    #print(report) #to see the report dic.
    rate=build_rate(report)
	#print(report)
    
    #print(rate) #to see the rate dic
    stats=build_statistics(report,rate)

    #print(stats) #to see the stats dic
    write_report(report,"report.csv")
    write_statistics(stats,"stats.csv")
    print("report has been generated in CSV file")



