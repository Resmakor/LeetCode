class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        events = []
        for birth, death in logs:
            events.append((birth, 1))
            events.append((death, -1))
        events = sorted(events)
        population, max_population, best_year = 0, 0, 0
        for year, change in events:
            population += change
            if population > max_population:
                max_population = population
                best_year = year
        return best_year
