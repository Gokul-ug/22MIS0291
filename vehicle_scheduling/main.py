import requests

from scheduler import knapsack
from middleware.logging_middleware import LoggerMiddleware


DEPOT_API = "http://4.224.186.213/evaluation-service/depots"
VEHICLE_API = "http://4.224.186.213/evaluation-service/vehicles"


def fetch_data():

    LoggerMiddleware.log("Fetching depots")

    depots_response = requests.get(DEPOT_API)

    LoggerMiddleware.log("Fetching vehicles")

    vehicles_response = requests.get(VEHICLE_API)

    depots = depots_response.json()["depots"]
    vehicles = vehicles_response.json()["vehicles"]

    return depots, vehicles


def main():

    depots, vehicles = fetch_data()

    for depot in depots:

        depot_id = depot["ID"]
        mechanic_hours = depot["MechanicHours"]

        LoggerMiddleware.log(
            f"Running scheduler for Depot {depot_id}"
        )

        result = knapsack(vehicles, mechanic_hours)

        print("\n===================================")
        print(f"Depot ID: {depot_id}")
        print(f"Mechanic Hours: {mechanic_hours}")
        print(f"Maximum Impact: {result['max_impact']}")
        print("Selected Tasks:")

        total_duration = 0

        for task in result["selected_tasks"]:

            total_duration += task["Duration"]

            print(
                f"TaskID: {task['TaskID']} | "
                f"Duration: {task['Duration']} | "
                f"Impact: {task['Impact']}"
            )

        print(f"Total Duration: {total_duration}")
        print("===================================\n")


if __name__ == "__main__":
    main()