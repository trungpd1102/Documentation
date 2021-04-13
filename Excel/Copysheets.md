Copy each sheet from sheets to a new excel file


VBA code:

'Code Created by Gitiho.com
Sub SplitEachWorksheet()
Dim FPath As String
FPath = Application.ActiveWorkbook.Path
Application.ScreenUpdating = False
Application.DisplayAlerts = False
For Each ws In ThisWorkbook.Sheets
ws.Copy
Application.ActiveWorkbook.SaveAs Filename:=FPath & "\" & ws.Name & ".xlsx"
Application.ActiveWorkbook.Close False
Next
Application.DisplayAlerts = True
Application.ScreenUpdating = True
End Sub


----Node: Unhide all sheets before run
