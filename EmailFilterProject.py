# Simulated inbox emails

inbox = [
    {"subject": "Newsletter: New season, new arrivals", "opened": False},
    {"subject": "15% off - today only!", "opened": True},
    {"subject": "Spam: Unlock a FREE 20$ gif card!", "opened": False},
    {"subject": "Newsletter: Weekly science  updates", "opened": False},
    {"subject": "Favorite store - special discount", "opened": True},
    {"subject": "Notification: Account security update", "opened": True},
    {"subject": "Newsletter: Tips for productive learning", "opened": False},
]

# keywords for favorite emails

favorites = ["Favorite store", "Special discount"]
# filtering logic
filtered_inbox = []

for email in inbox:

    if any (fav in email ["subject"] for fav in favorites):
        filtered_inbox.insert(0, email)
    elif "Newsletter" in email["subject"] and email["opened"] == False:
        continue
    else :
        filtered_inbox.append(email)

print("Filtered inbox:")
for e in filtered_inbox:

      print("-", e["subject"])
