class Tv:
    def __init__(self, status: bool, volume: int, channel: int):
        self.status = status
        self.channel = channel


    def get_status(self):
        return self.status
    
    def set_status(self, status, false=None, true=None):
        if status == false:
            self.status = true

