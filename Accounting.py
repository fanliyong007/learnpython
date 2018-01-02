# import xlrd
# data=xlrd.open_workbook("goal.xls")
# print(data.sheet_by_index(0).row_values(3))
# from docx import Document
# from docx.shared import Inches
# doc=Document()
# doc
from  docx import Document
doc=Document.open_workbook("source.docx")
print(doc.cell(1,1))