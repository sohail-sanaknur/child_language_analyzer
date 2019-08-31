#########################################################################
# Handling with File Contents and Preprocessing {Assignment2 of FIT9133}#
#########################################################################

#############################################################
# Student name:         Sohail.Sankanur                     #
# Monash Student ID:    29996368                            #
# Start Date:           07 Oct 2018                         #
# Last Modified Date:   12 Oct 2018                         #
#############################################################

## Explaination of task:
#>> In this task we have created a method named 'cleanfile'. This takes in an input argument which is the filename path
#>> this method would first filter out the relavent data
#>> After filtering out the relavent data we write the filtered data to a new file.

## Explaination of the code structure:
#>> In the code we have a method named 'cleanfile' which takes in an input argumrnt which would be a string.
#>> In the first part of the code in the method it checks weather the files 'SLI_cleaned' and 'TD_cleaned' exists in the
#   ENNI folder. If they are not present the file directories are created.
#>> After this step we take the filename and append the path to it.
#>> We then read the file transcripts.
#>> Each string from the transcript is split with the help of string split function and the delimeter used in "*CHI:"
#>> We further split the string based on the "%mor" delimeter and only the relevant data is obtained.
#>> All the relevant data is stored in a list in the form of strings.
#>> All the filtering tasks which are mentioned in task1 is performed on the string and the filtered strings are placed in a
#   new list
#>> We then write all the filtered strings to a file in SLI_cleaned or the TD_cleaned folder.

import os

def cleanFile(filename):   #method for fltering out relavent data out of file transcripts
    if not os.path.exists("ENNI/SLI_cleaned"):
        os.makedirs("ENNI/SLI_cleaned")

    if not os.path.exists("ENNI/TD_cleaned"):
        os.makedirs("ENNI/TD_cleaned")
    print("\n\nFiltered output of "+filename)
    if filename.find("SLI") > -1:
        cfilename = "ENNI/SLI_cleaned/" + filename.replace(".txt","") + "_cleaned.txt"
    else:
        cfilename = "ENNI/TD_cleaned/" + filename.replace(".txt","") + "_cleaned.txt"
    if filename.find("SLI") > -1:
        filename="ENNI/SLI/"+filename
    else:
        filename = "ENNI/TD/" + filename
    file_read = open(filename, 'r')
    splitChi= file_read.read().split("*CHI:")
    allstr = []
    finallist=[]
    for i in range(1,len(splitChi)):
        allstr.append(splitChi[i].split("%mor:")[0].replace("\n\t",' ').strip())
    for k in allstr:
        st = k
        tempstr = st
        tempstr=tempstr.replace("(..)","")
        tempstr=tempstr.replace("(...)","")
        tempstr=tempstr.replace("[*]","")
        tempstr=tempstr.replace("[* m:+ed]","[*]")
        wordremove = ""
        for i in range(0,len(st)):
            if st[i] == "[":
                for j in range(i,len(st)):
                    wordremove=wordremove+st[j]
                    if st[j]=="]":
                        if wordremove=="[//]" or wordremove=="[/]" or wordremove=="[*]":

                            break
                        else:
                            wordremove=" "+wordremove
                            tempstr = tempstr.replace(wordremove,"")

                            break
                wordremove=""

            tempstr = tempstr.replace("<","")
            tempstr = tempstr.replace(">","")

            if st[i] == "&" or st[i]=="+":
                for j in range(i,len(st)):
                    wordremove = wordremove+st[j]
                    if st[j]==" ":
                        tempstr = tempstr.replace(wordremove,"")
                        wordremove=""
        tempstr = tempstr.replace("(.)", "#TokenForReplacement#")
        tempstr=tempstr.replace("(","")
        tempstr=tempstr.replace(")","")
        tempstr = tempstr.replace("#TokenForReplacement#","(.)")
        tempstr=tempstr.replace("[*]","[* m:+ed]")
        print(tempstr)
        finallist.append(tempstr)

    #this part of the code writes the output relavent data to the new files.

    file_write=open(cfilename,'w')
    for i in finallist:
        file_write.write(i + "\n")
    file_read.close()
    file_write.close()

