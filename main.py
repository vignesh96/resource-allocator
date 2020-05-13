from collections import Counter
import constants
import math

class ResourceAllocator(object):

    def __init__(self):
        """ Constructor """
        self.units = constants.UNITS
        self.costs = constants.COSTS

    def possible_sums(self, number_list, total):
        """ Find all possible combinations that can be used to arrive to the sum 
        using Dynamic Programming """
        ways = [[Counter()]] + [[] for _ in range(total)]
        for instance, units in number_list.items():
            for i in range(units, total + 1):
                ways[i] += [way + Counter({instance: 1}) for way in ways[i-units]]
        return ways[total]

    def get_minimum_cost(self, possible_combos, costs_in_city, hours):
        """ Compute minimum cost based on the possible combinations """

        minimum_combo = None
        minimum_cost = math.inf
        for combo in possible_combos:
            cost = 0
            for ele in combo:
                cost += costs_in_city[ele] * combo[ele] * hours
            
            if cost < minimum_cost:
                minimum_cost = cost
                minimum_combo = combo

        return list(minimum_combo.items()), minimum_cost

    def build_json(self, city, cost, combo):
        """ Build final result in JSON format """
        return {"region": city, "total_cost": "${}".format(cost), "machines": combo}

    def start_process(self, total_units, hours):
        """ Start of the process """

        output_dict = {"Output":[]}
        cities = list(self.costs.keys())

        for city in cities:
            required_dict = {}
            costs_in_city = self.costs[city]
            keys_in_city = list(costs_in_city.keys())

            for key in keys_in_city:
                if key in self.units.keys():
                    required_dict[key] = self.units.get(key)
            
            # Get all possible sums
            possible_combos = self.possible_sums(required_dict, total_units)

            # Fetch the combo with minimum cost
            combo, minimum_cost = self.get_minimum_cost(possible_combos, costs_in_city, hours)
            output = self.build_json(city, minimum_cost, combo)
            output_dict["Output"].append(output)

        return output_dict

if __name__ == "__main__":
    capacity = input("No of units are required (Will always be multiple of 10):")    
    hours = input("No of hours the machine is required to run:")

    rs = ResourceAllocator()
    output = rs.start_process(total_units=capacity, hours=hours)
    print(output)