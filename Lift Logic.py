from tkinter import *
import random

# add all passenger of a floor to the lift if travelling in the same direction.
class Building(object):
    def __init__(self):
        Building.move(self)

    def move(self):
        for i in range(22):
            print("\nThe lift is on floor: " + str(lift.currentFloor))
            Building.check(self)
            lift.currentFloor += lift.direction
            lift.floorsMoved += 1
            if lift.currentFloor == numFloors - 1 or lift.currentFloor == 0:
                lift.direction *= -1

    def check(self):
        for person in floorsList[lift.currentFloor].peopleOnFloor:
            print("Person " + str(person.idPerson) + " is travelling in direction: " + str(person.direction) + " the lift direction is: " + str(lift.direction))
            if person.direction == lift.direction:
                People.destination(person)
                print("Person " + str(person.idPerson) + " started on floor " +  str(person.originFlr) + " travelling in direction " + str(person.direction) + " to floor " + str(person.destFlr))
                Building.algorithm(self, person)

    def algorithm(self, person):
        if len(lift.passengers) < lift.capacity:
            lift.passengers.append(person)
            floorsList[lift.currentFloor].peopleOnFloor.remove(person)
            print("Person " + str(person.idPerson) + " got in the lift at floor " + str(
                lift.currentFloor))

class Lift(object):
    def __init__(self):
        self.capacity = 6
        self.currentFloor = 0
        self.direction = 1
        self.floorsMoved = 0
        self.passengers = []


class People(object):
    def __init__(self, numFloors, personId):
        self.idPerson = personId
        self.originFlr = random.randint(0, numFloors)
        # randomly selects whether the passenger is travelling up or down
        self.direction = random.choice([-1,1])
        # print("\n"+str(self.originFlr))
        # print(self.direction)
        # print(self.destFlr)

    def destination(self):
        # A destination floor is generated based on whether the passenger is
        # travelling up or down where only the applicable floors will be chosen.
        if self.direction == 1:
            # direction 1 shows the passenger wishes to travel to a higher floor
            selection = list(range(self.originFlr + 1, numFloors + 1))
            self.direction = 1
        else:
            # direction -1 show the passenger wishes to travel to a lower floor
            selection = list(range(0, self.originFlr))
        self.destFlr = random.choice(selection)




class Floors(object):
    def __init__(self, peopleWaiting, floorId):
        self.idFloor = floorId
        self.count = 0
        self.peopleOnFloor = Floors.assign(self, peopleWaiting)
        print("Floor " + str(self.idFloor) + " has " + str(len(self.peopleOnFloor)) + " passengers waiting.")

    def assign(self, peopleWaiting):
        self.peopleOnFloor = []
        for k in peopleWaiting:
            if k.originFlr == floorId:
                self.peopleOnFloor.append(k)
        return self.peopleOnFloor



if __name__ == "__main__":
    master = Tk()
    liftTiles = {}
    peopleWaiting = []
    peopleArrived = []
    floorsList = []
    numFloors = 10
    numPeople = 20
    for personId in range(0, numPeople):
        peopleWaiting.append(People(numFloors - 1, personId))
    # print(peopleWaiting)

    for floorId in range(0, numFloors):
        floorsList.append(Floors(peopleWaiting, floorId))
    # print(floorsList[numFloors - 1].idFloor)
    # print(floorsList[numFloors - 1].peopleOnFloor)
    lift = Lift()
    Building()
    print("The lift has travelled " + str(lift.floorsMoved) + " floors.")



