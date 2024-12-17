import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C17I13M9_cff import Phase2C17I13M9
process = cms.Process('DIGI',Phase2C17I13M9)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D88Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2026D88_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedHLLHC14TeV_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
#Single Pions PU0 /store/mc/Phase2Fall22DRMiniAOD/SinglePion_Pt-0To200-gun/GEN-SIM-DIGI-RAW-MINIAOD/noPU_125X_mcRun4_realistic_v2-v1/2550000/16a17ebb-f3cc-41e9-a7f8-99c2fdcd9e90.root
#Single Pion PU200 /store/mc/Phase2Fall22DRMiniAOD/SinglePion_Pt-0To200-gun/GEN-SIM-DIGI-RAW-MINIAOD/PU200_125X_mcRun4_realistic_v2-v1/30000/004d15e3-a12f-4ba9-a2f3-4b7277ffa418.root
#Single Photon PU0 /store/mc/Phase2Fall22DRMiniAOD/SinglePhoton_Pt-2To200-gun/GEN-SIM-DIGI-RAW-MINIAOD/noPU_125X_mcRun4_realistic_v2-v1/2560000/0116edbb-b12b-45a9-b8b4-0e603466dc3b.root
#Single Photon PU200 /store/mc/Phase2Fall22DRMiniAOD/SinglePhoton_Pt-2To200-gun/GEN-SIM-DIGI-RAW-MINIAOD/PU200_125X_mcRun4_realistic_v2-v1/30000/0052a171-0ff4-4d9a-86e7-4d7a8498a31d.root not accessible: T0_CH_CERN_Tape
#Double Photon PU200 /store/mc/Phase2Fall22DRMiniAOD/DoublePhoton_FlatPt-1To100-gun/GEN-SIM-DIGI-RAW-MINIAOD/PU200_125X_mcRun4_realistic_v2-v1/30000/0075a153-cb64-4ed9-9157-a1b6db9fd431.root

#/store/mc/Phase2Fall22DRMiniAOD/DoublePhoton_FlatPt-1To100-gun/GEN-SIM-DIGI-RAW-MINIAOD/PU200_125X_mcRun4_realistic_v2-v1/30000/0075a153-cb64-4ed9-9157-a1b6db9fd431.root
#/store/mc/Phase2Fall22DRMiniAOD/SinglePhoton_Pt-2To200-gun/GEN-SIM-DIGI-RAW-MINIAOD/noPU_125X_mcRun4_realistic_v2-v1/2560000/0116edbb-b12b-45a9-b8b4-0e603466dc3b.root
#store/mc/Phase2Fall22DRMiniAOD/SinglePion_Pt-0To200-gun/GEN-SIM-DIGI-RAW-MINIAOD/noPU_125X_mcRun4_realistic_v2-v1/2550000/16a17ebb-f3cc-41e9-a7f8-99c2fdcd9e90.root
#/store/mc/Phase2Fall22DRMiniAOD/SinglePion_Pt-0To200-gun/GEN-SIM-DIGI-RAW-MINIAOD/noPU_125X_mcRun4_realistic_v2-v1/30000/004d15e3-a12f-4ba9-a2f3-4b7277ffa418.root



#/VBFHToTauTau_M-125_TuneCP5_14TeV-powheg-pythia8/Phase2Spring23DIGIRECOMiniAOD-noPU_131X_mcRun4_realistic_v5-v1/GEN-SIM-DIGI-RAW-MINIAOD
#/store/mc/Phase2Spring23DIGIRECOMiniAOD/VBFHToTauTau_M-125_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/noPU_131X_mcRun4_realistic_v5-v1/2530000/006f6626-cf25-4030-9835-cd507d7fcbec.root

#'/store/mc/Phase2Spring23DIGIRECOMiniAOD/VBFHToInvisible_M-125_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/noPU_131X_mcRun4_realistic_v5-v1/60000/02bca101-c7a5-4a1a-b5c2-dba050bcd060.root'

#/store/mc/Phase2Spring23DIGIRECOMiniAOD/VBFHToInvisible_M-125_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/noPU_131X_mcRun4_realistic_v5-v1/60000/02bca101-c7a5-4a1a-b5c2-dba050bcd060.root Hinvisible
#/store/mc/Phase2Spring23DIGIRECOMiniAOD/VBFHToTauTau_M-125_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/noPU_131X_mcRun4_realistic_v5-v1/2530000/006f6626-cf25-4030-9835-cd507d7fcbec.root Htautau
#VBF /store/mc/Phase2Spring23DIGIRECOMiniAOD/VBFHToInvisible_M-125_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/noPU_131X_mcRun4_realistic_v5-v1/60000/02bca101-c7a5-4a1a-b5c2-dba050bcd060.root
process.source = cms.Source("PoolSource",
       fileNames = cms.untracked.vstring('/store/mc/Phase2Spring23DIGIRECOMiniAOD/VBFHToInvisible_M-125_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW-MINIAOD/noPU_131X_mcRun4_realistic_v5-v1/60000/02bca101-c7a5-4a1a-b5c2-dba050bcd060.root'),
       inputCommands=cms.untracked.vstring(
           'keep *',
           )
        )
process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.20 $'),
    annotation = cms.untracked.string('SingleElectronPt10_cfi nevts:10'),
    name = cms.untracked.string('Applications')
)

# Output definition
#V16_DoublePhoton_FlatPt-1To100-gun_PU200_125X_mcRun4_realistic_v2-v1.root

process.TFileService = cms.Service(
    "TFileService",
    fileName = cms.string("VBFHToInv_with_STCs_first_try.root")
    )

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T21', '')

# load HGCAL TPG simulation
process.load('L1Trigger.L1THGCal.hgcalTriggerPrimitives_cff')

# Tacke STCs configuration for CEH
from L1Trigger.L1THGCal.l1tHGCalConcentratorProducer_cfi import custom_conc_proc
parameters = custom_conc_proc.clone(stcSize = custom_conc_proc.stcSize,
                                    type_energy_division = custom_conc_proc.type_energy_division,
                                    fixedDataSizePerHGCROC = custom_conc_proc.fixedDataSizePerHGCROC,
                                    Method = cms.vstring('thresholdSelect','superTriggerCellSelect','superTriggerCellSelect'),
)
process.l1tHGCalConcentratorProducer.ProcessorParameters = parameters

process.hgcl1tpg_step = cms.Path(process.L1THGCalTriggerPrimitives)


# load ntuplizer
process.load('L1Trigger.L1THGCalUtilities.hgcalTriggerNtuples_cff')
process.ntuple_step = cms.Path(process.L1THGCalTriggerNtuples)

# Schedule definition
process.schedule = cms.Schedule(process.hgcl1tpg_step, process.ntuple_step)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
