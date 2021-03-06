# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatData

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class WeekDungeonRewardExcel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = WeekDungeonRewardExcel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsWeekDungeonRewardExcel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # WeekDungeonRewardExcel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # WeekDungeonRewardExcel
    def GroupId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # WeekDungeonRewardExcel
    def DungeonType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # WeekDungeonRewardExcel
    def RewardParcelType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # WeekDungeonRewardExcel
    def RewardParcelId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # WeekDungeonRewardExcel
    def RewardParcelAmount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # WeekDungeonRewardExcel
    def RewardParcelProbability(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # WeekDungeonRewardExcel
    def IsDisplayed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # WeekDungeonRewardExcel
    def DropItemModelPrefabPath(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def Start(builder): builder.StartObject(8)
def WeekDungeonRewardExcelStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddGroupId(builder, GroupId): builder.PrependInt64Slot(0, GroupId, 0)
def WeekDungeonRewardExcelAddGroupId(builder, GroupId):
    """This method is deprecated. Please switch to AddGroupId."""
    return AddGroupId(builder, GroupId)
def AddDungeonType(builder, DungeonType): builder.PrependInt32Slot(1, DungeonType, 0)
def WeekDungeonRewardExcelAddDungeonType(builder, DungeonType):
    """This method is deprecated. Please switch to AddDungeonType."""
    return AddDungeonType(builder, DungeonType)
def AddRewardParcelType(builder, RewardParcelType): builder.PrependInt32Slot(2, RewardParcelType, 0)
def WeekDungeonRewardExcelAddRewardParcelType(builder, RewardParcelType):
    """This method is deprecated. Please switch to AddRewardParcelType."""
    return AddRewardParcelType(builder, RewardParcelType)
def AddRewardParcelId(builder, RewardParcelId): builder.PrependInt64Slot(3, RewardParcelId, 0)
def WeekDungeonRewardExcelAddRewardParcelId(builder, RewardParcelId):
    """This method is deprecated. Please switch to AddRewardParcelId."""
    return AddRewardParcelId(builder, RewardParcelId)
def AddRewardParcelAmount(builder, RewardParcelAmount): builder.PrependInt64Slot(4, RewardParcelAmount, 0)
def WeekDungeonRewardExcelAddRewardParcelAmount(builder, RewardParcelAmount):
    """This method is deprecated. Please switch to AddRewardParcelAmount."""
    return AddRewardParcelAmount(builder, RewardParcelAmount)
def AddRewardParcelProbability(builder, RewardParcelProbability): builder.PrependInt64Slot(5, RewardParcelProbability, 0)
def WeekDungeonRewardExcelAddRewardParcelProbability(builder, RewardParcelProbability):
    """This method is deprecated. Please switch to AddRewardParcelProbability."""
    return AddRewardParcelProbability(builder, RewardParcelProbability)
def AddIsDisplayed(builder, IsDisplayed): builder.PrependBoolSlot(6, IsDisplayed, 0)
def WeekDungeonRewardExcelAddIsDisplayed(builder, IsDisplayed):
    """This method is deprecated. Please switch to AddIsDisplayed."""
    return AddIsDisplayed(builder, IsDisplayed)
def AddDropItemModelPrefabPath(builder, DropItemModelPrefabPath): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(DropItemModelPrefabPath), 0)
def WeekDungeonRewardExcelAddDropItemModelPrefabPath(builder, DropItemModelPrefabPath):
    """This method is deprecated. Please switch to AddDropItemModelPrefabPath."""
    return AddDropItemModelPrefabPath(builder, DropItemModelPrefabPath)
def End(builder): return builder.EndObject()
def WeekDungeonRewardExcelEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)