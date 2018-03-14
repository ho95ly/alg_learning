
def recursive_activity_selector(event_time_list):
    event_seq = list()
    event_seq.append(event_time_list[0])
    event_num = len(event_time_list)
    i = 1
    while i < event_num:
        if event_time_list[i][0] >= event_seq[-1][1]:
            event_seq.append(event_time_list[i])
        i = i+1
    print('done.')
    return event_seq


if __name__ == '__main__':
    s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    tt = list()
    tt = [(x, y) for x, y in zip(s, f)]
    ls = recursive_activity_selector(tt)
    print(ls)






