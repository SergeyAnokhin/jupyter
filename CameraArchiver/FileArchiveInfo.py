import os
import re
import datetime
import pytz
from math import log2
import CameraArchiveConfig


class FileArchiveInfo:
    filename: str
    path: str
    path_relative: str
    dir: str
    dir_base: str
    dir_relative: str

    def __init__(self, config: CameraArchiveConfig, dir_base, full_filename):
        self.local = pytz.timezone("Europe/Paris")
        self.config = config
        self.dir_base = dir_base
        self.path = full_filename
        self.filename = os.path.basename(full_filename)
        self.dir = os.path.dirname(full_filename)
        self.path_relative = full_filename.replace(self.dir_base, '')
        self.dir_relative = os.path.dirname(self.path_relative)

    def get_extension(self):
        name, file_extension = os.path.splitext(self.filename)
        return file_extension.replace('.', '')

    def get_datetime(self):
        re_groups = re.search("(20\\d\\d)(\\d\\d)(\\d\\d)[_-]?(\\d\\d)(\\d\\d)(\\d\\d)", self.filename)
        year = int(re_groups.group(1))
        month = int(re_groups.group(2))
        day = int(re_groups.group(3))
        hour = int(re_groups.group(4))
        minute = int(re_groups.group(5))
        seconds = int(re_groups.group(6))
        return datetime.datetime(year, month, day, hour, minute, seconds)

    def get_datetime_utc(self):
        naive = self.get_datetime()
        local_dt = self.local.localize(naive)
        return local_dt.astimezone(pytz.utc)

    def get_month_id_utc(self):
        return self.get_datetime_utc().strftime('%Y.%m')

    def get_timestamp(self): # 'MDAlarm_20190131-153706'
        return self.get_datetime().strftime('%Y-%m-%dT%H:%M:%S.000Z')

    def get_timestamp_utc(self): # 'MDAlarm_20190131-153706'
        return self.get_datetime_utc().strftime('%Y-%m-%dT%H:%M:%S.000Z')

    def size(self):
        return os.path.getsize(self.path)

    def size_human(self):
        size = self.size()
        _suffixes = ['bytes', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
        # determine binary order in steps of size 10 
        # (coerce to int, // still returns a float)
        order = int(log2(size) / 10) if size else 0
        # format file size
        # (.4g results in rounded numbers for exact matches and max 3 decimals, 
        # should never resort to exponent values)
        return '{:.4g} {}'.format(size / (1 << (order * 10)), _suffixes[order])


