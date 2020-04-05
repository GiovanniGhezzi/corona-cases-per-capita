import json

def main():
    data = json.load( open("../data/corona-cases.json", 'r') )

    coro_nary = {} # create corona dictionary

    # copy relevant data into corona dictionary:
    for record in data["records"]:
        countryname = record["countriesAndTerritories"] # store the name in a variable
        if not record["popData2018"] == "": # check if population is empty
            if not (countryname in coro_nary): # the the country does not exist as a key in the dictionary
                coro_nary[countryname] = dict() # make dictionary under the country name
                coro_nary[countryname]["cases"] = int(record["cases"]) # make a "cases" key for the country dictionary
                coro_nary[countryname]["deaths"] = int(record["deaths"]) # make a "deaths" key for the country dictionary
                coro_nary[countryname]["population"] = int(record["popData2018"])# if not record["popData2018"] == "" else 0
            else: # if the country exists in the dictionary
                coro_nary[countryname]["cases"] += int(record["cases"]) # add the number of cases'''
                coro_nary[countryname]["deaths"] += int(record["deaths"]) # add the number of deaths'''

    for country in coro_nary:
        coro_nary[country]["cases_pmc"] = (10**6)*coro_nary[country]["cases"]/coro_nary[country]["population"]
        coro_nary[country]["deaths_pmc"] = (10**6)*coro_nary[country]["deaths"] / coro_nary[country]["population"]

    # print_dict(coro_nary)

    sorted_dict = {k: v for k, v in sorted(coro_nary.items(), key=lambda x: x[1]["deaths_pmc"], reverse=True)}
    print_dict(sorted_dict)


def print_dict(dict) -> None:
    i = 1
    for x in dict: # print corona dictionary
        print("{}) {}: \t\t {} cases, \t {} deaths, \t {} population, \t {:.2f} cases per million capita, \t {:.2f} deaths per million capita"
            .format(
                i,
                x, dict[x]["cases"],
                dict[x]["deaths"],
                dict[x]["population"],
                dict[x]["cases_pmc"],
                dict[x]["deaths_pmc"]
            ))
        i += 1

if __name__ == "__main__":
    main()


