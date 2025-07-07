import json
import random


def generate_fixtures():
    # Default password for all users: password123
    fixtures = []
    user_id = 1
    profile_id = 1

    # Indian and generic names
    male_first_names = [
        "Amit", "Rahul", "Vikram", "Suresh", "Ravi", "Arjun", "Sanjay", "Manish", "Deepak", "Anil"
    ]
    male_last_names = [
        "Sharma", "Verma", "Patel", "Singh", "Reddy", "Nair", "Gupta", "Mehra", "Joshi", "Kumar"
    ]
    female_first_names = [
        "Priya", "Anjali", "Sunita", "Kavita", "Neha", "Pooja", "Asha", "Sonia", "Ritu", "Meena"
    ]
    female_last_names = [
        "Sharma", "Verma", "Patel", "Singh", "Reddy", "Nair", "Gupta", "Mehra", "Joshi", "Kumari"
    ]
    specializations = [
        "Cardiologist", "Dermatologist", "Neurologist", "Pediatrician", "Orthopedic Surgeon", "Psychiatrist", "Gynecologist", "Dentist", "Ophthalmologist", "ENT Specialist"
    ]
    cities = [
        "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata", "Pune", "Jaipur", "Lucknow"
    ]
    states = [
        "Maharashtra", "Delhi", "Karnataka", "Telangana", "Gujarat", "Tamil Nadu", "West Bengal", "Rajasthan", "Uttar Pradesh"
    ]
    areas = [
        "Andheri", "Koramangala", "Banjara Hills", "Salt Lake", "Gachibowli", "Powai", "Juhu", "Malviya Nagar", "Viman Nagar", "MG Road"
    ]

    # Generate 15 doctors
    for i in range(1, 16):
        gender = random.choice(["male", "female"])
        if gender == "male":
            first_name = random.choice(male_first_names)
            last_name = random.choice(male_last_names)
        else:
            first_name = random.choice(female_first_names)
            last_name = random.choice(female_last_names)

        doctor_username = f"doctor{i}"
        doctor = {
            "model": "accounts.user",
            "fields": {
                "password": "pbkdf2_sha256$260000$HQyGxzxfOxv6nLKI8zF$w9Nmz1Rxm1fPY1HzJ2MU7MgKBfTJ1RfF3q9M1wJvXvQ=",  # "password123"
                "username": doctor_username,
                "email": f"{first_name.lower()}.{last_name.lower()}@example.com",
                "first_name": first_name,
                "last_name": last_name,
                "role": "doctor",
                "is_active": True,
                "date_joined": "2023-01-01T00:00:00Z",
            },
        }
        fixtures.append(doctor)

        doctor_profile = {
            "model": "accounts.profile",
            "pk": profile_id,
            "fields": {
                "user": user_id,
                "phone": f"+91{random.randint(7000000000, 9999999999)}",
                "dob": f"{random.randint(1960, 1990)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}",
                "about": f"MBBS from {random.choice(['AIIMS Delhi', 'CMC Vellore', 'KEM Mumbai', 'PGI Chandigarh'])}. {random.randint(5, 20)} years of experience in {random.choice(specializations)}.",
                "specialization": random.choice(specializations),
                "gender": gender,
                "address": f"House {random.randint(1, 99)}, {random.choice(areas)}, {random.choice(cities)}",
                "city": random.choice(cities),
                "state": random.choice(states),
                "postal_code": f"{random.randint(100000, 999999)}",
                "country": "India",
                "price_per_consultation": random.randint(500, 2000),
                "is_available": True,
            },
        }
        fixtures.append(doctor_profile)
        user_id += 1
        profile_id += 1

    # Generate 15 patients
    blood_groups = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
    allergies_list = ["None", "Dust Allergy", "Food Allergy", "Drug Allergy"]
    conditions_list = ["None", "High Blood Pressure", "Diabetes", "Asthma"]
    for i in range(1, 16):
        gender = random.choice(["male", "female"])
        if gender == "male":
            first_name = random.choice(male_first_names)
            last_name = random.choice(male_last_names)
        else:
            first_name = random.choice(female_first_names)
            last_name = random.choice(female_last_names)

        patient_username = f"patient{i}"
        patient = {
            "model": "accounts.user",
            "pk": user_id,
            "fields": {
                "password": "pbkdf2_sha256$260000$HQyGxzxfOxv6nLKI8zF$w9Nmz1Rxm1fPY1HzJ2MU7MgKBfTJ1RfF3q9M1wJvXvQ=",  # "password123"
                "username": patient_username,
                "email": f"{first_name.lower()}.{last_name.lower()}@example.com",
                "first_name": first_name,
                "last_name": last_name,
                "role": "patient",
                "is_active": True,
                "date_joined": "2023-01-01T00:00:00Z",
            },
        }
        fixtures.append(patient)

        patient_profile = {
            "model": "accounts.profile",
            "pk": profile_id,
            "fields": {
                "user": user_id,
                "phone": f"+91{random.randint(7000000000, 9999999999)}",
                "dob": f"{random.randint(1970, 2000)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}",
                "gender": gender,
                "address": f"Flat {random.randint(1,20)}A, House {random.randint(1, 99)}, {random.choice(areas)}, {random.choice(cities)}",
                "city": random.choice(cities),
                "state": random.choice(states),
                "postal_code": f"{random.randint(100000, 999999)}",
                "country": "India",
                "blood_group": random.choice(blood_groups),
                "allergies": random.choice(allergies_list),
                "medical_conditions": random.choice(conditions_list),
            },
        }
        fixtures.append(patient_profile)
        user_id += 1
        profile_id += 1

    # Write fixtures to file
    with open("fixtures/initial_data.json", "w") as f:
        json.dump(fixtures, f, indent=2)


if __name__ == "__main__":
    generate_fixtures()
