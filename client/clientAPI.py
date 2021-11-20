import requests

# base url
url = "https://localhost:5000/api"


def get_drones():   # list of drones out
    # GET /drones
    res = requests.get(f"{url}/drones")
    print(res)
    resj = res.json()
    for key, value in resj.items():
        if key == 0:
            print(f"Total drones out: {key[TotalDronesOut]}")
        else:
            print(
                f"IdDrone: {key[IdDrone]} to {key['IdClient']} for {key[TimeAvailable]}")


def get_droneById(id):  # info about the drone by id
    # GET /drone/{id}
    res = requests.get(f"{url}/drone/{id}")
    print(res)
    resj = res.json()
    print(
        f"Drone ID: {resj[IdDrone]}\n\
        Position: {resj[Position]}\n\
        Status: {resj['Status']} since {resj['Status'][Time]}\n\
        Client: {resj['IdClient']}")


def get_clientById(id):
    # GET /client/{id}
    res = requests.get(f"{url}/client/{id}")
    print(res)
    resj = res.json()
    print(
        f"Client ID: {resj[IdClient]}\n\
        Name: {resj['Name']}\n\
        Surname: {resj['Surname']}\n\
        Total Drones out: {resj[Drones][TotalNumber]}")
    for i in resj[Drones][IdDrone]:
        print(f"Drone ID: {i}")
