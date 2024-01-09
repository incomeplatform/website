from django.db import models

class Spreadsheet(models.Model):
    title = models.CharField(max_length=255)

class Row(models.Model):
    spreadsheet = models.ForeignKey(Spreadsheet, on_delete=models.CASCADE)
    row_number = models.IntegerField()

class Column(models.Model):
    spreadsheet = models.ForeignKey(Spreadsheet, on_delete=models.CASCADE)
    col_name = models.TextField()

class Cell(models.Model):
    spreadsheet = models.ForeignKey(Spreadsheet, on_delete=models.CASCADE)  # Add this line
    row = models.ForeignKey(Row, on_delete=models.CASCADE)
    col = models.ForeignKey(Column, on_delete=models.CASCADE)
    # No value field
