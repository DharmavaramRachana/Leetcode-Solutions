class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        starting_cities = set()

        for start, destination in paths:
            starting_cities.add(start)

        for start, destination in paths:
            if not destination in starting_cities:
                return destination
        