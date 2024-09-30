from pydantic_yaml import parse_yaml_file_as, to_yaml_file
from pydantic import BaseModel
from pathlib import Path

class AppConfig(BaseModel):
    test_return:str

class CurrentConfig:
    """
    Class that loads the YAML file and returns the configuration model
    """

    _Config = None
    _Config_YAML_file = None    # Maintained so I can write changes back to it

    @classmethod
    def getConfig(cls) -> AppConfig:
        """
        Class method to access the singleton config.
        
        Returns
        -------
        AppConfig
            The current config
        
        """
        yaml_path = Path("/etc/app/appconfig.yaml")
        if yaml_path.exists():
            cls._Config = parse_yaml_file_as(AppConfig, yaml_path)
            return cls._Config
        
        yaml_path = Path("appconfig.yaml")
        if yaml_path.exists():
            cls._Config = parse_yaml_file_as(AppConfig, yaml_path)
            return cls._Config
        
        # Send a default
        return AppConfig(test_return="CONFIG NOT FOUND")
