import pandas as pd

# Load all the required datasets
enrollment = pd.read_csv("clean_LearnerOpportunity_Raw.csv")
cohort = pd.read_csv("clean_CohortRaw.csv")
learner = pd.read_csv("clean_Learner_Raw.csv")
cognito = pd.read_csv("clean_Cognito_Raw2.csv")

# Merge enrollment and cohort data
merged1 = enrollment.merge(cohort, left_on='Assigned_Cohort', right_on='Cohort_Code', how='left')

# Merge with learner details
merged2 = merged1.merge(learner, left_on='Learner_ID', right_on='LEARNER_ID', how='left')

# Merge with cognito data (assuming Learner_ID == User_ID)
final_merged = merged2.merge(cognito, left_on='Learner_ID', right_on='User_ID', how='left')

# Select only the required columns
master_table = final_merged[[
    'Enrollment_ID',
    'Learner_ID',
    'Assigned_Cohort',
    'Apply_Date',
    'Status_x',
    'Cohort_Code',
    'Start_Date',
    'End_Date',
    'Size',
    'Gender',
    'Email',
    'Degree',
    'Institution',
    'Major'
]]

# Optional: Rename Status_x to Application_Status for clarity
master_table.rename(columns={'Status_x': 'Application_Status'}, inplace=True)

# Save to CSV
master_table.to_csv("master_table.csv", index=False)

# Show a preview
print("Master table saved as 'master_table.csv'")
print(master_table.head())
