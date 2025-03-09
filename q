[1mdiff --git a/app.py b/app.py[m
[1mindex 63115ea..62e8c47 100644[m
[1m--- a/app.py[m
[1m+++ b/app.py[m
[36m@@ -1,4 +1,5 @@[m
[31m-from datetime import datetime[m
[32m+[m[32mfrom datetime import date[m
[32m+[m[32mfrom email.policy import default[m
 from os import abort[m
 [m
 from flask import Flask, request, jsonify[m
[36m@@ -21,7 +22,7 @@[m [mclass Task(db.Model):[m
     id = db.Column(db.Integer, primary_key=True)[m
     title = db.Column(db.String(100), nullable=False)[m
     description = db.Column(db.String(200))[m
[31m-    due_date = db.Column(db.String(50), datetime.date.today().__str__())[m
[32m+[m[32m    due_date = db.Column(db.String(50), default=date.today().__str__())[m
     status = db.Column(db.String(20), default="Pending")[m
 [m
 [m
[36m@@ -34,9 +35,9 @@[m [mwith app.app_context():[m
 def create_task():[m
     data = request.json[m
     new_task = Task([m
[31m-        title=data.get('title'),  # Default title if missing[m
[32m+[m[32m        title=data.get('title', 'Untitled Task'),  # Default title if missing[m
         description=data.get('description', 'No description provided'),[m
[31m-        due_date=data.get('due_date', ''),[m
[32m+[m[32m        due_date=data.get('due_date', date.today().__str__()),[m
         status=data.get('status', 'Pending')[m
     )[m
     db.session.add(new_task)[m
