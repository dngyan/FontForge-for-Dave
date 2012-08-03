#!/usr/local/bin/fontforge
#Needs: fonts/AddExtremaTest2.sfd

import fontforge;

font=fontforge.open("fonts/AddExtremaTest2.sfd");
font.selection.all();

for g in font.selection.byGlyphs :
  c = g.foreground[0];
  d = c.dup();
  if ( c!=d ) :
    raise ValueError, "Comparison doesn't work";
  d.addExtrema("only_good_rm",1000);
  if ( c != d ) :
    raise ValueError, "addExtrema perterbed things badly in " + g.glyphname;

c = font["A"].foreground[0];
d = font["B"].foreground[0];
if ( c==d ) :
  raise ValueError, "Comparison thinks everything is the same";
