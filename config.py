from dotenv import dotenv_values


class Config:

    def __init__(self):
        self._config = dotenv_values()

    def get_config(self) -> dict[str, str | None]:
        return self._config

    def get_config_by_name(self, name: str) -> str | None:
        return self._config[name]

    def set_config(self, name: str, value: str | None) -> None:
        self._config[name] = value