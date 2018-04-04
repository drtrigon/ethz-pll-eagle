import subprocess
import zipfile
import os

EAGLE = "C:\\Program Files\\EAGLE-7.5.0\\bin\\eagle.exe"

outputfile = "H:\\My Documents\\eagle\\projects\\Blattdurchmesser\\Blattdurchmesser-gerber"
board = "H:\\My Documents\\eagle\\projects\\Blattdurchmesser\\Blattdurchmesser.brd"
#schem = "H:\\My Documents\\eagle\\projects\\Blattdurchmesser\\Blattdurchmesser.sch"

#dev = "-dGERBER_RS274X"
dev = "-dGERBER_RS274X_26"
#bom = "C:\\Program Files\\EAGLE-7.5.0\\ulp\\bom.ulp"

def run(args):
    print( args )
    print( subprocess.check_output(args) )

print("GERBER_RS274X CONTAINS: cmp, sol, plc, stc, sts")
print("GERBER_RS274X_26 CONTAINS: cmp, sol, mil, plc, stc, sts, crc, dpv, drh")

# http://www.rocketnumbernine.com/2011/12/14/automating-gerbers-from-eagle
run([EAGLE, "-X", dev, "-o%s.cmp" % outputfile, board, "Top", "Pads", "Vias"])
run([EAGLE, "-X", dev, "-o%s.sol" % outputfile, board, "Bottom", "Pads", "Vias"])
run([EAGLE, "-X", dev, "-o%s.mil" % outputfile, board, "Milling"])  # GERBER_RS274X_26 only
run([EAGLE, "-X", dev, "-o%s.plc" % outputfile, board, "Dimension", "tPlace", "tNames"])
run([EAGLE, "-X", dev, "-o%s.stc" % outputfile, board, "tStop"])
run([EAGLE, "-X", dev, "-o%s.sts" % outputfile, board, "bStop"])
run([EAGLE, "-X", dev, "-o%s.crc" % outputfile, board, "tCream"])   # GERBER_RS274X_26 only
run([EAGLE, "-X", dev, "-o%s.dpv" % outputfile, board, "Drills"])   # GERBER_RS274X_26 only
run([EAGLE, "-X", dev, "-o%s.drh" % outputfile, board, "Holes"])    # GERBER_RS274X_26 only

run([EAGLE, "-X", "-dEXCELLON", "-o%s.drd" % outputfile, board, "Drills", "Holes"])

with zipfile.ZipFile("%s.zip" % outputfile, 'w') as myzip:
    myzip.write("%s.cmp" % outputfile, os.path.basename("%s.cmp" % outputfile))
    myzip.write("%s.sol" % outputfile, os.path.basename("%s.sol" % outputfile))
    myzip.write("%s.mil" % outputfile, os.path.basename("%s.mil" % outputfile))
    myzip.write("%s.plc" % outputfile, os.path.basename("%s.plc" % outputfile))
    myzip.write("%s.stc" % outputfile, os.path.basename("%s.stc" % outputfile))
    myzip.write("%s.sts" % outputfile, os.path.basename("%s.sts" % outputfile))
    myzip.write("%s.crc" % outputfile, os.path.basename("%s.crc" % outputfile))
    myzip.write("%s.dpv" % outputfile, os.path.basename("%s.dpv" % outputfile))
    myzip.write("%s.drh" % outputfile, os.path.basename("%s.drh" % outputfile))
    myzip.write("%s.drd" % outputfile, os.path.basename("%s.drd" % outputfile))

# TODO: compare files against files created manually by standard procedure in eagle (clicking through dialogs)

#print( "" )
#run([EAGLE, '-S', bom, schem])  # not working!
#run([EAGLE, '-C', "RUN bom.ulp; QUIT;", schem])  # does not recognize file (schematic)

#print( "" )
#run([EAGLE, '-C', "ERC; DRC;", board])  # does not recognize file (board)
