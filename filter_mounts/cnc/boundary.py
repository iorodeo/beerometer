import os 
from py2gcode import gcode_cmd
from py2gcode import cnc_dxf

feedrate = 22.0

prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.FeedRate(feedrate))


param = {
        'fileName'    : 'filter_mount.dxf',
        'layers'      : ['boundary'],
        'depth'       : 0.6,
        'startZ'      : 0.0,
        'safeZ'       : 0.5,
        'toolDiam'    : 3.0/16.0,
        'direction'   : 'ccw',
        'cutterComp'  : 'outside',
        'maxCutDepth' : 0.04,
        'startDwell'  : 2.0,
        'startCond'   : 'minX',
        }
boundary = cnc_dxf.DxfBoundary(param)
prog.add(boundary)

prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.End(),comment=True)
print(prog)
baseName, dummy = os.path.splitext(__file__)
fileName = '{0}.ngc'.format(baseName)
print(fileName)
prog.write(fileName)
