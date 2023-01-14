# SJTU EE208

INDEX_DIR = "IndexFiles.index"

import sys, os, lucene, threading, time,string
from bs4 import BeautifulSoup
from datetime import datetime

# from java.io import File
from java.nio.file import Paths
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

def valid_filename(s):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    s = ''.join(c for c in s if c in valid_chars)
    return s

class Ticker(object):

    def __init__(self):
        self.tick = True

    def run(self):
        while self.tick:
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(1.0)

class IndexFiles(object):
    """Usage: python IndexFiles <doc_directory>"""

    def __init__(self, root, storeDir):

        if not os.path.exists(storeDir):
            os.mkdir(storeDir)

        # store = SimpleFSDirectory(File(storeDir).toPath())
        store = SimpleFSDirectory(Paths.get(storeDir))
        analyzer = CJKAnalyzer()
        analyzer = LimitTokenCountAnalyzer(analyzer, 1048576)
        config = IndexWriterConfig(analyzer)
        config.setOpenMode(IndexWriterConfig.OpenMode.CREATE)
        writer = IndexWriter(store, config)

        self.indexDocs(root, writer)
        ticker = Ticker()
        print('commit index')
        threading.Thread(target=ticker.run).start()
        writer.commit()
        writer.close()
        ticker.tick = False
        print('done')

    def indexDocs(self, root, writer):

        t1 = FieldType()
        t1.setStored(True)
        t1.setTokenized(True)
        #t1.setIndexOptions(IndexOptions.NONE)  # Not Indexed
        t1.setIndexOptions(IndexOptions.DOCS_AND_FREQS_AND_POSITIONS)

        t2 = FieldType()
        t2.setStored(False)
        t2.setTokenized(True)
        t2.setIndexOptions(IndexOptions.DOCS_AND_FREQS_AND_POSITIONS)  # Indexes documents, frequencies and positions.
        
        unit_list=["content.txt","image.txt","time.txt","title.txt","url.txt"]
        for web in os.listdir(root):
            webpath="webs/"+web
            for page in os.listdir(webpath):
                try:
                    print(page)
                    pagepath=webpath+'/'+page
                    doc=Document()
                    doc.add(Field("webname",web,t1))
                    
                    for unit in unit_list:
                        unitfile=pagepath+'/'+unit
                        with open(unitfile,'r') as tar:
                            reader=tar.read()
                            if("title" in unit):
                                print(reader)
                            doc.add(Field(unit[0:-4],reader,t1))
                        tar.close()
                    writer.addDocument(doc)
                except:
                    print("Failed")
                    continue


if __name__ == '__main__':
    lucene.initVM()#vmargs=['-Djava.awt.headless=true'])
    print('lucene', lucene.VERSION)
    # import ipdb; ipdb.set_trace()
    start = datetime.now()
    try:
        IndexFiles("webs", "index")
        end = datetime.now()
        print(end - start)
    except Exception as e:
        print("Failed: ", e)
        raise e
