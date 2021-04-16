# Portfolio Website for BEW1.2
## This project will probably not receive updates

This is a simple project that i used to learn Django

(5 Points) How is this project structure different than a Flask (or Node) application? What role are the urls.py and views.py files responsible for?

In Flask i think normally the url is defined right before the view it will return. But in django the define it in two separate files views in views and then urls in urls.

(5 Points) Why do we use 2 separate urls.py files? How do they interact?

If a url is app specific then the application should handle where the view is. That way if you wanted to take your messageboard application and install it in a new project you wouldn't need to worry about rerouting everything. Just include messageboard's urls.

(5 Points) When is it desirable to split our code over multiple apps? Why would we want to do so?

It makes it more modular. Easier to incorporate a previously made app into a new project. I would assume it is also easier to debug.
