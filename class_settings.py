from pydantic_settings import BaseSettings, SettingsConfigDict


class MyConfig(BaseSettings):

    model_config = SettingsConfigDict()

    db_name: str = "test"
    db_host: str = "191.189.1.21"
    db_port: int = 3306


    class Config:
        env_file = ".env"


setiings = MyConfig()

print(setiings)


