###################################################################
# Building a Class for Data Visualisation {Assignment2 of FIT9133}#
###################################################################

#############################################################
# Student name:         Sohail.Sankanur                     #
# Monash Student ID:    29996368                            #
# Start Date:           07 Oct 2018                         #
# Last Modified Date:   12 Oct 2018                         #
#############################################################


## Explaination of the task:
#>> In this task we have created a python class named Visualiser
#>> This class is used for visualisation of data which is obtained from task-2.
#>> In this class we have a method named 'compute_averages' which computes mean of the statistics values obtained.
#>> In this class we have another method named 'visualise_statistics' which plots bar graphs of the mean difference of
#   the data obtained from the previous task

## Explaination of the code structure:
#>> In the constructor method __init__ we have declared the instance variable and we assign the statistics value to it.
#>> The statistics value set is obtained as an input argument from the user which would be in the form of a list
#>> We have a method named 'compute_averages' which would compute the mean value for set of statistics values of SLI and
#   TD datasets.
#>> The allstats instance variable would be a list of all the statistics values. Each set of statistics value would be
#   stored in a list. Thus value are obtained form the statistics values list inside the allstats list and mean is computed
#   using the numpy mean method.
#>> The 'visualise_statistics'  is a method which would plot the bar graphs of the mean difference values of (SLI vs TD).
#>> The plot is done using the matplotlib library. matplotlib.pyplot is used for this task





import numpy as np
import matplotlib.pyplot as plt



class Visualiser:
    allstatsMeanData=[] #this is a class variable. It stores all the mean data generated.

    def __init__(self,allstats):    #constructer method which declared and assigns value to instance variables
        self.allstats = allstats


    def compute_averages(self): #this method computes the mean value for the set of statistics values generated

        t = []

        for j in range(0, len(self.allstats[0])):
            for i in np.array(self.allstats):
                t.append(i[j])
            Visualiser.allstatsMeanData.append(np.mean(t))
            t.clear()



    def visualise_statistics(self):  #this method plots the mean difference which would be used for data visualisation
        SLIlist=[]
        TDlist=[]
        for i in range(0,(len(Visualiser.allstatsMeanData)//2)):
            SLIlist.append(Visualiser.allstatsMeanData[i])
        for i in range((len(Visualiser.allstatsMeanData)//2),len(Visualiser.allstatsMeanData)):
            TDlist.append(Visualiser.allstatsMeanData[i])
        meanDifference = list((np.array(SLIlist) - np.array(TDlist)))
        left=[1,2,3,4,5,6]
        tick_label=['transcript_length','vocabulary','repetition','retracing','gramatical_errors','no. of pauses']
        print("\n\nSLI mean values are as follows:")
        print("mean transcript_length: "+str(SLIlist[0]))
        print("mean vocabulary: " + str(SLIlist[1]))
        print("mean repetition: " + str(SLIlist[2]))
        print("mean retracing: " + str(SLIlist[3]))
        print("mean gramatical errors: " + str(SLIlist[4]))
        print("mean number of pauses: " + str(SLIlist[5]))

        print("\n\nTD mean values are as follows:")
        print("mean transcript_length: " + str(TDlist[0]))
        print("mean vocabulary: " + str(TDlist[1]))
        print("mean repetition: " + str(TDlist[2]))
        print("mean retracing: " + str(TDlist[3]))
        print("mean gramatical errors: " + str(TDlist[4]))
        print("mean number of pauses: " + str(TDlist[5]))

        #plot of mean values of SLI
        plt.subplot(711)
        plt.bar(left, SLIlist, tick_label=tick_label,
                width=0.9, color=['green'])
        # naming the x-axis
        plt.xlabel('x - axis')
        # naming the y-axis
        plt.ylabel('y - axis')
        # plot title
        plt.title('SLI mean value plot')



        #plot of mean values of TD
        plt.subplot(714)

        plt.bar(left, TDlist, tick_label=tick_label,
                width=0.9, color=['green'])
        # naming the x-axis
        plt.xlabel('x - axis')
        # naming the y-axis
        plt.ylabel('y - axis')
        # plot title
        plt.title('TD mean value plot')

        #plot of mean difference values (SLI vs TD)
        plt.subplot(717)

        plt.bar(left, meanDifference, tick_label=tick_label,
                width=0.9, color=['red'])

        # naming the x-axis
        plt.xlabel('x - axis')
        # naming the y-axis
        plt.ylabel('y - axis')
        # plot title
        plt.title('SLI vs TD mean difference plot')

        # function to show the plot
        plt.show()
