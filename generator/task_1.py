from datetime import datetime, timezone
# 1 способ

def even_numbers(num):
    for item in range(0, num, 2):
        print(item)


even_numbers(12)


# 2 способ
def even_numbers2(num):
    for item in range(0, num):
        if item % 2 != 0:
            continue
        yield item


event_number_list = even_numbers2(15)
for number in event_number_list:

    # отсебячина
    #if number == 6:
        #event_number_list.throw(Exception("это нужно убрать"))
    #if number == 8:
        #event_number_list.close()
    print(number)
print(f" {datetime.now(timezone.utc).astimezone()}")


