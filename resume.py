import pandas as pd

# Load the data
df = pd.read_csv(r"C:\Challange\resume_data.csv")

while True:
    # Ask for skill # User Input
    skill = input("\nEnter a skill to filter (e.g., Python, FastAPI): ").strip().lower()

    # Filter logic
    matches = df[df['skills'].str.lower().str.contains(skill)]

    # Output
    if not matches.empty:
        print("\nMatching Candidates:\n")
        for _, row in matches.iterrows():
            print(f"✅ {row['name']} — Skills: {row['skills']}")
    else:
        print("❌ No matching candidates found.")

    # Ask if the user wants to search again
    again = input("\n🔄 Do you want to search again? (y/n): ").strip().lower()
    if again != 'y':
        print("👋 Exiting the Resume Filter. Have a great day!")
        break
