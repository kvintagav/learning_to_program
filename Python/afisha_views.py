	
all_events=["first","sec","third","fourt"]


events_column=[]
for index in range(len(all_events)):
	event = []
	event.append(index%2)
	event.append(all_events[index])
	events_column.append(event)

print (events_column)
