import time

# def simple_time_middleware(get_response):
#     print("Simple Time Middleware loaded once at server start!")

#     def middleware(request):
#         start_time = time.time()
#         print("⏳ Request started...")
#         print("checks your ticket and ID")
        

#         # call next middleware / view
#         response = get_response(request)
#         print("respnse....:i am come from view:...######",response) 
#         end_time = time.time()
#         duration = end_time - start_time
#         print("**scans your bag again** before letting you leave the airport (response processing).")

#         print(f"✅ Request completed in {duration:.4f} seconds")
        
#         return response

#     return middleware


# ___________________________________________________________________




# from django.http import JsonResponse

# def check_even(get_response):
#     print('check_even middleware')

#     def wrapper(request):
#         print('Start of check correct even ID')

#         number  =3

#         # First check POST
#         if "number" in request.POST:
#             number = request.POST.get("number")
#         # Then check GET (query params)
#         elif "number" in request.GET:
#             number = request.GET.get("number")

#         print(f"number: {number}")

#         if number:
#             try:
#                 if int(number) % 2 != 0:  # odd check
#                     return JsonResponse({"message": "Failed from the middleware"})
#             except ValueError:
#                 return JsonResponse({"message": "Invalid number format"})

#         response = get_response(request)
#         print(response)
#         print('End of check_even id process...!')
#         return response

#     return wrapper


# ___________________________________________________________________

from django.http import JsonResponse

   
class CheckEven:
    def __init__(self,get_response):
        print("CheckEven initialised")
        self.get_response=get_response
   
   
    def __call__(self,request):
        print("start check even")
        
        number=2
        if number:
            try:
                if int(number) % 2 != 0:  # odd check
                    return JsonResponse({"message": "Failed from the middleware"})
            except ValueError:
                return JsonResponse({"message": "Invalid number format"})

        request.POST={'data':number}

        response=self.get_response(request)

        print(f"End CheckEven")
        return response

