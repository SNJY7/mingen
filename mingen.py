# mingen - static site generator
# created on: Sunday 17 April 2022 03:31:45 PM IST

import os
import sys
import markdown

def enclose(tag, content, attributes=""):
    result = "<" + tag + " " + attributes + ">" + content + "</" + tag + ">" 
    return result

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
            index = index + enclose("li", "<a href=\"" + fileName[:-3] + ".html\">" + title[2:] + "</a>")
    if index == "":
        return index
    else:
        index =  enclose("ul", index)
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
    title = enclose("title", firstLine[2:-1])
    if mdFileName == "index.md":
        index_ = index(mdFilePath)
    else:
        index_ = ""
    body = enclose("body", enclose("header", enclose("nav", navLinks + nav(mdFilePath)) + "<hr>" + markdown.markdown(firstLine))  
         + enclose("main", markdown.markdown(mdFile) + index_) + "<hr>" + footer)
    htmlFile = enclose("html", enclose("head", head + title) + body)
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


try:
    navLinks_ = open(cwd+"/mingen/nav.md", "r")
    navLinks = navLinks_.read()
    navLinks_.close()
    navLinks = "<div class=navlinks>" + markdown.markdown(navLinks) + "</div>"
except:
    navLinks = ""

try:
    footer_ = open(cwd+"/mingen/footer.md", "r")
    footer = footer_.read()
    footer_.close()
    footer = "<footer>" + markdown.markdown(footer) + "</footer>"
except:
    footer = ""

try:
    head_ = open(cwd+"/mingen/head.html", "r")
    head = head_.read()
    head_.close()
except:
    head = ""
    
compile(cwd)
