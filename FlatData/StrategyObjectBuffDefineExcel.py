# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class StrategyObjectBuffDefineExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = StrategyObjectBuffDefineExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsStrategyObjectBuffDefineExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # StrategyObjectBuffDefineExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # StrategyObjectBuffDefineExcel
    def StrategyObjectBuffID(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # StrategyObjectBuffDefineExcel
    def StrategyObjectTurn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # StrategyObjectBuffDefineExcel
    def SkillGroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # StrategyObjectBuffDefineExcel
    def LocalizeCodeId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # StrategyObjectBuffDefineExcel
    def IconPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def Start(builder): builder.StartObject(5)
def StrategyObjectBuffDefineExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddStrategyObjectBuffID(builder, StrategyObjectBuffID): builder.PrependInt64Slot(0, StrategyObjectBuffID, 0)
def StrategyObjectBuffDefineExcelAddStrategyObjectBuffID(builder, StrategyObjectBuffID):
    """This method is deprecated. Please switch to AddStrategyObjectBuffID."""
    return AddStrategyObjectBuffID(builder, StrategyObjectBuffID)
def AddStrategyObjectTurn(builder, StrategyObjectTurn): builder.PrependInt32Slot(1, StrategyObjectTurn, 0)
def StrategyObjectBuffDefineExcelAddStrategyObjectTurn(builder, StrategyObjectTurn):
    """This method is deprecated. Please switch to AddStrategyObjectTurn."""
    return AddStrategyObjectTurn(builder, StrategyObjectTurn)
def AddSkillGroupId(builder, SkillGroupId): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(SkillGroupId), 0)
def StrategyObjectBuffDefineExcelAddSkillGroupId(builder, SkillGroupId):
    """This method is deprecated. Please switch to AddSkillGroupId."""
    return AddSkillGroupId(builder, SkillGroupId)
def AddLocalizeCodeId(builder, LocalizeCodeId): builder.PrependUint32Slot(3, LocalizeCodeId, 0)
def StrategyObjectBuffDefineExcelAddLocalizeCodeId(builder, LocalizeCodeId):
    """This method is deprecated. Please switch to AddLocalizeCodeId."""
    return AddLocalizeCodeId(builder, LocalizeCodeId)
def AddIconPath(builder, IconPath): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(IconPath), 0)
def StrategyObjectBuffDefineExcelAddIconPath(builder, IconPath):
    """This method is deprecated. Please switch to AddIconPath."""
    return AddIconPath(builder, IconPath)
def End(builder): return builder.EndObject()
def StrategyObjectBuffDefineExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)