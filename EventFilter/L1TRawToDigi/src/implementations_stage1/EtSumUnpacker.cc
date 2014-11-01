#include "FWCore/Framework/interface/MakerMacros.h"

#include "EventFilter/L1TRawToDigi/interface/Unpacker.h"

#include "CaloCollections.h"

namespace l1t {
  namespace stage1 {
    class EtSumUnpacker : public Unpacker {
      public:
        virtual bool unpack(const Block& block, UnpackerCollections *coll) override;
    };
  }
}

// Implementation

namespace l1t {
  namespace stage1 {
    bool
      EtSumUnpacker::unpack(const Block& block, UnpackerCollections *coll)
      {

        LogDebug("L1T") << "Block ID  = " << block.header().getID() << " size = " << block.header().getSize();

        int nBX = int(ceil(block.header().getSize() / 2.)); 

        // Find the first and last BXs
        int firstBX = -(ceil((double)nBX/2.)-1);
        int lastBX;
        if (nBX % 2 == 0) {
          lastBX = ceil((double)nBX/2.)+1;
        } else {
          lastBX = ceil((double)nBX/2.);
        }

        auto res_ = static_cast<CaloCollections*>(coll)->getEtSums();
        res_->setBXRange(firstBX, lastBX);

        LogDebug("L1T") << "nBX = " << nBX << " first BX = " << firstBX << " lastBX = " << lastBX;

        // Initialise index
        int unsigned i = 0;

        // Loop over multiple BX and then number of jets filling jet collection
        for (int bx=firstBX; bx<lastBX; bx++){
          uint32_t raw_data0 = block.payload()[i++];
          uint32_t raw_data1 = block.payload()[i++];        

          /* if (raw_data0 == 0 || raw_data1==0) continue; */

          uint16_t candbit[4];
          candbit[0] = raw_data0 & 0xFFFF;
          candbit[1] = (raw_data0 >> 16) & 0xFFFF;
          candbit[2] = raw_data1 & 0xFFFF;
          candbit[3] = (raw_data1 >> 16) & 0xFFFF;

          int totet=candbit[0] & 0xFFF;
          int totht=candbit[1] & 0xFFF;
          int etmiss=candbit[2] & 0xFFF;
          int etmissphi=candbit[3] & 0x7F;

          l1t::EtSum et = l1t::EtSum();
          et.setHwPt(totet);
          et.setType(l1t::EtSum::kTotalEt);       
          LogDebug("L1T") << "ET: pT " << et.hwPt();
          res_->push_back(bx,et);

          l1t::EtSum ht = l1t::EtSum();
          ht.setHwPt(totht);
          ht.setType(l1t::EtSum::kTotalHt);       
          LogDebug("L1T") << "HT: pT " << ht.hwPt();
          res_->push_back(bx,ht);

          l1t::EtSum met = l1t::EtSum();
          met.setHwPt(etmiss);
          met.setHwPhi(etmissphi);
          met.setType(l1t::EtSum::kMissingEt);       
          LogDebug("L1T") << "MET: phi " << met.hwPhi() << " pT " << met.hwPt();
          res_->push_back(bx,met);

        }

        return true;

      }
  }
}

DEFINE_L1T_UNPACKER(l1t::stage1::EtSumUnpacker);
