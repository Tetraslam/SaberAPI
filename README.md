# Welcome to the API Docs for SaberAPI!

### 1.1 What is SaberAPI?

SaberAPI is a small API I (Tetraslam) developed as a small project to learn. It allows you to access information about the 7 different forms of lightsaber fighting through simple web browser requests.

### 1.2 How does it work?

SaberAPI uses flask to create an interface for sending requests to the (very small) database of information about the 7 lightsaber forms. It allows you to view only one form's details by sending the form number after the request: `http://127.0.0.1:5000/form3` will show you information on the third form. This is the result:

![](https://i.imgur.com/nQdZwKi.png)

### ### 1.3 How do I use it?

When you run `api.py`, the command line will give an IP on which the API is running. go to that link in your web browser, and you should see the same result as below (will differ once I make different versions):

![](https://i.imgur.com/LKjZg6B.png)

To see each form's details, you can use the IP, with `/form(numberhere)` , for example, `http://127.0.0.1:5000/form5`. Additionally, if you don't fancy typing in the URL each time, I've helpfully added hyperlinks to each form's location, although it may differ depending on default port and IPs.




