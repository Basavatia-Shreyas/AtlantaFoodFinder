from django.shortcuts import render

# Create your views here.
<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
          // input custom colors here
          }
        }
      }
    }
  </script>
</head>
<body class="">
<nav class="flex justify-between items-center p-6 bg-gray-100">
  <h1 class="text-5xl font-serif text-green-800" style="font-family: 'Playfair Display', serif; font-weight: 700;">
    Atlanta Food Finder
  </h1>
  <ul class="flex space-x-6">
    <li><a href="#" class="text-lg font-semibold text-gray-700 hover:text-green-700">My Profile</a></li>
    <li><a href="#" class="text-lg font-semibold text-gray-700 hover:text-green-700">Favorites</a></li>
    <li>
      <a href="#" class="text-lg font-semibold text-gray-700 hover:text-green-700 shadow-lg hover:shadow-xl transition-shadow duration-300 border-b-2 border-black pb-1">Sign In</a>
    </li>
    <li>
      <a href="#" class="text-lg font-semibold text-gray-700 hover:text-green-700 shadow-lg hover:shadow-xl transition-shadow duration-300 border-b-2 border-black pb-1">Register</a>
    </li>
  </ul>
</nav>
<form class="px-6 py-3 max-w-sm">
    <label for="default-search" class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white">Search</label>
    <div class="relative">
        <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
            <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
            </svg>
        </div>
        <input type="search" id="default-search" class="block w-full p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-green-500 focus:border-green-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-green-500 dark:focus:border-green-500" placeholder="Search Restaurant, Location..." required />
        <button type="submit" class="text-white absolute end-2.5 bottom-2.5 bg-green-700 hover:bg-green-800 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800">Search</button>
    </div>
</form>




<div class="grid grid-cols-3 gap-10"> <!-- Adjusted gap for spacing -->
  <!-- This is an example component -->
  <div class='flex items-center bg-white'>
    <div class='w-full max-w-sm mx-auto bg-white rounded-3xl shadow-xl overflow-hidden'>
      <div class='max-w-sm mx-auto'>
        <div class='h-[236px]' style='background-image:url(https://img.freepik.com/free-photo/pasta-spaghetti-with-shrimps-sauce_1220-5072.jpg?w=2000&t=st=1678041911~exp=1678042511~hmac=e4aa55e70f8c231d4d23832a611004f86eeb3b6ca067b3fa0c374ac78fe7aba6);background-size:cover;background-position:center'></div>
        <div class='p-4 sm:p-6'>
          <p class='font-bold text-gray-700 text-[22px] leading-7 mb-1'> Shake Shack </p>
          <div class='flex flex-row'>
            <p class='text-[17px] font-bold text-[#0FB478]'>Address</p>
          </div>
          <p class='text-[#7C7C80] font-[15px] mt-6'>Description of restaurant</p>
          <a target='_blank' class='block mt-10 w-full px-4 py-3 font-medium tracking-wide text-center capitalize transition-colors duration-300 transform bg-[#FFC933] rounded-[14px] hover:bg-[#FFC933DD] focus:outline-none focus:ring focus:ring-teal-300 focus:ring-opacity-80'>
              Do Something
          </a>
          <a target='_blank' class='block mt-1.5 w-full px-4 py-3 font-medium tracking-wide text-center capitalize transition-colors duration-300 transform rounded-[14px] hover:bg-[#F2ECE7] hover:text-[#000000dd] focus:outline-none focus:ring focus:ring-teal-300 focus:ring-opacity-80'>
              Visit Website
          </a>
        </div>
      </div>
    </div>
  </div>

  <!-- Repeat the card structure for more restaurants -->
  <div class='flex items-center bg-white'>
    <div class='w-full max-w-sm mx-auto bg-white rounded-3xl shadow-xl overflow-hidden'>
      <div class='max-w-sm mx-auto'>
        <div class='h-[236px]' style='background-image:url(https://img.freepik.com/free-photo/pasta-spaghetti-with-shrimps-sauce_1220-5072.jpg?w=2000&t=st=1678041911~exp=1678042511~hmac=e4aa55e70f8c231d4d23832a611004f86eeb3b6ca067b3fa0c374ac78fe7aba6);background-size:cover;background-position:center'></div>
        <div class='p-4 sm:p-6'>
          <p class='font-bold text-gray-700 text-[22px] leading-7 mb-1'> Shake Shack </p>
          <div class='flex flex-row'>
            <p class='text-[17px] font-bold text-[#0FB478]'>Address</p>
          </div>
          <p class='text-[#7C7C80] font-[15px] mt-6'>Description of restaurant</p>
          <a target='_blank' class='block mt-10 w-full px-4 py-3 font-medium tracking-wide text-center capitalize transition-colors duration-300 transform bg-[#FFC933] rounded-[14px] hover:bg-[#FFC933DD] focus:outline-none focus:ring focus:ring-teal-300 focus:ring-opacity-80'>
              Do Something
          </a>
          <a target='_blank' class='block mt-1.5 w-full px-4 py-3 font-medium tracking-wide text-center capitalize transition-colors duration-300 transform rounded-[14px] hover:bg-[#F2ECE7] hover:text-[#000000dd] focus:outline-none focus:ring focus:ring-teal-300 focus:ring-opacity-80'>
              Visit Website
          </a>
        </div>
      </div>
    </div>
  </div>

  <!-- Add additional restaurant cards here -->

      <div class='flex items-center bg-white'>
    <div class='w-full max-w-sm mx-auto bg-white rounded-3xl shadow-xl overflow-hidden'>
      <div class='max-w-sm mx-auto'>
        <div class='h-[236px]' style='background-image:url(https://img.freepik.com/free-photo/pasta-spaghetti-with-shrimps-sauce_1220-5072.jpg?w=2000&t=st=1678041911~exp=1678042511~hmac=e4aa55e70f8c231d4d23832a611004f86eeb3b6ca067b3fa0c374ac78fe7aba6);background-size:cover;background-position:center'></div>
        <div class='p-4 sm:p-6'>
          <p class='font-bold text-gray-700 text-[22px] leading-7 mb-1'> Shake Shack </p>
          <div class='flex flex-row'>
            <p class='text-[17px] font-bold text-[#0FB478]'>Address</p>
          </div>
          <p class='text-[#7C7C80] font-[15px] mt-6'>Description of restaurant</p>
          <a target='_blank' class='block mt-10 w-full px-4 py-3 font-medium tracking-wide text-center capitalize transition-colors duration-300 transform bg-[#FFC933] rounded-[14px] hover:bg-[#FFC933DD] focus:outline-none focus:ring focus:ring-teal-300 focus:ring-opacity-80'>
              Do Something
          </a>
          <a target='_blank' class='block mt-1.5 w-full px-4 py-3 font-medium tracking-wide text-center capitalize transition-colors duration-300 transform rounded-[14px] hover:bg-[#F2ECE7] hover:text-[#000000dd] focus:outline-none focus:ring focus:ring-teal-300 focus:ring-opacity-80'>
              Visit Website
          </a>
        </div>
      </div>
    </div>
  </div>


      <div class='flex items-center bg-white'>
    <div class='w-full max-w-sm mx-auto bg-white rounded-3xl shadow-xl overflow-hidden'>
      <div class='max-w-sm mx-auto'>
        <div class='h-[236px]' style='background-image:url(https://img.freepik.com/free-photo/pasta-spaghetti-with-shrimps-sauce_1220-5072.jpg?w=2000&t=st=1678041911~exp=1678042511~hmac=e4aa55e70f8c231d4d23832a611004f86eeb3b6ca067b3fa0c374ac78fe7aba6);background-size:cover;background-position:center'></div>
        <div class='p-4 sm:p-6'>
          <p class='font-bold text-gray-700 text-[22px] leading-7 mb-1'> Shake Shack </p>
          <div class='flex flex-row'>
            <p class='text-[17px] font-bold text-[#0FB478]'>Address</p>
          </div>
          <p class='text-[#7C7C80] font-[15px] mt-6'>Description of restaurant</p>
          <a target='_blank' class='block mt-10 w-full px-4 py-3 font-medium tracking-wide text-center capitalize transition-colors duration-300 transform bg-[#FFC933] rounded-[14px] hover:bg-[#FFC933DD] focus:outline-none focus:ring focus:ring-teal-300 focus:ring-opacity-80'>
              Do Something
          </a>
          <a target='_blank' class='block mt-1.5 w-full px-4 py-3 font-medium tracking-wide text-center capitalize transition-colors duration-300 transform rounded-[14px] hover:bg-[#F2ECE7] hover:text-[#000000dd] focus:outline-none focus:ring focus:ring-teal-300 focus:ring-opacity-80'>
              Visit Website
          </a>
        </div>
      </div>
    </div>
  </div>




      <div class='flex items-center bg-white'>
    <div class='w-full max-w-sm mx-auto bg-white rounded-3xl shadow-xl overflow-hidden'>
      <div class='max-w-sm mx-auto'>
        <div class='h-[236px]' style='background-image:url(https://img.freepik.com/free-photo/pasta-spaghetti-with-shrimps-sauce_1220-5072.jpg?w=2000&t=st=1678041911~exp=1678042511~hmac=e4aa55e70f8c231d4d23832a611004f86eeb3b6ca067b3fa0c374ac78fe7aba6);background-size:cover;background-position:center'></div>
        <div class='p-4 sm:p-6'>
          <p class='font-bold text-gray-700 text-[22px] leading-7 mb-1'> Shake Shack </p>
          <div class='flex flex-row'>
            <p class='text-[17px] font-bold text-[#0FB478]'>Address</p>
          </div>
          <p class='text-[#7C7C80] font-[15px] mt-6'>Description of restaurant</p>
          <a target='_blank' class='block mt-10 w-full px-4 py-3 font-medium tracking-wide text-center capitalize transition-colors duration-300 transform bg-[#FFC933] rounded-[14px] hover:bg-[#FFC933DD] focus:outline-none focus:ring focus:ring-teal-300 focus:ring-opacity-80'>
              Do Something
          </a>
          <a target='_blank' class='block mt-1.5 w-full px-4 py-3 font-medium tracking-wide text-center capitalize transition-colors duration-300 transform rounded-[14px] hover:bg-[#F2ECE7] hover:text-[#000000dd] focus:outline-none focus:ring focus:ring-teal-300 focus:ring-opacity-80'>
              Visit Website
          </a>
        </div>
      </div>
    </div>
  </div>



      <div class='flex items-center bg-white'>
    <div class='w-full max-w-sm mx-auto bg-white rounded-3xl shadow-xl overflow-hidden'>
      <div class='max-w-sm mx-auto'>
        <div class='h-[236px]' style='background-image:url(https://img.freepik.com/free-photo/pasta-spaghetti-with-shrimps-sauce_1220-5072.jpg?w=2000&t=st=1678041911~exp=1678042511~hmac=e4aa55e70f8c231d4d23832a611004f86eeb3b6ca067b3fa0c374ac78fe7aba6);background-size:cover;background-position:center'></div>
        <div class='p-4 sm:p-6'>
          <p class='font-bold text-gray-700 text-[22px] leading-7 mb-1'> Shake Shack </p>
          <div class='flex flex-row'>
            <p class='text-[17px] font-bold text-[#0FB478]'>Address</p>
          </div>
          <p class='text-[#7C7C80] font-[15px] mt-6'>Description of restaurant</p>
          <a target='_blank' class='block mt-10 w-full px-4 py-3 font-medium tracking-wide text-center capitalize transition-colors duration-300 transform bg-[#FFC933] rounded-[14px] hover:bg-[#FFC933DD] focus:outline-none focus:ring focus:ring-teal-300 focus:ring-opacity-80'>
              Do Something
          </a>
          <a target='_blank' class='block mt-1.5 w-full px-4 py-3 font-medium tracking-wide text-center capitalize transition-colors duration-300 transform rounded-[14px] hover:bg-[#F2ECE7] hover:text-[#000000dd] focus:outline-none focus:ring focus:ring-teal-300 focus:ring-opacity-80'>
              Visit Website
          </a>
        </div>
      </div>
    </div>
  </div>



      <div class='flex items-center bg-white'>
    <div class='w-full max-w-sm mx-auto bg-white rounded-3xl shadow-xl overflow-hidden'>
      <div class='max-w-sm mx-auto'>
        <div class='h-[236px]' style='background-image:url(https://img.freepik.com/free-photo/pasta-spaghetti-with-shrimps-sauce_1220-5072.jpg?w=2000&t=st=1678041911~exp=1678042511~hmac=e4aa55e70f8c231d4d23832a611004f86eeb3b6ca067b3fa0c374ac78fe7aba6);background-size:cover;background-position:center'></div>
        <div class='p-4 sm:p-6'>
          <p class='font-bold text-gray-700 text-[22px] leading-7 mb-1'> Shake Shack </p>
          <div class='flex flex-row'>
            <p class='text-[17px] font-bold text-[#0FB478]'>Address</p>
          </div>
          <p class='text-[#7C7C80] font-[15px] mt-6'>Description of restaurant</p>
          <a target='_blank' class='block mt-10 w-full px-4 py-3 font-medium tracking-wide text-center capitalize transition-colors duration-300 transform bg-[#FFC933] rounded-[14px] hover:bg-[#FFC933DD] focus:outline-none focus:ring focus:ring-teal-300 focus:ring-opacity-80'>
              Do Something
          </a>
          <a target='_blank' class='block mt-1.5 w-full px-4 py-3 font-medium tracking-wide text-center capitalize transition-colors duration-300 transform rounded-[14px] hover:bg-[#F2ECE7] hover:text-[#000000dd] focus:outline-none focus:ring focus:ring-teal-300 focus:ring-opacity-80'>
              Visit Website
          </a>
        </div>
      </div>
    </div>
  </div>


      <div class='flex items-center bg-white'>
    <div class='w-full max-w-sm mx-auto bg-white rounded-3xl shadow-xl overflow-hidden'>
      <div class='max-w-sm mx-auto'>
        <div class='h-[236px]' style='background-image:url(https://img.freepik.com/free-photo/pasta-spaghetti-with-shrimps-sauce_1220-5072.jpg?w=2000&t=st=1678041911~exp=1678042511~hmac=e4aa55e70f8c231d4d23832a611004f86eeb3b6ca067b3fa0c374ac78fe7aba6);background-size:cover;background-position:center'></div>
        <div class='p-4 sm:p-6'>
          <p class='font-bold text-gray-700 text-[22px] leading-7 mb-1'> Shake Shack </p>
          <div class='flex flex-row'>
            <p class='text-[17px] font-bold text-[#0FB478]'>Address</p>
          </div>
          <p class='text-[#7C7C80] font-[15px] mt-6'>Description of restaurant</p>
          <a target='_blank' class='block mt-10 w-full px-4 py-3 font-medium tracking-wide text-center capitalize transition-colors duration-300 transform bg-[#FFC933] rounded-[14px] hover:bg-[#FFC933DD] focus:outline-none focus:ring focus:ring-teal-300 focus:ring-opacity-80'>
              Do Something
          </a>
          <a target='_blank' class='block mt-1.5 w-full px-4 py-3 font-medium tracking-wide text-center capitalize transition-colors duration-300 transform rounded-[14px] hover:bg-[#F2ECE7] hover:text-[#000000dd] focus:outline-none focus:ring focus:ring-teal-300 focus:ring-opacity-80'>
              Visit Website
          </a>
        </div>
      </div>
    </div>
  </div>

      <div class='flex items-center bg-white'>
    <div class='w-full max-w-sm mx-auto bg-white rounded-3xl shadow-xl overflow-hidden'>
      <div class='max-w-sm mx-auto'>
        <div class='h-[236px]' style='background-image:url(https://img.freepik.com/free-photo/pasta-spaghetti-with-shrimps-sauce_1220-5072.jpg?w=2000&t=st=1678041911~exp=1678042511~hmac=e4aa55e70f8c231d4d23832a611004f86eeb3b6ca067b3fa0c374ac78fe7aba6);background-size:cover;background-position:center'></div>
        <div class='p-4 sm:p-6'>
          <p class='font-bold text-gray-700 text-[22px] leading-7 mb-1'> Shake Shack </p>
          <div class='flex flex-row'>
            <p class='text-[17px] font-bold text-[#0FB478]'>Address</p>
          </div>
          <p class='text-[#7C7C80] font-[15px] mt-6'>Description of restaurant</p>
          <a target='_blank' class='block mt-10 w-full px-4 py-3 font-medium tracking-wide text-center capitalize transition-colors duration-300 transform bg-[#FFC933] rounded-[14px] hover:bg-[#FFC933DD] focus:outline-none focus:ring focus:ring-teal-300 focus:ring-opacity-80'>
              Do Something
          </a>
          <a target='_blank' class='block mt-1.5 w-full px-4 py-3 font-medium tracking-wide text-center capitalize transition-colors duration-300 transform rounded-[14px] hover:bg-[#F2ECE7] hover:text-[#000000dd] focus:outline-none focus:ring focus:ring-teal-300 focus:ring-opacity-80'>
              Visit Website
          </a>
        </div>
      </div>
    </div>
  </div>


</div>

<div class="flex-grow bg-gray-200 h-screen flex items-center justify-center">
    <div class="w-full max-w-4xl h-96 bg-gray-300 flex items-center justify-center">
      <span class="text-2xl font-semibold text-gray-500">Image Placeholder</span>
    </div>
  </div>
</body>
</html>