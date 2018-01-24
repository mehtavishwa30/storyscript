class String:

    def __init__(self, data):
        self.chunks = [data]

    def add(self, bit):
        self.chunks.append(bit)

    def json(self):
        stripped_chunk = [bit.strip() for bit in self.chunks]
        joined_string = ' '.join(stripped_chunk)
        return {'$OBJECT': 'string', 'string': joined_string}
