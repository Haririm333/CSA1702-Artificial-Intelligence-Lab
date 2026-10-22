class VacuumCleanerAgent:
    def __init__(self, initial_location='A', room_states=None):
        self.location = initial_location
        self.room_states = room_states if room_states else {'A': 'Dirty', 'B': 'Dirty'}
        self.cost = 0

    def sense(self):
        return self.location, self.room_states[self.location]

    def act(self):
        loc, status = self.sense()
        print(f"Agent at Location {loc} | Status: {status}")

        if status == 'Dirty':
            print(f"Action: SUCK dirt at Location {loc}")
            self.room_states[loc] = 'Clean'
            self.cost += 1
        else:
            new_loc = 'B' if loc == 'A' else 'A'
            print(f"Action: MOVE to Location {new_loc}")
            self.location = new_loc
            self.cost += 1

    def run(self):
        print(f"Initial State: {self.room_states}, Agent Start: {self.location}\n")
        steps = 0
        while any(status == 'Dirty' for status in self.room_states.values()) and steps < 6:
            self.act()
            steps += 1
            print(f"Current State: {self.room_states}\n")

        print("Final Result:")
        print(f"All rooms cleaned! Total actions taken: {self.cost}")

agent = VacuumCleanerAgent(initial_location='A', room_states={'A': 'Dirty', 'B': 'Dirty'})
agent.run()
