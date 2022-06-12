## Why is my Project Different from the Others?
The main purpose of my project is to inform users about the local businesses and which one would be the best option for them to go for. Simultaneously, local businesses can use this as a platform to promote their products and service. It cannot be considered social media as users don't directly talk to each other and anyway, the aim of the application is to provide information and reviews about businesses like a directory, and not for communication between people. It cannot be considered e-commerce since no bookings are done and nothing is sold. It is also not an encyclopedia since it is user-interactive. Moreover, I have utilized Javascript but still my application is not single-page.

---

## Why is my Project More Complex from the Others?
My application includes features like 'search by location' which was tricky to make, and also contains infinite-scrolling using Django's Paginator class, on most pages where items are listed, which was another complex thing to make. Another difficult thing for me to do was, since my application is not single-page, combining JavaScript and Django was hard while keeping in mind quality. I also included feature to upload images/files which was a new thing I had to learn about. All the business listings in my website are ordered by the average of all the review ratings in the business, with the highest on the top, which is something I have never done before.

---

## What is contained in each file of my project?
The static folders include two types of files, one of them is a CSS stylesheet, whereas the rest of them are Javascript files for the HTML code running on the front-end. The views.py contains all the Python Views/Functions. The urls.py file contains all thr urls for the front-end and back-end of my application. The templates folder contains the HTML files of my application. The models.py file contains my Django models User, Business, Review & Category. These are the main files of my projects.

---

## How do you run my application?

cd capstone

python3 manage.py makemigrations

python3 manage.py migrate 

After making migrations, you simply have to run the command 'python3 manage.py runserver' and the application should work. There are no extra packages required to be installed.
