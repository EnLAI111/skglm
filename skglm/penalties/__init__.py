from .base import BasePenalty  # noqa F401

from .separable import (  # noqa F401
    L1_plus_L2, L0_5, L1, L2_3, MCPenalty, WeightedL1, IndicatorBox, BasePenalty
)

from .block_separable import L2_05, L2_1, BlockMCPenalty  # noqa F401
