import random
import time
import matplotlib.pyplot as plt
from typing import List

# --- Configuration ---
# You can tweak these parameters to see how the ecosystem changes.

# ECOSYSTEM PARAMETERS
INITIAL_PLANTS = 10000
PLANT_CARRYING_CAPACITY = 20000
PLANT_GROWTH_RATE = 0.1 # 10% growth per day

# SIMULATION PARAMETERS
SIMULATION_DAYS = 200
SIMULATION_SPEED = 0.05 # Seconds per day (for visualization)


class Species:
    """A base class for all species in the ecosystem."""
    def __init__(self, name: str, population: int, reproduction_rate: float, food_requirement: float):
        self.name = name
        self.population = population
        self.reproduction_rate = reproduction_rate
        self.food_requirement = food_requirement # Food units needed per individual

    def is_extinct(self) -> bool:
        """Check if the species has gone extinct."""
        return self.population <= 0

    def __repr__(self) -> str:
        return f"{self.name}(Population: {int(self.population)})"

    def update(self, ecosystem: 'Ecosystem'):
        """Abstract method for a species' daily actions. To be implemented by subclasses."""
        raise NotImplementedError

class Herbivore(Species):
    """A species that eats plants."""
    def __init__(self, name: str, population: int, reproduction_rate: float, food_requirement: float):
        super().__init__(name, population, reproduction_rate, food_requirement)

    def update(self, ecosystem: 'Ecosystem'):
        if self.is_extinct():
            return

        # 1. Calculate food needed and attempt to eat
        food_needed = self.population * self.food_requirement
        food_eaten = ecosystem.graze_plants(food_needed)

        # 2. Calculate births and deaths based on food
        # Starvation happens if not enough food was eaten
        if food_eaten < food_needed:
            # Calculate the proportion of the population that will starve
            shortfall = food_needed - food_eaten
            starvation_rate = (shortfall / food_needed) * 0.5 # A factor to make starvation less brutal
            starvation_deaths = self.population * starvation_rate
            self.population -= starvation_deaths
        
        # Reproduction is proportional to how much food was eaten
        births = self.population * self.reproduction_rate * (food_eaten / food_needed)
        self.population += births

        # 3. Natural death rate (a small fraction dies of old age/disease)
        natural_deaths = self.population * 0.01
        self.population -= natural_deaths

        # Ensure population is an integer and not negative
        self.population = max(0, int(self.population))

class Carnivore(Species):
    """A species that eats other species (prey)."""
    def __init__(self, name: str, population: int, reproduction_rate: float, food_requirement: float, prey: List[str]):
        super().__init__(name, population, reproduction_rate, food_requirement)
        self.prey_names = prey # List of names of species it can eat

    def update(self, ecosystem: 'Ecosystem'):
        if self.is_extinct():
            return

        # 1. Hunt for prey
        food_needed = self.population * self.food_requirement
        food_eaten = 0
        
        potential_prey = [s for s in ecosystem.species if s.name in self.prey_names and not s.is_extinct()]
        if potential_prey:
            # Simple hunting model: hunt a random prey species
            target_prey = random.choice(potential_prey)
            # Successful hunts depend on predator and prey populations
            hunt_success_rate = 0.1 
            hunts = self.population * hunt_success_rate
            
            prey_killed = min(hunts, target_prey.population * 0.5) # Can't kill more than 50% of prey in a day
            target_prey.population -= prey_killed
            food_eaten = prey_killed # Assume 1 prey = 1 food unit

        # 2. Update population based on food eaten (similar to Herbivore)
        if food_eaten < food_needed:
            shortfall = food_needed - food_eaten
            starvation_rate = (shortfall / food_needed) * 0.5
            starvation_deaths = self.population * starvation_rate
            self.population -= starvation_deaths

        births = self.population * self.reproduction_rate * (food_eaten / food_needed if food_needed > 0 else 0)
        self.population += births
        
        # 3. Natural death rate
        natural_deaths = self.population * 0.02
        self.population -= natural_deaths
        
        self.population = max(0, int(self.population))


class Ecosystem:
    """Manages the environment and all species within it."""
    def __init__(self):
        self.plants = INITIAL_PLANTS
        self.species: List[Species] = []
        self.day = 0
        self.history = {'day': [], 'plants': []}

    def add_species(self, new_species: Species):
        """Add a new species to the ecosystem."""
        self.species.append(new_species)
        self.history[new_species.name] = [] # Initialize history tracking for the new species

    def graze_plants(self, amount: float) -> float:
        """Allows herbivores to consume plants. Returns the amount actually eaten."""
        eaten = min(self.plants, amount)
        self.plants -= eaten
        return eaten

    def simulate_day(self):
        """Simulate one full day in the ecosystem."""
        self.day += 1

        # 1. Plants grow (Logistic growth model)
        growth = self.plants * PLANT_GROWTH_RATE * (1 - self.plants / PLANT_CARRYING_CAPACITY)
        self.plants = min(PLANT_CARRYING_CAPACITY, self.plants + growth)
        
        # 2. Species take their turns (update)
        # We iterate over a copy because species might be removed if they go extinct
        for s in list(self.species):
            s.update(self)

        # 3. Remove extinct species
        self.species = [s for s in self.species if not s.is_extinct()]
        
        # 4. Record history for plotting
        self.record_history()
        
    def record_history(self):
        """Records the current state of the ecosystem for later analysis."""
        self.history['day'].append(self.day)
        self.history['plants'].append(self.plants)
        for s in self.species:
            if s.name in self.history:
                self.history[s.name].append(s.population)
        
        # For any extinct species, record 0
        all_species_names = list(self.history.keys())
        all_species_names.remove('day')
        all_species_names.remove('plants')
        current_species_names = [s.name for s in self.species]
        for name in all_species_names:
            if name not in current_species_names:
                 self.history[name].append(0)


    def run_simulation(self):
        """Runs the full simulation for a set number of days."""
        print("--- Ecosystem Simulation Start ---")
        
        for i in range(SIMULATION_DAYS):
            self.simulate_day()
            
            # Print status update to console
            print(f"--- Day {self.day} ---")
            print(f"Plants: {int(self.plants)}")
            for s in self.species:
                print(s)
            
            if not self.species:
                print("\nAll species have gone extinct. The ecosystem is barren.")
                break
            
            time.sleep(SIMULATION_SPEED)
        
        print("\n--- Simulation Ended ---")
        self.plot_history()

    def plot_history(self):
        """Uses matplotlib to plot the population history."""
        plt.style.use('seaborn-v0_8-darkgrid')
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Plot plants on a secondary axis if their numbers are very different
        ax2 = ax.twinx()
        ax2.plot(self.history['day'], self.history['plants'], 'g--', label='Plants (Right Axis)', alpha=0.7)
        ax2.set_ylabel('Plant Biomass', color='g')
        ax2.tick_params(axis='y', labelcolor='g')

        # Plot animal species
        for species_name, populations in self.history.items():
            if species_name not in ['day', 'plants']:
                if any(p > 0 for p in populations): # Only plot if it existed
                    ax.plot(self.history['day'], populations, label=species_name, linewidth=2)
        
        ax.set_xlabel('Day')
        ax.set_ylabel('Population')
        ax.set_title('Ecosystem Population Dynamics')
        
        # Create a single legend
        lines, labels = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax2.legend(lines + lines2, labels + labels2, loc='upper left')

        plt.show()

# --- Main execution ---
if __name__ == "__main__":
    # 1. Create the ecosystem
    world = Ecosystem()

    # 2. Create and add species with their specific attributes
    rabbits = Herbivore(name="Rabbit", population=150, reproduction_rate=0.1, food_requirement=2)
    deer = Herbivore(name="Deer", population=50, reproduction_rate=0.05, food_requirement=5)
    
    foxes = Carnivore(name="Fox", population=20, reproduction_rate=0.04, food_requirement=1.5, prey=["Rabbit"])
    wolves = Carnivore(name="Wolf", population=10, reproduction_rate=0.02, food_requirement=3, prey=["Rabbit", "Deer"])
    
    world.add_species(rabbits)
    world.add_species(deer)
    world.add_species(foxes)
    world.add_species(wolves)

    # 3. Run the simulation
    world.run_simulation()