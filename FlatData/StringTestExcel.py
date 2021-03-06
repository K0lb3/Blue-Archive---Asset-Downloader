# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class StringTestExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = StringTestExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsStringTestExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # StringTestExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # StringTestExcel
    def String(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # StringTestExcel
    def StringLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # StringTestExcel
    def StringIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

    # StringTestExcel
    def Sentence1(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # StringTestExcel
    def Script(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def Start(builder): builder.StartObject(3)
def StringTestExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddString(builder, String): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(String), 0)
def StringTestExcelAddString(builder, String):
    """This method is deprecated. Please switch to AddString."""
    return AddString(builder, String)
def StartStringVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def StringTestExcelStartStringVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartStringVector(builder, numElems)
def AddSentence1(builder, Sentence1): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(Sentence1), 0)
def StringTestExcelAddSentence1(builder, Sentence1):
    """This method is deprecated. Please switch to AddSentence1."""
    return AddSentence1(builder, Sentence1)
def AddScript(builder, Script): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(Script), 0)
def StringTestExcelAddScript(builder, Script):
    """This method is deprecated. Please switch to AddScript."""
    return AddScript(builder, Script)
def End(builder): return builder.EndObject()
def StringTestExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)