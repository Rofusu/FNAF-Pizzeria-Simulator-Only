class StateManager:
    def __init__(self, start_state, states_dict):
        self.states = states_dict
        self.state_name = start_state
        self.state = self.states[self.state_name]

    def handle_events(self, events):
        self.state.handle_events(events)

    def update(self, dt):
        if self.state.done:
            next_state_name = self.state.next_state
            if next_state_name == "ExitGame":
                self.state_name = "ExitGame"
                return
            self.state.done = False
            self.state_name = next_state_name
            self.state = self.states[self.state_name]
        self.state.update(dt)

    def draw(self, screen):
        self.state.draw(screen)