from typing import Union

from . import XXHashService
from .MersenneTwister import MersenneTwister

uint = ulong = long = int
double = float


def CreateKey(name: str) -> bytes:  # 0x02AAE200-0x02AAE288
    # v3 = XXHashService_CalculateHash(name, 0LL);
    seed = XXHashService.CalculateHash(name)
    # v4 = sub_1996DC4(MersenneTwister__TypeInfo);
    # MersenneTwister__ctor_1(v4, v3, 0LL);
    return MersenneTwister(seed).NextBytes(8)


def XOR(name: str, data: bytes) -> bytes:
    seed = XXHashService.CalculateHash(name)
    twister = MersenneTwister(seed)
    xor_key = twister.NextBytes(len(data))

    if len(data) >= 1:
        data = bytes(x ^ y for x, y in zip(data, xor_key))
    return data


def ConvertInt(
    value: Union[int, long, uint, ulong], key: bytes
) -> Union[int, long, uint, ulong]:
    pass


def ConvertFloat(value: Union[float, double], key: bytes) -> Union[float, double]:
    pass


def EncryptFloat(value: Union[float, double], key: bytes) -> Union[float, double]:
    pass


def EncryptStr(value: str, key: bytes) -> str:
    pass


def ConvertStr(value: str, key: bytes) -> str:
    pass

