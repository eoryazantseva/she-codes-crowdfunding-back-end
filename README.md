# crowdfunding_back_end

# WishFrog - Where Birthday Dreams Hop to Reality! 🐸🎂🌟

by Evgeniia Riazantseva

She Codes crowdfunding project - DRF Backend.

## About

WishFrog is a delightful crowdfunding platform where birthday dreams come to life with a hop and a leap! With WishFrog, parents, families, and friends can come together to make a child's birthday wishes a reality. This playful platform is all about granting magical moments, where every birthday celebration becomes a joyous leap into a world of enchantment and happiness. At WishWorth, we encourage parents, family members, and friends to invest in meaningful birthday gifts that align with a child's dreams and create lasting memories. Say goodbye to plastic waste toys that end up forgotten and instead embrace gifts that hold long-lasting value and significance.

Join WishFrog today and be a part of a movement that nurtures the planet and fosters cherished celebrations. 
Together, we'll cultivate sustainable joy and make every birthday an eco-friendly journey filled with love, purpose, and dreams worth cherishing! 🌎🎈🎁

## Features

{{ The features your MVP will include. (Remember this is a working document, you can change these as you go!) }}
* User Accounts: WishFrog offers a seamless user account creation process, allowing individuals to register with unique usernames, email addresses, and securely encrypted passwords. These accounts provide access to a personalized dashboard to manage crowdfunding campaigns.
* Project Creation: SUsers can create birthday campaigns that focus on meaningful gifts aligned with a child's dreams. Each campaign will include essential attributes such as the project title, the project owner (the user who initiated the campaign), a detailed description, an inspiring image, the target amount to be fundraised, and an option to indicate if the project is currently open to accepting new supporters. The creation date of each campaign will be prominently displayed, inspiring early engagement.
* Pledging Support: family members, friends and enthusiastic supporters can make pledges to back birthday campaigns. Each pledge will encompass crucial details, including the pledged amount, the campaign it supports, the name of the supporter, an option for anonymous pledges, and a heartfelt comment accompanying the pledge.
* Update/Delete Functionality: Project owners will have the power to update their project descriptions, keeping supporters engaged with the latest developments. We'll implement suitable permissions, ensuring that only authorized users can delete a pledge, providing a secure and transparent process.
* Status Codes & Error Handling: Our API will deliver relevant status codes for both successful and unsuccessful requests, ensuring smooth interactions. Additionally, WishFrog's custom 404 page will gracefully handle any failed requests, making the user experience as delightful as possible.
* Token Authentication: Security is paramount at WishFrog. Token Authentication will safeguard user accounts and pledges, keeping everyone's data protected.
* Responsive Design: Funducation's website will be fully responsive, delivering a seamless experience across desktops, tablets, and mobile devices.

### Stretch Goals

{{ Outline three features that will be your stretch goals if you finish your MVP }}

* Social Media Integration: Implement social media integration to allow users to easily share their favorite projects and pledges with their friends, family, and followers. 
* Gift Tracking and Follow-ups: Implement a tracking system to monitor gift usage and follow up with campaign owners to see how the gifts have impacted the child's life. This feature will help showcase the positive outcomes of sustainable and meaningful gift-giving.
* Adding a video card feature to the WishWorth platform would be a fantastic way to enable users to send heartfelt congratulatory videos to the birthday child. 

## API Specification

| HTTP Method | Url | Purpose | Request Body | Successful Response Code | Authentication <br /> Authorization
| --- | ------- | ------ | ---- | -----| ----|
| GET | projects/ | Return all projects | N/A | 200 | N/A |
| POST | projects/ | Create a new project | project object | 201 | User must be logged in. |

## Database Schema
{{ Insert your database schema }}

![image info goes here](./docs/image.png)

## Wireframes
{{ Insert your wireframes }}

![image info goes here](./docs/image.png)

## Colour Scheme
{{ Insert your colour scheme }}

![image info goes here](./docs/image.png)

## Fonts
{{ outline your heading & body font(s) }}

## Submission Documentation
{{ Fill this section out for submission }}

Deployed Project: [Deployed website](http://linkhere.com/)

### How To Run
{{ What steps to take to run this code }}

### Updated Database Schema
{{ Updated schema }}

![image info goes here](./docs/image.png)

### Updated Wireframes
{{  Updated wireframes }}

![image info goes here](./docs/image.png)

### How To Register a New User
{{ Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data). }}

### Screenshots
* [] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
![image info goes here](./docs/image.png)

* [] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
![image info goes here](./docs/image.png)

* [] A screenshot of Insomnia, demonstrating a token being returned.
![image info goes here](./docs/image.png)