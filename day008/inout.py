def mark_attendance(answer):
    if answer.lower() == "in":
        return "present"
    else:
        return "absent"

answer = input("Enter in/out: ")
print(mark_attendance(answer))