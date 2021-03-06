# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterLevelStatFactorExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterLevelStatFactorExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCharacterLevelStatFactorExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # CharacterLevelStatFactorExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CharacterLevelStatFactorExcel
    def Level(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterLevelStatFactorExcel
    def CriticalFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterLevelStatFactorExcel
    def StabilityFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterLevelStatFactorExcel
    def DefenceFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # CharacterLevelStatFactorExcel
    def AccuracyFactor(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(5)
def CharacterLevelStatFactorExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddLevel(builder, Level): builder.PrependInt64Slot(0, Level, 0)
def CharacterLevelStatFactorExcelAddLevel(builder, Level):
    """This method is deprecated. Please switch to AddLevel."""
    return AddLevel(builder, Level)
def AddCriticalFactor(builder, CriticalFactor): builder.PrependInt64Slot(1, CriticalFactor, 0)
def CharacterLevelStatFactorExcelAddCriticalFactor(builder, CriticalFactor):
    """This method is deprecated. Please switch to AddCriticalFactor."""
    return AddCriticalFactor(builder, CriticalFactor)
def AddStabilityFactor(builder, StabilityFactor): builder.PrependInt64Slot(2, StabilityFactor, 0)
def CharacterLevelStatFactorExcelAddStabilityFactor(builder, StabilityFactor):
    """This method is deprecated. Please switch to AddStabilityFactor."""
    return AddStabilityFactor(builder, StabilityFactor)
def AddDefenceFactor(builder, DefenceFactor): builder.PrependInt64Slot(3, DefenceFactor, 0)
def CharacterLevelStatFactorExcelAddDefenceFactor(builder, DefenceFactor):
    """This method is deprecated. Please switch to AddDefenceFactor."""
    return AddDefenceFactor(builder, DefenceFactor)
def AddAccuracyFactor(builder, AccuracyFactor): builder.PrependInt64Slot(4, AccuracyFactor, 0)
def CharacterLevelStatFactorExcelAddAccuracyFactor(builder, AccuracyFactor):
    """This method is deprecated. Please switch to AddAccuracyFactor."""
    return AddAccuracyFactor(builder, AccuracyFactor)
def End(builder): return builder.EndObject()
def CharacterLevelStatFactorExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)