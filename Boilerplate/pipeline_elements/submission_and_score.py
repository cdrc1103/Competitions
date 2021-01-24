def create_submission(result, score, DESCRIPTION, file_name):
    
    with open(f"submissions/{DESCRIPTION}_{file_name}_{score}.sub",'w') as file:

        # overwrite potential existing lines
        file.write("")

        # write number of signed up libraries
        print(str(len(result)), file=file)
        
        # iterated over signed up library objects
        for res in result:
            string1 = str(res.pizzas_per_team)
            string2 = ' '.join(map(str, res.pizza_ids))
            print(f"{string1} {string2}", file=file)