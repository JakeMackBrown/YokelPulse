from decouple import config

# Print environment variable values
print("GOOGLE_MAPS_API_KEY:", config('GOOGLE_MAPS_API_KEY'))
print("SECRET_KEY:", config('SECRET_KEY'))
