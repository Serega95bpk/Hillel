shedule = {'monday': ['clean house', 'drive car', 'meet with freands'], 'thuesday': None, 'wednesday': ['manicure', 'hammam', 'beer']}

shedule_list = []
for v in shedule.values():
    shedule_list.append(v)

shedule_list = shedule_list[0] + shedule_list[2]

print(len(shedule_list))