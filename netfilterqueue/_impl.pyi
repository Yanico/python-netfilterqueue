import socket
from enum import IntEnum
from typing import Callable, Dict, Optional, Tuple

COPY_NONE: int
COPY_META: int
COPY_PACKET: int

class Packet:
    hook: int
    hw_protocol: int
    id: int
    mark: int
    def get_hw(self) -> Optional[bytes]: ...
    def get_payload(self) -> bytes: ...
    def get_payload_len(self) -> int: ...
    def get_timestamp(self) -> float: ...
    def get_mark(self) -> int: ...
    def set_payload(self, payload: bytes) -> None: ...
    def set_mark(self, mark: int) -> None: ...
    def retain(self) -> None: ...
    def accept(self) -> None: ...
    def drop(self) -> None: ...
    def repeat(self) -> None: ...

class NetfilterQueue:
    def __new__(self, *, af: int = ..., sockfd: int = ...) -> NetfilterQueue: ...
    def bind(
        self,
        queue_num: int,
        user_callback: Callable[[Packet], None],
        max_len: int = ...,
        mode: int = COPY_PACKET,
        range: int = ...,
        sock_len: int = ...,
    ) -> None: ...
    def unbind(self) -> None: ...
    def get_fd(self) -> int: ...
    def run(self, block: bool = ...) -> None: ...
    def run_socket(self, s: socket.socket) -> None: ...

PROTOCOLS: Dict[int, str]