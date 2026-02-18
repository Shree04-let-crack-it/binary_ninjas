import streamlit as st
import json
import os
import uuid
import speech_recognition as sr
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

DATA_FILE = "complaints.json"

# --------------------------
# Initialize storage
# --------------------------
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

def load_complaints():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_complaints(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# --------------------------
# Speech to Text
# --------------------------
def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Speak now.")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except:
        return "Could not understand audio."

# --------------------------
# Layout
# --------------------------
st.set_page_config(page_title="Complaint Management System", layout="wide")
st.title("📢 Complaint Management System")

role = st.sidebar.selectbox("Select Dashboard", ["User", "Admin", "Officer"])

# Auto refresh every 5 seconds
st_autorefresh(interval=5000, key="refresh")

complaints = load_complaints()

# ==========================
# USER DASHBOARD
# ==========================
if role == "User":
    st.header("📝 Raise Complaint")

    complaint_text = st.text_area("Enter Complaint")

    if st.button("🎤 Speak Complaint"):
        complaint_text = speech_to_text()
        st.success(f"Recognized: {complaint_text}")

    if st.button("Submit Complaint"):
        if complaint_text:
            new_complaint = {
                "id": str(uuid.uuid4()),
                "text": complaint_text,
                "status": "Pending",
                "priority": "Normal",
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            complaints.append(new_complaint)
            save_complaints(complaints)
            st.success("Complaint Submitted Successfully!")
        else:
            st.warning("Please enter a complaint.")

# ==========================
# ADMIN DASHBOARD
# ==========================
elif role == "Admin":
    st.header("🛠 Admin Panel")

    if complaints:
        for c in complaints:
            with st.expander(f"Complaint ID: {c['id']}"):
                st.write("📝", c["text"])
                st.write("📌 Status:", c["status"])
                st.write("⚡ Priority:", c["priority"])
                st.write("⏰", c["timestamp"])

                col1, col2 = st.columns(2)

                with col1:
                    new_priority = st.selectbox(
                        "Set Priority",
                        ["Low", "Normal", "High", "Critical"],
                        key=c["id"]
                    )
                    if st.button("Update Priority", key="p"+c["id"]):
                        c["priority"] = new_priority
                        save_complaints(complaints)
                        st.success("Priority Updated")

                with col2:
                    if st.button("Delete Complaint", key="d"+c["id"]):
                        complaints = [x for x in complaints if x["id"] != c["id"]]
                        save_complaints(complaints)
                        st.warning("Complaint Deleted")
                        st.rerun()
    else:
        st.info("No complaints yet.")

# ==========================
# OFFICER DASHBOARD
# ==========================
elif role == "Officer":
    st.header("👮 Officer Panel")

    if complaints:
        for c in complaints:
            st.card = st.container()
            with st.card:
                st.subheader(f"Priority: {c['priority']}")
                st.write(c["text"])
                st.write("Status:", c["status"])
                st.write("Time:", c["timestamp"])
    else:
        st.info("No complaints available.")
