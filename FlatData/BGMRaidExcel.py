# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class BGMRaidExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = BGMRaidExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsBGMRaidExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # BGMRaidExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # BGMRaidExcel
    def StageId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # BGMRaidExcel
    def PhaseIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # BGMRaidExcel
    def BGMId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(3)
def BGMRaidExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddStageId(builder, StageId): builder.PrependInt64Slot(0, StageId, 0)
def BGMRaidExcelAddStageId(builder, StageId):
    """This method is deprecated. Please switch to AddStageId."""
    return AddStageId(builder, StageId)
def AddPhaseIndex(builder, PhaseIndex): builder.PrependInt64Slot(1, PhaseIndex, 0)
def BGMRaidExcelAddPhaseIndex(builder, PhaseIndex):
    """This method is deprecated. Please switch to AddPhaseIndex."""
    return AddPhaseIndex(builder, PhaseIndex)
def AddBGMId(builder, BGMId): builder.PrependInt64Slot(2, BGMId, 0)
def BGMRaidExcelAddBGMId(builder, BGMId):
    """This method is deprecated. Please switch to AddBGMId."""
    return AddBGMId(builder, BGMId)
def End(builder): return builder.EndObject()
def BGMRaidExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)