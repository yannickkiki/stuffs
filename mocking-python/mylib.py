import os
import os.path


class RemovalService:
    """A service for removing objects from the filesystem."""

    @staticmethod
    def rm(filename):
        if os.path.isfile(filename):
            os.remove(filename)


class UploadService:

    def __init__(self, removal_service):
        self.removal_service = removal_service

    def upload_complete(self, filename):
        self.removal_service.rm(filename)
