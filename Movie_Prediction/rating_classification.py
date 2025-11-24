def rating(rating):
    if rating>=7.5:
        return 'Excellent'
    elif rating>=6.5:
        return 'Good'
    elif rating>=4.5:
        return 'Average'
    else:
        return 'Bad'
    

df_1 = df_n['rating_category']=df_n['Rating'].apply(rating)