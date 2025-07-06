import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample employee data
data = {
    'Name': ['moshahid', 'badal', 'sudha', 'manoj', 'suresh', 'anushka', 'amit', 'shivansh' ],
    'Department': ['pl', 'pl', 'pl', 'p0', 'bo', 'pl', 'tl', 'tl' ],
    'Performance Score': [88, 75, 93, 80, 90, 85, 88, 95,],
    'Attendance (%)': [92, 85, 98, 87, 96, 89, 82, 97,]
}
df = pd.DataFrame(data)

# Title
st.title("👩‍💼 Employee Performance Dashboard")

# Sidebar filter
departments = df['Department'].unique()
selected_dept = st.sidebar.multiselect("Filter by Department", departments, default=departments)

filtered_df = df[df['Department'].isin(selected_dept)]

# Summary Stats
st.header("📊 Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Employees", len(filtered_df))
col2.metric("Avg Performance", f"{filtered_df['Performance Score'].mean():.2f}")
col3.metric("Avg Attendance", f"{filtered_df['Attendance (%)'].mean():.2f}%")

# Table
st.subheader("🧾 Employee Data")
st.dataframe(filtered_df)

# Performance Chart
st.subheader("📈 Performance Score by Employee")
fig1, ax1 = plt.subplots()
ax1.bar(filtered_df['Name'], filtered_df['Performance Score'], color='skyblue')
ax1.set_ylabel("Performance Score")
ax1.set_title("Performance")
st.pyplot(fig1)

# Attendance Pie Chart
st.subheader("📅 Attendance Distribution")
fig2, ax2 = plt.subplots()
ax2.pie(filtered_df['Attendance (%)'], labels=filtered_df['Name'], autopct='%1.1f%%', startangle=90)
ax2.axis('equal')
st.pyplot(fig2)
