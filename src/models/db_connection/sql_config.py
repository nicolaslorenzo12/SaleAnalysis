from dataclasses import dataclass

@dataclass(frozen=True)
class SqlConfig:
    user: str
    password: str
    server: str
    database: str