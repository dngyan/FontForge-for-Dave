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
INSTALL = /usr/bin/install -c
CC = gcc

_CFLAGS = -I$(top_srcdir)/inc -I../inc -I$(srcdir) -I. -I$(top_srcdir)/fontforge \
    -Wmissing-prototypes -Wunused -Wimplicit -Wreturn-type -Wparentheses -Wformat -Wchar-subscripts $(X_CFLAGS) \
    -DHAVE_CONFIG_H '-DSHAREDIR="$(sharedir)"' -DLIBDIR='"$(libdir)"' \
     -I/usr/include/python2.6 '-DPREFIX="/usr/local"'
CFLAGS = -g -O2 -I/usr/include/freetype2/ -I/usr/include/freetype2 -I/usr/include/cairo -I/usr/include/pango-1.0 -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include -I/usr/src/freetype-2.4.9/src/truetype/ -I/usr/src/freetype-2.4.9/src/truetype//../../include -I/usr/src/freetype-2.4.9/src/truetype//../../include/freetype $(_CFLAGS)

LIBS = -rpath $(libdir)  -L/usr/lib -lm

PLUGINS = gb12345.la

all: $(PLUGINS)

clean:
	-rm -rf .libs *.la *.lo

distclean: clean
	-rm -rf Makefile

%.lo: %.c
	$(LIBTOOL) --mode=compile $(CC) $(CFLAGS) -c $<

%.la: %.lo
	$(LIBTOOL) --mode=link $(CC) -export-dynamic -module -o $@ $< $(LIBS)

install: all
	mkdir -p $(DESTDIR)$(plugindir)
	-mv .libs/*.{so,dll,dylib,lai}* $(DESTDIR)$(plugindir)
	mv *.la $(DESTDIR)$(plugindir)


