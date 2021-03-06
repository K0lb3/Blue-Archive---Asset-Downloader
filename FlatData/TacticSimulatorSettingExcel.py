# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TacticSimulatorSettingExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TacticSimulatorSettingExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsTacticSimulatorSettingExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # TacticSimulatorSettingExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TacticSimulatorSettingExcel
    def GroundId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticSimulatorSettingExcel
    def GetExp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticSimulatorSettingExcel
    def GetStarGrade(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TacticSimulatorSettingExcel
    def Equipment(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(4)
def TacticSimulatorSettingExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddGroundId(builder, GroundId): builder.PrependInt64Slot(0, GroundId, 0)
def TacticSimulatorSettingExcelAddGroundId(builder, GroundId):
    """This method is deprecated. Please switch to AddGroundId."""
    return AddGroundId(builder, GroundId)
def AddGetExp(builder, GetExp): builder.PrependInt64Slot(1, GetExp, 0)
def TacticSimulatorSettingExcelAddGetExp(builder, GetExp):
    """This method is deprecated. Please switch to AddGetExp."""
    return AddGetExp(builder, GetExp)
def AddGetStarGrade(builder, GetStarGrade): builder.PrependInt64Slot(2, GetStarGrade, 0)
def TacticSimulatorSettingExcelAddGetStarGrade(builder, GetStarGrade):
    """This method is deprecated. Please switch to AddGetStarGrade."""
    return AddGetStarGrade(builder, GetStarGrade)
def AddEquipment(builder, Equipment): builder.PrependInt64Slot(3, Equipment, 0)
def TacticSimulatorSettingExcelAddEquipment(builder, Equipment):
    """This method is deprecated. Please switch to AddEquipment."""
    return AddEquipment(builder, Equipment)
def End(builder): return builder.EndObject()
def TacticSimulatorSettingExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)