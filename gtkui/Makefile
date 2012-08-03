SHELL = /bin/sh

prefix = /usr/local
exec_prefix = ${prefix}

sharedir = /usr/local/share/fontforge
srcdir = .
top_srcdir = ..
top_builddir = ..

bindir = ${exec_prefix}/bin
libdir = ${exec_prefix}/lib
plugindir = $(sharedir)/plugins

LIBTOOL = $(SHELL) $(top_builddir)/libtool
CC = gcc
INSTALL = /usr/bin/install -c
INSTALL_DATA = ${INSTALL} -m 644

X_CFLAGS = 
X_LIBS = 
X_11LIB = -lXi -lX11
X_EXTRA_LIBS = 
X_PRE_LIBS =  -lSM -lICE  -lXft
STATIC_LIBS = 

ffgtk_OBJECTS = fontview.o startgtk.o uiutil.o cursors.o windowmenu.o prefs.o \
    openfontdlg.o stamp.o pythonui.o
gtk_widget_OBJECTS = gwwvmenubar.o gwwvask.o gwwvprogress.o
glade_OBJECTS = ff_interface.o support.o

_CFLAGS = -I$(top_srcdir)/inc -I../inc -I$(srcdir) -I$(top_srcdir) -Wmissing-prototypes -Wunused -Wimplicit -Wreturn-type -Wparentheses -Wformat -Wchar-subscripts $(X_CFLAGS) \
    -DHAVE_CONFIG_H '-DSHAREDIR="$(sharedir)"' -DLIBDIR='"$(libdir)"' \
     -I/usr/include/python2.6 '-DPREFIX="/usr/local"'
CFLAGS = -g -O2 -I/usr/include/freetype2/ -I/usr/include/freetype2 -I/usr/include/cairo -I/usr/include/pango-1.0 -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include -I/usr/src/freetype-2.4.9/src/truetype/ -I/usr/src/freetype-2.4.9/src/truetype//../../include -I/usr/src/freetype-2.4.9/src/truetype//../../include/freetype $(_CFLAGS) `pkg-config --cflags gtk+-2.0`
LDFLAGS =  -L/usr/local/lib
LIBS = -rpath $(libdir) ../libfontforge.la ../libgutils.la \
    ../libgunicode.la \
    `pkg-config --libs gtk+-2.0` `pkg-config --libs gmodule-2.0` \
    -liconv  /usr/lib/python2.6/config/libpython2.6.dll.a -lpthread -lintl $(STATIC_LIBS) -lm

all: fontforgegtk

fontforgegtk: $(ffgtk_OBJECTS) $(gtk_widget_OBJECTS) $(glade_OBJECTS) stubs.o
	$(LIBTOOL) --mode=link $(CC) -export-dynamic $(LDFLAGS) -o fontforgegtk \
		$(ffgtk_OBJECTS) $(gtk_widget_OBJECTS) $(glade_OBJECTS) stubs.o \
		`pkg-config --libs gtk+-2.0` `pkg-config --libs gmodule-2.0` $(LIBS)

#ff_interface.c: interface.c add-my-widgets.sed
#	sed -f add-my-widgets.sed < interface.c > ff_interface.c

%.o: %.c $(srcdir)../fontforge/splinefont.h $(srcdir)/viewsgtk.h  $(srcdir)/../fontforge/uiinterface.h $(srcdir)/../fontforge/fontforgevw.h
	$(CC) $(CFLAGS) -c $<

clean:
	-rm -f fontforgegtk
	-rm -f *.o
	-rm -rf .libs

distclean cleaner: clean
	-rm -f Makefile

install:
	mkdir -p $(sharedir)/pixmaps
	mkdir -p $(DESTDIR)$(bindir)
	-$(INSTALL_DATA) $(srcdir)/pixmaps/*.{png,xbm} $(sharedir)/pixmaps
	$(LIBTOOL) --mode=install $(INSTALL) -c fontforgegtk $(DESTDIR)$(bindir)
