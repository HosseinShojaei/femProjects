# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2021 replay file
# Internal Version: 2020_03_06-18.20.37 167380
# Run by Administrator on Sun Nov 27 21:24:13 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=102.125, 
    height=145.724548339844)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('HosseinShojaeiFEM.cae')
#: The model database "D:\FEM\FEMproject(Hossein-Shojaei)\ABAQUS\HosseinShojaeiFEM.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['Truss_Part']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].setValues(displayedObject=None)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Job Job-1: Abaqus/Standard completed successfully.
#: Job Job-1 completed successfully. 
o3 = session.openOdb(
    name='D:/FEM/FEMproject(Hossein-Shojaei)/ABAQUS/Job-1.odb')
#: Model: D:/FEM/FEMproject(Hossein-Shojaei)/ABAQUS/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       4
#: Number of Node Sets:          15
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Max. In-Plane Principal'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='CF', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='DMENER', outputPosition=INTEGRATION_POINT, )
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['D:/FEM/FEMproject(Hossein-Shojaei)/ABAQUS/Job-1.odb'])
odb = session.odbs['D:/FEM/FEMproject(Hossein-Shojaei)/ABAQUS/Job-1.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='EE', outputPosition=INTEGRATION_POINT, refinement=(
    INVARIANT, 'Max. In-Plane Principal'), )
session.Path(name='Path-1', type=NODE_LIST, expression=(('TRUSS_PART-1', (4, 3, 
    )), ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='EE', outputPosition=INTEGRATION_POINT, refinement=(
    COMPONENT, 'EE11'))
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
pth = session.paths['Path-1']
xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=False, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
    projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE, 
    removeDuplicateXYPairs=True, includeAllElements=False)
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
session.viewports['Viewport: 1'].odbDisplay.setDeformedVariable(
    variableLabel='UT')
odb = session.odbs['D:/FEM/FEMproject(Hossein-Shojaei)/ABAQUS/Job-1.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
pth = session.paths['Path-1']
xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=False, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
    projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE, 
    removeDuplicateXYPairs=True, includeAllElements=False)
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
session.viewports['Viewport: 1'].odbDisplay.setDeformedVariable(
    variableLabel='U')
odb = session.odbs['D:/FEM/FEMproject(Hossein-Shojaei)/ABAQUS/Job-1.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
pth = session.paths['Path-1']
xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=False, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
    projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE, 
    removeDuplicateXYPairs=True, includeAllElements=False)
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
pth = session.paths['Path-1']
xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=False, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
    projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE, 
    removeDuplicateXYPairs=True, includeAllElements=False)
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='COORD', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'))
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
pth = session.paths['Path-1']
xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=False, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
    projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE, 
    removeDuplicateXYPairs=True, includeAllElements=False)
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Max. Principal'))
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
pth = session.paths['Path-1']
xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=False, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
    projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE, 
    removeDuplicateXYPairs=True, includeAllElements=False)
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='EE', outputPosition=INTEGRATION_POINT, refinement=(
    COMPONENT, 'EE11'))
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
pth = session.paths['Path-1']
xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=False, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
    projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE, 
    removeDuplicateXYPairs=True, includeAllElements=False)
c1 = session.Curve(xyData=xy1)
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
odb = session.odbs['D:/FEM/FEMproject(Hossein-Shojaei)/ABAQUS/Job-1.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='EE', outputPosition=INTEGRATION_POINT, refinement=(
    INVARIANT, 'Min. Principal'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='EE', outputPosition=INTEGRATION_POINT, refinement=(
    INVARIANT, 'Max. Principal (Abs)'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Max. In-Plane Principal'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='EE', outputPosition=INTEGRATION_POINT, refinement=(
    INVARIANT, 'Max. In-Plane Principal'), )
session.Path(name='Path-1', type=NODE_LIST, expression=(('TRUSS_PART-1', (4, 3, 
    )), ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=7373.88, 
    farPlane=12935.7, width=6099.72, height=3257.04, viewOffsetX=-118.94, 
    viewOffsetY=-155.601)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['D:/FEM/FEMproject(Hossein-Shojaei)/ABAQUS/Job-1.odb'])
odb = session.odbs['D:/FEM/FEMproject(Hossein-Shojaei)/ABAQUS/Job-1.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='TRIAX', outputPosition=INTEGRATION_POINT, )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='PEQC4', outputPosition=INTEGRATION_POINT, )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Max. In-Plane Principal'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='PS', outputPosition=INTEGRATION_POINT, refinement=(
    INVARIANT, 'Max. In-Plane Principal'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='TF', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='IE', outputPosition=INTEGRATION_POINT, refinement=(
    INVARIANT, 'Max. In-Plane Principal'), )
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
    'EEQUT', 'SE'))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Job Job-1: Abaqus/Standard completed successfully.
#: Job Job-1 completed successfully. 
o3 = session.openOdb(
    name='D:/FEM/FEMproject(Hossein-Shojaei)/ABAQUS/Job-1.odb')
#: Model: D:/FEM/FEMproject(Hossein-Shojaei)/ABAQUS/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       4
#: Number of Node Sets:          15
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
#* There is no valid step data available on the database. If the analysis is 
#* running, the database must be closed and reopened once the results have been 
#* initialized. The requested operation has been cancelled.
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
#* There is no valid step data available on the database. If the analysis is 
#* running, the database must be closed and reopened once the results have been 
#* initialized. The requested operation has been cancelled.
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
    'E', 'VE', 'PE', 'VEEQ', 'PEEQ', 'PEEQT', 'PEEQMAX', 'PEMAG', 'PEQC', 'EE', 
    'IE', 'THE', 'NE', 'LE', 'TE', 'TEEQ', 'TEVOL', 'EEQUT', 'ER', 'SE', 'SPE', 
    'SEPE', 'SEE', 'SEP', 'SALPHA'))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Job Job-1: Abaqus/Standard completed successfully.
#: Job Job-1 completed successfully. 
