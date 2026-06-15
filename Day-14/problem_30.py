# Problem 30
# The App Feature Flag Controller
# 
# Deployment panels turn features on or off using a dictionary of boolean flags (e.g., {"chat_enabled": True, "video_enabled": False}). Loop through the panel configurations and print only the feature names that are currently set to True.


features = {
    "chat_enabled": True,
    "video_enabled": False,
    "file_sharing_enabled": True,
    "notifications_enabled": True,
    "analytics_enabled": False,
    "voice_call_enabled": True,
    "dark_mode_enabled": False,
    "encryption_enabled": True
}

for (k,v) in features.items():
  if v:
    print(k)

