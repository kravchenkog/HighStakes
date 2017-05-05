import os
import pandas




def get_points_collection():
    all_points = {}
    all_points["column"] = []
    all_points["dozer"] = []
    all_points["even_odd"] = []
    all_points["four"] = []
    all_points["low_high"] = []
    all_points["number"] = []
    all_points["pair"] = []
    all_points["six"] = []
    all_points["three"] = []
    all_points["blackred"] = []
    all_points["column"].append(get_cells_from_file("points_column.csv"))
    all_points["dozer"] = get_cells_from_file("points_dozer.csv")
    all_points["even_odd"] = get_cells_from_file("points_even_odd.csv")
    all_points["four"] = get_cells_from_file("points_four.csv")
    all_points["low_high"] = get_cells_from_file("points_low_high.csv")
    all_points["number"] = get_cells_from_file("points_number.csv")
    all_points["pair"] = get_cells_from_file("points_pair.csv")
    all_points["six"] = get_cells_from_file("points_six.csv")
    all_points["three"] = get_cells_from_file("points_three.csv")
    all_points["blackred"] = get_cells_from_file("points_black_red.csv")
    all_points["red"] = get_cells_from_file("points_red.csv")
    return all_points

def get_cells_from_file(filename):
    directory = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(directory, filename)
    list_of_xy = []
    with open(file) as f:
        content = pandas.read_csv(file, header=None)

        for i in range(content.shape[0]):
            list_of_xy.append(list(content.iloc[i, :]))

    return list_of_xy

points_collection = get_points_collection()