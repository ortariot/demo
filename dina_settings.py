from dynaconf import Dynaconf


settings = Dynaconf(settings_file=["settings.toml"])


print(settings.test.db_port)
print(settings.default.db_name)
