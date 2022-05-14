# mingen - static site generator
# created on: Sunday 17 April 2022 03:31:45 PM IST

import os
import sys
import markdown

cwd = os.getcwd()

mdPath = cwd + "/md"
htmlPath = cwd
siteName = cwd[cwd.rindex("/")+1:]

def index(folderPath):
    fileList = os.listdir(folderPath)
    index = ""
    for fileName in fileList:
        if fileName[-3:] == ".md":
            if fileName == "index.md":
                continue
            file_ = open(folderPath+"/"+fileName, "r")
            title = file_.readline()
            file_.close()
            index = index + "<li><a href=\"" + fileName[:-3] + ".html\">" + title[2:] + "</a></li>"
    if index == "":
        return index
    else:
        index = "<h2>Pages</h2><ul>" + index + "</ul>"
        return index

def nav(filePath):
    filePath = filePath[filePath.find("/md")+3:]
    nav = ""
    while filePath != "":
        nav = nav + " > " + "<a href=\"" + filePath + "\">" + filePath[filePath.rindex("/")+1:] + " </a>"
        filePath = filePath[:filePath.rindex("/")]
    nav = "<a href=\"/\">" + siteName + "</a>" + nav
    nav = "<div class=nav>" + nav + "</div>"
    return nav

def md2html(mdFilePath, mdFileName):
    mdFile_ = open(mdFilePath+"/"+mdFileName, "r")
    firstLine = mdFile_.readline()
    mdFile = mdFile_.read()
    mdFile_.close()
    
    htmlPath = mdFilePath.replace("/md", "", 1)
    if os.path.isdir(htmlPath) != True:
        os.mkdir(htmlPath)
    htmlFile_ = open(htmlPath+"/"+mdFileName[:-3]+".html", "w+")
    css = "<link rel=\"stylesheet\" href=\"/main.css\">"
    title = "<title>" + firstLine[2:-1] + "</title>"
    head = "<head>" + "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">" + title + css + "</head>"
    if mdFileName == "index.md":
        index_ = index(mdFilePath)
    else:
        index_ = ""
    body = "<body>" + "<header>" + markdown.markdown(firstLine) + "</header>" + "<nav>" + nav(mdFilePath) + "</nav>" + "<main>" + markdown.markdown(mdFile) + index_ + "</main>" + "</body>"
    htmlFile = "<html>" + head + body + "</html>"
    htmlFile_.write(htmlFile)
    htmlFile_.close()

def compile(filePath):
    fileList = os.listdir(filePath)
    index(filePath)
    for fileName in fileList:
        if os.path.isdir(filePath+"/"+fileName):
            index(filePath+"/"+fileName)
            compile(filePath+"/"+fileName)
        elif fileName[-3:] == ".md":
            md2html(filePath, fileName)

compile(mdPath)
