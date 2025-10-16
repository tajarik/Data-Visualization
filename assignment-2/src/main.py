import matplotlib.pyplot as plt
from charts import run_query, save_and_report
import queries as q

# ------------------------
# 1. Pie chart – Flight delays
# ------------------------
df1 = run_query(q.PIE_FLIGHTS)
fig1, ax1 = plt.subplots()
ax1.pie(df1['total_flights'], labels=df1['departure_status'], autopct='%1.1f%%', startangle=90)
ax1.set_title("On-Time vs Delayed Flights")
save_and_report(fig1, "pie_flight_delays.png", df1, "Shows percentage of on-time vs delayed flights")

# ------------------------
# 2. Bar chart – Airline revenue
# ------------------------
df2 = run_query(q.BAR_REVENUE)
fig2, ax2 = plt.subplots()
ax2.bar(df2['airline_name'], df2['total_revenue'], color="skyblue")
ax2.set_title("Top 5 Airlines by Revenue")
ax2.set_ylabel("Revenue ($)")
ax2.set_xlabel("Airline")
plt.xticks(rotation=30, ha="right")
save_and_report(fig2, "bar_airline_revenue.png", df2, "Shows top 5 airlines ranked by revenue")

# ------------------------
# 3. Horizontal bar – Booking platforms
# ------------------------
df3 = run_query(q.HORIZONTAL_PLATFORM)
fig3, ax3 = plt.subplots()
ax3.barh(df3['booking_platform'], df3['total_bookings'], color="green")
ax3.set_title("Bookings by Platform")
ax3.set_xlabel("Total Bookings")
ax3.set_ylabel("Platform")
save_and_report(fig3, "hbar_booking_platforms.png", df3, "Shows booking distribution across platforms")

# ------------------------
# 4. Line chart – Monthly bookings
# ------------------------
df4 = run_query(q.LINE_BOOKINGS)
fig4, ax4 = plt.subplots()
ax4.plot(df4['month'], df4['total_bookings'], marker="o")
ax4.set_title("Monthly Booking Trends")
ax4.set_xlabel("Month")
ax4.set_ylabel("Bookings")
plt.xticks(rotation=45)
save_and_report(fig4, "line_booking_trends.png", df4, "Shows how bookings change month to month")

# ------------------------
# 5. Histogram – Baggage weights
# ------------------------
df5 = run_query(q.HIST_BAGGAGE)
fig5, ax5 = plt.subplots()
ax5.hist(df5['weight_in_kg'], bins=10, color="orange", edgecolor="black")
ax5.set_title("Distribution of Baggage Weights")
ax5.set_xlabel("Weight (kg)")
ax5.set_ylabel("Frequency")
save_and_report(fig5, "hist_baggage_weights.png", df5, "Shows distribution of baggage weights")

# ------------------------
# 6. Scatter – Price vs Baggage weight
# ------------------------
df6 = run_query(q.SCATTER_PRICE_BAGGAGE)
fig6, ax6 = plt.subplots()
ax6.scatter(df6['weight_in_kg'], df6['price'], alpha=0.6, color="purple")
ax6.set_title("Ticket Price vs Baggage Weight")
ax6.set_xlabel("Baggage Weight (kg)")
ax6.set_ylabel("Ticket Price ($)")
save_and_report(fig6, "scatter_price_vs_baggage.png", df6, "Shows relationship between baggage weight and ticket price")

print("\n🎉 All charts generated successfully! Check the /charts folder.")

from export_excel import export_to_excel

dataframes = {
    "Flight Delays": df1,
    "Airline Revenue": df2,
    "Booking Platforms": df3,
    "Monthly Bookings": df4,
    "Baggage Weights": df5,
    "Price vs Baggage": df6
}

export_to_excel(dataframes, "airport_report.xlsx")

