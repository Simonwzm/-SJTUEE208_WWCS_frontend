INDEX_DIR = "IndexFiles.index"

import sys, os, lucene, threading, time,string
from bs4 import BeautifulSoup
from datetime import datetime
from java.nio.file import Paths
import org.apache.lucene.analysis.miscellaneous
from org.apache.lucene.analysis.miscellaneous import LimitTokenCountAnalyzer
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.document import Document, Field, FieldType, StringField
from org.apache.lucene.index import FieldInfo, IndexWriter, IndexWriterConfig, IndexOptions
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.util import Version
from org.apache.lucene.analysis.cjk import CJKAnalyzer

from importlib.resources import contents
import re
import sys
import urllib.parse
import urllib.request
def is_Chinese(query):
    for _char in query:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False
print(is_Chinese('s1s是'))