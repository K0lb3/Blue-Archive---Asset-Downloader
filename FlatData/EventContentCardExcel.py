# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EventContentCardExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EventContentCardExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsEventContentCardExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # EventContentCardExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # EventContentCardExcel
    def CardGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EventContentCardExcel
    def LocalizeEtcId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # EventContentCardExcel
    def IconPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # EventContentCardExcel
    def RewardParcelType(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # EventContentCardExcel
    def RewardParcelTypeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # EventContentCardExcel
    def RewardParcelTypeLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EventContentCardExcel
    def RewardParcelTypeIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # EventContentCardExcel
    def RewardParcelId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # EventContentCardExcel
    def RewardParcelIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # EventContentCardExcel
    def RewardParcelIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EventContentCardExcel
    def RewardParcelIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

def Start(builder): builder.StartObject(5)
def EventContentCardExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddCardGroupId(builder, CardGroupId): builder.PrependInt32Slot(0, CardGroupId, 0)
def EventContentCardExcelAddCardGroupId(builder, CardGroupId):
    """This method is deprecated. Please switch to AddCardGroupId."""
    return AddCardGroupId(builder, CardGroupId)
def AddLocalizeEtcId(builder, LocalizeEtcId): builder.PrependUint32Slot(1, LocalizeEtcId, 0)
def EventContentCardExcelAddLocalizeEtcId(builder, LocalizeEtcId):
    """This method is deprecated. Please switch to AddLocalizeEtcId."""
    return AddLocalizeEtcId(builder, LocalizeEtcId)
def AddIconPath(builder, IconPath): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(IconPath), 0)
def EventContentCardExcelAddIconPath(builder, IconPath):
    """This method is deprecated. Please switch to AddIconPath."""
    return AddIconPath(builder, IconPath)
def AddRewardParcelType(builder, RewardParcelType): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelType), 0)
def EventContentCardExcelAddRewardParcelType(builder, RewardParcelType):
    """This method is deprecated. Please switch to AddRewardParcelType."""
    return AddRewardParcelType(builder, RewardParcelType)
def StartRewardParcelTypeVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def EventContentCardExcelStartRewardParcelTypeVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartRewardParcelTypeVector(builder, numElems)
def AddRewardParcelId(builder, RewardParcelId): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(RewardParcelId), 0)
def EventContentCardExcelAddRewardParcelId(builder, RewardParcelId):
    """This method is deprecated. Please switch to AddRewardParcelId."""
    return AddRewardParcelId(builder, RewardParcelId)
def StartRewardParcelIdVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def EventContentCardExcelStartRewardParcelIdVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartRewardParcelIdVector(builder, numElems)
def End(builder): return builder.EndObject()
def EventContentCardExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)