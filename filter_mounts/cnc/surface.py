"""
Notes: 

 May want to modifiy so that different stock thicknesses can be accomodated.
 The current assumptions are.

 Stock thickness 0.63" 
 Final part thickness 0.55"

"""
import os 
from py2gcode import gcode_cmd
from py2gcode import cnc_dxf




feedrate = 24.0

prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.FeedRate(feedrate))

param = {
        'fileName'       : 'filter_mount_array.dxf',
        'layers'         : ['surface mill'],
        'depth'          : 0.08,
        'startZ'         : 0.0,
        'safeZ'          : 0.25,
        'overlap'        : 0.4,
        'overlapFinish'  : 0.5,
        'maxCutDepth'    : 0.04,
        'toolDiam'       : 0.5,
        'cornerCut'      : False,
        'direction'      : 'ccw',
        'startDwell'     : 2.0,
        }
pocket = cnc_dxf.DxfRectPocketFromExtent(param)
prog.add(pocket)

prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.End(),comment=True)
print(prog)
baseName, dummy = os.path.splitext(__file__)
fileName = '{0}.ngc'.format(baseName)
print(fileName)
prog.write(fileName)
