#########################################################
# Programme to run the analyser {Assignment2 of FIT9133}#
#########################################################

#############################################################
# Student name:         Sohail.Sankanur                     #
# Monash Student ID:    29996368                            #
# Start Date:           07 Oct 2018                         #
# Last Modified Date:   12 Oct 2018                         #
#############################################################

## Explaination of the runme_29996368:
#>> In this code all the three tasks which are created are used.
#>> Firtly in this code we would import all the three task codes.
#>> All the transcripts which are present in the SLI and the TD folder are then fed to the task-1 and relavent data is
#   filtered out. 'cleanFile' methid is used for this task
#>> Now using the task2 python script all the statistics values are found for the filtered transcripts and they are
#   stored in a list
#>> Analyser objects are created for SLI and TD filtered transcripts and statistics values are generated
#>> Now for the visualisation of the data the task-3 is used
#>> Visualiser object is created and mean values for the statistics values for the SLI and TD datasets are calculated
#>> The mean values are computed using the 'compute_averages' method of the Visualiser class in task-2
#>> Using the 'visualise_statistics' method of the Visualiser class from task-3 the bar graphs for the mean difference
#   of (SLI vs TD) is calculated.


###>> The assignmet is designed such that all the outputs are interactively printed during execution of this programme <<####



from task2_29996368 import Analyser
from task3_29996368 import Visualiser
from task1_29996368 import cleanFile
import os




TDFileList=sorted(os.listdir("ENNI/TD"))
for i in TDFileList:
    if i.startswith("."):
        TDFileList.remove(i)

SLIFileList=sorted(os.listdir("ENNI/SLI"))
for i in SLIFileList:
    if i.startswith("."):
        SLIFileList.remove(i)

SLIFileList.sort(key=lambda x: int(os.path.splitext(x.split('-')[1])[0]))
TDFileList.sort(key=lambda x: int(os.path.splitext(x.split('-')[1])[0]))

for i in SLIFileList:
    cleanFile(i)

for i in TDFileList:
    cleanFile(i)

all_stats=[]
import os
SLIcleanedList=os.listdir("ENNI/SLI_cleaned/")
for i in SLIcleanedList:
    if i.startswith("."):
        SLIcleanedList.remove(i)
SLIcleanedList.sort(key=lambda x: int((os.path.splitext(x.split('-')[1])[0]).split("_")[0]))
for i in SLIcleanedList:
    print("\n\nStatistics of " + i)
    SLIobj = Analyser()
    SLIobj.analyse_script("ENNI/SLI_cleaned/"+i)
    all_stats.append([SLIobj.len_transcript, SLIobj.unique_count, SLIobj.rep_count, SLIobj.retrace_count, SLIobj.grammer_error_count,
                 SLIobj.pauses_count])
    print(SLIobj)
vis=Visualiser(all_stats)
vis.compute_averages()

all_stats.clear()
import os
TDcleanedList=os.listdir("ENNI/TD_cleaned/")
for i in TDcleanedList:
    if i.startswith("."):
        TDcleanedList.remove(i)
TDcleanedList.sort(key=lambda x: int((os.path.splitext(x.split('-')[1])[0]).split("_")[0]))
for i in TDcleanedList:
    print("\n\nStatistics of " + i)
    TDobj = Analyser()
    TDobj.analyse_script("ENNI/TD_cleaned/"+i)
    all_stats.append([TDobj.len_transcript, TDobj.unique_count, TDobj.rep_count, TDobj.retrace_count, TDobj.grammer_error_count,
                 TDobj.pauses_count])
    print(TDobj)
vis=Visualiser(all_stats)
vis.compute_averages()

vis.visualise_statistics()


