import os
from CameraArchiveConfig import CameraArchiveConfig
from FileArchiveInfo import FileArchiveInfo


class FileArchive:
    frm: FileArchiveInfo
    to: FileArchiveInfo

    def __init__(self, config: CameraArchiveConfig, root, filename):
        self.config = config

        full_filename = os.path.join(root, filename)
        self.frm = FileArchiveInfo(config, config.path_from, full_filename)

        full_filename = os.path.join(config.path_to, self.frm.get_datetime().strftime('%Y-%m\\%d'), self.frm.path_relative.strip('\\'))
        self.to = FileArchiveInfo(config, config.path_to, full_filename)

    def __repr__(self):
        return '{}: \n\t <= {}\n\t => {}'.format(self.frm.dir_relative,  self.frm.path, self.to.path)


