# Copyright (c) 2023, H S Rai and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import math as math

class Circle(Document):
    #this method will run every time a document is saved
    def before_save(self):
    	self.area = round(math.pi * self.diameter ** 2 / 4., 3)
    	self.perimeter = round(math.pi * self.diameter, 3)
