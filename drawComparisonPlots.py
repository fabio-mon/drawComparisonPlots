#!/bin/python
import os,sys,copy,math
import json
from array import array
import ROOT as r
from optparse import OptionParser
from math import sqrt
import importlib

#r.gStyle.SetPalette(1)
r.gStyle.SetOptStat(0)
r.gStyle.SetOptTitle(0)
r.gStyle.SetNumberContours(200)
r.gROOT.SetBatch(True)

def extra_texts():
    # print "... drawing extra texts"
    ### extra text
    cmstextfont   = 61  # font of the "CMS" label
    cmstextsize   = 0.05  # font size of the "CMS" label
    chantextsize = 18
    extratextfont = 52     # for the "preliminary"
    extratextsize = 0.76 * cmstextsize # for the "preliminary"
    lumitextfont  = 42
    cmstextinframe = False

    yoffset = -0.046

    #lumibox = r.TLatex  (0.9, 0.964+yoffset, "137 fb^{-1} (13 TeV)")
    lumibox = r.TLatex  (0.9, 0.964+yoffset, "1 fb^{-1} (13 TeV)")
    lumibox.SetNDC()
    lumibox.SetTextAlign(31)
    lumibox.SetTextSize(extratextsize)
    lumibox.SetTextFont(lumitextfont)
    lumibox.SetTextColor(r.kBlack)

    # xpos  = 0.177
    xpos  = 0.137
    if cmstextinframe:
        ypos  = 0.94 ## inside the frame
    else:
        ypos  = 0.995  ## ouside the frame
    CMSbox = r.TLatex  (xpos, ypos+yoffset+0.01, "CMS")       
    CMSbox.SetNDC()
    CMSbox.SetTextSize(cmstextsize)
    CMSbox.SetTextFont(cmstextfont)
    CMSbox.SetTextColor(r.kBlack)
    CMSbox.SetTextAlign(13) ## inside the frame

    # simBox = r.TLatex  (xpos, ypos - 0.05+yoffset, "Simulation")
    simBox = r.TLatex  (xpos + 0.12, ypos+yoffset, "Simulation")
    #simBox = r.TLatex  (xpos + 0.12, ypos+yoffset, "Preliminary")
    simBox.SetNDC()
    simBox.SetTextSize(extratextsize)
    simBox.SetTextFont(extratextfont)
    simBox.SetTextColor(r.kBlack)
    simBox.SetTextAlign(13)

    channelLabel = r.TLatex  (0.6-0.05, 0.8, "HH #rightarrow #gamma#gammab#bar{b}")
    channelLabel.SetNDC()
    # channelLabel.SetTextAlign(31)
    channelLabel.SetTextSize(1.15*extratextsize)
    channelLabel.SetTextFont(lumitextfont)
    channelLabel.SetTextColor(r.kBlack)

    #channelLabel0 = r.TLatex  (0.6-0.05, 0.7, "Expected (#kappa_{#lambda} = 1)")
    channelLabel0 = r.TLatex  (0.2, 0.8, "Observed")
    channelLabel0.SetNDC()
    channelLabel0.SetTextSize(1.15*extratextsize)
    channelLabel0.SetTextFont(lumitextfont)
    channelLabel0.SetTextColor(r.kBlack)


    return [lumibox, CMSbox, simBox]#, channelLabel, channelLabel0]
    # lumibox.Draw()
    # CMSbox.Draw()
    # simBox.Draw()
    # channelLabel.Draw()


parser = OptionParser()
parser.add_option("--settings",          default="",                        help="Configuration file for plots")
parser.add_option("--outdir",            default="./plots/",                help="Output dir for plots")
(options,args)=parser.parse_args()

settings = importlib.import_module(options.settings)
inputs=settings.inputs
variables=settings.variables

# define histograms
print ("Define histograms")
histos = {}
for inputname, inputcontent in inputs.items():
    print ("> doing input "+inputname)
    histos[inputname] = {}
    for variablename, variablesettings in variables.items():
        print (">> doing variable "+variablename)
        histos[inputname][variablename] = r.TH1F(
            inputname+"_"+variablename,
            inputname+"_"+variablename,
            variablesettings["Nbin"],
            variablesettings["xmin"],
            variablesettings["xmax"]
        )
        
print ("Fill histograms")
for inputname, inputcontent in inputs.items():
    print ("> doing input "+inputname)
    for filelumi in inputcontent["filelumis"]:
        filename = filelumi[0]
        objname = filelumi[1]
        lumi = filelumi[2]
        print (">> doing file "+filename+"/"+objname) 
        ch = r.TChain()
        ch.Add(filename+"/"+objname)

        for variablename, variablesettings in variables.items():
            print (">>> doing variable "+variablename)
            Nev = ch.Draw( variablesettings["formula"]+">>+"+inputname+"_"+variablename, inputcontent["weight"]+"*"+str(lumi) , "goff" )
            print (">>> draw %i events"%Nev)
            print (">>> number of entries %i"%histos[inputname][variablename].GetEntries())



print ("Draw histograms")
histostacks = {}
histosums = {}

for variablename, variablesettings in variables.items():
    c = r.TCanvas('c', 'c', 800, 800)
    c.SetFrameLineWidth(3)
    c.SetBottomMargin(0.13)
    c.SetLeftMargin(0.13)

    histostacks[variablename] = r.THStack("stack_"+variablename,"")
    histosums[variablename] = r.TH1F(
        "sum_"+variablename,
        "sum_"+variablename,
        variablesettings["Nbin"],
        variablesettings["xmin"],
        variablesettings["xmax"]
    )

    legend = r.TLegend(0.5,0.68,0.9,0.88)
    legend.SetBorderSize(0)
    legend.SetFillStyle(-1)
    legend.SetTextFont(42)
    legend.SetTextSize(0.035)

    ymin=0.
    ymax=-999.
    for inputname, inputcontent in inputs.items():
        histos[inputname][variablename].SetFillStyle(inputcontent["fillstyle"])
        histos[inputname][variablename].SetFillColor(inputcontent["fillcolor"])
        if "linecolor" in inputcontent:
            histos[inputname][variablename].SetLineColor(inputcontent["linecolor"])
            histos[inputname][variablename].SetLineWidth(3)
        if "markerstyle" in inputcontent:
            histos[inputname][variablename].SetMarkerStyle(inputcontent["markerstyle"])
        if inputcontent["stack"]==1:
            histostacks[variablename].Add(histos[inputname][variablename])
            histosums[variablename].Add(histos[inputname][variablename])

        if( "E1" in inputcontent["drawstyle"]):
            legend.AddEntry(histos[inputname][variablename],inputcontent["title"],"PL")
        elif(inputcontent["fillstyle"]==0):
            legend.AddEntry(histos[inputname][variablename],inputcontent["title"],"L")
        else:
            legend.AddEntry(histos[inputname][variablename],inputcontent["title"],"F")

        if ymax==-999.:
            ymax=histos[inputname][variablename].GetMaximum()
        elif histosums[variablename].GetMaximum()>ymax:
            ymax=histosums[variablename].GetMaximum()
        elif histos[inputname][variablename].GetMaximum()>ymax:
            ymax=histos[inputname][variablename].GetMaximum()


    if not( ("ymin" in variablesettings) and ("ymax" in variablesettings) ):
        variablesettings["ymin"] = ymin*0.75
        variablesettings["ymax"] = ymax*1.35
        
    hPad = r.gPad.DrawFrame(variablesettings["xmin"],variablesettings["ymin"],
                            variablesettings["xmax"],variablesettings["ymax"])

    #if any draw the stack
    if histosums[variablename].GetEntries>0:
        histostacks[variablename].Draw("hist SAME")
        r.gPad.RedrawAxis("");
        r.gPad.RedrawAxis("G");

        histosums[variablename].SetMarkerSize(0.);
        histosums[variablename].SetLineColor(r.kBlack);
        histosums[variablename].SetFillColor(r.kBlack);
        histosums[variablename].SetFillStyle(3003);
        histosums[variablename].Draw("E2,same");  
        

    hPad.GetXaxis().SetTitleSize(0.05)
    hPad.GetYaxis().SetTitleSize(0.05)
    hPad.GetXaxis().SetTitleOffset(1.25)
    hPad.GetYaxis().SetTitleOffset(1.25)

    hPad.GetXaxis().SetTitle(variablesettings["title"])
    
    evdensity = (variablesettings["xmax"]-variablesettings["xmin"])/variablesettings["Nbin"]
    xaxistitle = variablesettings["title"]
    #unit = xaxistitle.split('(', 1)[1].split(')')[0]
    unit=""
    pos_start_unit = xaxistitle.rfind("(")+1
    pos_end_unit = xaxistitle.rfind(")")
    if (pos_start_unit!=-1) and (pos_end_unit!=-1):
        unit = xaxistitle[ pos_start_unit : pos_end_unit ]

    ytitle = ""
    if unit!="":
        ytitle = "Events / %.2f %s"%(evdensity,unit)
    else:
        ytitle = "Events / %.2f"%evdensity

    hPad.GetXaxis().SetTitle(variablesettings["title"])
    hPad.GetYaxis().SetTitle(ytitle)
    c.Update()

    #then draw all the rest
    for inputname, inputcontent in inputs.items():
        if inputcontent["stack"]==0:
            histos[inputname][variablename].Draw(inputcontent["drawstyle"]+" SAME")


    legend.Draw()
    et = extra_texts()
    for t in et: t.Draw()

    c.Print(options.outdir+"/c_"+variablename+".pdf")
    c.Print(options.outdir+"/c_"+variablename+".png")
    c.SaveAs(options.outdir+"/c_"+variablename+".root")

    if variablesettings["ymin"]<=0:
        print ("[WARNING]: ymin<=0 for variable %s --> cannot draw logarithmic plot"%variablename)
    else:
        c.SetLogy()
        c.Print(options.outdir+"/c_log_"+variablename+".pdf")
        c.Print(options.outdir+"/c_log_"+variablename+".png")
        c.SaveAs(options.outdir+"/c_log_"+variablename+".root")
    
