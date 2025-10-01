"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Team practices and intramural competitions",
        "schedule": "Mondays, Wednesdays, Fridays, 4:00 PM - 6:00 PM",
        "max_participants": 15,
        "participants": ["liam@mergington.edu", "noah@mergington.edu"]
    },
    "Soccer Club": {
        "description": "Outdoor soccer practice and friendly matches",
        "schedule": "Tuesdays and Thursdays, 4:30 PM - 6:00 PM",
        "max_participants": 18,
        "participants": ["lucas@mergington.edu", "mia@mergington.edu"]
    },
    "Track and Field": {
        "description": "Running, jumping and throwing events training",
        "schedule": "Wednesdays and Saturdays, 3:30 PM - 5:30 PM",
        "max_participants": 25,
        "participants": ["sophos@mergington.edu", "harper@mergington.edu"]
    },
    "Art Studio": {
        "description": "Drawing, painting, and mixed-media workshops",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": ["ava@mergington.edu", "charlotte@mergington.edu"]
    },
    "Drama Club": {
        "description": "Acting, stagecraft, and school productions",
        "schedule": "Thursdays, 5:00 PM - 7:00 PM",
        "max_participants": 25,
        "participants": ["isabella@mergington.edu", "amelia@mergington.edu"]
    },
    "Choir": {
        "description": "Vocal training and choral performances",
        "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
        "max_participants": 30,
        "participants": ["ella@mergington.edu", "liara@mergington.edu"]
    },
    "Debate Team": {
        "description": "Public speaking and competitive debating",
        "schedule": "Mondays, 5:00 PM - 6:30 PM",
        "max_participants": 16,
        "participants": ["ethan@mergington.edu", "oliver@mergington.edu"]
    },
    "Science Club": {
        "description": "Hands-on experiments, research projects, and fairs",
        "schedule": "Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["grace@mergington.edu", "aiden@mergington.edu"]
    },
    "Math Olympiad": {
        "description": "Problem solving and competitive math training",
        "schedule": "Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 18,
        "participants": ["noelle@mergington.edu", "benjamin@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up for this activity")

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
