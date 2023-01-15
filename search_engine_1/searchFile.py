# SJTU EE208

INDEX_DIR = "IndexFiles.index"

import sys, os, lucene
import jpype

from java.util import HashMap
from java.io import File
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.util import Version
from org.apache.lucene.analysis.cjk import CJKAnalyzer
from org.apache.lucene.analysis.miscellaneous import PerFieldAnalyzerWrapper

def run(searcher, analyzer,command,site='',date=["0000","00","00"],title_only=0):
    print()
    print ("Searching for:", command)
    if(title_only):
        query = QueryParser("title", analyzer).parse(command)
    if is_Chinese(command):
        query = QueryParser("content", analyzer).parse(command)
    else:
        query = QueryParser("contentEnglish", analyzer).parse(command)
    scoreDocs = searcher.search(query, 1000).scoreDocs
    print ("%s total matching documents." % len(scoreDocs))
    tar_list=[]
    for i,scoreDoc in enumerate(scoreDocs):
        doc=searcher.doc(scoreDoc.doc)
        unit_dict=dict()
        if(site and doc.get("webname")!=site or date and (doc.get("time")[0:4]!=date[0] or doc.get("time")[5:7]!=date[1] or doc.get("time")[8:10]!=date[2]) ):
            continue
        unit_dict["source"]=doc.get("webname")
        unit_dict["url"]=doc.get("url")
        try:
            unit_dict["content"]=doc.get("content")
            fullcontent=doc.get("content")
            unit_dict["contentEnglish"]=doc.get("contentEnglish")
            if not fullcontent:
                fullcontent=doc.get("contentEnglish")
        except:
            # unit_dict["contentEnglish"]=doc.get("contentEnglish")
            pass
        try:
            length=len(fullcontent)
            pos=fullcontent.find(command)
        except:
            continue
        if pos<30:
            st=0
        else:
            st=pos-30
        if length-pos<30:
            ed=length
        else:
            ed=pos+30
        nearbycontents=fullcontent[st:ed]
        unit_dict["para"]=nearbycontents
        unit_dict["fullcontent"] = fullcontent
        unit_dict["img"]=doc.get("image")
        unit_dict["date"]=doc.get("time")
        unit_dict["title"]=doc.get("title")
        tar_list.append(unit_dict)
    return tar_list

def is_Chinese(query):
    for _char in query:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False

# if __name__ == '__main__':
#     STORE_DIR="index"
#     lucene.initVM(vmargs=['-Djava.awt.headless=true'])
#     print ('lucene', lucene.VERSION)
#     directory = SimpleFSDirectory(File(STORE_DIR).toPath())
#     searcher = IndexSearcher(DirectoryReader.open(directory))
#     perField = HashMap()
#     perField.put('content.txt', CJKAnalyzer())
#     perField.put('contentEnglish.txt',StandardAnalyzer()) 
#     analyzer = PerFieldAnalyzerWrapper(CJKAnalyzer(), perField)
#     while True:
#         print()
#         print ("Hit enter with no input to quit.")
#         command =input("Query:")
#         # command = unicode(command, 'GBK')
#         if command == '':
#             break
#         site=input("site:")
#         date=input("date:")
#         title_only=input("title_only?")
#         run(searcher, analyzer,command,site,date,title_only)
#     del searcher

def main(command,site,date,title_only):
    STORE_DIR = "./search_engine_1/index"
    try:
        vm_env = lucene.initVM(vmargs=['-Djava.awt.headless=true'])
    except:
        vm_env = lucene.getVMEnv()
    vm_env.attachCurrentThread()
    #base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    directory = SimpleFSDirectory(File(STORE_DIR).toPath())
    searcher = IndexSearcher(DirectoryReader.open(directory))
    perField = HashMap()
    perField.put('content.txt', CJKAnalyzer())
    perField.put('contentEnglish.txt',StandardAnalyzer())
    analyzer = PerFieldAnalyzerWrapper(CJKAnalyzer(), perField)
    results = run(searcher, analyzer,command,site,date,title_only)
    del searcher    
    return results