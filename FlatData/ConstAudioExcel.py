# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConstAudioExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConstAudioExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsConstAudioExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ConstAudioExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ConstAudioExcel
    def DefaultSnapShotName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConstAudioExcel
    def BattleSnapShotName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConstAudioExcel
    def RaidSnapShotName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConstAudioExcel
    def ExSkillCutInSnapShotName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def Start(builder): builder.StartObject(4)
def ConstAudioExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddDefaultSnapShotName(builder, DefaultSnapShotName): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(DefaultSnapShotName), 0)
def ConstAudioExcelAddDefaultSnapShotName(builder, DefaultSnapShotName):
    """This method is deprecated. Please switch to AddDefaultSnapShotName."""
    return AddDefaultSnapShotName(builder, DefaultSnapShotName)
def AddBattleSnapShotName(builder, BattleSnapShotName): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(BattleSnapShotName), 0)
def ConstAudioExcelAddBattleSnapShotName(builder, BattleSnapShotName):
    """This method is deprecated. Please switch to AddBattleSnapShotName."""
    return AddBattleSnapShotName(builder, BattleSnapShotName)
def AddRaidSnapShotName(builder, RaidSnapShotName): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(RaidSnapShotName), 0)
def ConstAudioExcelAddRaidSnapShotName(builder, RaidSnapShotName):
    """This method is deprecated. Please switch to AddRaidSnapShotName."""
    return AddRaidSnapShotName(builder, RaidSnapShotName)
def AddExSkillCutInSnapShotName(builder, ExSkillCutInSnapShotName): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(ExSkillCutInSnapShotName), 0)
def ConstAudioExcelAddExSkillCutInSnapShotName(builder, ExSkillCutInSnapShotName):
    """This method is deprecated. Please switch to AddExSkillCutInSnapShotName."""
    return AddExSkillCutInSnapShotName(builder, ExSkillCutInSnapShotName)
def End(builder): return builder.EndObject()
def ConstAudioExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)