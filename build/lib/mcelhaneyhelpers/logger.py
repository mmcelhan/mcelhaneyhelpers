from .mmcelhan_helpers import make_dir_if_not_exists, generate_text_file_with_timestamp
import os


class Logger:
    def __init__(self):
        self.output_dir = 'logs'
        make_dir_if_not_exists(self.output_dir)
        self.file_name = generate_text_file_with_timestamp('log')

    def log_api_response(self, response):
        with open(os.path.join(self.output_dir, self.file_name), 'a') as f:
            f.writelines('%s, %s\n' % (response, response.text))
        return None

    def write_log(self, text):
        # writes log to generated output file
        with open(os.path.join(self.output_dir, self.file_name), 'w') as f:
            f.writelines('%s\n' % text)
        return None
