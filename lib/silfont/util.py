#!/usr/bin/env python
'General classes and functions for use in pysilfont scripts'
__url__ = 'http://github.com/silnrsi/pysilfont'
__copyright__ = 'Copyright (c) 2014 SIL International (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'David Raymond'

import os, subprocess, difflib, sys

class dirTree(dict) :
    """ An object to hold list of all files and directories in a directory
        with option to read sub-directory contents into dirTree objects.
        Iterates through readSub levels of subfolders
        Flags to keep track of changes to files etc"""
    def __init__(self,dirn,readSub = 9999) :
        self.removedfiles = {} # List of files that have been renamed or deleted since reading from disk
        for name in os.listdir(dirn) :
            if name[-1:] == "~" : continue
            item=dirTreeItem()
            if os.path.isdir(os.path.join(dirn, name)) :
                item.type = "d"
                if readSub :
                    item.dirtree = dirTree(os.path.join(dirn,name),readSub-1)
            self[name] = item

    def subTree(self,path) : # Returns dirTree object for a subtree based on subfolder name(s)
        # 'path' can be supplied as either a relative path (eg "subf/subsubf") or array (eg ['subf','subsubf']
        if type(path) is str : path = self._split(path)
        subf=path[0]
        if subf in self:
            dtree =  self[subf].dirtree
        else : return None

        if len(path) == 1 :
            return dtree
        else :
            path.pop(0)
            return dtree.subTree(path)

    def _split(self,path) : # Turn a relative path into an array of subfolders
        npath = [os.path.split(path)[1]]
        while os.path.split(path)[0] :
            path = os.path.split(path)[0]
            npath.insert(0,os.path.split(path)[1])
        return npath

class dirTreeItem(object) :

    def __init__(self, type = "f", dirtree = None, read = False, added = False, changed = False, towrite = False, written = False, fileObject = None, fileType = None, flags = {}) :
        self.type = type                # "d" or "f"
        self.dirtree = dirtree          # dirtree for a sub-directory
        # Remaining properties are for calling scripts to use as they choose to track actions etc
        self.read = read                # Item has been read by the script
        self.added = added              # Item has been added to dirtree, so does not exist on disk
        self.changed = changed          # Item has been changed, so may need updating on disk
        self.towrite = towrite          # Item should be written out to disk
        self.written = written          # Item has been written to disk
        self.fileObject = fileObject    # An object representing the file
        self.fileType = fileType        # The type of the file object
        self.flags = {}                 # Any other flags a script might need

    def setinfo(self, read = None, added = None, changed = None, towrite = None, written = None, fileObject = None, fileType = None, flags = None) :
        pass
        if read : self.read = read
        if added : self.added = added
        if changed : self.changed = changed
        if towrite: self.towrite = towrite
        if written : self.written = written
        if fileObject is not None : self.fileObject = fileObject
        if fileType : self.fileType = fileType
        if flags : self.flags = flags

class ufo_diff(object): # For diffing 2 ufos as part of testing
    # returncodes:
    #   0 - ufos are the same
    #   1 - Differences were found
    #   2 - Errors running the difference (eg can't open file
    # diff - text of the differences
    # errors - text of the errors

    def __init__(self, ufo1, ufo2, ignoreOHCtime=True):

        diffcommand = ["diff", "-r", "-c1", ufo1, ufo2]

        # By default, if only difference in fontinfo is the openTypeHeadCreated timestamp ignore that

        if ignoreOHCtime: # Exclude fontinfo if only diff is openTypeHeadCreated
                          # Otherwise leave it in so differences are reported by main diff
            fi1 = os.path.join(ufo1,"fontinfo.plist")
            fi2 = os.path.join(ufo2, "fontinfo.plist")
            fitest = subprocess.Popen(["diff", fi1, fi2, "-c1"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            text = fitest.communicate()
            if fitest.returncode == 1:
                difftext = text[0].split("\n")
                if difftext[4].strip() == "<key>openTypeHeadCreated</key>" and len(difftext) == 12:
                    diffcommand.append("--exclude=fontinfo.plist")

        # Now do the main diff
        test = subprocess.Popen(diffcommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        text = test.communicate()
        self.returncode = test.returncode
        self.diff = text[0]
        self.errors = text[1]

    def print_text(self): # Print diff info or errors from the diffcommand
        if self.returncode == 0:
            print("UFOs are the same")
        elif self.returncode == 1:
            print("UFOs are different")
            print(self.diff)
        elif self.returncode == 2:
            print("Failed to compare UFOs")
            print(self.errors)

class text_diff(object): # For diffing 2 text files with option to ignore timestamps
    # See ufo_diff for class attribute details

    def __init__(self, log1, log2, ignore=0): # ignore - characters to ignore from left; typically 20 for timestamps
        errors = []
        try:
            l1 = [x[ignore:-1] for x in open(log1, "r").readlines()]
        except IOError:
            errors.append("Can't open " + log1)
        try:
            l2 = [x[ignore:-1] for x in open(log2, "r").readlines()]
        except IOError:
            errors.append("Can't open " + log2)

        if errors == []:
            self.errors = ""
            self.diff = "\n".join([x for x in difflib.unified_diff(l1, l2, log1, log2, n=0)])
            self.returncode = 0 if self.diff == "" else 1
        else:
            self.diff = ""
            self.errors = "\n".join(errors)
            self.returncode = 2

    def print_text(self): # Print diff info or errors the unified_diff command
        if self.returncode == 0:
            print("Files are the same")
        elif self.returncode == 1:
            print("Files are different")
            print(self.diff)
        elif self.returncode == 2:
            print("Failed to compare Files")
            print(self.errors)