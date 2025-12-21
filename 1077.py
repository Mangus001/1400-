directions_code = {1:'северный', 2:'южный', 3:'восточный', 4:'западный',
                   5:'северо-западный', 6:'северо-восточный', 7:'юго-западный', 8:'юго-восточный'}
winds_june = [int(input()) for _ in range(30)]
winds_june.extend([int(input()) for _ in range(30)])
winds = winds_june[:30] + winds_june[30:]
