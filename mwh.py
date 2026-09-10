# Mindcare: Mental Wellness Hub - Version 2.0
# Features: book/cancel counseling sessions, mood tracking, online wellness resource search

resources = ["Meditation", "Breathing Exercises", "Stress Management"]

def book_session(member_id, counselor_id):
    print("Session booked for member", member_id, "with counselor", counselor_id)

def cancel_session(member_id):
    print("Session cancelled for member", member_id)

def track_mood(member_id, mood):
    print("Mood recorded for member", member_id, ":", mood)

def search_resource(title):
    if title in resources:
        print(title, "is available")
