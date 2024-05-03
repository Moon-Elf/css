def keyless(str2,col_size):
    str1= str2.replace(" ","")
    cipher_text = ""
    arr = []
    i = 0
    while(i<len(str1)):
        print(str1[i:i+col_size])
        arr.append([x for x in str1[i:i+col_size]])
        i += col_size
    print(arr)
    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
          if(i >= len(arr[j])):
           cipher_text
          else:
           cipher_text+= arr[j][i]
    return cipher_text


print(keyless("meet me at the park",4))