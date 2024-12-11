import itertools
import random

def sampling_d(gruppa_d,points_d):
    num_simulations = 1000
    list_combinations = list(itertools.combinations(gruppa_d, 2))

    for match in list_combinations:
        team_1, team_2 = match
        wins_team1 = 0
        wins_team2 = 0
        for i in range(num_simulations):
            p1 = gruppa_d[team_1] / (gruppa_d[team_1] + gruppa_d[team_2])

            if random.random() < p1:
                points_d[team_1] += 3
            else:
                points_d[team_2] += 3
    # sorted_points = sorted(points_d.keys(), key=lambda point: points_d[point], reverse=True)
    # start_value = 1
    # places_d = {key: index + start_value for index, key in enumerate(sorted_points)}
    sorted_results_gruppa_d = dict(sorted(points_d.items(), key=lambda x: x[1], reverse=True))
    standings_gruppd_d = {team: rank for rank, team in enumerate(sorted_results_gruppa_d, 1)}
    finish_points = {team: points / num_simulations for team, points in points_d.items()}
    print(finish_points)


def main():
    gruppa_d = {'Франция': 10, 'Дания': 5, 'Австралия': 3, 'Тунис': 1}
    points_d = {'Франция': 0, 'Дания': 0, 'Австралия': 0, 'Тунис': 0}
    sampling_d(gruppa_d, points_d)



if __name__ == "__main__":
    main()