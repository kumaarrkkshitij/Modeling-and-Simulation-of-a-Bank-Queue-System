# Del Mundo, Guiane Carlo M.
# Kumaarr, Kkshitij
# CS-302
# 6IMODSIM PROJECT

import random
import statistics
import pandas as pd
from flask import Flask, render_template, request

# -----------------------------
# Load Dataf

# -----------------------------

DATA_FILE = "simulated_bank_data.csv"

data = pd.read_csv(DATA_FILE)

# -----------------------------
# Queue Simulation
# -----------------------------

def simulate_queue(arrival_times, service_times, num_tellers):
    teller_times = [0] * num_tellers
    waiting_times = []

    for arrival, service in zip(arrival_times, service_times):
        next_free = min(teller_times)
        teller_index = teller_times.index(next_free)

        start_time = max(arrival, next_free)
        waiting_times.append(start_time - arrival)

        teller_times[teller_index] = start_time + service

    return waiting_times

def format_time(minutes):
    total_seconds = round(minutes * 60)
    m, s = divmod(total_seconds, 60)
    return f"{m} min {s} sec"

# -----------------------------
# Routes
# -----------------------------

app = Flask(__name__)

@app.route("/")
def index():
    # Show daily and overall results
    daily_results = []
    all_waits = []

    for day, group in data.groupby("day"):
        tellers = group["tellers"].iloc[0]
        arrivals = group["arrival_time"].tolist()
        services = group["service_time"].tolist()

        waits = simulate_queue(arrivals, services, tellers)
        if not waits:
            continue

        avg_wait = statistics.mean(waits)
        max_wait = max(waits)
        num_customers = len(waits)

        daily_results.append({
            "day": day,
            "tellers": tellers,
            "customers": num_customers,
            "avg_wait": format_time(avg_wait),
            "max_wait": format_time(max_wait)
        })

        all_waits.extend(waits)

    overall = None
    if all_waits:
        overall = {
            "avg_wait": format_time(statistics.mean(all_waits)),
            "max_wait": format_time(max(all_waits))
        }

    return render_template("index.html", daily_results=daily_results, overall=overall)


@app.route("/scenario", methods=["GET", "POST"])
def scenario():
    # Run manager scenario with form input
    result = None
    if request.method == "POST":
        num_tellers = int(request.form["tellers"])
        num_customers = int(request.form["customers"])

        arrivals = sorted(random.choices(data["arrival_time"], k=num_customers))
        services = random.choices(data["service_time"], k=num_customers)
        waits = simulate_queue(arrivals, services, num_tellers)

        if waits:
            result = {
                "tellers": num_tellers,
                "customers": num_customers,
                "avg_wait": format_time(statistics.mean(waits)),
                "max_wait": format_time(max(waits))
            }

    return render_template("scenario.html", result=result)

# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
