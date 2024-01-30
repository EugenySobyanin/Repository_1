# первое решение (чтоб работало) не выполнено условие задачи
# from random import choice

# class MarsURLEncoder:

#     def __init__(self):
#         self.list_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
#         self.first_half_url = ''
#         self.second_half_url = ''
#         self.code_part = ''
        

#     def encode(self, long_url):
#         """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
#         counter = 0
#         for el in long_url:
#             if el == '/':
#                 counter += 1
#             if counter < 3:
#                 self.first_half_url += el
#             elif counter > 2:
#                 self.second_half_url += el
#         for el in range(len(self.second_half_url) // 2):
#             self.code_part += choice(self.list_char)
#         return self.first_half_url + '/'+ self.code_part
        

#     def decode(self, short_url):
#         """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
#         return self.first_half_url + self.second_half_url




# Решение 2 (неправильно понял условие с укорачиванием ссылок(все куда проще))
# from random import choice

# class MarsURLEncoder:

#     def __init__(self):
#         self.list_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
#         self.urls_dict = {}


#     def encode(self, long_url):
#         """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
#         counter = 0
#         first_half = ''
#         second_half = ''
#         code_half = ''
#         for el in long_url:
#             if el == '/':
#                 counter += 1
#             if counter < 3:
#                 first_half += el
#             elif counter > 2:
#                 second_half += el
#         for el in range(len(second_half) // 2):
#             code_half += choice(self.list_char)
#         self.urls_dict[code_half] = long_url
#         return first_half + '/' + code_half
    
    
#     def decode(self, short_url):
#         counter  = 0
#         code_half = ''
#         for el in short_url:
#             if el == '/':
#                 counter += 1
#             if counter > 2:
#                 code_half += el
#         return self.urls_dict[code_half[1:]]
 
 
   
# url_1 = MarsURLEncoder()
# encode = url_1.encode('https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html')
# print(encode)

# print(url_1.urls_dict)

# decode = url_1.decode(encode)

# print(decode)






# Решение 3 (это решение сработало)

from random import choice

class MarsURLEncoder:

    def __init__(self):
        self.list_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        self.urls_dict = {}

    def encode(self, long_url):
        code_half = ''
        for i in range(11):
            code_half += choice(self.list_char)
        self.urls_dict[code_half] = long_url
        return f'https://ma.rs/{code_half}'
    
    def decode(self, short_url):
        counter  = 0
        code_half = ''
        for el in short_url:
            if el == '/':
                counter += 1
            if counter > 2:
                code_half += el
        return self.urls_dict[code_half[1:]]
            
url_1 = MarsURLEncoder()
encode = url_1.encode('https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html')
print(encode)

print(url_1.urls_dict)

decode = url_1.decode(encode)
print(decode)