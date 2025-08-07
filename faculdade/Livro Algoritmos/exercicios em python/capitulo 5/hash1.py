from collections import defaultdict

def groupAnagrams(str):
    anagram_map = defaultdict(list)
    result = []

    for s in str:
        sorted_s = tuple(sorted(s))
        anagram_map[sorted_s].append(s)
    anagram_values = anagram_map.values()
    print(anagram_values)
    print(anagram_map)
    for value in anagram_map.values():
        result.append(value)

    return result



str = {"eat", "tea", "tan", "ate", "nat", "bat"}

print("Resultado: ", groupAnagrams(str))
### 

city_map = {}

cities = ["Calgary", "Vancouver", "Toronto"]
city_map["Canada"] = []

city_map["Canada"] += cities

city_keys = city_map.keys()
city_list = city_map.values()
city_items = city_map.items()


print(city_keys)
print(city_list)
print(city_items)
