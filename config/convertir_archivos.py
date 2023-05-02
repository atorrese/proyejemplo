import os
''''import shutil
from asposecellscloud.apis.cells_api import CellsApi

cells_api = CellsApi(os.getenv('ProductClientId'), os.getenv('ProductClientSecret'))
file1 = cells_api.cells_workbook_put_convert_workbook("Book1.bmp", format="csv")
shutil.move(file1, "destFile.csv")'''

import jpype
import asposecells

jpype.startJVM()
from asposecells.api import Workbook

workbook = Workbook("input.csv")
workbook.save("Output.bmp")
jpype.shutdownJVM()