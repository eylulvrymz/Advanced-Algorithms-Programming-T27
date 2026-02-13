def merge_intervals(interval_list):
    #check for an empty list
    if len(interval_list) == 0:
        return interval_list, False
    interval_list.sort()
    #to count the number of comparisns performed
    comp_count = 0
    #we start with the smallest interval after sorting to compare
    merged_interval= [interval_list[0]]
    #we continue from index 1 of the list to start comparing
    for i in range (1,len(interval_list)):
        current = interval_list[i]
        #the last viewed is the most recent merged interval
        last_viewed = merged_interval[-1]
        comp_count+=1
        #if the first element of the current interval overlaps with the last element of the last merged interval merge them together
        if current[0]<= last_viewed[1]:
            if current [1] > last_viewed[1]:
                last_viewed[1] = current[1]
        else:
            #no overlap detected so add the current interval to our merged_interval list for the next comparison
            merged_interval.append(current)
    return merged_interval, comp_count
#testing
test_data=[[1,3],[2,6],[15,18],[8,10]]
final_merged, total_comparison = merge_intervals(test_data)
print("Merged Intervals:")
print(final_merged)
print("Total Comparisons:")
print(total_comparison)
        
    
