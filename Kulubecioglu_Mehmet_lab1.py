class Agent:
    def __init__(self, performance, environment, actuators, sensors):
        self.performance = performance
        self.environment = environment
        self.actuators = actuators
        self.sensors = sensors
    
    def describe(self):
        print(f"Performance: {self.performance}")
        print(f"Environment: {self.environment}")
        print(f"Actuators: {self.actuators}")
        print(f"Sensors: {self.sensors}")


# PEAS definition for Titanic Ocean Explorer Agent
performance = "Explore deep ocean areas and collect data"
environment = "Deep ocean, varying temperatures, high pressure"
actuators = ["propeller", "arms for sample collection", "lights"]
sensors = ["sonar", "temperature sensor", "pressure gauge", "camera"]

# Create the Titanic Ocean Explorer agent
titanic_explorer = Agent(performance, environment, actuators, sensors)

# Output the PEAS description
titanic_explorer.describe()

# Basit Refleks Ajanı
class ReflexAgent:
    def action(self, percept):
        # Reflex agent acts based on the current percept
        return f"Action based on current percept: {percept}"

# Model Tabanlı Ajan
class ModelBasedAgent:
    def __init__(self):
        self.internal_state = "Initial State"
    
    def update_state(self, percept):
        # Update internal state based on the percept
        self.internal_state = f"Updated state based on {percept}"

# Amaç Tabanlı Ajan
class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal
    
    def action(self):
        # Amaç doğrultusunda hareket eder
        return f"Performing action to achieve goal: {self.goal}"

# Fayda Tabanlı Ajan
class UtilityBasedAgent:
    def __init__(self):
        pass

    def evaluate(self, state):
        # Her durum için fayda değerini hesaplar
        utility = hash(state) % 100  # Basit bir fayda değeri
        return f"Utility of state: {utility}"

# Öğrenen Ajan
class LearningAgent:
    def learn(self):
        # Öğrenme ajanı, çevreyi tanıyarak öğrenir
        return "Learning from the environment..."

# Test Reflex Agent
reflex_agent = ReflexAgent()
print(reflex_agent.action("percept1"))

# Test Model-Based Agent
model_based_agent = ModelBasedAgent()
model_based_agent.update_state("percept2")
print(model_based_agent.internal_state)

# Amaç Tabanlı Ajanı Test Et
goal_based_agent = GoalBasedAgent("Reach the surface")
print(goal_based_agent.action())

# Fayda Tabanlı Ajanı Test Et
utility_agent = UtilityBasedAgent()
print(utility_agent.evaluate("some_state"))

# Öğrenen Ajanı Test Et
learning_agent = LearningAgent()
print(learning_agent.learn())
