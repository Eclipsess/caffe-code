import re
import os
import sys

def rmDecimal(xmlPath, savePath):
    """
    transport decimal in xmin ymin xmax ymax to int
    """
    fr = open(xmlPath,'r')
    fw = open(savePath,'w')
    reNum = re.compile(r'<depth>1</depth>')
    for t in fr.readlines():
        t = reNum.sub('<depth>3</depth>',t)
        fw.write(t)
    fr.close()
    fw.close()

if __name__ == '__main__':
    xmlFold = './../data/Annotations/'
    saveFold = './../data/tmpAnnotations/'
    for xmlName in os.listdir(xmlFold):
        xmlPath = xmlFold + xmlName
        savePath = saveFold + xmlName
        rmDecimal(xmlPath, savePath)
    print 'transport finished'

