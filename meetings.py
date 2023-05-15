filename = input("Enter the meeting file: ")

infected = []

with open(filename, "r") as f:
    for line in f:
        meeting = line.split()
        names = meeting[1:]

        if len(infected) == 0:
            for i in range(len(names)):
                if names[i][-1] == "*":
                    infected.append(names[i][:-1])

                    if i == len(names) - 1:
                        infected.append(names[i-1])
                        if len(names) > 2:
                            infected.append(names[0])
                    else:
                        infected.append(names[i-1])
                        infected.append(names[i+1])

                    break
        else:
            for i in range(len(names)):
                if names[i] in infected:
                    if i == len(names) - 1:
                        if names[i-1] not in infected:
                            infected.append(names[i-1])
                        if len(names) > 2 and names[0] not in infected:
                            infected.append(names[0])
                    else:
                        if names[i-1] not in infected:
                            infected.append(names[i-1])
                        if names[i+1] not in infected:
                            infected.append(names[i+1])

                    break

        if len(infected) > 0:
            output = str(meeting[0]) + "\t" + " ".join(sorted(infected, reverse=True))
            output += " " + str(len(infected))
            print(output)

f.close()
