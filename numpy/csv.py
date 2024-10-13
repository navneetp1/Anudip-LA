import numpy as np

try: 
    data = np.genfromtxt(r'C:\Python Programs\numpy\house_prices.csv', dtype=[('Index','i4'),('Price','f8')], delimiter=",", encoding=None)

    print("Total no of records found: ", len(data))
    print("Displaying only 6 records for observational purposes..\n")
    # iterating over some records (6 in this case)
    count = 0
    for record in data:
        count+=1
        index, value = record
        if index == -1:
            continue
        print(f"Index: {index}, Price: {value}")
        if(count > 6):
            break

    prices = []
    indexes = []
    counter = 0
    for record in data:
        counter += 1
        price = record["Price"]
        index = record["Index"]
        if not np.isnan(price):
            prices.append(price)
            indexes.append(index)

    prices_array = np.array(prices)

    avg = np.mean(prices_array).astype("float32")
    print("\nAverage Price:", avg)
    # print(prices)


    high_prices = []
    for i in range(len(prices_array)):
        if prices_array[i] > avg:
            high_prices.append((indexes[i], prices_array[i]))

    np.savetxt('high_prices.csv',high_prices,delimiter=",",fmt="%s",header="INDEX | PRICE")


    print_counter = 0
    print("\nHigh priced Houses: ")
    print("Displaying only 6 records for observational purposes..\n")

    print("Index  |  Price")
    for index,price in high_prices:
        print_counter += 1
        print("  ",index,"\t",price)
        if print_counter > 6:
            break
    
    

except Exception as e:
    print("Some error occured: ", e)
finally:
    print("All operations completed successfully.")
    print("New CSV file creation was a success.")







        