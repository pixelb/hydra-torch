# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
#
# Generated by configen, do not edit.
# See https://github.com/facebookresearch/hydra/tree/main/tools/configen
# fmt: off
# isort:skip_file
# flake8: noqa

from dataclasses import dataclass, field
from omegaconf import MISSING
from typing import Any


@dataclass
class ASGDConf:
    _target_: str = "torch.optim.asgd.ASGD"
    params: Any = MISSING
    lr: Any = 0.01
    lambd: Any = 0.0001
    alpha: Any = 0.75
    t0: Any = 1000000.0
    weight_decay: Any = 0
