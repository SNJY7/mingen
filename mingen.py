# mingen - static site generator
# created on: Sunday 17 April 2022 03:31:45 PM IST

import os
import sys
import markdown

cwd = os.getcwd()

mdPath = cwd + "/md"
htmlPath = cwd

def md2html(mdFilePath, mdFileName):
    mdFile_ = open(mdFilePath+"/"+mdFileName, "r")
    firstLine = mdFile_.readline()
    mdFile = mdFile_.read()
    htmlPath = mdFilePath.replace("/md", "", 1)
    if os.path.isdir(htmlPath) != True:
        os.mkdir(htmlPath)
    htmlFile_ = open(htmlPath+"/"+mdFileName[:-3]+".html", "w+")
    css = "<link rel=\"stylesheet\" href=\"main.css\">\n"
    title = "<title>" + firstLine[2:] + "</title>"
    head = "<head>\n" + "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n" + title + css + "</head>\n"
    body = "<body>\n" + "<header>" + markdown.markdown(firstLine) + "</header>" + markdown.markdown(mdFile) + "\n</body>\n"
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
