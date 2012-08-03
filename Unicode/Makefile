SHELL = /bin/sh

prefix = /usr/local
exec_prefix = ${prefix}

top_srcdir = ..
top_builddir = ..
libdir = ${exec_prefix}/lib

bindir = ${exec_prefix}/bin

GU_VERSION=3
GU_REVISION=2
GU_AGE=0

LIBTOOL = $(SHELL) $(top_builddir)/libtool
CC = gcc

libgunicode_OBJECTS =  ArabicForms.lo alphabet.lo backtrns.lo char.lo \
 cjk.lo memory.lo ucharmap.lo unialt.lo ustring.lo utype.lo \
 usprintf.lo gwwiconv.lo

Incs = -I$(top_srcdir)/inc -I../inc -I/usr/pkg/include -I/usr/pkg/include/giflib
CFLAGS = -g -O2 -I/usr/include/freetype2/ -I/usr/include/freetype2 -I/usr/include/cairo -I/usr/include/pango-1.0 -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include -I/usr/src/freetype-2.4.9/src/truetype/ -I/usr/src/freetype-2.4.9/src/truetype//../../include -I/usr/src/freetype-2.4.9/src/truetype//../../include/freetype  -I/usr/include/python2.6 $(Incs) -Wmissing-prototypes -Wunused -Wimplicit -Wreturn-type -Wparentheses -Wformat -Wchar-subscripts -DHAVE_CONFIG_H

../libgunicode.la: $(libgunicode_OBJECTS)
	$(LIBTOOL) --mode=link $(CC) -no-undefined  -L/usr/local/lib -o ../libgunicode.la $(libgunicode_OBJECTS) \
	    -liconv  /usr/lib/python2.6/config/libpython2.6.dll.a -lpthread -lintl \
	    -rpath $(libdir) -version-info $(GU_VERSION):$(GU_REVISION):$(GU_AGE)

%.lo: %.c
	$(LIBTOOL) --mode=compile $(CC) $(CFLAGS) -c $<

clean:
	-rm -fr *.o *.lo ../libgunicode.la .libs/* .libs

distclean cleaner:
	-rm -f *.o *.lo ../libgunicode.la .libs/* .libs Makefile
