# min - static site generator
# created on: Sunday 17 April 2022 03:31:45 PM IST

import os
import markdown

cwd = os.getcwd()

def md2html(mdFilePath, mdFileName):
    mdFile_ = open(mdFilePath+"/"+mdFileName, "r")
    mdFile = mdFile_.read()
    htmlFile_ = open(mdFilePath+"/"+mdFileName[:-3]+".html", "w+")
    css = "<link rel=\"stylesheet\" href=\"/main.css\">\n"
    head = "<head>\n" + "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n" + css + "\n</head>\n"
    body = "<body>\n" + markdown.markdown(mdFile) + "</body>\n"
    htmlFile = "<html>\n" + head + body + "</html>"
    htmlFile_.write(htmlFile)
    mdFile_.close()
    htmlFile_.close()

def compile(filePath):
    fileList = os.listdir(filePath)
    for fileName in fileList:
        if os.path.isdir(filePath+"/"+fileName):
            compile(filePath+"/"+fileName)
        elif fileName[-3:] == ".md":
            md2html(filePath, fileName)


compile(cwd)
