class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        if len(paths) == 1:
            return paths[0][1]
        cities_a = set([path[0] for path in paths])
        cities_b = set([path[1] for path in paths])
        destination = list(cities_b.difference(cities_a))[0]
        return destination
            