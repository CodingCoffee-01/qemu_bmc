"""
QEMU Monitor Protocol (QMP) development library & tooling.

This package provides a fairly low-level class for communicating
asynchronously with QMP protocol servers, as implemented by QEMU, the
QEMU Guest Agent, and the QEMU Storage Daemon.

`QMPClient` provides the main functionality of this package. All errors
raised by this library dervive from `AQMPError`, see `aqmp.error` for
additional detail. See `aqmp.events` for an in-depth tutorial on
managing QMP events.
"""

# Copyright (C) 2020, 2021 John Snow for Red Hat, Inc.
#
# Authors:
#  John Snow <jsnow@redhat.com>
#
# Based on earlier work by Luiz Capitulino <lcapitulino@redhat.com>.
#
# This work is licensed under the terms of the GNU GPL, version 2.  See
# the COPYING file in the top-level directory.

import warnings

from .error import AQMPError
from .events import EventListener
from .message import Message
from .protocol import ConnectError, Runstate, StateError
from .qmp_client import ExecInterruptedError, ExecuteError, QMPClient


_WMSG = """

The Asynchronous QMP library is currently in development and its API
should be considered highly fluid and subject to change. It should
not be used by any other scripts checked into the QEMU tree.

Proceed with caution!
"""

warnings.warn(_WMSG, FutureWarning)


# The order of these fields impact the Sphinx documentation order.
__all__ = (
    # Classes, most to least important
    'QMPClient',
    'Message',
    'EventListener',
    'Runstate',

    # Exceptions, most generic to most explicit
    'AQMPError',
    'StateError',
    'ConnectError',
    'ExecuteError',
    'ExecInterruptedError',
)
