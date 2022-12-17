import ROOT as r
import settings_common

variables = settings_common.variables

inputs = {}
for inputname,inputcontent in settings_common.inputs.items():
    #print inputname
    if (not "cHHH1" in inputname) and (not "SM" in inputname):
        #print "not found"
        continue
    inputs[inputname]=inputcontent

#print inputs
