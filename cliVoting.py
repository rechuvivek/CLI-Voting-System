def main():
    parties = {
        1: "Party 1",
        2: "Party 2",
        3: "Party 3",
        4: "Party 4",
        5: "NOTA"
    }

    votes = {}

    for partyId,partyName in parties.items():
        votes[partyId] = {
            "total": 0,
            "valid": 0,
            "invalid": 0
        }
    
    print(votes)
    
    completedVoters = set()

    print("::VOTING SYSTEM::\n")

    while True:
        voterId = input("Enter your Unique Identification Number:\n").strip()
        voterAge = int(input("Enter your age:\n").strip())

        print("Parties for Election:\n")
        for partyId,partyName in parties.items():
            print(partyId,". ",partyName,"\n")
        
        vote = int(input("Enter the ID for the party you want to vote:").strip())

        if vote not in parties:
            print("Invalid party entered Please choose from the below:",list(parties.keys()))
            continue
        
        valid = True
        
        if voterId in completedVoters:
            valid = False
        elif voterAge<18:
            valid = False
        votes[vote]['total'] +=1
        if valid:
            votes[vote]['valid']+=1
            completedVoters.add(voterId)
            print(f"Vote casted successfully for {voterId} against {parties[vote]}")
        else:
            votes[vote]['invalid']+=1
            if voterId not in completedVoters:
                completedVoters.add(voterId)
                print(f"Vote was unsucessfull for {voterId} against {parties[vote]}")
            else:
                print(f"Vote was unsucessfull for {voterId} against {parties[vote]} due to Duplicate Voter")
        
        toContinue = input("Are there more voters:").strip().upper()
        if(toContinue != 'Y'):
            break

    print("::ELECTION RESULTS::\n")

    totalValidVotes = sum(v['valid'] for v in votes.values())
    results =[]

    for partyId in parties:
        if totalValidVotes>0:
            votePercent = (votes[partyId]["valid"]/totalValidVotes)*100
        else:
            votePercent = 0.0
        results.append({
            'id':partyId,
            'name':parties[partyId],
            'total':votes[partyId]['total'],
            'valid':votes[partyId]["valid"],
            'invalid':votes[partyId]["invalid"],
            'votePercent':votePercent
        })
    
    results.sort(key=lambda x: x['valid'], reverse=True)

    for i,result in enumerate(results):
        if i<len(results)-1:
            lead = result['valid']-results[i+1]['valid']
        else:
            lead = 0
        result['lead']=lead
    
    print(f"Total number of valid Votes casted are {totalValidVotes}")

    for result in results:
        print(f"{result['name']}")
        print(f"Total Votes:{result['total']}")
        print(f"Total Valid Votes:{result['valid']}")
        print(f"Total Invalid Votes:{result['invalid']}")
        print(f"Vote % :{result['votePercent']}")
        print(f"Lead:{result['lead']}")

    if results:
        winner = results[0]
        print(f"Winner: {winner['name']} with {winner['valid']} valid votes ({winner['votePercent']:.2f}%)")


if __name__ == "__main__":
    main()