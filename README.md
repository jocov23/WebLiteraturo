# WebLiteraturo
  This project is a full-stack web application built with the Django Framework to catalog my personal bookshelf with a bit of other features, like the registration, listing and information specifying of books together with a user registration-login system
  
  When you clone this repository you will see that its database is filled with books, which reflects how many I have as of 01/14/2026, you can delete them all on the admin page (login details are in guide.txt) for your own use

## Features
  - **Registration and Login of Users:** It is possible to create a profile and have special perms with it (such as adding new books, synopses, opinions and adding pic to books without it)
  - **Registration of books:** Each logged user can add a book with its pic, name, author, year and publisher
  - **Listing page:** The previously added books can be seen on the initial page
  - **creation of synopses and their visualization alongside other users:** Each user can create and see synopses created by others in a details page
  - **creation of opinions ant their visualization alongside other users:** Each user can create and see opinions about selected books created by others in a details page

<div display="grid align="center">
  <img src="https://github.com/user-attachments/assets/48f8cd44-4100-4622-8c37-21d529e54808" width="400px" />
  <img src="https://github.com/user-attachments/assets/ad96a288-0077-4783-b58b-a578f010ccc0" width="400px" />
<div>
  <br>

  
## Technologies
  - **Frontend:**
      - HTML5
      - CSS3

  - **Backend/API:**
      - Django framework (Python 3.13)
      - Django RESTful API
      - Docker & Docker-compose
      - MySql:8
      
## Initialization
 ```
   WARNING: you must have docker desktop installed and opened in your device before-hand!! 
  ```
1. **Clone the repository:**
  ```
    git clone https://github.com/jocov23/WebLiteraturo.git
  ``` 
2. **Go to the project directory**
  ```
    cd WebLiteraturo
  ```
3. **Initialize the containers**
  ```
    docker-compose up --build -d
  ```
4. **Open your browser to http://localhost:8000 to view the project.**
   ```
    If any problem or doubt arise check guide.txt file!
   ```

## Contact
  - **E-mail:** jocov2309@gmail.com

  - **LinkedIn:** linkedin.com/in/joao-vitor-freitasb 

  - **Discord:** jocov23
---

Feel free to fork, star or contribute.

    
  
