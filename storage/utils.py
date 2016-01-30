import unicodedata
from django.core.files.storage import FileSystemStorage
import time
import hashlib

class ASCIIFileSystemStorage(FileSystemStorage):
    """
    Convert unicode characters in name to ASCII characters.
    """
    def get_valid_name(self, name):
        oldname = unicodedata.normalize('NFC', name).encode('ascii', 'ignore')
        list0 = oldname.rsplit('.', 1)
        nonce = str(time.time())
        new_name = hashlib.sha1(nonce).hexdigest()
        name = '.'.join([new_name[:5], list0[1]])
        return super(ASCIIFileSystemStorage, self).get_valid_name(name)
