import os
from utils import params_reader

class App:
    def __init__(self):
        '''
        Initialize class.
        '''
        # Define class variables
        self.config_path = 'config'
        self.config_name = 'config.toml'
        self.config_file = os.path.join(self.config_path, self.config_name)

        # Instantiate classes with required params
        self.params_handler = params_reader.ParamsReader(self.config_file)

    def load_config(self):
        '''
        Load configuration from config path.
        Set variables for use in class methods.
        '''
        config_handler = self.params_handler.get_config()
        param_operation = config_handler['operation']
        self.param_input_dir = param_operation['input_dir']
        self.param_input_dir_videos = os.path.join(self.param_input_dir, param_operation['videos_dir'])
        self.param_input_dir_playlists = os.path.join(self.param_input_dir, param_operation['playlists_dir'])

        self.param_output_dir = param_operation['output_dir']
        self.param_mode = param_operation['mode']

    def execute_application(self) -> None:
        '''
        Execute application.
        '''
        self.load_config()