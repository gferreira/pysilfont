#!/usr/bin/env python
'''Export fonts in a GlyphsApp file to UFOs'''
__url__ = 'http://github.com/silnrsi/pysilfont'
__copyright__ = 'Copyright (c) 2017 SIL International (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'Victor Gaultney'

from silfont.core import execute

import glyphsLib
import silfont.ufo
import silfont.etutil
from io import open
import os, shutil

argspec = [
    ('glyphsfont', {'help': 'Input font file'}, {'type': 'filename'}),
    ('masterdir', {'help': 'Output directory for masters'}, {}),
    ('--nofixes', {'help': 'Bypass code fixing data', 'action': 'store_true', 'default': False}, {}),
    ('--nofea', {'help': "Don't output features.fea", 'action': 'store_true', 'default': False}, {}),
    ('-l', '--log', {'help': 'Log file'}, {'type': 'outfile', 'def': '_glyphs2ufo.log'})]


def doit(args):
    logger = args.logger
    logger.log("Creating UFO objects from GlyphsApp file", "I")
    with open(args.glyphsfont, 'r', encoding='utf-8') as gfile:
        gfont = glyphsLib.parser.load(gfile)
    ufos = glyphsLib.to_ufos(gfont, include_instances=False, family_name=None, propagate_anchors=False)

    # Extract directory name for use with backups
    (glyphsdir, filen) = os.path.split(args.glyphsfont)

    librestorekeys = ("org.sil.pysilfontparams", "org.sil.altLineMetrics", "org.sil.lcg.toneLetters",
                   "org.sil.lcg.transforms", "public.glyphOrder", "public.postscriptNames")
    libdeletekeys = ("UFOFormat", "com.schriftgestaltung.blueFuzz", "com.schriftgestaltung.blueScale",
                     "com.schriftgestaltung.blueShift")
    libdeleteempty = ("com.schriftgestaltung.DisplayStrings",)

    inforestorekeys = ("openTypeHeadCreated", "openTypeNamePreferredFamilyName", "openTypeNamePreferredSubfamilyName",
                       "openTypeNameUniqueID", "openTypeOS2WeightClass", "openTypeOS2WidthClass", "postscriptFontName",
                       "postscriptFullName", "styleMapFamilyName", "styleMapStyleName")
    integerkeys = ("openTypeOS2WeightClass", "openTypeOS2WidthClass")
    infodeleteempty = ("openTypeOS2Selection",)
    # infodeletekeys = ("openTypeOS2Type",)

    for ufo in ufos:

        sn = ufo.info.styleName                              # )
        sn = sn.replace("Italic Italic", "Italic")           # ) Temp fixes due to glyphLib incorrectly
        sn = sn.replace("Italic Bold Italic", "Bold Italic") # ) forming styleName
        sn = sn.replace("Extra Italic Light Italic", "Extra Light Italic") # )
        ufo.info.styleName = sn                              # )
        fontname = ufo.info.familyName.replace(" ", "") + "-" + ufo.info.styleName.replace(" ", "")

        # Fixes to the data
        if not args.nofixes:
            logger.log("Fixing data in " + fontname, "P")
            # lib.plist processing
            logger.log("Checking lib.plist", "P")

            # Process UFO.lib if present
            if "UFO.lib" in ufo.lib:
                logger.log("UFO.lib field found in lib.plist for " + fontname + ". Values will be copied to root", "P")
                ul = ufo.lib["UFO.lib"]
                # Copy fields from UFO.lib to root
                for key in ul:
                    if key in librestorekeys:
                        continue # They will be restored later
                    if key in libdeleteempty:
                        if ul[key] == "" or ul[key] == []:
                            logger.log("Emtpy field ignored: " + key, "I")
                            continue
                    if key in libdeletekeys:
                        logger.log(key + " ignored", "I")
                        continue
                    if key in ufo.lib:
                        current = ufo.lib[key]
                        logmess = " updated from UFO.lib. "
                    else:
                        current = None
                        logmess = " copied from UFO.lib. "
                    new = ul[key]
                    if current == new:
                        continue
                    else:
                        ufo.lib[key] = new
                        logchange(logger, logmess, key, current, new)
                del ufo.lib["UFO.lib"]
                logger.log("UFO.lib field deleted", "I")

            # Restore values from original UFOs, assuming nameed as <fontname>.ufo in same directory as input .gylphs file

            ufodir = os.path.join(glyphsdir,fontname+".ufo")
            try:
                origlibplist = silfont.ufo.Uplist(font=None, dirn=ufodir, filen="lib.plist")
            except Exception as e:
                logger.log("Unable to open lib.plist in " + ufodir + "; values will not be restored", "E")
                origlibplist = None

            if origlibplist is not None:
                for key in librestorekeys:
                    if key in origlibplist:
                        new = origlibplist.getval(key)
                        current = None if key not in ufo.lib else ufo.lib[key]
                        if current == new:
                            continue
                        else:
                            ufo.lib[key] = new
                            logchange(logger, " restored from backup ufo. ", key, current, new)

            # Delete unneeded keys

            for key in libdeletekeys:
                if key in ufo.lib:
                    current = ufo.lib[key]
                    del ufo.lib[key]
                    logchange(logger, " deleted. ", key, current, None)

            for key in libdeleteempty:
                if key in ufo.lib and (ufo.lib[key] == "" or ufo.lib[key] == []):
                    current = ufo.lib[key]
                    del ufo.lib[key]
                    logchange(logger, " empty field deleted. ", key, current, None)

            ufo.lib["org.sil.glyphsappversion"] = gfont.appVersion

            # fontinfo.plist processing

            logger.log("Checking fontinfo.plist", "P")

            try:
                origfontinfo = silfont.ufo.Uplist(font=None, dirn=ufodir, filen="fontinfo.plist")
            except Exception as e:
                logger.log("Unable to open fontinfo.plist in " + ufodir + "; values will not be restored", "E")
                origfontinfo = None

            if origfontinfo is not None:
                for key in inforestorekeys:
                    if key in origfontinfo:
                        new = origfontinfo.getval(key)
                        if key in integerkeys: new = int(new)
                        current = None if not hasattr(ufo.info, key) else  getattr(ufo.info, key)
                        if current == new:
                            continue
                        else:
                            setattr(ufo.info, key, new)
                            logchange(logger, " restored from backup ufo. ", key, current, new)

            # Delete unneeded keys

            # for key in infodeletekeys:
            #     if hasattr(ufo.info, key):
            #        current = getattr(ufo.info, key)
            #        setattr(ufo.info, key, None)
            #        logchange(logger, " deleted. ", key, current, None)

            for key in infodeleteempty:
                if hasattr(ufo.info, key) and getattr(ufo.info, key) == "":
                    setattr(ufo.info, key, None)
                    logchange(logger, " empty field deleted. ", key, current, None)
        if args.nofea:ufo.features.text = "" # Suppress output of features.fea

        # Write ufo out
        ufopath = os.path.join(args.masterdir, fontname + ".ufo")
        logger.log("Writing out " + ufopath, "P")
        if os.path.exists(ufopath): shutil.rmtree(ufopath)
        ufo.save(ufopath)

        # Now correct the newly-written fontinfo.plist with changes that can't be made via glyphsLib
        if not args.nofixes:
            fontinfo = silfont.ufo.Uplist(font=None, dirn=ufopath, filen="fontinfo.plist")
            changes = False
            for key in ("guidelines", "postscriptBlueValues", "postscriptFamilyBlues", "postscriptFamilyOtherBlues",
                        "postscriptOtherBlues"):
                if fontinfo.getval(key) == [] :
                    fontinfo.remove(key)
                    changes = True
                    logchange(logger, " empty list deleted", key, None, [])
            if changes:
                # Create outparams.  Just need any valid values, since font will need normalizing later
                params = args.paramsobj
                paramset = params.sets["main"]
                outparams = {"attribOrders": {}}
                for parn in params.classes["outparams"]: outparams[parn] = paramset[parn]
                logger.log("Writing updated fontinfo.plist", "I")
                silfont.ufo.writeXMLobject(fontinfo, params=outparams,dirn=ufopath, filen="fontinfo.plist", exists=True, fobject=True)

def logchange(logger, logmess, key, old, new):
    oldstr = str(old) if len(str(old)) < 22 else str(old)[0:20] + "..."
    newstr = str(new) if len(str(new)) < 22 else str(new)[0:20] + "..."
    logmess = key + logmess
    if old is None:
        logmess = logmess + " New value: " + newstr
    else:
        if new is None:
            logmess = logmess + " Old value: " + oldstr
        else:
            logmess = logmess + " Old value: " + oldstr + ", new value: " + newstr
    logger.log(logmess, "I")
    # Extra verbose logging
    if len(str(old)) > 21 :
        logger.log("Full old value: " + str(old), "V")
    if len(str(new)) > 21 :
        logger.log("Full new value: " + str(new), "V")
    logger.log("Types: Old - " + str(type(old)) + ", New - " + str(type(new)), "V")


def cmd(): execute(None, doit, argspec)
if __name__ == "__main__": cmd()
