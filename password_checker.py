COMMON_PASSWORDS = ["password", "123456", "qwerty", "admin", "letmein", "welcome"]


def check_password(password):
    score = 0
    tips = []

    # Length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        tips.append("Use 12 or more characters for a stronger password.")
    else:
        tips.append("Use at least 8 characters.")

    # Character types
    if any(c.islower() for c in password):
        score += 1
    else:
        tips.append("Add lowercase letters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("Add uppercase letters.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("Add numbers.")

    if any(not c.isalnum() for c in password):
        score += 1
    else:
        tips.append("Add special characters like ! @ # $.")

    # Common passwords
    if any(word in password.lower() for word in COMMON_PASSWORDS):
        score = max(score - 2, 0)
        tips.append("Avoid common words like 'password' or '123456'.")

    # Rating
    if score <= 2:
        rating = "Weak"
    elif score <= 4:
        rating = "Medium"
    else:
        rating = "Strong"

    return rating, score, tips


def main():
    print("Password Strength Checker")
    password = input("Enter a password to check: ")
    rating, score, tips = check_password(password)

    print(f"\nStrength: {rating} (score {score}/6)")
    if tips:
        print("How to improve:")
        for tip in tips:
            print(f"- {tip}")


if __name__ == "__main__":
    main()
