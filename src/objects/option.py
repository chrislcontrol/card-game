from dataclasses import dataclass


@dataclass
class Option:
    description: str
    callback: callable
