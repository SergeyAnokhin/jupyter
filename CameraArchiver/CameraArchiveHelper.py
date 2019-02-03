import os
import json
import re
import datetime
from FileArchive import FileArchive
from elasticsearch import Elasticsearch


def report_to_elastic(file: FileArchive):
    config = file.config
    
    fullfilename_ftp = file.to.path.replace("\\\\diskstation", '').replace('\\', '/')

    dict = {
        "ext": file.frm.get_extension(),  # 'jpg'
        "volume": "/volume2",
        # "/Camera/Foscam/FI9805W_C4D6553DECE1/snap/MDAlarm_20190201-124005.jpg",
        "path": fullfilename_ftp,
        "@timestamp": file.frm.get_timestamp_utc(),  # "2019-02-01T11:40:05.000Z",
        "doc": "event",
        "sensor": config.sensor,
        "position": config.position,
        "camera": config.camera,
        "value": file.frm.size(),
        "tags": [
            "synology_camera",
            "python_camera_archiver"
        ]
    }
    json_data = json.dumps(dict, indent=4, sort_keys=True)
    print('{}@{}'.format(config.camera, file.frm.get_timestamp_utc()), json_data)
    # es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    # res = es.index(index="cameraarchive-" + file.month_id_utc,
    #                doc_type='doc',
    #                body=json_data,
    #                id='{}@{}'.format(config.camera, file.get_timestamp_utc()))

