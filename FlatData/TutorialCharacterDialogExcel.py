# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TutorialCharacterDialogExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TutorialCharacterDialogExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsTutorialCharacterDialogExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # TutorialCharacterDialogExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TutorialCharacterDialogExcel
    def TalkId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # TutorialCharacterDialogExcel
    def AnimationName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TutorialCharacterDialogExcel
    def LocalizeKR(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TutorialCharacterDialogExcel
    def LocalizeJP(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TutorialCharacterDialogExcel
    def LocalizeTH(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TutorialCharacterDialogExcel
    def LocalizeTW(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TutorialCharacterDialogExcel
    def LocalizeEN(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TutorialCharacterDialogExcel
    def LocalizeDE(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TutorialCharacterDialogExcel
    def LocalizeFR(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TutorialCharacterDialogExcel
    def SoundPathKR(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TutorialCharacterDialogExcel
    def SoundPathJP(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TutorialCharacterDialogExcel
    def SoundPathTH(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TutorialCharacterDialogExcel
    def SoundPathTW(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TutorialCharacterDialogExcel
    def SoundPathEN(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TutorialCharacterDialogExcel
    def SoundPathDE(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TutorialCharacterDialogExcel
    def SoundPathFR(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def Start(builder): builder.StartObject(16)
def TutorialCharacterDialogExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddTalkId(builder, TalkId): builder.PrependInt64Slot(0, TalkId, 0)
def TutorialCharacterDialogExcelAddTalkId(builder, TalkId):
    """This method is deprecated. Please switch to AddTalkId."""
    return AddTalkId(builder, TalkId)
def AddAnimationName(builder, AnimationName): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(AnimationName), 0)
def TutorialCharacterDialogExcelAddAnimationName(builder, AnimationName):
    """This method is deprecated. Please switch to AddAnimationName."""
    return AddAnimationName(builder, AnimationName)
def AddLocalizeKR(builder, LocalizeKR): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeKR), 0)
def TutorialCharacterDialogExcelAddLocalizeKR(builder, LocalizeKR):
    """This method is deprecated. Please switch to AddLocalizeKR."""
    return AddLocalizeKR(builder, LocalizeKR)
def AddLocalizeJP(builder, LocalizeJP): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeJP), 0)
def TutorialCharacterDialogExcelAddLocalizeJP(builder, LocalizeJP):
    """This method is deprecated. Please switch to AddLocalizeJP."""
    return AddLocalizeJP(builder, LocalizeJP)
def AddLocalizeTH(builder, LocalizeTH): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeTH), 0)
def TutorialCharacterDialogExcelAddLocalizeTH(builder, LocalizeTH):
    """This method is deprecated. Please switch to AddLocalizeTH."""
    return AddLocalizeTH(builder, LocalizeTH)
def AddLocalizeTW(builder, LocalizeTW): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeTW), 0)
def TutorialCharacterDialogExcelAddLocalizeTW(builder, LocalizeTW):
    """This method is deprecated. Please switch to AddLocalizeTW."""
    return AddLocalizeTW(builder, LocalizeTW)
def AddLocalizeEN(builder, LocalizeEN): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeEN), 0)
def TutorialCharacterDialogExcelAddLocalizeEN(builder, LocalizeEN):
    """This method is deprecated. Please switch to AddLocalizeEN."""
    return AddLocalizeEN(builder, LocalizeEN)
def AddLocalizeDE(builder, LocalizeDE): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeDE), 0)
def TutorialCharacterDialogExcelAddLocalizeDE(builder, LocalizeDE):
    """This method is deprecated. Please switch to AddLocalizeDE."""
    return AddLocalizeDE(builder, LocalizeDE)
def AddLocalizeFR(builder, LocalizeFR): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(LocalizeFR), 0)
def TutorialCharacterDialogExcelAddLocalizeFR(builder, LocalizeFR):
    """This method is deprecated. Please switch to AddLocalizeFR."""
    return AddLocalizeFR(builder, LocalizeFR)
def AddSoundPathKR(builder, SoundPathKR): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(SoundPathKR), 0)
def TutorialCharacterDialogExcelAddSoundPathKR(builder, SoundPathKR):
    """This method is deprecated. Please switch to AddSoundPathKR."""
    return AddSoundPathKR(builder, SoundPathKR)
def AddSoundPathJP(builder, SoundPathJP): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(SoundPathJP), 0)
def TutorialCharacterDialogExcelAddSoundPathJP(builder, SoundPathJP):
    """This method is deprecated. Please switch to AddSoundPathJP."""
    return AddSoundPathJP(builder, SoundPathJP)
def AddSoundPathTH(builder, SoundPathTH): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(SoundPathTH), 0)
def TutorialCharacterDialogExcelAddSoundPathTH(builder, SoundPathTH):
    """This method is deprecated. Please switch to AddSoundPathTH."""
    return AddSoundPathTH(builder, SoundPathTH)
def AddSoundPathTW(builder, SoundPathTW): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(SoundPathTW), 0)
def TutorialCharacterDialogExcelAddSoundPathTW(builder, SoundPathTW):
    """This method is deprecated. Please switch to AddSoundPathTW."""
    return AddSoundPathTW(builder, SoundPathTW)
def AddSoundPathEN(builder, SoundPathEN): builder.PrependUOffsetTRelativeSlot(13, flatbuffers.number_types.UOffsetTFlags.py_type(SoundPathEN), 0)
def TutorialCharacterDialogExcelAddSoundPathEN(builder, SoundPathEN):
    """This method is deprecated. Please switch to AddSoundPathEN."""
    return AddSoundPathEN(builder, SoundPathEN)
def AddSoundPathDE(builder, SoundPathDE): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(SoundPathDE), 0)
def TutorialCharacterDialogExcelAddSoundPathDE(builder, SoundPathDE):
    """This method is deprecated. Please switch to AddSoundPathDE."""
    return AddSoundPathDE(builder, SoundPathDE)
def AddSoundPathFR(builder, SoundPathFR): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(SoundPathFR), 0)
def TutorialCharacterDialogExcelAddSoundPathFR(builder, SoundPathFR):
    """This method is deprecated. Please switch to AddSoundPathFR."""
    return AddSoundPathFR(builder, SoundPathFR)
def End(builder): return builder.EndObject()
def TutorialCharacterDialogExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)