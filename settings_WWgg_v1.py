import ROOT as r

r.gROOT.ProcessLineSync(".x DeltaRmin.C+")

variables = {
    "mgg":{
        "formula":"CMS_hgg_mass",
        "title":"m_{gg} (GeV)",
        "xmin":100,
        "xmax":180.,
        #"ymin":0.001,
        #"ymax":1.e+04,
        "Nbin":16
    },
    "leadphotonID":{
        "formula":"Leading_Photon_MVA",
        "title":"lead photon ID score",
        "xmin":-1,
        "xmax":1,
        #"ymin":0.001,
        #"ymax":1.e+04,
        "Nbin":20
    },
    "subleadphotonID":{
        "formula":"Subleading_Photon_MVA",
        "title":"sublead photon ID score",
        "xmin":-1,
        "xmax":1,
        #"ymin":0.001,
        #"ymax":1.e+04,
        "Nbin":20
    },
    "minphotonID":{
        "formula":"min(Leading_Photon_MVA,Subleading_Photon_MVA)",
        "title":"min photon ID score",
        "xmin":-1,
        "xmax":1,
        "ymin":1.,
        "ymax":1.e+05,
        "Nbin":20
    },
    "maxphotonID":{
        "formula":"max(Leading_Photon_MVA,Subleading_Photon_MVA)",
        "title":"max photon ID score",
        "xmin":-1,
        "xmax":1,
        #"ymin":0.001,
        #"ymax":1.e+04,
        "Nbin":20
    }

}

inputfolder="/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/WWZ_SignalTopology_Checks/2017/All_Backgrounds/"

common_selections="((CMS_hgg_mass>80 && CMS_hgg_mass<100)*(Leading_Photon_pt/CMS_hgg_mass>0.33)*(Subleading_Photon_pt/CMS_hgg_mass>0.25)*(Leading_Photon_MVA>-0.7)*(Subleading_Photon_MVA>-0.7) )"

signal_selections="((CMS_hgg_mass>80 && CMS_hgg_mass<100)*(Leading_Photon_pt/CMS_hgg_mass>0.33)*(Subleading_Photon_pt/CMS_hgg_mass>0.25)*(passPhotonSels==1)*(Leading_Photon_MVA>-0.7)*(Subleading_Photon_MVA>-0.7) )"

#common_selections="((CMS_hgg_mass>100 && CMS_hgg_mass<115 || CMS_hgg_mass>135 && CMS_hgg_mass<180)*(Leading_Photon_MVA>-0.9)*(Subleading_Photon_MVA>-0.9) )"

IDsideband_selections="((Leading_Photon_pt/CMS_hgg_mass>0.35)*(Subleading_Photon_pt/CMS_hgg_mass>0.25)*(passPhotonSels==1)*(CMS_hgg_mass<115 || CMS_hgg_mass>135)*(min(Leading_Photon_MVA,Subleading_Photon_MVA)<-0.7)*(max(Leading_Photon_MVA,Subleading_Photon_MVA)>-0.7) )"

inputs = {

    "data":{
        "title":"data",
        "fillcolor":0,
        "fillstyle":0,
        "markerstyle":20,
        "drawstyle":"E1",
        "weight":common_selections+"*(weight)",
        "stack":0,
        "filelumis":[
            ["/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/WWZ_SignalTopology_Checks/2017/SingleElectron_Data_2017_hadded/SingleElectron_Data_2017_MoreVars.root", "Data_13TeV_HHWWggTag_1", 1.]
        ]
    },

    "DYjets":{
        "title":"DY+jets",
        "linecolor":r.kBlue,
        "fillcolor":r.kBlue,
        "fillstyle":1,
        "drawstyle":"hist",
        "weight":common_selections+"*(weight*1.05)",
        "stack":1,
        "filelumis":[
            ["/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/WWZ_SignalTopology_Checks/2017/Zee_hadded/Zee_v14-v1_hadded_MoreVars.root", 
             "DYJetsToLL_M_50_TuneCP5_13TeV_amcatnloFXFX_pythia8_13TeV_HHWWggTag_1", 41.5]
        ]
    },

    "ttbar":{
        "title":"ttbar",
        "linecolor":r.kYellow,
        "fillcolor":r.kYellow,
        "fillstyle":1,
        "drawstyle":"hist",
        "weight":common_selections+"*(weight)",
        "stack":1,
        "filelumis":[
            [inputfolder+"/TTJets_hadded_MoreVars.root", 
             "TTJets_TuneCP5_13TeV_amcatnloFXFX_pythia8_13TeV_HHWWggTag_1", 41.5]
        ]
    },

    "gjets":{
        "title":"#gamma+jets",
        "linecolor":r.kGreen+2,
        "fillcolor":r.kGreen+2,
        "fillstyle":1,
        "drawstyle":"hist",
        "weight":common_selections+"*(weight)",
        "stack":1,
        "filelumis":[
            [inputfolder+"/GJet_Pt-20to40_hadded_MoreVars.root", 
             "GJet_Pt_20to40_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8_13TeV_HHWWggTag_1", 41.5],
            [inputfolder+"/GJet_Pt-40toInf_hadded_MoreVars.root", 
             "GJet_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8_13TeV_HHWWggTag_1", 41.5]            
        ]
    },


    "ggjets":{
        "title":"#gamma#gamma+jets",
        "linecolor":r.kCyan-9,
        "fillcolor":r.kCyan-9,
        "fillstyle":1,
        "drawstyle":"hist",
        "weight":common_selections+"*(weight)",
        "stack":1,
        "filelumis":[
            [inputfolder+"/DiPhotonJetsBox_MGG-80toInf_hadded_MoreVars.root", 
             "DiPhotonJetsBox_MGG_80toInf_13TeV_Sherpa_13TeV_HHWWggTag_1", 41.5]
        ]
    },

    "qcd":{
        "title":"qcd",
        "linecolor":r.kRed,
        "fillcolor":r.kRed,
        "fillstyle":1,
        "drawstyle":"hist",
        "weight":common_selections+"*(weight)",
        "stack":1,
        "filelumis":[
            ["/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/WWZ_SignalTopology_Checks/2017/All_Backgrounds/QCD_Pt-30to40_hadded.root", 
             "QCD_Pt_30to40_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8_13TeV_HHWWggTag_1", 41.5],
            ["/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/WWZ_SignalTopology_Checks/2017/All_Backgrounds/QCD_Pt-40toInf_hadded.root", 
             "tagsDumper/trees/QCD_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8_13TeV_HHWWggTag_1", 41.5]
            
        ]
    },




    
}

#input2={}
#for inputname in inputs.keys():
#    if inputname=="gjets":
#        input2["gjets"] = inputs["gjets"]

#inputs=input2
