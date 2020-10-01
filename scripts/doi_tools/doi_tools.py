# -*- coding: utf-8 -*-

import xml.dom.minidom as prettyXML
import  argparse

def prettydoi(filename):
    exportedXML = open(filename,'r')

    xml = prettyXML.parse(exportedXML)
    prettyXml = xml.toprettyxml()

    prettyDoi = open('prettyDoi.xml','w')
    doistr = prettyXml.encode('ascii', 'xmlcharrefreplace')
    prettyDoi.write(doistr)
    prettyDoi.close()

def main():
    opt=['prettydoi', 'test']
    parser = argparse.ArgumentParser()
    parser.add_argument("--script", metavar="A", type=str, choices=opt, default=opt[2] ,required = False, help="Algoritmo a ser executado (%(choices)s)")
    parser.add_argument("doc", metavar="DOCUMENTO", type=argparse.FileType(), help="Arquivo contendo as paginas da memoria")
    parser.add_argument('filename')
    args = parser.parse_args()

    documento = argumentos["doc"].readlines()

    algoritmos = { 
		"prettydoi" : prettydoi,
		"test": test,
	}

    chamarAlgoritmo = algoritmos[argumentos["alg"]]

	chamarAlgoritmo(tamanhoCache, paginas)


if __name__ == "__main__":
	main()