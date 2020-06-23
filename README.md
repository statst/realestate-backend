# Realalistic Estate-Backend

## Project Description

 RealisticEstates is an application designed for users to find home. Users can search homes on the website, check the description of the property and schedule an appointment with an agent.

Link to deployed app: [Realistic Estate](http://realisticesates.com.s3-website-us-east-1.amazonaws.com/)

# Request-Response Cycle and routes

![](Images/Snip20200623_1.png)

## User Stories

- _As a user, I would be able to search a house using an input search bar._
- _As a user, I want to see listings of all properties based on search criteria._
- _As a user, I want to be able to navigate the individual home and see descriptions of particular houses._
- _As a user, I want to be able to contact agents of the property._
- _As a user, I want to be able to contact agents of the property._

_**Post Stretch Goal**_

- _As a user, I would like to see neighbourhood details on google map when i choose a particular house._


## Estate listings JSON Data
```yaml
{
count: 6,
next: "http://ec2-18-222-61-213.us-east-2.compute.amazonaws.com/api/listestates/?format=json&page=2",
previous: null,
results: [
{
title: "Home",
address: "9 NE Bronx",
city: "Bronx",
state: "New York",
price: 778899,
sale_type: "For Sale",
home_type: "House",
bedrooms: 4,
bathrooms: "3.5",
sqft: 3050,
photo_main: "http://ec2-18-222-61-213.us-east-2.compute.amazonaws.com/media/photos/2020/06/14/new-home-1540871_1920.jpg",
slug: "Home-1"
},
{
title: "Home",
address: "99 E Brooklyn St",
city: "New York",
state: "New York",
price: 666999,
sale_type: "For Sale",
home_type: "House",
bedrooms: 3,
bathrooms: "2.5",
sqft: 3024,
photo_main: "http://ec2-18-222-61-213.us-east-2.compute.amazonaws.com/media/photos/2020/06/14/jacques-bopp-Hh18POSx5qk-unsplash.jpg",
slug: "Home-3"
},
{
title: "Home",
address: "12 W Bronx",
city: "New York",
state: "New York",
price: 998999,
sale_type: "For Sale",
home_type: "House",
bedrooms: 4,
bathrooms: "4.0",
sqft: 4000,
photo_main: "http://ec2-18-222-61-213.us-east-2.compute.amazonaws.com/media/photos/2020/06/14/stephen-leonardi-Al9Cl-b7EFU-unsplash.jpg",
slug: "Home-4"
},
{
title: "Home",
address: "12 SW Broat St",
city: "NEWARK",
state: "Delaware",
price: 546546,
sale_type: "For Sale",
home_type: "House",
bedrooms: 6,
bathrooms: "6.0",
sqft: 4550,
photo_main: "http://ec2-18-222-61-213.us-east-2.compute.amazonaws.com/media/photos/2020/06/11/fran-hogan-BDRzsymkZho-unsplash.jpg",
slug: "Home-2"
}
]
}
```
### Doctors
![Doctors](project-planning/Doctors.png)

### Reviews
![Reviews](project-planning/Reviews.png)

## ZooDoc Req-Res Cycle
![Req-Res Cycle](project-planning/Djangobackend.png)


## Technologies and Frameworks Used

- Python, Django RestFramework, Simple JWT DjangoRestFramework, PostgreSQL

## Installation

```
Install the Realestate Backend:
1. Fork & clone the repository
2. cd into cloned directory
3. Activate virtual environment using pipenv shell command
4. Install dependencies such as Django, Django-Rest-Framework and JWT-Authentication using pipenv install
5. Run python3 manage.py runserver, it will start a local version of the backend on port 8000.
3. Submit any issues

```

## Contribute
Repo Links:
[Frontend Repo](https://github.com/statst/realestate-frontend) | 
[Backend Repo](https://github.com/statst/realestate-backend)