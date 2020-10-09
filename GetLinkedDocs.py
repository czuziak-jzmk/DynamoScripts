# Load the Python Standard and DesignScript Libraries
import sys
import clr
import os
clr.AddReference('ProtoGeometry')
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')
clr.AddReference('RevitNodes')
from Autodesk.Revit.DB import *
from Autodesk.DesignScript.Geometry import *
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
import Revit
clr.ImportExtensions(Revit.Elements)

filePath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
print filePath
# The inputs to this node will be stored as a list in the IN variables.
dataEnteringNode = IN

# Place your code below this line
doc = DocumentManager.Instance.CurrentDBDocument
category = BuiltInCategory.OST_RvtLinks
linkDoc = FilteredElementCollector(doc).OfCategory(category).WhereElementIsNotElementType().ToElements()
docs = []

for i in linkDoc:
	if not IN[0]: 
		bool = doc.GetElement(UnwrapElement(i).GetTypeId()).IsNestedLink

	link = UnwrapElement(i).GetLinkDocument()
	path = link.GetWorksharingCentralModelPath()
	if not docs.Contains(path) and not bool:
		docs.Add(path)
	if not docs.Contains(path) and IN[0]:
		docs.Add(path)

OUT = docs

