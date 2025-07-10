import time
from multiprocessing import Pool

def calculate_intersection(A, B):
    x1, y1, x2, y2 = A
    x3, y3, x4, y4 = B

    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denominator == 0:
        return None

    t_numerator = (x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)
    u_numerator = (x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2)
    t = t_numerator / denominator
    u = u_numerator / denominator

    if 0 <= t <= 1 and 0 <= u <= 1:
        x = x1 + t * (x2 - x1)
        y = y1 + t * (y2 - y1)
        if (x != x1 and x != x2 and x != x3 and x != x4 and
                y != y1 and y != y2 and y != y3 and y != y4):
            return [x, y]
    return None


def process_segment_chunk(args):
    start_i, end_i, result_arr = args
    intersections = []
    count_of_no_calcs = 0
    for i in range(start_i, end_i):
        added = False
        for j in range(i + 1, len(result_arr)):
            seg1 = result_arr[i]
            seg2 = result_arr[j]
            if seg1[0] != seg2[0] and seg1[1] != seg2[1] and seg1[2] != seg2[2] and seg1[3] != seg2[3] and seg1[3] != seg2[2] and seg1[2] != seg2[0]:
                temp = calculate_intersection(seg1, seg2)
                if temp is not None:
                    intersections.append([
                        temp,
                        [seg1[0], seg1[1]],
                        [seg1[2], seg1[3]],
                        [seg2[0], seg2[1]],
                        [seg2[2], seg2[3]]
                    ])
                    added = False
                elif added is False:
                    intersections.append([
                        temp,
                        [seg1[0], seg1[1]],
                        [seg1[2], seg1[3]]
                    ])
                    added = True
            else:
                count_of_no_calcs += 1
    return [end_i,intersections]

def remove_duplicate_intersections(intersections):
    eq_counter = 0
    l_begin = len(intersections)
    index = 0
    while index < l_begin:
        comp_index = index+1
        while comp_index<l_begin:
            if intersections[comp_index][0] is None and intersections[index][0] is None:
                if (intersections[comp_index][1][0] == intersections[index][1][0] and \
                        intersections[comp_index][1][1] == intersections[index][1][1] and \
                        intersections[comp_index][2][0] == intersections[index][2][0] and \
                        intersections[comp_index][2][1] == intersections[index][2][1]):

                    del intersections[comp_index]
                    l_begin-=1
                    eq_counter += 1
                elif intersections[comp_index][0] != None and intersections[index][0] != None:
                    if (intersections[comp_index][0][0] == intersections[index][0][0] and
                            intersections[comp_index][0][1] == intersections[index][0][1]):
                        del intersections[comp_index]
                        l_begin -= 1
            comp_index+=1
    index+=1
    return intersections

def process_intersections(raw_data, num_processes=10, chunk_size=100):
    result_arr = []
    for pseudos in raw_data:
        coord_list_length = len(pseudos)
        for coord_list_index in range(1, coord_list_length - 1):
            reverse_index = coord_list_length - coord_list_index
            if pseudos[reverse_index][2] == 0 and pseudos[reverse_index - 1][2] == 0:
                x1 = pseudos[reverse_index - 1][0]
                y1 = pseudos[reverse_index - 1][1]
                x2 = pseudos[reverse_index][0]
                y2 = pseudos[reverse_index][1]
                result_arr.append([x1, y1, x2, y2])


    tasks = []
    total_segments = len(result_arr)
    for start in range(0, total_segments, chunk_size):
        end = min(start + chunk_size, total_segments)
        tasks.append((start, end, result_arr))
    count = 0
    with Pool(num_processes) as pool:
        count+=1
        results = pool.map(process_segment_chunk, tasks)
    intersections = []
    for res in results:
        intersections.extend(res[1])

    return intersections
    