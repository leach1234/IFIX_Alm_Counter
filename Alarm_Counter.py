###############################################################################
## Alarm_Counter.py
## Reads in alarm logs for IFIX, and count alarms per type
## Created by Andrew Leach
###############################################################################

#import all external code	
import csv
import sys
import glob

#Declare site name
site_name =""


#Opens all file in local directory
for names in glob.glob('*.ALM'):
	#Prints file being processed
	print ("Process file " + names)

	#Setup array
	alarm_dict = {}
	
	with open(names) as csv_file:
		#open csv file
		csv_reader = csv.reader(csv_file, delimiter=',')

		for row in csv_reader:
			#runs through all of the alarms
		
			#create the site name
			site_act = (str(row))
			site_act = site_act[25:]
			site_act = site_act[:7]
			
			status = (str(row))
			status = status[66:]
			status = status[:3]
			
			
			#Check to see if site name match declared site
			if (site_act == site_name or site_name == "") and status == "CFN":
		
				#create the alarm tag
				tag_ID = (str(row))
				tag_ID = tag_ID[35:]
				tag_ID = tag_ID[:28]
				#remove trailing spaces
				tag_ID = tag_ID.strip()
				
				time_alm = (str(row))
				time_alm = time_alm[13:]
				time_alm = time_alm[:8]
				#print (time_alm)
				if (tag_ID in alarm_dict) == True:
					#exists, therefore only increment counter
					alarm_dict[tag_ID][0]  += 1
					alarm_dict[tag_ID][3]  = alarm_dict[tag_ID][3] + "," + str(time_alm)
				else:
					#generates the alarm description
					deciption = (str(row))
					deciption = deciption[-43:-2]
					deciption = deciption.strip()
					#create new entry
					alarm_dict[tag_ID] = [1, deciption, time_alm, ""]


	#create text fill
	temp_file = names[:6]
	temp_file = temp_file + ".csv"
	text_file=open(temp_file,'w')
	#writes the header
	text_file.writelines('Count, Tag, Desciption, Time First Occur,, Following Occurance\n')
	#loop though all directory and then write to text file
	for items in alarm_dict:
		text_file.writelines(str(alarm_dict[items][0]) + "," + items + "," + alarm_dict[items][1] + "," + str(alarm_dict[items][2]) + "," + alarm_dict[items][3])
		text_file.writelines('\n')
		#print (items)
	#Close the text file		
	text_file.close()
	print ("File Processing Complete " + names)
print("Complete")