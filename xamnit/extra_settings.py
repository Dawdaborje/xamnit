import dataclasses


@dataclasses.dataclass
class ExtraApp:
    name: str
    description: str
    module_path: str
