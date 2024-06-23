import tomli
import os

class ParamsReader:
    def __init__(self, config_path):
        self.config_path = config_path

    def get_config(self):
        """
        Get configuration from .toml file.

        Parameters:
        -----------
        - path : str
            - Path to the .toml configuration file.

        Returns:
        --------
        - config : dict
            - Parsed configuration data from the .toml file.

        Raises:
        -------
        - None
        """
        with open(self.config_path, mode="rb") as f_conf:
            config = tomli.load(f_conf)
        return config