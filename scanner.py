def analyze_rules(rules):
    issues = []

    if "allow read, write: if true" in rules:
        issues.append("CRITICAL: Public read/write access")

    if "request.auth" not in rules:
        issues.append("WARNING: No authentication enforced")

    return issues


def risk_score(issues):
    score = 0
    for i in issues:
        if "CRITICAL" in i:
            score += 50
        elif "WARNING" in i:
            score += 20
    return min(score, 100)


def suggest_fix():
    return """
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{userId} {
      allow read, write: if request.auth != null;
    }
  }
}
"""

with open("firestore.rules", "r") as f:
    rules = f.read()

issues = analyze_rules(rules)
score = risk_score(issues)

print("=== SECURITY SCAN RESULTS ===")
print("Issues Found:")
for i in issues:
    print(" -", i)
print("\nRisk Score:", score, "/ 100")
print("\nSuggested Fix:")
print(suggest_fix())