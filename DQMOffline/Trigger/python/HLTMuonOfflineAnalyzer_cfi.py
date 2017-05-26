import FWCore.ParameterSet.Config as cms

hltMuonOfflineAnalyzer = cms.EDAnalyzer("HLTMuonOfflineAnalyzer",

    ## Used when fetching triggerSummary and triggerResults
    hltProcessName = cms.string("HLT"),

    ## Location of plots in DQM
    destination = cms.untracked.string("HLT/Muon/Distributions/globalMuons"),

    ## HLT paths passing any one of these regular expressions will be included
    hltPathsToCheck = cms.vstring(
      "HLT_Mu17_TrkIsoVVL_v",
      "HLT_Mu45_eta2p1_v1",
      "HLT_Mu50_v",
      "HLT_IsoMu24_v",
      "HLT_IsoTkMu24_v",
#      "HLT_Mu17_Mu8_DZ_v",
#      "HLT_Mu17_TkMu8_DZ_v",
      "HLT_IsoMu20_eta2p1_v",
      "HLT_IsoTkMu20_eta2p1_v",
      "HLT_IsoMu24_eta2p1_v",
      "HLT_IsoTkMu24_eta2p1_v",
      "HLT_IsoMu27_v",
      "HLT_IsoTkMu27_v",
      "HLT_IsoMu20_v",
      "HLT_IsoTkMu20_v",
      "HLT_IsoMu22_v",
      "HLT_IsoTkMu22_v",
      "HLT_IsoMu22_eta2p1_v",
      "HLT_IsoTkMu22_eta2p1_v",
      "HLT_IsoMu18_v",
      "HLT_IsoTkMu18_v",
      "HLT_PAL1DoubleMuOpen_v", #for HI
      "HLT_PAL1DoubleMuOpen_OS_v", #for HI
      "HLT_PAL1DoubleMuOpen_SS_v", #for HI
      "HLT_PAL1DoubleMu0_v", #for HI
      "HLT_PAL1DoubleMu0_HighQ_v", #for HI
      "HLT_PAL1DoubleMu0_MGT1_v", #for HI
      "HLT_PAL1DoubleMu10_v", #for HI
      "HLT_PAL2DoubleMu0_v", #for HI
      "HLT_PAL2DoubleMu10_v", #for HI
      "HLT_PAL3DoubleMu0_v", #for HI
      "HLT_PAL3DoubleMu0_HIon_v", #for HI
      "HLT_PAL3DoubleMu10_v", #for HI
      "HLT_PAL2Mu12_v", #for HI
      "HLT_PAL2Mu15_v", #for HI
      "HLT_PAL3Mu3_v", #for HI 
      "HLT_PAL3Mu5_v", #for HI 
      "HLT_PAL3Mu7_v", #for HI 
      "HLT_PAL3Mu12_v", #for HI
      "HLT_PAL3Mu15_v", #for HI
      "HLT_PASingleMuOpen_PixelTrackGt0_FullTrackLt10_v", #for HI Forward
      "HLT_PASingleMuOpen_PixelTrackGt0_FullTrackLt15_v", #for HI Forward
      "HLT_PASingleMuOpen_PixelTrackGt0Lt10_v", #for HI Forward
      "HLT_PASingleMuOpen_PixelTrackGt0Lt15_v", #for HI Forward
      "HLT_PASingleMuOpen_HFOneTowerVeto_SingleTrack_v", #for HI Forward
      "HLT_PASingleMuOpen_HFOneTowerVeto_v", #for HI Forward
      "HLT_PASingleMuOpen_HFTwoTowerVeto_SingleTrack_v", #for HI Forward
      "HLT_PASingleMuOpen_HFTwoTowerVeto_v", #for HI Forward
      "HLT_PADoubleMuOpen_HFOneTowerVeto_SingleTrack_v", #for HI Forward
      "HLT_PADoubleMuOpen_HFOneTowerVeto_v", #for HI Forward
      "HLT_PADoubleMuOpen_HFTwoTowerVeto_SingleTrack_v", #for HI Forward
      "HLT_PADoubleMuOpen_HFTwoTowerVeto_v" #for HI Forward
    ),

#HLT_Mu15_eta2p1_TriCentral_40_20_20_BTagIP3D1stTrack_v3 matches HLT_Mu15_eta2p1_v

    ## All input tags are specified in this pset for convenience
    inputTags = cms.PSet(
        recoMuon       = cms.InputTag("muons"),
        beamSpot       = cms.InputTag("offlineBeamSpot"),
        offlinePVs     = cms.InputTag("offlinePrimaryVertices"),
        triggerSummary = cms.InputTag("hltTriggerSummaryAOD"),
        triggerResults = cms.InputTag("TriggerResults")
    ),

    ## Both 1D and 2D plots use the binnings defined here
    binParams = cms.untracked.PSet(
        ## parameters for fixed-width plots
        NVertex    = cms.untracked.vdouble( 20,  1,   60),
        NVertexFine= cms.untracked.vdouble( 40,  1,   60),
        eta        = cms.untracked.vdouble( 20,  -2.40,   2.40),
        phi        = cms.untracked.vdouble( 20,  -3.14,   3.14),
        phiHEP17   = cms.untracked.vdouble( -3.14, -2.512, -1.884, -1.256, -0.827, -0.52,
                                             0.  ,  0.52 ,  0.827,  1.256,  1.884,  2.512, 3.14),
        z0         = cms.untracked.vdouble( 10, -0.15,  0.15),
        z0Fine     = cms.untracked.vdouble( 20, -0.15,  0.15),
        d0         = cms.untracked.vdouble( 10,  -0.50,   0.50),
        zMass      = cms.untracked.vdouble( 50,  65.00, 115.00),
        jpsiMass   = cms.untracked.vdouble( 60,   0.00,   6.00),
        charge     = cms.untracked.vdouble(  2,  -2.00,   2.00),
        deltaR     = cms.untracked.vdouble( 20,   0.00,   0.05),
        deltaR2    = cms.untracked.vdouble( 20,    0.0,   4.5 ),
        phiCoarse  = cms.untracked.vdouble( 10,  -3.14,   3.14),
        resolutionRel = cms.untracked.vdouble( 40,  -0.30,   0.30),
        resolutionEta = cms.untracked.vdouble( 20,  -0.01,   0.01),
        resolutionPhi = cms.untracked.vdouble( 20,  -0.01,   0.01),
        ## parameters for variable-width plots
        etaCoarse = cms.untracked.vdouble(-2.4, -2.1, -1.6, -1.2, -0.8, 0.0,
                                           0.8,  1.2,  1.6,  2.1,  2.4),
        ptCoarse = cms.untracked.vdouble(10.0, 20.0, 40.0, 60.0, 80.0, 100.0, 200.0),
        ptFine   = cms.untracked.vdouble(10.0,15.0, 20.0,30.0, 40.0,50.0, 60.0,70.0, 80.0,90.0, 100.0,150., 200.0),
        pt = cms.untracked.vdouble(  0.0,   2.0,   4.0, 
                                     6.0,   8.0,  10.0, 
                                    20.0,  30.0,  40.0, 
                                   100.0, 200.0, 400.0),
    ),

    ## These parameters define which objects are used to fill plots
    plotCuts = cms.PSet(
        ## not applied on eta plots
        maxEta = cms.untracked.double(2.10),
        ## only fill plots for muons with pt > ceil(hltThreshold * minPtFactor)
        ## ex: for HLT_Mu17, ceil(17 * 1.2 ) = 21, so we require pT > 21
        minPtFactor = cms.untracked.double(1.20),
        ## deltaR cuts
        L1DeltaR = cms.untracked.double(0.30),
        L2DeltaR = cms.untracked.double(0.30),
        L3DeltaR = cms.untracked.double(0.05),
    ),

    ## Only events passing all these triggers will be considered
    requiredTriggers   = cms.untracked.vstring(),

    ## This collection is used to fill most distributions
    targetParams = cms.PSet(
        ## The d0 and z0 cuts are required for the inner track of the
        ## reco muons, taken with respect to the beamspot
        d0Cut = cms.untracked.double(2.0),
        z0Cut = cms.untracked.double(25.0),
        ## cuts
        recoCuts = cms.untracked.string("isGlobalMuon && abs(eta) < 2.4"),
        hltCuts  = cms.untracked.string("abs(eta) < 2.4"),
    ),

    ## If this PSet is empty, then no "tag and probe" plots are produced;
    ## the cuts used for the tags are specified by targetParams
    probeParams = cms.PSet(
        ## The d0 and z0 cuts are required for the inner track of the
        ## reco muons, taken with respect to the beamspot
        d0Cut = cms.untracked.double(2.0),
        z0Cut = cms.untracked.double(25.0),
        ## cuts
        recoCuts = cms.untracked.string("isGlobalMuon && abs(eta) < 2.0"),
        hltCuts  = cms.untracked.string("abs(eta) < 2.0"),
    ),

)
