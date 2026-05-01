def find_max_saiki(num_list,now,limit):
    list_len=len(num_list)
    if now>=list_len or limit<=0:
        return 0
    else:
        tmp_not_choice=find_max_saiki(num_list,now+1,limit)
        if num_list[now]>limit:
            return tmp_not_choice
        else:
            tmp_choice=find_max_saiki(num_list,now+1,limit-num_list[now])+num_list[now]
            return max(tmp_choice,tmp_not_choice)