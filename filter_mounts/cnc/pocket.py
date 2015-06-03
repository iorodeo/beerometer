import os 
from py2gcode import gcode_cmd
from py2gcode import cnc_dxf

feedrate = 22.0
safeZ = 0.25
toolDiam = 3.0/16.0
fileName = 'filter_mount_array.dxf'
overlap = 0.5
overlapFinish = 0.6
maxCutDepth = 0.04
direction = 'ccw'
startDwell = 2.0

prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.FeedRate(feedrate))

param = {
        'fileName'       : fileName,
        'layers'         : ['resistor pocket'],
        'components'     : True,
        'depth'          : 0.25,
        'startZ'         : 0.0,
        'safeZ'          : safeZ,
        'overlap'        : overlap,
        'overlapFinish'  : overlapFinish,
        'maxCutDepth'    : maxCutDepth,
        'toolDiam'       : toolDiam,
        'cornerCut'      : False,
        'direction'      : direction,
        'startDwell'     : startDwell,
        }
pocket = cnc_dxf.DxfRectPocketFromExtent(param)
prog.add(pocket)


param = {
        'fileName'       : fileName,
        'layers'         : ['connector pocket'],
        'components'     : True,
        'depth'          : 0.6,
        'startZ'         : 0.0,
        'safeZ'          : safeZ,
        'overlap'        : overlap,
        'overlapFinish'  : overlapFinish,
        'maxCutDepth'    : maxCutDepth,
        'toolDiam'       : toolDiam,
        'cornerCut'      : False,
        'direction'      : direction,
        'startDwell'     : startDwell,
        }
pocket = cnc_dxf.DxfRectPocketFromExtent(param)
prog.add(pocket)


param = {
        'fileName'       : fileName,
        'layers'         : ['filter outer pocket'],
        'depth'          : 0.5,
        'startZ'         : 0.0,
        'safeZ'          : safeZ, 
        'overlap'        : overlap,
        'overlapFinish'  : overlapFinish,
        'maxCutDepth'    : maxCutDepth,
        'toolDiam'       : toolDiam,
        'direction'      : direction,
        'startDwell'     : startDwell,
        }
pocket = cnc_dxf.DxfCircPocket(param)
prog.add(pocket)

param = {
        'fileName'       : fileName,
        'layers'         : ['filter inner pocket'],
        'depth'          : 0.1,
        'startZ'         : -0.5,
        'safeZ'          : safeZ, 
        'overlap'        : overlap,
        'overlapFinish'  : overlapFinish, 
        'maxCutDepth'    : maxCutDepth,
        'toolDiam'       : toolDiam,
        'direction'      : direction,
        'startDwell'     : startDwell 
        }
pocket = cnc_dxf.DxfCircPocket(param)
prog.add(pocket)

param = {
        'fileName'       : fileName,
        'layers'         : ['led pocket'],
        'depth'          : 0.6,
        'startZ'         : 0,
        'safeZ'          : safeZ, 
        'overlap'        : overlap,
        'overlapFinish'  : overlapFinish,
        'maxCutDepth'    : maxCutDepth,
        'toolDiam'       : toolDiam,
        'direction'      : direction,
        'startDwell'     : startDwell,
        }
pocket = cnc_dxf.DxfCircPocket(param)
prog.add(pocket)

prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.End(),comment=True)
print(prog)
baseName, dummy = os.path.splitext(__file__)
fileName = '{0}.ngc'.format(baseName)
print(fileName)
prog.write(fileName)
