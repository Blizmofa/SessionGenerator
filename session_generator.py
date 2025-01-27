from scapy.all import *
import random


class SessionGenerator:
    def __init__(self, parameters: dict, open_session: dict, close_session: dict) -> None:
        self.seq = random.randint(0, 4294967295)# Initial sequence number
        self.ack = 0

    m