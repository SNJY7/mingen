# mingen - static site generator
# created on: Sunday 17 April 2022 03:31:45 PM IST

import os
import sys
import markdown

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
        index = "<ul>" + index + "</ul>"
        return index

def nav(filePath):
    filePath = filePath.replace(cwd, "")
    nav = ""
    while filePath != "":
        nav = " / " + "<a href=\"" + filePath + "\">" + filePath[filePath.rindex("/")+1:] + "</a>" + nav
        filePath = filePath[:filePath.rindex("/")]
    nav = "<a href=\"/\">" + siteName + "</a>" + nav
    nav = "<div class=navpath><p>" + nav + "</p></div>"
    return nav

def md2html(mdFilePath, mdFileName):
    mdFile_ = open(mdFilePath+"/"+mdFileName, "r")
    firstLine = mdFile_.readline()
    mdFile = mdFile_.read()
    mdFile_.close()
    
    htmlFile_ = open(mdFilePath+"/"+mdFileName[:-3]+".html", "w+")
    title = "<title>" + firstLine[2:-1] + "</title>"
    head_ = "<head>" + head + title + "</head>"
    if mdFileName == "index.md":
        index_ = index(mdFilePath)
    else:
        index_ = ""
    body = "<body>" + "<header>" + "<nav>" +  navLinks + nav(mdFilePath) + "</nav>" + "<hr>" + markdown.markdown(firstLine) + "</header>" + "<main>" + markdown.markdown(mdFile) + index_ + "</main>" + "<hr>" + footer + "</body>"
    htmlFile = "<html>" + head_ + body + "</html>"
    htmlFile_.write(htmlFile)
    htmlFile_.close()

def compile(filePath):
    fileList = os.listdir(filePath)
    for fileName in fileList:
        if os.path.isdir(filePath+"/"+fileName):
            if fileName == "mingen":
                continue
            compile(filePath+"/"+fileName)
        elif fileName[-3:] == ".md":
            md2html(filePath, fileName)

cwd = os.getcwd()
siteName = cwd[cwd.rindex("/")+1:]

navLinks_ = open(cwd+"/mingen/nav.md", "r")
navLinks = navLinks_.read()
navLinks_.close()
navLinks = "<div class=navlinks>" + markdown.markdown(navLinks) + "</div>"

footer_ = open(cwd+"/mingen/footer.md", "r")
footer = footer_.read()
footer_.close()
footer = "<footer>" + markdown.markdown(footer) + "</footer>"

head_ = open(cwd+"/mingen/head.md", "r")
head = head_.read()
head_.close()

compile(cwd)
