from django.contrib import admin
from .models import Spreadsheet, Row, Column, Cell

class CellInline(admin.TabularInline):
    model = Cell
    extra = 1

class RowInline(admin.TabularInline):
    model = Row
    extra = 1

class ColumnInline(admin.TabularInline):
    model = Column
    extra = 1

class SpreadsheetAdmin(admin.ModelAdmin):
    inlines = [RowInline, ColumnInline, CellInline]

admin.site.register(Spreadsheet, SpreadsheetAdmin)
