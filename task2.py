##############################################################
# Building a Class for Data Analysis {Assignment2 of FIT9133}#
##############################################################

#############################################################
# Student name:         Sohail.Sankanur                     #
# Monash Student ID:    29996368                            #
# Start Date:           07 Oct 2018                         #
# Last Modified Date:   12 Oct 2018                         #
#############################################################

## Explaination of task:
#>> In this task we have created a class named Analyser
#>> This class is used to find statistics values from the filtered files. The statistics values could be used for data analytics
#>> In the class we have the method named 'analyse_script' which is used for finding the statistics values of the filtered
#   transcripts

## Explaination of the code structure:
#>> In the constructer method __init__ we create instance variables and assign default value 0 to all the variables
#>> In the analyse_script method we take an input argument which is string.
#>> The string is he name of the cleaned files which is obtained from task-1
#>> In this method we read the cleaned files and store them in a python list in the form of strings
#>> Out of this list all the statistics values required are calculated and stored
#>> The statistics vales can be used for further data analytics
#>> We have the __str__ method. Thus if we print the object all the statistics data of the object are printed.

class Analyser:

    def __init__(self):     #method for declaring and assigning values to instance variables
        self.len_transcript = 0
        self.unique_count = 0
        self.allwords = []
        self.uniquewords = []
        self.liststrings=[]
        self.rep_count = 0
        self. retrace_count = 0
        self.grammer_error_count = 0
        self.pauses_count = 0

    def analyse_script(self, cleaned_file):     # method for analysing the fintered transcripts and finding the statistics values
        fileread = open(str(cleaned_file), 'r')
        self.liststrings = fileread.readlines()
        self.len_transcript = len(self.liststrings)
        fileread = open(str(cleaned_file),'r')
        self.allwords = fileread.read().split()

        for i in self.allwords:
            i=i.replace(",","")
            i=i.replace(":","")
            i=i.replace("::","")
            if i in self.uniquewords:
                continue
            elif i == "[/]":
                self.rep_count += 1
                continue
            elif i == "[//]":
                self.retrace_count +=1
                continue
            elif i == "[*":
                self.grammer_error_count += 1
                continue
            elif i == "m:+ed]":
                continue
            elif i == "(.)":
                self.pauses_count +=1
                continue
            elif i=="m+ed]" or i=="*EXA" or i == "." or i == "!" or i == "?" or i == "[/]" or i == "[//]" or i == "[*]" or i == "(.)" or i.find(".")>-1:
                continue
            else:
                self.unique_count += 1
                self.uniquewords.append(i)



    def __str__(self):      #method which shows the statistics values in human readable format
        a=  "Length of the transcript is: "+str(self.len_transcript)+"\n"+"Size of the vocabulary is: "+\
               str(self.unique_count)+"\n"+"Number of repetition for certain words or phrases is: "+\
               str(self.rep_count)+"\n"+"Number of retracing for certain words or phrases is: "+\
            str(self.retrace_count)+"\n"+"Number of grammatical errors detected are: "+str(self.grammer_error_count)+\
            "\n"+"Number of pauses made are: "+str(self.pauses_count)
        return a

