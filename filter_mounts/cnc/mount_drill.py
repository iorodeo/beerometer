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
        'layers'      : ['mount drill'],
        'dxfTypes'    : ['CIRCLE'],
        'startZ'      : 0.02,
        'stopZ'       : -0.60,
        'safeZ'       : 0.25,
        'stepZ'       : 0.05,
        'startDwell'  : 2.0,
        }
drill = cnc_dxf.DxfDrill(param)
prog.add(drill)

prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.End(),comment=True)
print(prog)
baseName, dummy = os.path.splitext(__file__)
fileName = '{0}.ngc'.format(baseName)
print(fileName)
prog.write(fileName)
