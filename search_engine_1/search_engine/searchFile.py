# SJTU EE208

INDEX_DIR = "IndexFiles.index"

import sys, os, lucene

from java.io import File
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.util import Version
from org.apache.lucene.analysis.cjk import CJKAnalyzer

def run(searcher, analyzer,command, debug=True):
    print()
    print ("Searching for:", command)
    query = QueryParser("content", analyzer).parse(command)
    scoreDocs = searcher.search(query, 50).scoreDocs
    print ("%s total matching documents." % len(scoreDocs))
    tar_list=[]
    for i,scoreDoc in enumerate(scoreDocs):
        doc=searcher.doc(scoreDoc.doc)
        unit_dict=dict()
        unit_dict["source"]=doc.get("webname")
        if debug:
            unit_dict["content"]=doc.get("content")[:5]
            unit_dict["title"]=doc.get("title")[:5]
            unit_dict["url"]=doc.get("url")[:5]
            unit_dict["img"]=doc.get("image")[:5]
        else:
            unit_dict["content"]=doc.get("content")
            unit_dict["url"]=doc.get("url")
            unit_dict["title"]=doc.get("title")
            unit_dict["img"]=doc.get("image")
        unit_dict["date"]=doc.get("time")
        tar_list.append(unit_dict)
    return tar_list



if __name__ == '__main__':
    STORE_DIR="index"
    lucene.initVM(vmargs=['-Djava.awt.headless=true'])
    print ('lucene', lucene.VERSION)
    directory = SimpleFSDirectory(File(STORE_DIR).toPath())
    searcher = IndexSearcher(DirectoryReader.open(directory))
    analyzer = CJKAnalyzer()
    while True:
        print()
        print ("Hit enter with no input to quit.")
        command =input("Query:")
        # command = unicode(command, 'GBK')
        if command == '':
            break
        print(run(searcher, analyzer,command))
    del searcher