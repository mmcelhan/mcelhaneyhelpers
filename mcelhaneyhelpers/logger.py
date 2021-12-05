import mmcelhan_helpers as hlp
import os


class Logger:
    def __init__(self):
        self.output_dir = 'logs'
        hlp.make_dir_if_not_exists(self.output_dir)
        self.file_name = hlp.generate_text_file_with_timestamp('log')

    def log_api_response(self, response):
        with open(os.path.join(self.output_dir, self.file_name), 'a') as f:
            f.writelines('%s, %s\n' % (response, response.text))
        return None

    def write_log(self, text):
        # writes log to generated output file
        with open(os.path.join(self.output_dir, self.file_name), 'w') as f:
            f.writelines('%s\n' % text)
        return None