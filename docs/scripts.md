# Pysilfont commands and scripts

Below is a table listing all the commands installed by Pysilfont followed by descriptions of each command.

All these commands work in consistent ways in terms of certain standard options (eg -h for help) and default names for many files - see details in [Pysilfont Documentation](docs.md#standard-command-line-options).

There are further example scripts supplied with Pysilfont, and some of these are also [documented further down](#example-scripts)

## Table of scripts

| Command | Description |
| ------- | ----------- |
| [ffchangeglyphnames](#ffchangeglyphnames) | Update glyph names in a ttf font based on csv file |
| [ffcopyglyphs](#ffcopyglyphs) | Copy glyphs from one font to another, without using ffbuilder |
| [ffremovealloverlaps](#ffremovealloverlaps) | Remove overlap on all glyphs in a ttf font |
| [psfaddanchors](#psfaddanchors) | Read anchor data from XML file and apply to UFO |
| [psfbuildcomp](#psfbuildcomp) | Add composite glyphs to UFO based on a Composite Definitions file |
| [psfchangegdlnames](#psfchangegdlnames) | Change graphite names within GDL based on mappings files |
| [psfchangettfglyphnames](#psfchangettfglyphnames) | Change glyph names in a ttf from working names to production names |
| [psfcheckbasicchars](#psfcheckbasicchars) | Check UFO for glyphs that represent recommended basic characters |
| [psfcompdef2xml](#psfcompdef2xml) | Convert composite definition file to XML format |
| [psfcompressgr](#psfcompressgr) | Compress Graphite tables in a ttf font |
| [psfcopymeta](#psfcopymeta) | Copy basic metadata from one UFO to another, for fonts in related families |
| [psfcreateinstances](#psfcreateinstances) | Create one or more instance UFOs from one or more designspace files |
| [psfcsv2comp](#psfcsv2comp) | Create composite definition file from csv |
| [psfdeleteglyphs](#psfdeleteglyphs) | Deletes glyphs from a UFO based on a list |
| [psfexpandstroke](#psfexpandstroke) | Expand an unclosed UFO stroke font into monoline forms |
| [psfexportanchors](#psfexportanchors) | Export UFO anchor data to a separate XML file |
| [psfexportpsnames](#psfexportpsnames) | Export a map of glyph name to PS name to a csv file |
| [psfexportunicodes](#psfexportunicodes) | Export a map of glyph name to unicode value to a csv file |
| [psfftml2odt](#psfftml2odt) | Create a LibreOffice Writer file from an FTML test description |
| [psfglyphs2ufo](#psfglyphs2ufo) | Export all the masters in a .glyphs file to UFOs |
| [psfmakewoffmetadata](#psfmakewoffmetadata) | Make the WOFF metadata xml file based on input UFO and FONTLOG.txt |
| [psfnormalize](#psfnormalize) | Normalize a UFO and optionally converts it between UFO2 and UFO3 versions |
| [psfrenameglyphs](#psfrenameglyphs) | Within a UFO, assign new working names to glyphs based on csv input file |
| [psfsetassocfeat](#psfsetassocfeat) | Add associate feature info to glif lib based on a csv file |
| [psfsetassocuids](#psfsetassocuids) | Add associate UID info to glif lib based on a csv file |
| [psfsetglyphorder](#psfsetglyphorder) | Load glyph order data into public.glyphOrder based on a text file |
| [psfsetkeys](#psfsetkeys) | Set key(s) with given value(s) in a UFO p-list file |
| [psfsetpsnames](#psfsetpsnames) | Add public.postscriptname to glif lib based on a csv file |
| [psfsetunicodes](#psfsetunicodes) | Set unicode values for a glif based on a csv file |
| [psfsetversion](#psfsetversion) | Change all the version-related info in a UFO's fontinfo.plist |
| [psfsubset](#psfsubset) | Create a subset of an existing UFO |
| [psfsyncmeta](#psfsyncmeta) | Copy basic metadata from one member of a font family to other family members |
| [psfsyncmasters](#psfsyncmasters) | Sync metadata in master UFO files based on a Designspace file |
| [psftoneletters](#psftoneletters) | Add Latin script tone letters (pitch contours) to a UFO |
| [psfufo2ttf](#psfufo2ttf) | Generate a ttf file without OpenType tables from a UFO |
| [psfxml2compdef](#psfxml2compdef) | Convert composite definition file from XML format |

---
#### ffchangeglyphnames
Usage: **`ffchangeglyphnames [-i INPUT] [--reverse] ifont [ofont]`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

Update the glyph names in a ttf font based on csv file.

Example usage:

```
ffchangeglyphnames -i glyphmap.csv font.ttf
```
will update the glyph names in the font based on mapping file glyphmap.csv

If \-\-reverse  is used, it change names in reverse.

---
####  ffcopyglyphs
Usage: **`ffcopyglyphs -i INPUT [-r RANGE] [--rangefile RANGEFILE] [-n NAME] [--namefile NAMEFILE] [-a] [-f] [-s SCALE] ifont [ofont]`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

_This section is Work In Progress!_

optional arguments:

```
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Font to get glyphs from
  -r RANGE, --range RANGE
                        StartUnicode..EndUnicode no spaces, e.g. 20..7E
  --rangefile RANGEFILE
                        File with USVs e.g. 20 or a range e.g. 20..7E or both
  -n NAME, --name NAME  Include glyph named name
  --namefile NAMEFILE   File with glyph names
  -a, --anchors         Copy across anchor points
  -f, --force           Overwrite existing glyphs in the font
  -s SCALE, --scale SCALE
                        Scale glyphs by this factor
```

---
#### ffremovealloverlaps
Usage: **`ffremovealloverlaps ifont [ofont]`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

Remove overlap on all glyphs in a ttf font

---
####  psfaddanchors
Usage: **`psfaddanchors [-i ANCHORINFO]  [-a] [-r {X,S,E,P,W,I,V}] ifont [ofont]`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

_This section is Work In Progress!_

Read anchor data from XML file and apply to UFO

optional arguments:

```
  -i ANCHORINFO, --anchorinfo ANCHORINFO
                        XML file with anchor data
  -a, --analysis        Analysis only; no output font generated  
  -r {X,S,E,P,W,I,V}, --report {X,S,E,P,W,I,V}
                        Set reporting level for log file
```

---

####  psfbuildcomp
Usage: **`psfbuildcomp [-i CDFILE] [-a] [-f] [-r {X,S,E,P,W,I,V}] ifont [ofont]`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

Creates or updates composite glyphs in a UFO based on an external text file of definitions. The syntax for these definitions is described in [composite.md](composite.md).

Example usage:

```
psfbuildcomp -i composites.txt font.ufo
psfbuildcomp -i newcomps.txt -f -r V Andika-BoldItalic.ufo Andika-BoldItalic.ufo
```

optional arguments:

```
  -i CDFILE, --cdfile CDFILE
                        Composite Definitions input file
  -a, --analysis        Analysis only; no output font generated
  -f, --force           Force overwrite of glyphs having outlines
  -r {X,S,E,P,W,I,V}, --report {X,S,E,P,W,I,V}
                        Set reporting level for log
```

---
#### psfchangegdlnames
Usage: **`psfchangegdlnames [-n NAMES] [--names2 [NAMES2]] [--psnames PSNAMES] input [output]`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

Changes the graphite names within GDL files(s) based on mappings file(s). It can work on an individual file or on all the gdl/gdh files within a folder. It also updates postscript names in postscript() statements

Two mappings files are required (NAMES and PSNAMES).  Optionally a second GDL names mapping file, NAMES2 can be supplied.

The mapping files are csv files of the format `"old name,new name"`. It logs if any graphite names are in the GDL but not found in the mapping files.

Example usage:

```
psfchangegdlnames -n gdlmap.csv --psnames psnames.csv source/graphite
```
will update all the .gdl and.gdh files within the source/graphite folder.

---
#### psfchangettfglyphnames
Usage: **`psfchangettfglyphnames iufo ittf ottf`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

Used to change the glyph names in a ttf from working names to production names, typically as the last step in a build sequence.

The name map is obtained from the `public.postscriptNames` attribute in the input UFO and then applied to the input ttf to create the output ttf.

Example usage:

```
psfchangettfglyphnames source/Harmattan-Regular.ufo results/in.ttf results/out.ttf
```

---
#### psfcheckbasicchars
Usage: **`psfcheckbasicchars ufo`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

Used to check a UFO for the presence of glyphs that represent the characters in the list of [Recommended characters for Non-Roman fonts](http://scriptsource.org/entry/gg5wm9hhd3). Any missing characters are noted in the resulting log file along with the recommended AGL glyph name.

Example usage:

```
psfcheckbasicchars Nokyung-Regular.ufo
```

---
#### psfcompdef2xml
Usage: **`psfcompdef2xml [-p PARAMS] input output log`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

Convert composite definition file from XML format

_This section is Work In Progress!_

  input                 Input file of CD in single line format
  output                Output file of CD in XML format
  log                   Log file

  -p PARAMS, --params PARAMS
                        XML formatting parameters: indentFirst, indentIncr,
                        attOrder

 Defaults    
    output              \_out.xml
    log                 \_log.txt

---
#### psfcompressgr
Usage: **`psfcompressgr ifont [ofont]`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

Compress Graphite tables in a font

---
####  psfcopymeta
Usage: **`psfcopymeta [-r] fromfont tofont`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

This copies selected fontlist.plist and lib.plist metadata (eg copyright, openTypeNameVersion, decender) between fonts in different (related) families.

It is usually run against the master (regular) font in each family then data synced within family afterwards using [psfsyncmeta](#psfsyncmeta).

Example usage:

```
psfcopymeta GentiumPlus-Regular.ufo GentiumBookPlus-Bold
```

If run with -r or \-\-reportonly it just reports what values would be updated.

Look in psfcopymeta.py for a full list of metadata copied.  Note that only fontinfo.plist and lib.plist are updated; the target font is not normalized.

Also psfcopymeta does not use Pysilfont's backup mechanism for fonts.

---
#### psfcreateinstances
Usage:

**`psfcreateinstances -f [--roundInstances] designspace_file_or_folder`**

**`psfcreateinstances [-i INSTANCENAME] [-a INSTANCEATTR] [-v INSTANCEVAL] [-o OUTPUT]
[--forceInterpolation] [--roundInstances] designspace_file`**


Create one or more instance UFOs from one or more designspace files.

There are two modes of operation, differentiated by the `-f` (folder) option:

When `-f` is specified:
- the final parameter can be either:
  - a single designspace file
  - a folder, in which case all designspace files within the folder are processed.
- all instances specified in the designspace file(s) are created.
- interpolation is always done, even when the designspace coordinates of an instance match a master.

Omitting the `-f` requires that the final parameter be a designspace file (not a folder) but gives more control over instance creation, as follows:

- Specific instance(s) to be created can be identified by either:
  - instance name, specified by `-i`, or
  - a point on one of the defined axes, specified by `-a` and `-v`. If more than one instance matches this axis value, all are built.
- The default location for the generated UFO(s) can be changed using `-o` option to specify a path to be prefixed to that specified in the designspace.
- In cases where the designspace coordinates of an instance match a master, glyphs will be copied rather than interpolated, which is useful for masters that do not have compatible glyph designs and thus cannot be interpolated. This behavior can be overridden using the `--forceInterpolation` option.  

Whenever interpolation is done, the calculations can result in non-integer values within the instance UFOs. The `--roundInstances` option will apply integer rounding to all such values.

---
#### psfcsv2comp
Usage: **`psfcsv2comp [-i INPUT] [--gname GNAME] [--base BASE] [--anchors ANCHORS] [--usv USV] output.txt`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

Create a composite definitions file based on data extracted from a csv file.

The INPUT csv file must have column headers and must include columns for the following data:
- the name of the composite glyph
- the name of the base glyph used to create the composites
- one column for each possible anchor to which a component can be attached. The column headers identify the name of the anchor to be used, and the column content names the glyph (if any) to be attached at that anchor.

Optionally, another column can be used to specify the USV (codepoint) for the composite.

Command-line options:

- INPUT: Name of input csv file (default `glyph_data.csv`)
- GNAME:  the column header for the column that contains the name of the composite glyph (default `gname`)
- BASE: the column header for the column that contains the base of the composites (default `base`)
- ANCHORS: comma-separated list of column headers naming the attachment points (default `above,below`).
- USV: the column header for the column that contains hexadecimal USV

**Limitations:** At present, this tool supports only a small subset of the capabilities of composite definition syntax. Note, in particular, that it assumes all components are attached to the _base_ rather than the _previous glyph_.

---
####  psfdeleteglyphs
Usage: **`psfdeleteglyphs [-i DELETELIST] [--reverse] infont [outfont]`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

This deletes glyphs in a UFO based on an external file with one glyphname per line. The `--reverse` option will instead delete all glyphs in the UFO that are not in the list. it does not analyze composites, so be careful not to delete glyphs that are referenced as components in other glyphs.

The following example will delete all glyphs that are _not_ listed in `keepthese.txt`:

```
psfdeleteglyphs Andika-Regular.ufo -i keepthese.txt --reverse
```

---
#### psfexpandstroke

Usage: **`psfexpandstroke infont outfont expansion`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

Expands the outlines (typically unclosed) in an UFO stroke font into monoline forms with a fixed width.

Example that expands the stokes in a UFO font `SevdaStrokeMaster-Regular.ufo` by 13 units on both sides, giving them a total width of 26 units, and writes the result to `Sevda-Regular.ufo`.

```
psfexpandstroke SevdaStrokeMaster-Regular.ufo Sevda-Regular.ufo 13
```

Note that this only expands the outlines - it does not remove any resulting overlap.


---
####  psfexportanchors
Usage: **`psfexportanchors [-r {X,S,E,P,W,I,V}]  [-g] [-s] ifont [output]`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

This exports anchor data from a UFO font to an XML file. (An "anchor" is also called an "attachment point" which is sometimes abbreviated to "AP".)

Example that exports the anchors contained in the UFO font `CharisSIL-Regular.ufo`, sorts the resulting glyph elements by name (PSName) rather than glyph ID (GID), and writes them to an XML file `CharisSIL-Regular_ap.xml`.

```
psfexportanchors -s font-charis/source/CharisSIL-Regular.ufo CharisSIL-Regular_ap.xml
```

If the command line includes

- -g, then the GID attribute will be present in the glyph element.
- -s, then the glyph elements will be sorted by PSName attribute (rather than by GID attribute).
- -u, then the UID attribute will include a "U+" prefix

---
####  psfexportpsnames
Usage: **`psfexportpsnames [-o OUTPUT] [--nocomments] ifont`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

Export a mapping of glyph name to postscript name to a csv file, format "glyphname,postscriptname"

It includes comments at the start saying when it was run etc unless \-\-nocomments is specified

---
####  psfexportunicodes
Usage: **`psfexportunicodes  [-o OUTPUT] [--nocomments] ifont`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

Export a mapping of glyph name to unicode to a csv file, format "glyphname,unicode" for glyphs that have a defined unicode. Does not support double-encoded glyphs.

It includes comments at the start saying when it was run etc unless \-\-nocomments is specified

---
#### psfftml2odt
Usage: **`psfftml2odt [-f FONT] input [output]`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

This creates a LibreOffice writer document based on input test data in [Font Test Markup Language](https://github.com/silnrsi/ftml) format and font information specified with command line parameters.

Example that uses FTML input contained in the file `test-ss.xml` and creates a LibreOffice writer document named `test-ss.odt`. There will be two columns in the output document, one for the installed font `Andika New Basic` and one for the font contained in the file `AndikaNewBasic-Regular.ttf`. (This compares a newly built font with an installed reference.)

```
psfftml2odt -f "Andika New Basic" -f "AndikaNewBasic-Regular.ttf" test-ss.xml test-ss.odt
```

If the font specified with the -f parameter contains a '.' it is assumed to be a file name, otherwise it is assumed to be the name of an installed font. In the former case, the font is embedded in the .odt document, in the latter case the font is expected to be installed on the machine that views the .odt document.

---
####  psfglyphs2ufo
Usage: **`psfglyphs2ufo [--nofixes] [--nofea] fontfile.glyphs masterdir`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

Exports one UFO file per master found in the fontfile.glyphs file, and places it in the directory specified as masterdir.

In a round-trip ufo -> glyphs -> ufo there is currently there is some data loss in the standard glyphs -> ufo conversion, so (unless `--nofixes` is set) the script fixes some data and restores some fields from the original ufos if they are present in the masterdir.

Currently features.fea does not round-trip sucessfully, so `--nofea` can be used to suppress the production of a features.fea file.

Example usage:

```
psfglyphs2ufo CharisSIL-RB.glyphs masterufos
```

If this Glyphs file contains two masters, Regular and Bold, then it will export a UFO for each into a 'masterufos' directory. To have the fonts exported to the current directory, give it a blank directory name:

```
psfglyphs2ufo CharisSIL-RB.glyphs ""
```
---
#### psfmakewoffmetadata
Usage: **`psfmakewoffmetadata -n PRIMARYFONTNAME -i ORGID [-f FONTLOG]  [-o OUTPUT] fontfile.ufo`**


Make the WOFF metadata xml file based on input UFO and FONTLOG.txt.

The primary font name and orgid need to be supplied on the command line. By default it reads FONTLOG.txt from the folder it is run in and outputs to *primaryfontname*-WOFF-metadata.xml.

Example:

```
psfmakewoffmetadata -n "Nokyung" -i "org.sil.fonts" source/Nokyung-Regular.ufo
```

It constructs the information needed from:

- The supplied primary font name and orgid
- Information within the primary font file
- Information within the FONTLOG.txt

FONTLOG.txt needs to be formatted according to the pattern used for most SIL font packages. The description in the xml file is created using the contents of the FONTLOG, starting after the "Basic Font Information" header and finishing before the "Information for Contributors" header (if present) or the "Acknowledgements" header otherwise. The credits are created from the N:, W:, D: and E: sets of values in the acknowledgements section, though E: is not used. One credit is created from each set of values and sets should be separated by blank lines.

---
####  psfnormalize
Usage: **`psfnormalize [-v VERSION] ifont [ofont]`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

This normalizes a UFO font (and optionally converts from one version to another if -v is specified). _Note that most pysilfont scripts automatically output normalized UFOs, so psfnormalize is normally only needed after fonts have been processed by external font tools._

Example that normalizes the named font:

```
psfnormalize Nokyung-Regular.ufo
```

The normalization follows the [default behaviours](docs.md#normalization), but these can be overridden using [custom parameters](parameters.md)

If you are a macOS user, see _pysilfont/actionsosx/README.txt_ to install an action that will enable you to run psfnormalize without using the command line.

---
####  psfrenameglyphs
Usage: **`psfrenameglyphs [--mergecomps] -i INPUT ifont [ofnt]`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

Within a UFO, assign new working names to glyphs based on csv input file, format "oldname,newname". The algorithm will handle circular rename specifications such as:
```
glyph1,glyph2
glyph2,glyph1
```
Unless default value for `renameGlyphs` [parameter](parameters.md) is overridden, the .glif filenames in the UFO will also be adjusted.

This program modifies the glyphs themselves and, if present in lib.plist, the `public.glyphOrder`,  `com.schriftgestaltung.glyphOrder` and `public.postscriptNames` definitions. Any composite glyphs that reference renamed glyphs are adjusted accordingly.

In normal usage, all oldnames and all newnames mentioned in the csv must be unique. The `--mergecomps` option enables special processing that allows newnames to occur more than once in the csv, with the result that the first mention is a normal rename while subsequent mentions indicate glyphs that should be deleted but any references updated to the first (renamed) glyph. Any moving anchors (i.e., those whose names start with `_`) on the deleted glyphs will be copied to the first glyph. For example:
```
dotabove,dot1      # this glyph has _above anchor
dotbelow,dot1      # this glyph has _below anchor
dotcenter,dot1     # this glyph has _center anchor
```
would cause `dotabove` to be renamed `dot1` while `dotbelow` and `dotabove` would be deleted. Any composite glyphs that reference any of `dotabove`, `dotbelow`, or `dotcenter` will be adjusted to refer to `dot1`. The `_below` anchor from `dotbelow` and the `_center` anchor from `dotcenter` will be copied to `dot1` (overwriting any anchors by the same names).

---
####  psfsetassocfeat
Usage: **`psfsetassocfeat [-i INPUT] ifont [ofont]`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

Add associate feature info to  org.sil.assocFeatureValue glif lib based on a csv file, format "glyphname,featurename[,featurevalue]"

---
####  psfsetassocuids
Usage: **`psfsetassocuids [-i INPUT] ifont [ofont]`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

Add associate UID info to org.sil.assocUIDs in glif lib based on a csv file - could be one value for variant UIDs and multiple for ligatures,   format "glyphname,UID[,UID]"

---
####  psfsetglyphorder
Usage: **`psfsetglyphorder [--gname GNAME] [--header HEADER] [--field FIELD] [-i INPUT] ifont [ofont]`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

From the INPUT file, load `public.glyphOrder` in lib.plist to control the order of glyphs in generated TTF files. FIELD can be used to specify a different order to load, such as `com.schriftgestaltung.glyphOrder`.

The input file can be in one of two formats:
- Plain text file with one glyph name per line in the desired order
- csv file with headers using glyph_name and sort_final columns

With the csv file:
- The glyph names are sorted by the values in the sort_final column, which can be integer or real. HEADER can be used to specify alternate column header to sort_final.  Multiple comma-separated values can be used with `--header` and `--field` to update two or more orders in a single command call.
- GNAME can be used to specify column header to use instead of glyph_name.

---
####  psfsetkeys
Usage: **`psfsetkeys [--plist PLIST] [-i INPUT] [-k KEY] [-v VALUE] ifont [ofont]`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

Set keys in a UFO p-list file.
A single key can be set by specifying KEY and VALUE.
Multiple keys can be set using a csv INPUT file, format "key,value".

PLIST selects which p-list to modify.
If not specified defaults to `fontinfo` which means the `fontinfo.plist` file is modified.

Example:

Set a key in the file `lib.plist`.
```
psfsetkeys --plist lib -k com.schriftgestaltung.width -v Regular font.ufo
```

---
####  psfsetpsnames
Usage: **`psfsetpsnames [--gname GNAME] [-i INPUT] ifont [ofont]`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

From the INPUT file, load `public.postscriptName` in lib.plist to specify final production names for glyphs.

The input file can be in one of two formats:
- simple csv in form glyphname,postscriptname
- csv file with headers using glyph_name and ps_name columns

With the csv file, GNAME can be used to specify column header to use instead of glyph_name.

---
####  psfsetunicodes
Usage: **`psfsetunicodes [-i INPUT] ifont [ofont]`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

Set the unicodes of glyphs in a font based on a csv file. With no header row, the csv format is assumed to be "glyphname,UID", otherwise column headers `glyph_name` and `USV` are used. Unicode values must be hex digits with no prefix.

The input font may have any number of Unicode values associated with any glyph. In the case that there is exactly one for a specific glyph, then the first time that glyph appears in the csv, that Unicode value will be replaced. In subsequent mentions of that glyph, or if there are already more than one Unicode values associated with a glyph, new values are simply appended.

When replacing or adding a Unicode value, any other glyph that has that same Unicode value will have it removed.

---
####  psfsetversion
Usage: **`psfsetversion font [newversion]`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

This updates the various font version fields based on 'newversion' supplied which may be:

- Full openTypeNameVersion string, except for the opening “Version “ text, eg “1.234 beta2”
- +1 to increment to the patch version number - see below
- not supplied, in which case the current values will be validated and existing openTypeNameVersion string displayed

It will update the openTypeNameVersion, versionMajor and versionMinor fields. It works assuming that openTypeNameVersion is of the form:

"Version M.mpp" or "Version M.mpp extrainfo", eg "Version 1.323 Beta2"


Based on [FDBP](https://silnrsi.github.io/FDBP/en-US/Versioning.html), the version number is parsed as M.mpp where M is major, m is minor and pp is patch number.  M matches the versionMajor and mpp the versionMinor fields.

Incrementing will fail if either the openTypeNameVersion is not formatted correctly or the version numbers in there don’t match those in versionMajor and versionMinor.

Examples of usage:

```
psfsetversion font.ufo "1.423"
```

will set:

- openTypeNameVersion to "Version 1.423"
- versionMajor to 1
- versionMinor to 423

`psfsetversion font.ufo +1`

If values were originally as in the first example, openTypeNameVersion will be changed to "Version 1.424" and versionMinor to 424

Note that only fontinfo.plist is updated, so the font is not normalized and Pysilfont's backup mechanism for fonts is not used.

---
#### psfsubset
Usage: **`psfsubset -i INPUT [--header HEADER] ifont ofont`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

This script writes an output UFO that is a subset of the input UFO. The subset contains only the glyphs identified in the INPUT file (plus any components needed for them).

The INPUT file can be a plain text file (one glyph per line) or a csv file. In the case of csv, the HEADER parameter is used to indicate which column from the csv to use (default is `glyph_name`).

Glyphs can be identified either by their name or the Unicode codepoint (USV). Glyph names and USVs can be intermixed in the list: anything that is between 4 and 6 hexadecimal digits is first processed as a USV and then, if there is no glyph encoded with that USV, processed as a glyph name.

Glyph orders and psname mappings, if present in the font, are likewise subsetted.

---
####  psfsyncmeta
Usage: **`psfsyncmeta [-s] [-m [MASTER]] [-r] [-n] [--normalize] ifont`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

Verifies and synchronises some fontinfo.plist and lib.plist metadata across a family of fonts.  By default it uses the regular font as the master and updates any other fonts that exist assuming standard name endings of -Regular, -Italic, -Bold and -BoldItalic.  Optionally a single font file can be synced against any other font as master, regardless of file naming.

Example usage for family of fonts:

```
psfsyncmeta CharisSIL-Regular.ufo
```

This will sync the metadata in CharisSIL-Italic, CharisSIL-Bold and CharisSIL-BoldItalic against values in CharisSIL-Regular.  In addition it will verify certain fields in all fonts (including Regular) are valid and follow [FDBP](https://silnrsi.github.io/FDBP/en-US/index.html) best-practice standards.

Example usages for a single font:

```
psfsyncmeta -s font-Italic.ufo
psfsyncmeta -s font-Italic.ufo -m otherfont.ufo
```
The first will sync font-Italic against font-Regular and the second against otherfont.

Look in psfsyncmeta.py for a full details of metadata actions.

Note that by default only fontinfo.plist and lib.plist are updated, so fonts are not normalized.  Use \-\-normalize to additionally normalize all fonts in the family.

Also psfsyncmeta does not use Pysilfont's backup mechanism for fonts.

-n (--new) appends \_new to ufo and file names for testing purposes

---
####  psfsyncmasters
Usage: **`psfsyncmasters primaryds [secondds] [-n]`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

Synchronises some fontinfo.plist and lib.plist metadata across a family of fonts based
on a designspace file. It looks in the designspace file for a master with `info copy="1"` set then syncs the values from that master to other masters defined in the file.

If a second designspace file is supplied, it also syncs to masters found in there (not yet tested!)

Example usage:

```
psfsyncmasters CharisSIL.designspace
```

Note that only fontinfo.plist and lib.plist files are updated, so fonts are not normalized and Pysilfont's backup mechanism for fonts is not used.

-n (--new) appends \_new to ufo and file names for testing purposes


---
####  psftoneletters
Usage: **`psftoneletters infont outfont`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

This uses the parameters from the UFO lib.plist org.sil.lcg.toneLetters key to create Latin script tone letters (pitch contours).

Example usage:

```
psftoneletters Andika-Regular.ufo Andika-Regular.ufo
```

---
#### psfufo2ttf
Usage: **`psfufo2ttffont ...`**

To be documented

---
#### psfxml2compdef
Usage: **`psfxml2compdef input output`**

_([Standard options](docs.md#standard-command-line-options) also apply)_

Convert composite definition file from XML format

_This section is Work In Progress!_

- input                 Input file of CD in XML format
- output                Output file of CD in single line format

---

## Example Scripts

When Pysilfont is downloaded, there are example scripts in pysilfont/examples.  These are a mixture of scripts that are under development, scripts that work but would likely need amending for a specific project's need and others that are just examples of how things could be done.

Some are documented below; for others just read the scripts!

_This section is Work In Progress!_
