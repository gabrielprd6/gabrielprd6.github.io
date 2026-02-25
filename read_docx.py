import zipfile
import xml.etree.ElementTree as ET
import sys

def read_docx(path):
    word_namespace = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
    ns = '{' + word_namespace + '}'
    try:
        with zipfile.ZipFile(path) as docx:
            tree = ET.XML(docx.read('word/document.xml'))
            paragraphs = []
            for paragraph in tree.iter(ns + 'p'):
                texts = [node.text for node in paragraph.iter(ns + 't') if node.text]
                if texts:
                    paragraphs.append(''.join(texts))
        return '\n'.join(paragraphs)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        with open(sys.argv[2], "w", encoding="utf-8") as f:
            f.write(read_docx(sys.argv[1]))
