import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://facerecognition118-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "21C31A6941":
        {
            "name": "Rahulsrinath",
            "Branch": "CSO",
            "Starting_Year":2021,
            "Total_Attendance":6,
            "standing": "A",
            "year":4,
            "Last_attendance_time": "2024-09-20 00:54:34"
        },
    "963852":
        {
            "name": "Elonmusk",
            "Branch": "CSO",
            "Starting_Year":2021,
            "Total_Attendance":2,
            "standing": "B",
            "year":4,
            "Last_attendance_time": "2024-09-20 00:64:34"
        },
    "21C31A6951":
        {
            "name": "HarshaVardhan",
            "Branch": "CSO",
            "Starting_Year":2021,
            "Total_Attendance":2,
            "standing": "A",
            "year":4,
            "Last_attendance_time": "2024-09-20 00:64:34"
        },
    "21C31A6954":
        {
            "name": "Abhinav sai",
            "Branch": "CSO",
            "Starting_Year":2021,
            "Total_Attendance":2,
            "standing": "A",
            "year":4,
            "Last_attendance_time": "2024-09-20 00:64:34"
        },
    "21C31A6933":
        {
            "name": "Dhanush",
            "Branch": "CSO",
            "Starting_Year":2021,
            "Total_Attendance":2,
            "standing": "B",
            "year":4,
            "Last_attendance_time": "2024-09-20 00:64:34"
        },
}



for key,value in data.items():
     ref.child(key).set(value)