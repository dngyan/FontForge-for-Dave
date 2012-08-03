SHELL = /bin/sh

prefix = /usr/local
exec_prefix = ${prefix}

srcdir = .
top_srcdir = ..
top_builddir = ..

bindir = ${exec_prefix}/bin
libdir = ${exec_prefix}/lib

GD_VERSION=4
GD_REVISION=10
GD_AGE=0

LIBTOOL = $(SHELL) $(top_builddir)/libtool
CC = gcc

X_CFLAGS = 
X_LIBS = 
X_11LIB = -lXi -lX11
X_EXTRA_LIBS = 
X_PRE_LIBS =  -lSM -lICE  -lXft
STATIC_LIBS = 

libgdraw_OBJECTS =  choosericons.lo ctlvalues.lo drawboxborder.lo \
 gaskdlg.lo gbuttons.lo gcolor.lo gchardlg.lo gcontainer.lo gdraw.lo \
 gdrawbuildchars.lo gdrawerror.lo gdrawtxt.lo gdrawtxtinit.lo \
 gfilechooser.lo gfiledlg.lo ggadgets.lo ggroupbox.lo \
 gimageclut.lo gimagecvt.lo gimagepsdraw.lo \
 gimagewriteeps.lo gdrawgimage.lo \
 gimagexdraw.lo gkeysym.lo glist.lo \
 gmenu.lo gprogress.lo gpsdraw.lo gpstxtinit.lo gradio.lo gresource.lo \
 gresourceimage.lo gresedit.lo gsavefiledlg.lo gscrollbar.lo gtabset.lo \
 gtextfield.lo gtextinfo.lo gwidgets.lo gxdraw.lo gxcdraw.lo \
 ghvbox.lo gmatrixedit.lo gdrawable.lo gspacer.lo xkeysyms_unicode.lo

Incs = -I$(top_srcdir)/inc -I../inc -I/usr/pkg/include -I/usr/pkg/include/giflib
CFLAGS = -g -O2 -I/usr/include/freetype2/ -I/usr/include/freetype2 -I/usr/include/cairo -I/usr/include/pango-1.0 -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include -I/usr/src/freetype-2.4.9/src/truetype/ -I/usr/src/freetype-2.4.9/src/truetype//../../include -I/usr/src/freetype-2.4.9/src/truetype//../../include/freetype  -I/usr/include/python2.6 $(Incs) -Wmissing-prototypes -Wunused -Wimplicit -Wreturn-type -Wparentheses -Wformat -Wchar-subscripts $(X_CFLAGS) -DNOTHREADS -DHAVE_CONFIG_H -DLIBDIR='"$(libdir)"'

../libgdraw.la: $(libgdraw_OBJECTS)
	$(LIBTOOL) --mode=link $(CC) -no-undefined $(CFLAGS) -o ../libgdraw.la $(libgdraw_OBJECTS) \
	    ../libgutils.la ../libgunicode.la $(X_LIBS)  -L/usr/local/lib -liconv  /usr/lib/python2.6/config/libpython2.6.dll.a -lpthread -lintl \
	    $(STATIC_LIBS) $(X_PRE_LIBS) $(X_11LIB) $(X_EXTRA_LIBS)  \
	    -rpath $(libdir) -version-info $(GD_VERSION):$(GD_REVISION):$(GD_AGE)

%.lo: %.c

%.lo: %.c $(srcdir)/gdrawP.h $(srcdir)/ggadgetP.h $(srcdir)/gwidgetP.h $(srcdir)/gxdrawP.h $(srcdir)/fontP.h
	$(LIBTOOL) --mode=compile $(CC) $(CFLAGS) -c $<

clean:
	-rm -rf *.lo *.o .libs/* .libs ../libgdraw.la

distclean cleaner:
	-rm -rf *.lo *.o ../libgdraw.la .libs/* .libs Makefile
