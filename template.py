from Autodesk.Revit.DB import *
from Autodesk.DesignScript.Geometry import *
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
import sys
import clr
clr.AddReference('RevitAPI')
clr.AddReference('ProtoGeometry')
clr.AddReference('RevitServices')

doc = DocumentManager.Instance.CurrentDBDocument
dataEnteringNode = IN

OUT = 0
