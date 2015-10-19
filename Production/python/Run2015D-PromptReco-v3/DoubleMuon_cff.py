import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/629/00000/E2B8C5F0-F45E-E511-ADC8-02163E01410C.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/630/00000/7413EB59-1A5F-E511-BC4E-02163E014792.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/672/00000/1C758C5C-F45E-E511-9510-02163E012800.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/673/00000/D6A3FFFF-F95E-E511-A430-02163E0139D3.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/674/00000/DE7BE8F5-035F-E511-9FA0-02163E01478E.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/675/00000/4AA27F21-8B5F-E511-9AED-02163E014472.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/675/00000/D44C0C15-8B5F-E511-BCD8-02163E014178.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/676/00000/02657C39-BA5F-E511-9533-02163E0145EC.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/676/00000/30EF462F-BA5F-E511-B0CC-02163E013692.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/676/00000/36166449-BA5F-E511-A4E5-02163E014520.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/676/00000/56B2FA2D-BA5F-E511-8341-02163E0137AE.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/676/00000/78D63A2A-BA5F-E511-8943-02163E0143F2.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/676/00000/822CBE2D-BA5F-E511-98E2-02163E013708.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/676/00000/DE35842F-BA5F-E511-96E2-02163E0135EE.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/677/00000/1889D9AA-345F-E511-8078-02163E01374B.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/677/00000/746A90AC-345F-E511-9FB9-02163E0123C5.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/677/00000/EC03B297-345F-E511-BDC4-02163E01184F.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/725/00000/7A55B3B1-205F-E511-9117-02163E011FBF.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/727/00000/543E874E-385F-E511-83F2-02163E01350A.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/728/00000/0091808E-3C5F-E511-AB2D-02163E014708.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/1A59B4EF-1960-E511-8A9B-02163E011FEF.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/30E7F1F4-1960-E511-B10B-02163E01475F.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/32F792EC-1960-E511-A2E6-02163E011F0C.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/3C9A2DF5-1960-E511-A6FC-02163E01474C.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/4E68D3F6-1960-E511-BAE6-02163E01385B.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/5CA7EAF1-1960-E511-9B85-02163E014552.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/6ABE7B95-1A60-E511-A9AD-02163E01466A.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/6AEB0DF0-1960-E511-A241-02163E0123FC.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/8651AA0D-1A60-E511-BA5A-02163E0141C4.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/92BE40F4-1960-E511-8EFD-02163E014364.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/981FA415-1A60-E511-95A3-02163E0143FA.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/BC25D4F7-1960-E511-8CA6-02163E0135D9.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/C66B1CF6-1960-E511-B961-02163E011928.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/729/00000/E4B119EF-1960-E511-8A50-02163E01188A.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/734/00000/2E6633ED-DB5F-E511-8C11-02163E0140E6.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/734/00000/BEBE436C-DC5F-E511-88B3-02163E014213.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/801/00000/D6B6CBC6-7F60-E511-AC7D-02163E0134EC.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/801/00000/EC27C1C2-7F60-E511-9D52-02163E0134CE.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/834/00000/70FEF702-FF5F-E511-AABA-02163E0122FF.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/842/00000/B6BC66BA-4260-E511-935C-02163E0142FC.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/843/00000/0C413E97-E560-E511-ADB4-02163E013423.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/843/00000/38109793-E560-E511-BAA7-02163E01474A.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/843/00000/422DC5C5-E560-E511-BDA7-02163E0142CE.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/843/00000/506ADEB1-E560-E511-9692-02163E01446D.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/843/00000/7A5A9E91-E560-E511-9E2C-02163E0119C1.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/843/00000/8CCFC394-E560-E511-AB92-02163E01445A.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/843/00000/A6B6FD95-E560-E511-BF68-02163E012893.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/843/00000/C66510A0-E560-E511-A6A8-02163E013632.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/843/00000/D4AF4C93-E560-E511-8399-02163E011928.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/843/00000/F66FC8AD-E560-E511-B9BB-02163E01348E.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/843/00000/F839909C-E560-E511-94F1-02163E0143D4.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/865/00000/229A93AE-F060-E511-A6E6-02163E014720.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/866/00000/2E8858D0-F660-E511-BDE1-02163E01474A.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/867/00000/9C0E8015-1D61-E511-8E01-02163E012800.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/867/00000/F8C31B0E-1D61-E511-B063-02163E01473F.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/868/00000/2CCFD328-B561-E511-80AA-02163E0137F5.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/868/00000/3A9C3343-B561-E511-AF50-02163E0142F0.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/868/00000/5410332E-B561-E511-AFA8-02163E01439C.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/868/00000/8A56A12A-B561-E511-8489-02163E0144C4.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/868/00000/9AE0832B-B561-E511-AC19-02163E012128.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/868/00000/A2B6FF26-B561-E511-B407-02163E0145ED.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/868/00000/C2D38D29-B561-E511-AC65-02163E014236.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/868/00000/C2FA7529-B561-E511-AA15-02163E0119B6.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/869/00000/B80BECCA-1461-E511-AFF4-02163E01427C.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/924/00000/66C8146A-5F61-E511-83FC-02163E011BBF.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/925/00000/DC0B812A-6561-E511-AF93-02163E01461C.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/926/00000/9A6CFA1F-8C61-E511-80DD-02163E01215F.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/935/00000/06B51193-9D61-E511-A7F1-02163E011943.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/936/00000/40786412-0062-E511-A752-02163E011E2A.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/936/00000/5048B013-0062-E511-951D-02163E01461C.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/936/00000/560EDE14-0062-E511-A067-02163E011B5D.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/936/00000/5CD6014D-0362-E511-BCC8-02163E014294.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/936/00000/A444E614-0062-E511-A1ED-02163E013786.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/936/00000/F2E4ABE2-0062-E511-A21A-02163E0146D9.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/936/00000/FE5FDA23-0062-E511-ACC5-02163E0146D0.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/941/00000/02A6270D-0262-E511-B481-02163E0141DA.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/941/00000/0C4479CE-0062-E511-9936-02163E013811.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/256/941/00000/10AA8DF0-0062-E511-B01C-02163E0146ED.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/027/00000/2C13225C-FD62-E511-AC58-02163E0146F8.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/027/00000/7EBECA45-1363-E511-B66F-02163E01356C.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/027/00000/98E2C20E-0063-E511-804B-02163E014393.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/394/00000/52D48213-2564-E511-B739-02163E014419.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/395/00000/3ACCB54A-2664-E511-A7AD-02163E01465E.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/396/00000/3CA354AD-1365-E511-A98E-02163E014280.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/397/00000/EA646D5E-3F64-E511-874D-02163E0129FD.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/397/00000/EC933853-3F64-E511-ABD9-02163E014423.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/398/00000/C685BE14-2C64-E511-B219-02163E0138F9.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/399/00000/B6B31E32-5E64-E511-AD91-02163E014610.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/399/00000/BCE2D536-5E64-E511-9EA8-02163E0133EA.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/399/00000/DAAA6836-5E64-E511-924C-02163E0127B9.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/400/00000/34B1C98D-3065-E511-91A0-02163E0142E2.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/400/00000/6A10AEEC-2F65-E511-832D-02163E01201D.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/400/00000/6CC760EA-2F65-E511-B3C6-02163E0139B9.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/400/00000/7E502AEA-2F65-E511-A118-02163E0133DD.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/400/00000/86AB48EB-2F65-E511-B753-02163E012300.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/400/00000/98E1E078-3065-E511-AFFC-02163E01416F.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/400/00000/B08AD283-3165-E511-902F-02163E0142C5.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/400/00000/B49B5AF2-2F65-E511-85C0-02163E014315.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/400/00000/C85CBDEC-2F65-E511-BFDE-02163E01201D.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/400/00000/CA33D60E-3065-E511-B6A6-02163E0145F1.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/400/00000/CAF6061B-3065-E511-8137-02163E0140F7.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/400/00000/D8FABAEB-2F65-E511-8E13-02163E014115.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/460/00000/5614321C-DD64-E511-BE58-02163E01441F.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/461/00000/76DC6958-0D65-E511-AC8E-02163E01434F.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/487/00000/564A5FD2-4E66-E511-9EE5-02163E0133C8.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/487/00000/7CB81624-4366-E511-9CB7-02163E011A2E.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/487/00000/80C6BA22-4366-E511-935E-02163E01421E.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/487/00000/A21A6636-4066-E511-B2D1-02163E011DE0.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/487/00000/D424C83D-4066-E511-B737-02163E011AFE.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/490/00000/42B8CA1C-4966-E511-9412-02163E012B9E.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/529/00000/56A6948D-C665-E511-9F38-02163E0146AE.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/531/00000/B26DC190-8166-E511-AE66-02163E0133A7.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/531/00000/E842748C-8166-E511-9965-02163E011FB1.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/599/00000/908F5705-8666-E511-8362-02163E01432A.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/611/00000/466D4EA1-6466-E511-B8E1-02163E013660.root',
       '/store/data/Run2015D/DoubleMuon/MINIAOD/PromptReco-v3/000/257/644/00000/E46A495F-1467-E511-A44B-02163E011A9B.root' ] );


secFiles.extend( [
               ] )
