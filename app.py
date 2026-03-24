import random

def predict_health(symptom, days, severity):
    symptom = symptom.lower()

    # Disease prediction
    if "fever" in symptom and "cough" in symptom:
        disease = "Flu"
        risk = "Medium"
        medicines = ["Paracetamol", "Cough Syrup"]
        doctor_type = "General Physician"

    elif "headache" in symptom:
        disease = "Migraine"
        risk = "Low"
        medicines = ["Ibuprofen", "Rest"]
        doctor_type = "Neurologist"

    elif "vomit" in symptom or "nausea" in symptom:
        disease = "Food Poisoning"
        risk = "Medium"
        medicines = ["ORS", "Antiemetic"]
        doctor_type = "General Physician"

    else:
        disease = "Unknown"
        risk = "High"
        medicines = ["Consult Doctor"]
        doctor_type = "General Checkup"

    # Risk update based on duration
    if days >= 3:
        risk = "High"

    # Doctor dataset with contact & availability
    doctors = [
        {"name": "Dr. Sharma", "specialty": "General Physician", "availability": "10 AM - 2 PM", "contact": "9876543210"},
        {"name": "Dr. Reddy", "specialty": "Neurologist", "availability": "2 PM - 6 PM", "contact": "9123456780"},
        {"name": "Dr. Mehta", "specialty": "General Physician", "availability": "9 AM - 1 PM", "contact": "9988776655"},
        {"name": "Dr. Patel", "specialty": "General Checkup", "availability": "11 AM - 4 PM", "contact": "9090909090"}
    ]

    suitable = [d for d in doctors if d["specialty"] == doctor_type]
    doctor = random.choice(suitable) if suitable else random.choice(doctors)

    # Appointment suggestion
    appointment = f"Book appointment with {doctor['name']} between {doctor['availability']}"

    # Emergency medicines (if high risk)
    emergency_meds = []
    if risk == "High":
        emergency_meds = ["ORS", "Paracetamol", "Electrolyte drinks"]

    # Alert system
    if risk == "High":
        alert = "⚠️ Immediate doctor consultation required!"
    elif risk == "Medium":
        alert = "⚠️ Monitor symptoms carefully."
    else:
        alert = "✅ No major issue, basic care is enough."

    return disease, risk, medicines, doctor, alert, appointment, emergency_meds


# 🩺 INTERACTIVE SYSTEM

print("\n🩺 SwasthAI – AI Health Assistant\n")

symptom = input("Enter your symptoms: ")
days = int(input("How many days have you had these symptoms? "))
severity = input("Is it mild / moderate / severe? ")

disease, risk, medicines, doctor, alert, appointment, emergency_meds = predict_health(symptom, days, severity)

print("\n========== RESULT ==========\n")
print("🩺 Disease:", disease)
print("⚠️ Risk Level:", risk)

print("\n👨‍⚕️ Doctor Recommendation:")
print(doctor["name"], "-", doctor["specialty"])
print("Available at:", doctor["availability"])
print("Contact:", doctor["contact"])

print("\n📅 Appointment:")
print(appointment)

print("\n💊 Basic Medicines:")
for med in medicines:
    print("-", med)

if emergency_meds:
    print("\n🚑 Emergency Medicines:")
    for med in emergency_meds:
        print("-", med)

print("\n🚨 Alert:", alert)
print("\n================================\n")