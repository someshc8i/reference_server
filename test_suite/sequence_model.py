class Sequence:
    def __init__(self, name, sequence, is_circular, sha512, md5, size):
        self.name = name
        self.sequence = sequence
        self.is_circular = is_circular
        self.sha512 = sha512
        self.md5 = md5
        self.size = size
