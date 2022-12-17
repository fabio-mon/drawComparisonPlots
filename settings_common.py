import ROOT as r

variables = {
    "mHH":{
        "formula":"mHH",
        "title":"m_{HH} (GeV)",
        "xmin":240,
        "xmax":1300.,
        #"ymin":0.001,
        #"ymax":1.e+04,
        "Nbin":100
    },
    "costhetaHH":{
        "formula":"fabs(costhetaHH)",
        "title":"cos(#theta*) (GeV)",
        "xmin":0.,
        "xmax":1.,
        #"ymin":0.001,
        #"ymax":1.e+04,
        "Nbin":100
    },
    "leadHPt":{
        "formula":"leadH.Pt()",
        "title":"Lead H p_{T} (GeV)",
        "xmin":0.,
        "xmax":500.,
        #"ymin":0.001,
        #"ymax":1.e+04,
        "Nbin":100
    },       
    "subleadHPt":{
        "formula":"subleadH.Pt()",
        "title":"Sublead H p_{T} (GeV)",
        "xmin":0.,
        "xmax":500.,
        #"ymin":0.001,
        #"ymax":1.e+04,
        "Nbin":100
    },        
    "leadHEta":{
        "formula":"leadH.Eta()",
        "title":"Lead H #eta (GeV)",
        "xmin":-3.,
        "xmax":3.,
        #"ymin":0.001,
        #"ymax":1.e+04,
        "Nbin":100
    },       
    "subleadHEta":{
        "formula":"subleadH.Eta()",
        "title":"Sublead H #eta (GeV)",
        "xmin":-3.,
        "xmax":3.,
        #"ymin":0.001,
        #"ymax":1.e+04,
        "Nbin":100
    },        
    "leadHPtOverMHH":{
        "formula":"leadH.Pt()/mHH",
        "title":"Lead H p_{T}/m_{HH} (GeV)",
        "xmin":0.,
        "xmax":0.7,
        #"ymin":0.001,
        #"ymax":1.e+04,
        "Nbin":100
    },       
    "subleadHPtOverMHH":{
        "formula":"subleadH.Pt()/mHH",
        "title":"Sublead H p_{T}/m_{HH} (GeV)",
        "xmin":0.,
        "xmax":0.7,
        #"ymin":0.001,
        #"ymax":1.e+04,
        "Nbin":100
    }        
}

inputs = {

    "rewLOfake_to_NLOcHHH0":{
        "title":"Rew. LO benchm.",
        "linecolor":r.kRed,
        "fillcolor":0,
        "fillstyle":0,
        "drawstyle":"hist",
        "weight":"(weight)",
        "stack":0,
        "filelumis":[
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_LOfake2017_to_NLOcHHH//genevents2017bbgg_reweighted_NLOcHHH0.root",
             "LOSMfake", 1./369000],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_LOfake2017_to_NLOcHHH//genevents2017bbgg_reweighted_NLOcHHH0.root",
             "LO3fake", 1./400000],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_LOfake2017_to_NLOcHHH//genevents2017bbgg_reweighted_NLOcHHH0.root",
             "LO4fake", 1./388000],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_LOfake2017_to_NLOcHHH//genevents2017bbgg_reweighted_NLOcHHH0.root",
             "LO5fake", 1./392000],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_LOfake2017_to_NLOcHHH//genevents2017bbgg_reweighted_NLOcHHH0.root",
             "LO6fake", 1./400000],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_LOfake2017_to_NLOcHHH//genevents2017bbgg_reweighted_NLOcHHH0.root",
             "LO7fake", 1./392000]
        ]
    },

    "rewcHHH_to_NLOcHHH0":{
        "title":"Rew. NLO samples",
        "linecolor":r.kGreen+2,
        "fillcolor":0,
        "fillstyle":0,
        "drawstyle":"hist",
        "weight":"(weight)",
        "stack":0,
        "filelumis":[
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_cHHH_to_cHHH_2017_v2/genevents2017bbggNLO_reweighted_NLOcHHH0.root",
             "LOcHHH1fake", 1.],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_cHHH_to_cHHH_2017_v2/genevents2017bbggNLO_reweighted_NLOcHHH0.root",
             "LOcHHH2p45fake", 1.],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_cHHH_to_cHHH_2017_v2/genevents2017bbggNLO_reweighted_NLOcHHH0.root",
             "LOcHHH5fake", 1.]
        ]
    },

    "NLOcHHH0":{
        "title":"NLO #kappa_{#lambda}=0",
        "linecolor":r.kBlue,
        "fillcolor":0,
        "fillstyle":0,
        "drawstyle":"hist",
        "weight":"(weight)",
        "stack":0,
        "filelumis":[
            ["/afs/cern.ch/user/f/fmonti/work/flashggNewNew/CMSSW_10_6_8/src/flashgg/Reweight_trees/validation_trees/genevents2017bbggNLO.root",
             "LOcHHH0fake", 1./11667.555]
        ]
    },

    "rewLOfake_to_NLOcHHH1":{
        "title":"Rew. LO benchm.",
        "linecolor":r.kRed,
        "fillcolor":0,
        "fillstyle":0,
        "drawstyle":"hist",
        "weight":"(weight)",
        "stack":0,
        "filelumis":[
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_LOfake2017_to_NLOcHHH//genevents2017bbgg_reweighted_NLOSM.root",
             "LOSMfake", 1./369000],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_LOfake2017_to_NLOcHHH//genevents2017bbgg_reweighted_NLOSM.root",
             "LO3fake", 1./400000],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_LOfake2017_to_NLOcHHH//genevents2017bbgg_reweighted_NLOSM.root",
             "LO4fake", 1./388000],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_LOfake2017_to_NLOcHHH//genevents2017bbgg_reweighted_NLOSM.root",
             "LO5fake", 1./392000],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_LOfake2017_to_NLOcHHH//genevents2017bbgg_reweighted_NLOSM.root",
             "LO6fake", 1./400000],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_LOfake2017_to_NLOcHHH//genevents2017bbgg_reweighted_NLOSM.root",
             "LO7fake", 1./392000]
        ]
    },

    "rewcHHH_to_NLOcHHH1":{
        "title":"Rew. NLO samples",
        "linecolor":r.kGreen+2,
        "fillcolor":0,
        "fillstyle":0,
        "drawstyle":"hist",
        "weight":"(weight)",
        "stack":0,
        "filelumis":[
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_cHHH_to_cHHH_2017_v2/genevents2017bbggNLO_reweighted_NLOSM.root",
             "LOcHHH0fake", 1.],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_cHHH_to_cHHH_2017_v2/genevents2017bbggNLO_reweighted_NLOSM.root",
             "LOcHHH2p45fake", 1.],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_cHHH_to_cHHH_2017_v2/genevents2017bbggNLO_reweighted_NLOSM.root",
             "LOcHHH5fake", 1.]
        ]
    },
 
    "NLOSM":{
        "title":"NLO SM",
        "linecolor":r.kBlue,
        "fillcolor":0,
        "fillstyle":0,
        "drawstyle":"hist",
        "weight":"(weight)",
        "stack":0,
        "filelumis":[
            ["/afs/cern.ch/user/f/fmonti/work/flashggNewNew/CMSSW_10_6_8/src/flashgg/Reweight_trees/validation_trees/genevents2017bbggNLO.root",
             "LOcHHH1fake", 1./5335.2524]
        ]
    },

    "rewLOfake_to_NLOcHHH2p45":{
        "title":"Rew. LO benchm.",
        "linecolor":r.kRed,
        "fillcolor":0,
        "fillstyle":0,
        "drawstyle":"hist",
        "weight":"(weight)",
        "stack":0,
        "filelumis":[
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_LOfake2017_to_NLOcHHH//genevents2017bbgg_reweighted_NLOcHHH2.root",
             "LOSMfake", 1./369000],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_LOfake2017_to_NLOcHHH//genevents2017bbgg_reweighted_NLOcHHH2.root",
             "LO3fake", 1./400000],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_LOfake2017_to_NLOcHHH//genevents2017bbgg_reweighted_NLOcHHH2.root",
             "LO4fake", 1./388000],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_LOfake2017_to_NLOcHHH//genevents2017bbgg_reweighted_NLOcHHH2.root",
             "LO5fake", 1./392000],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_LOfake2017_to_NLOcHHH//genevents2017bbgg_reweighted_NLOcHHH2.root",
             "LO6fake", 1./400000],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_LOfake2017_to_NLOcHHH//genevents2017bbgg_reweighted_NLOcHHH2.root",
             "LO7fake", 1./392000]
        ]
    },

    "rewcHHH_to_NLOcHHH2p45":{
        "title":"Rew. NLO samples",
        "linecolor":r.kGreen+2,
        "fillcolor":0,
        "fillstyle":0,
        "drawstyle":"hist",
        "weight":"(weight)",
        "stack":0,
        "filelumis":[
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_cHHH_to_cHHH_2017_v2/genevents2017bbggNLO_reweighted_NLOcHHH2.root",
             "LOcHHH0fake", 1.],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_cHHH_to_cHHH_2017_v2/genevents2017bbggNLO_reweighted_NLOcHHH2.root",
             "LOcHHH1fake", 1.],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_cHHH_to_cHHH_2017_v2/genevents2017bbggNLO_reweighted_NLOcHHH2.root",
             "LOcHHH5fake", 1.]
        ]
    },

    "NLOcHHH2p45":{
        "title":"NLO #kappa_{#lambda}=2.45",
        "linecolor":r.kBlue,
        "fillcolor":0,
        "fillstyle":0,
        "drawstyle":"hist",
        "weight":"(weight)",
        "stack":0,
        "filelumis":[
            ["/afs/cern.ch/user/f/fmonti/work/flashggNewNew/CMSSW_10_6_8/src/flashgg/Reweight_trees/validation_trees/genevents2017bbggNLO.root",
             "LOcHHH2p45fake", 1./2259.0679]
        ]
    },

    "rewLOfake_to_NLOcHHH5":{
        "title":"Rew. LO benchm.",
        "linecolor":r.kRed,
        "fillcolor":0,
        "fillstyle":0,
        "drawstyle":"hist",
        "weight":"(weight)",
        "stack":0,
        "filelumis":[
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_LOfake2017_to_NLOcHHH//genevents2017bbgg_reweighted_NLOcHHH5.root",
             "LOSMfake", 1./369000],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_LOfake2017_to_NLOcHHH//genevents2017bbgg_reweighted_NLOcHHH5.root",
             "LO3fake", 1./400000],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_LOfake2017_to_NLOcHHH//genevents2017bbgg_reweighted_NLOcHHH5.root",
             "LO4fake", 1./388000],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_LOfake2017_to_NLOcHHH//genevents2017bbgg_reweighted_NLOcHHH5.root",
             "LO5fake", 1./392000],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_LOfake2017_to_NLOcHHH//genevents2017bbgg_reweighted_NLOcHHH5.root",
             "LO6fake", 1./400000],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_LOfake2017_to_NLOcHHH//genevents2017bbgg_reweighted_NLOcHHH5.root",
             "LO7fake", 1./392000]
        ]
    },
    "rewcHHH_to_NLOcHHH5":{
        "title":"Rew. NLO samples",
        "linecolor":r.kGreen+2,
        "fillcolor":0,
        "fillstyle":0,
        "drawstyle":"hist",
        "weight":"(weight)",
        "stack":0,
        "filelumis":[
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_cHHH_to_cHHH_2017_v2/genevents2017bbggNLO_reweighted_NLOcHHH5.root",
             "LOcHHH0fake", 1.],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_cHHH_to_cHHH_2017_v2/genevents2017bbggNLO_reweighted_NLOcHHH5.root",
             "LOcHHH1fake", 1.],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/29JAN2021/from_cHHH_to_cHHH_2017_v2/genevents2017bbggNLO_reweighted_NLOcHHH5.root",
             "LOcHHH2p45fake", 1.]
        ]
    },

    "NLOcHHH5":{
        "title":"NLO #kappa_{#lambda}=5",
        "linecolor":r.kBlue,
        "fillcolor":0,
        "fillstyle":0,
        "drawstyle":"hist",
        "weight":"(weight)",
        "stack":0,
        "filelumis":[
            ["/afs/cern.ch/user/f/fmonti/work/flashggNewNew/CMSSW_10_6_8/src/flashgg/Reweight_trees/validation_trees/genevents2017bbggNLO.root",
             "LOcHHH5fake", 1./15692.822]
        ]
    }

}
