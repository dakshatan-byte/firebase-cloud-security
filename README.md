🔐 Firebase Security Misconfiguration Detection & Auto-Remediation Framework

📌 Project Overview
This project focuses on identifying and fixing security misconfigurations in Firebase Firestore — one of the most commonly misconfigured cloud databases. The system intentionally introduces a vulnerability, simulates a real-world attack, detects the issue using a custom-built scanner, and automatically suggests and applies a secure fix. The entire detection engine is containerized using Docker for portability and consistency.

🎯 Objective
The primary goal of this project is to demonstrate how improperly configured Firebase security rules can expose sensitive user data to unauthorized access — and how such vulnerabilities can be detected and remediated in an automated manner.

🔍 Problem Statement
Firebase Firestore allows developers to define access control through security rules. A common misconfiguration is setting rules to allow public read and write access without any authentication check. This exposes all stored data to anyone on the internet, making it a critical security risk. Many real-world data breaches have occurred due to this exact misconfiguration.

🏗 System Architecture
The system is divided into five core components:

Vulnerable Firebase Setup — A Firestore database is configured with intentionally insecure rules that allow unrestricted public access.
Attack Simulation — A script simulates an unauthorized attacker attempting to access sensitive data without any credentials.
Detection Engine — A scanner analyzes the Firebase security rules file, identifies misconfigurations, and classifies them by severity (Critical or Warning).
Risk Scoring Module — Based on the issues detected, a numerical risk score out of 100 is calculated to quantify the security posture.
Auto-Remediation — The system suggests corrected security rules that enforce authentication before allowing any data access, and these rules are redeployed to Firebase.


🛠 Technologies Used

Firebase & Firestore — Cloud NoSQL database used as the target environment
Firebase CLI — Used to deploy and manage security rules
Python — Used to build the attack simulation and detection engine
Docker — Used to containerize the scanner for portability across systems
GitHub — Used for version control and team collaboration

👥 Team & Work Division
StudentResponsibility: Student 1 (Dakshata) — MacFirebase setup, vulnerable rule deployment, attack simulation, secure rule deployment
Student 2 (Bhavika) — WindowsScanner development, risk scoring, auto-remediation module

🔐 Security Vulnerability Explained
The vulnerability used in this project is CWE-284: Improper Access Control. When Firebase rules are set to allow all reads and writes without authentication, any person with the database URL can access or modify all data. This is classified as a Critical severity issue as it directly exposes sensitive information such as usernames, roles, and passwords.

🔧 Remediation Approach
The remediation enforces that only authenticated users can read or write data. This is achieved by modifying the Firebase security rules to check for a valid authentication token before granting access. After applying the fix, the same attack is re-run to verify that access is now denied.

🐳 Docker Containerization
To enhance portability and simulate a real DevSecOps environment, the detection engine is containerized using Docker. This means the scanner can be run on any machine regardless of the underlying operating system or Python environment, making it suitable for CI/CD pipelines and automated security audits.

📊 Results Summary
ScenarioAccessRisk ScoreBefore FixData fully exposed70 / 100After FixAccess completely denied 20/100

📚 References

Firebase Security Rules Documentation — firebase.google.com/docs/rules
OWASP Cloud Security Top 10 — owasp.org
Docker Documentation — docs.docker.com
CWE-284: Improper Access Control — cwe.mitre.org
