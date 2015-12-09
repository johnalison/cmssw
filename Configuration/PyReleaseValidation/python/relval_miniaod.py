# import the definition of the steps and input files:
from  Configuration.PyReleaseValidation.relval_steps import *

# here only define the workflows as a combination of the steps defined above:
workflows = Matrix()

# each workflow defines a name and a list of steps to be done. 
# if no explicit name/label given for the workflow (first arg),
# the name of step1 will be used


## re-miniAOD of the production tests
workflows[1601301] = ['', ['ProdMinBias_13_MINIAOD','REMINIAODPROD','HARVESTREMINIAODPROD']]
workflows[1601302] = ['', ['ProdTTbar_13_MINIAOD','REMINIAODPROD','HARVESTREMINIAODPROD']]
workflows[1601303] = ['', ['ProdQCD_Pt_3000_3500_13_MINIAOD','REMINIAODPROD','HARVESTREMINIAODPROD']]

## re-miniAOD workflows -- fullSim noPU
workflows[1601315] = ['', ['SingleElectronPt10_UP15_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601316] = ['', ['SingleElectronPt1000_UP15_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601317] = ['', ['SingleElectronPt35_UP15_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601318] = ['', ['SingleGammaPt10_UP15_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601319] = ['', ['SingleGammaPt35_UP15_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601306] = ['', ['SingleMuPt1_UP15_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601320] = ['', ['SingleMuPt10_UP15_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601321] = ['', ['SingleMuPt100_UP15_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601322] = ['', ['SingleMuPt1000_UP15_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601323] = ['', ['NuGun_UP15_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]

workflows[1601324] = ['', ['TTbarLepton_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601335] = ['', ['Wjet_Pt_80_120_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601336] = ['', ['Wjet_Pt_3000_3500_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601337] = ['', ['SMS-T1tttt_mGl-1500_mLSP-100_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601338] = ['', ['QCD_FlatPt_15_3000HS_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]

workflows[1601309] = ['', ['Higgs200ChargedTaus_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601313] = ['', ['QCD_Pt_3000_3500_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]

workflows[1601339] = ['', ['QCD_Pt_600_800_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]

workflows[1601347] = ['', ['Upsilon1SToMuMu_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601349] = ['', ['BsToMuMu_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601350] = ['', ['JpsiMuMu_Pt-15_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]

workflows[1601325] = ['', ['TTbar_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601326] = ['', ['WE_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601329] = ['', ['ZEE_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601331] = ['', ['ZTT_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601332] = ['', ['H125GGgluonfusion_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601333] = ['', ['PhotonJets_Pt_10_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601334] = ['', ['QQH1352T_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]

workflows[1601328] = ['', ['QCD_Pt_80_120_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601327] = ['', ['WM_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601330] = ['', ['ZMM_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]

workflows[1601310] = ['', ['ADDMonoJet_d3MD3_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601312] = ['', ['ZpMM_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601314] = ['', ['WpM_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]

workflows[1601340] = ['', ['PhiToMuMu_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601341] = ['', ['RSKKGluon_m3000GeV_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]

workflows[1601343] = ['', ['ZpMM_2250_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601344] = ['', ['ZpEE_2250_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601345] = ['', ['ZpTT_1500_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601348] = ['', ['EtaBToJpsiJpsi_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]

workflows[1601351] = ['', ['BuMixing_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601352] = ['', ['HSCPstop_M_200_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601353] = ['', ['RSGravitonToGaGa_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]

workflows[1601354] = ['', ['WpToENu_M-2000_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]
workflows[1601355] = ['', ['DisplacedSUSY_stopToBottom_M_300_1000mm_13_REMINIAOD','REMINIAOD','HARVESTREMINIAOD']]

## re-miniAOD workflows -- fullSim PU 50ns
workflows[16050200]=['',['ZEE_13_PU50_REMINIAOD','REMINIAOD_PU50','HARVESTREMINIAOD_PU50']]
workflows[16050202]=['',['TTbar_13_PU50_REMINIAOD','REMINIAOD_PU50','HARVESTREMINIAOD_PU50']]
workflows[16050203]=['',['H125GGgluonfusion_13_PU50_REMINIAOD','REMINIAOD_PU50','HARVESTREMINIAOD_PU50']]
workflows[16050204]=['',['QQH1352T_13_PU50_REMINIAOD','REMINIAOD_PU50','HARVESTREMINIAOD_PU50']]
workflows[16050205]=['',['ZTT_13_PU50_REMINIAOD','REMINIAOD_PU50','HARVESTREMINIAOD_PU50']]
workflows[16050206]=['',['ZMM_13_PU50_REMINIAOD','REMINIAOD_PU50','HARVESTREMINIAOD_PU50']]
workflows[16050207]=['',['NuGun_UP15_PU50_REMINIAOD','REMINIAOD_PU50','HARVESTREMINIAOD_PU50']]
workflows[16050208]=['',['SMS-T1tttt_mGl-1500_mLSP-100_13_PU50_REMINIAOD','REMINIAOD_PU50','HARVESTREMINIAOD_PU50']]

## re-miniAOD workflows -- fullSim PU 25ns
workflows[16025200]=['',['ZEE_13_PU25_REMINIAOD','REMINIAOD_PU25','HARVESTREMINIAOD_PU25']]
workflows[16025202]=['',['TTbar_13_PU25_REMINIAOD','REMINIAOD_PU25','HARVESTREMINIAOD_PU25']]
workflows[16025203]=['',['H125GGgluonfusion_13_PU25_REMINIAOD','REMINIAOD_PU25','HARVESTREMINIAOD_PU25']]
workflows[16025204]=['',['QQH1352T_13_PU25_REMINIAOD','REMINIAOD_PU25','HARVESTREMINIAOD_PU25']]
workflows[16025205]=['',['ZTT_13_PU25_REMINIAOD','REMINIAOD_PU25','HARVESTREMINIAOD_PU25']]
workflows[16025206]=['',['ZMM_13_PU25_REMINIAOD','REMINIAOD_PU25','HARVESTREMINIAOD_PU25']]
workflows[16025207]=['',['NuGun_UP15_PU25_REMINIAOD','REMINIAOD_PU25','HARVESTREMINIAOD_PU25']]
workflows[16025208]=['',['SMS-T1tttt_mGl-1500_mLSP-100_13_PU25_REMINIAOD','REMINIAOD_PU25','HARVESTREMINIAOD_PU25']]

## re-miniAOD workflows -- data 2015b
workflows[160134.701] = ['',[ 'RunHLTPhy2015B_MINIAOD','REMINIAODDR2_50ns','HARVESTREMINIAODDR2_50ns']]
workflows[160134.702] = ['',[ 'RunDoubleEG2015B_MINIAOD','REMINIAODDR2_50ns','HARVESTREMINIAODDR2_50ns']]
workflows[160134.703] = ['',[ 'RunDoubleMuon2015B_MINIAOD','REMINIAODDR2_50ns','HARVESTREMINIAODDR2_50ns']]
workflows[160134.704] = ['',[ 'RunJetHT2015B_MINIAOD','REMINIAODDR2_50ns','HARVESTREMINIAODDR2_50ns']]
workflows[160134.705] = ['',[ 'RunMET2015B_MINIAOD','REMINIAODDR2_50ns','HARVESTREMINIAODDR2_50ns']]
workflows[160134.706] = ['',[ 'RunMuonEG2015B_MINIAOD','REMINIAODDR2_50ns','HARVESTREMINIAODDR2_50ns']]
workflows[160134.707] = ['',[ 'RunSingleEl2015B_MINIAOD','REMINIAODDR2_50ns','HARVESTREMINIAODDR2_50ns']]
workflows[160134.708] = ['',[ 'RunSingleMu2015B_MINIAOD','REMINIAODDR2_50ns','HARVESTREMINIAODDR2_50ns']]
workflows[160134.709] = ['',[ 'RunSinglePh2015B_MINIAOD','REMINIAODDR2_50ns','HARVESTREMINIAODDR2_50ns']]
workflows[160134.710] = ['',[ 'RunZeroBias2015B_MINIAOD','REMINIAODDR2_50ns','HARVESTREMINIAODDR2_50ns']]

## re-miniAOD workflows -- data 2015c
workflows[160134.801] = ['',[ 'RunHLTPhy2015C_MINIAOD','REMINIAODDR2_25ns','HARVESTREMINIAODDR2_25ns']]
workflows[160134.802] = ['',[ 'RunDoubleEG2015C_MINIAOD','REMINIAODDR2_25ns','HARVESTREMINIAODDR2_25ns']]
workflows[160134.803] = ['',[ 'RunDoubleMuon2015C_MINIAOD','REMINIAODDR2_25ns','HARVESTREMINIAODDR2_25ns']]
workflows[160134.804] = ['',[ 'RunJetHT2015C_MINIAOD','REMINIAODDR2_25ns','HARVESTREMINIAODDR2_25ns']]
workflows[160134.805] = ['',[ 'RunMET2015C_MINIAOD','REMINIAODDR2_25ns','HARVESTREMINIAODDR2_25ns']]
workflows[160134.806] = ['',[ 'RunMuonEG2015C_MINIAOD','REMINIAODDR2_25ns','HARVESTREMINIAODDR2_25ns']]
workflows[160134.807] = ['',[ 'RunDoubleEGPrpt2015C_MINIAOD','REMINIAODDR2_25ns','HARVESTREMINIAODDR2_25ns']]
workflows[160134.808] = ['',[ 'RunSingleMuPrpt2015C_MINIAOD','REMINIAODDR2_25ns','HARVESTREMINIAODDR2_25ns']]
workflows[160134.809] = ['',[ 'RunSingleEl2015C_MINIAOD','REMINIAODDR2_25ns','HARVESTREMINIAODDR2_25ns']]
workflows[160134.810] = ['',[ 'RunSingleMu2015C_MINIAOD','REMINIAODDR2_25ns','HARVESTREMINIAODDR2_25ns']]
workflows[160134.811] = ['',[ 'RunSinglePh2015C_MINIAOD','REMINIAODDR2_25ns','HARVESTREMINIAODDR2_25ns']]
workflows[160134.812] = ['',[ 'RunZeroBias2015C_MINIAOD','REMINIAODDR2_25ns','HARVESTREMINIAODDR2_25ns']]

## re-miniAOD workflows -- data 2015d
workflows[160134.901] = ['',[ 'RunHLTPhy2015D_MINIAOD','REMINIAODDR2_25ns','HARVESTREMINIAODDR2_25ns']]
workflows[160134.902] = ['',[ 'RunDoubleEG2015D_MINIAOD','REMINIAODDR2_25ns','HARVESTREMINIAODDR2_25ns']]
workflows[160134.903] = ['',[ 'RunDoubleMuon2015D_MINIAOD','REMINIAODDR2_25ns','HARVESTREMINIAODDR2_25ns']]
workflows[160134.904] = ['',[ 'RunJetHT2015D_MINIAOD','REMINIAODDR2_25ns','HARVESTREMINIAODDR2_25ns']]
workflows[160134.905] = ['',[ 'RunMET2015D_MINIAOD','REMINIAODDR2_25ns','HARVESTREMINIAODDR2_25ns']]
workflows[160134.906] = ['',[ 'RunMuonEG2015D_MINIAOD','REMINIAODDR2_25ns','HARVESTREMINIAODDR2_25ns']]
workflows[160134.907] = ['',[ 'RunDoubleEGPrpt2015D', 'HLTDR2_25ns','RECODR2_25nsreHLT','HARVESTDR2_25nsreHLT']]
workflows[160134.908] = ['',[ 'RunSingleMuPrpt2015D', 'HLTDR2_25ns','RECODR2_25nsreHLT','HARVESTDR2_25nsreHLT']]
workflows[160134.909] = ['',[ 'RunSingleEl2015D_MINIAOD','REMINIAODDR2_25ns','HARVESTREMINIAODDR2_25ns']]
workflows[160134.910] = ['',[ 'RunSingleMu2015D_MINIAOD','REMINIAODDR2_25ns','HARVESTREMINIAODDR2_25ns']]
workflows[160134.911] = ['',[ 'RunSinglePh2015D_MINIAOD','REMINIAODDR2_25ns','HARVESTREMINIAODDR2_25ns']]
workflows[160134.912] = ['',[ 'RunZeroBias2015D_MINIAOD','REMINIAODDR2_25ns','HARVESTREMINIAODDR2_25ns']]

