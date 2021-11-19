# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class AcademyLocationExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AcademyLocationExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsAcademyLocationExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # AcademyLocationExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # AcademyLocationExcel
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # AcademyLocationExcel
    def LocalizeEtcId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # AcademyLocationExcel
    def PrefabPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AcademyLocationExcel
    def IconImagePath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AcademyLocationExcel
    def OpenCondition(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # AcademyLocationExcel
    def OpenConditionAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # AcademyLocationExcel
    def OpenConditionLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # AcademyLocationExcel
    def OpenConditionIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

    # AcademyLocationExcel
    def OpenConditionCount(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # AcademyLocationExcel
    def OpenConditionCountAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int64Flags, o)
        return 0

    # AcademyLocationExcel
    def OpenConditionCountLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # AcademyLocationExcel
    def OpenConditionCountIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # AcademyLocationExcel
    def RewardParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # AcademyLocationExcel
    def RewardParcelId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # AcademyLocationExcel
    def OpenTeacherRank(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(9)
def AcademyLocationExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddId(builder, Id): builder.PrependInt64Slot(0, Id, 0)
def AcademyLocationExcelAddId(builder, Id):
    """This method is deprecated. Please switch to AddId."""
    return AddId(builder, Id)
def AddLocalizeEtcId(builder, LocalizeEtcId): builder.PrependUint32Slot(1, LocalizeEtcId, 0)
def AcademyLocationExcelAddLocalizeEtcId(builder, LocalizeEtcId):
    """This method is deprecated. Please switch to AddLocalizeEtcId."""
    return AddLocalizeEtcId(builder, LocalizeEtcId)
def AddPrefabPath(builder, PrefabPath): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(PrefabPath), 0)
def AcademyLocationExcelAddPrefabPath(builder, PrefabPath):
    """This method is deprecated. Please switch to AddPrefabPath."""
    return AddPrefabPath(builder, PrefabPath)
def AddIconImagePath(builder, IconImagePath): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(IconImagePath), 0)
def AcademyLocationExcelAddIconImagePath(builder, IconImagePath):
    """This method is deprecated. Please switch to AddIconImagePath."""
    return AddIconImagePath(builder, IconImagePath)
def AddOpenCondition(builder, OpenCondition): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(OpenCondition), 0)
def AcademyLocationExcelAddOpenCondition(builder, OpenCondition):
    """This method is deprecated. Please switch to AddOpenCondition."""
    return AddOpenCondition(builder, OpenCondition)
def StartOpenConditionVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def AcademyLocationExcelStartOpenConditionVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartOpenConditionVector(builder, numElems)
def AddOpenConditionCount(builder, OpenConditionCount): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(OpenConditionCount), 0)
def AcademyLocationExcelAddOpenConditionCount(builder, OpenConditionCount):
    """This method is deprecated. Please switch to AddOpenConditionCount."""
    return AddOpenConditionCount(builder, OpenConditionCount)
def StartOpenConditionCountVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def AcademyLocationExcelStartOpenConditionCountVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartOpenConditionCountVector(builder, numElems)
def AddRewardParcelType(builder, RewardParcelType): builder.PrependInt32Slot(6, RewardParcelType, 0)
def AcademyLocationExcelAddRewardParcelType(builder, RewardParcelType):
    """This method is deprecated. Please switch to AddRewardParcelType."""
    return AddRewardParcelType(builder, RewardParcelType)
def AddRewardParcelId(builder, RewardParcelId): builder.PrependInt64Slot(7, RewardParcelId, 0)
def AcademyLocationExcelAddRewardParcelId(builder, RewardParcelId):
    """This method is deprecated. Please switch to AddRewardParcelId."""
    return AddRewardParcelId(builder, RewardParcelId)
def AddOpenTeacherRank(builder, OpenTeacherRank): builder.PrependInt64Slot(8, OpenTeacherRank, 0)
def AcademyLocationExcelAddOpenTeacherRank(builder, OpenTeacherRank):
    """This method is deprecated. Please switch to AddOpenTeacherRank."""
    return AddOpenTeacherRank(builder, OpenTeacherRank)
def End(builder): return builder.EndObject()
def AcademyLocationExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)