class IO_helper:
    @staticmethod
    def save(path, data):
        with open(path, 'w') as f:
            f.write(stringify(data))