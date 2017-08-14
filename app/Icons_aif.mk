ifeq (WINS,$(findstring WINS, $(PLATFORM)))
ZDIR=\epoc32\release\$(PLATFORM)\$(CFG)\Z
else
ZDIR=\epoc32\data\z
endif

TARGETDIR=$(ZDIR)\SYSTEM\APPS\PYTHON
ICONTARGETFILENAME=$(TARGETDIR)\PYTHON_AIF.MIF

do_nothing :
	@rem do_nothing

MAKMAKE : do_nothing

BLD : do_nothing

CLEAN : do_nothing

LIB : do_nothing

CLEANLIB : do_nothing

#
# Modify:
#  /c8,8 python_logo.svg
# to
#  /c8,8 /Hpython_aif.mbg python_logo.svg 
# to generate index header file
#
RESOURCE :
	mifconv $(ICONTARGETFILENAME) \
		/c8,8 python_logo.svg

FREEZE : do_nothing

SAVESPACE : do_nothing

RELEASABLES :
	@echo $(ICONTARGETFILENAME)

FINAL : do_nothing
