SHELL = /bin/sh

prefix = /usr/local
exec_prefix = ${prefix}

srcdir = .
top_srcdir = ..
top_builddir = ..

bindir = ${exec_prefix}/bin
libdir = ${exec_prefix}/lib

GU_VERSION=1
GU_REVISION=3
GU_AGE=0

GFTP_VERSION=1
GFTP_REVISION=0
GFTP_AGE=0

LIBTOOL = $(SHELL) $(top_builddir)/libtool
CC = gcc

STATIC_LIBS = 

libgutils_OBJECTS = divisors.lo fsys.lo gcol.lo gimage.lo gimagereadbmp.lo \
 gimageread.lo gimagereadgif.lo gimagereadjpeg.lo gimagereadpng.lo \
 gimagereadras.lo gimagereadrgb.lo gimagereadtiff.lo gimagereadxbm.lo \
 gimagereadxpm.lo gimagewritebmp.lo gimagewritegimage.lo \
 gimagewritejpeg.lo gimagewritepng.lo gimagewritexbm.lo gimagewritexpm.lo \
 gwwintl.lo dynamic.lo \
 gio.lo giofile.lo giohosts.lo giomime.lo giothread.lo giotrans.lo
libgioftp_OBJECTS = gioftp.lo

Incs = -I$(top_srcdir)/inc -I../inc -I/usr/pkg/include -I/usr/pkg/include/giflib
CFLAGS = -g -O2 -I/usr/include/freetype2/ -I/usr/include/freetype2 -I/usr/include/cairo -I/usr/include/pango-1.0 -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include -I/usr/src/freetype-2.4.9/src/truetype/ -I/usr/src/freetype-2.4.9/src/truetype//../../include -I/usr/src/freetype-2.4.9/src/truetype//../../include/freetype  -I/usr/include/python2.6 $(Incs) -Wmissing-prototypes -Wunused -Wimplicit -Wreturn-type -Wparentheses -Wformat -Wchar-subscripts $(X_CFLAGS) -DNOTHREADS -DHAVE_CONFIG_H -DLIBDIR='"$(libdir)"'

both: ../libgutils.la ../libgioftp.la

../libgutils.la: $(libgutils_OBJECTS)
	$(LIBTOOL) --mode=link $(CC) -no-undefined $(CFLAGS)  -L/usr/local/lib -o ../libgutils.la $(libgutils_OBJECTS) \
	    ../libgunicode.la -liconv  /usr/lib/python2.6/config/libpython2.6.dll.a -lpthread -lintl \
	    $(STATIC_LIBS)  \
	    -rpath $(libdir) -version-info $(GU_VERSION):$(GU_REVISION):$(GU_AGE)

../libgioftp.la: $(libgioftp_OBJECTS)
	$(LIBTOOL) --mode=link $(CC) -no-undefined $(CFLAGS)  -L/usr/local/lib -o ../libgioftp.la $(libgioftp_OBJECTS) \
	    ../libgunicode.la -liconv  /usr/lib/python2.6/config/libpython2.6.dll.a -lpthread -lintl \
	    $(STATIC_LIBS)  \
	    -rpath $(libdir) -version-info $(GFTP_VERSION):$(GFTP_REVISION):$(GFTP_AGE)

%.lo: %.c
	$(LIBTOOL) --mode=compile $(CC) $(CFLAGS) -c $<

clean:
	-rm -fr *.lo *.o .libs/* .libs ../libgutils.la ../libgioftp.la

distclean cleaner:
	-rm -fr *.lo *.o ../libgutils.la Makefile ../libgioftp.la .libs/* .libs
