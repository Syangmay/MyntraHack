import pandas as pd


def jackets(attr, count):
    dfjackets = pd.read_csv('data/mjackets.csv')

    del dfjackets['Waist Rise']
    del dfjackets['Fit']
    del dfjackets['Brand Fit Name']
    del dfjackets['Type of Pleat']
    del dfjackets['Weave Type']
    del dfjackets['Fly Type']
    del dfjackets['Distress']
    del dfjackets['Hemline']
    del dfjackets['Occasion']
    del dfjackets['Features']


    dfjackets['Print or Pattern Type']=dfjackets['Print or Pattern Type'].fillna(value='Solid')
    dfjackets['Closure']=dfjackets['Closure'].fillna(value='Zip')
    dfjackets['Number of Pockets']=dfjackets['Number of Pockets'].fillna(value='0')


    #attr=['Quilted Jacket', 'Bomber', 'Puffer', 'Padded Jacket', 'Leather Jacket', 'Long Sleeves', 'Sporty Jacket']
    #count=[2, 3.0, 2, 2, 3.0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0]
    dfjackets.insert(13,'Score', 1)

    for ind in dfjackets.index:
        if dfjackets['Type'][ind] in attr:
                a=attr.index(dfjackets['Type'][ind])
                dfjackets['Score'][ind]+=count[a]

        if dfjackets['Sleeve Length'][ind] in attr:
                a=attr.index(dfjackets['Sleeve Length'][ind])
                dfjackets['Score'][ind]+=count[a]

        if dfjackets['Print or Pattern Type'][ind] in attr:
                a=attr.index(dfjackets['Print or Pattern Type'][ind])
                dfjackets['Score'][ind]+=count[a]

        if dfjackets['Closure'][ind] in attr:
                a=attr.index(dfjackets['Closure'][ind])
                dfjackets['Score'][ind]+=count[a]

        if dfjackets['Lining Fabric'][ind] in attr:
                a=attr.index(dfjackets['Lining Fabric'][ind])
                dfjackets['Score'][ind]+=count[a]

        if dfjackets['Number of Pockets'][ind] in attr:
                a=attr.index(dfjackets['Number of Pockets'][ind])
                dfjackets['Score'][ind]+=count[a]



    td=dfjackets['Score'].mean()
    #for final in dfjackets.index:
    #    if dfjackets['Score'][final] >= int(td):
#            print(dfjackets['title'][final],dfjackets['name'][final],dfjackets['price'][final])
#    print(td)
    dfjackets = dfjackets.sort_values(['Score'], ascending=[False])

    return dfjackets['title'].tolist()[:60], dfjackets['productId'].tolist()[:60], dfjackets['name'].tolist()[:60], dfjackets['price'].tolist()[:60]

    #dfjackets['Print or Pattern Type'].value_counts()


#att=['Zip','Button','Solid','Colourblocked','Self Design','Bomber','Sporty Jacket','Padded Jacket','Denim Jacket','Tailored Jacket','Puffer Jacket','Quilted Jacket','Biker Jacket','Leather Jacket',
     'Polyester','Unlined','Cotton','Fleece','Nylon','Polycotton','Sleeveless ','Long Sleeves']
