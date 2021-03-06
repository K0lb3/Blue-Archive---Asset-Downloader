# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class VoiceSkillUseExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = VoiceSkillUseExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsVoiceSkillUseExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # VoiceSkillUseExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # VoiceSkillUseExcel
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # VoiceSkillUseExcel
    def VoiceHash(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # VoiceSkillUseExcel
    def VoiceHashAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint32Flags, o)
        return 0

    # VoiceSkillUseExcel
    def VoiceHashLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # VoiceSkillUseExcel
    def VoiceHashIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def Start(builder): builder.StartObject(2)
def VoiceSkillUseExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddName(builder, Name): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(Name), 0)
def VoiceSkillUseExcelAddName(builder, Name):
    """This method is deprecated. Please switch to AddName."""
    return AddName(builder, Name)
def AddVoiceHash(builder, VoiceHash): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(VoiceHash), 0)
def VoiceSkillUseExcelAddVoiceHash(builder, VoiceHash):
    """This method is deprecated. Please switch to AddVoiceHash."""
    return AddVoiceHash(builder, VoiceHash)
def StartVoiceHashVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def VoiceSkillUseExcelStartVoiceHashVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartVoiceHashVector(builder, numElems)
def End(builder): return builder.EndObject()
def VoiceSkillUseExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)