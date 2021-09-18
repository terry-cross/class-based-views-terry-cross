# class-based-views

In Django, we've been purely focused on working with function-based views -- frankly, because they're easy and they get the job done. But sometimes we need to eke just a little more functionality out a view... especially if we need to be able to take in different methods (GET, POST, etc.). We can do that inside of a function, but what if there was a way to make it cleaner and easier to understand?

Welcome to Django's class-based views. Building on Python's amazingly powerful inheritance system, a class-based view allows us to have standalone views, make classes of helper functions that can be easily used in multiple views (called [mixins](https://docs.djangoproject.com/en/3.1/topics/class-based-views/mixins/)), and separate out exactly how our views should work depending on how they're requested.

Start here: [https://docs.djangoproject.com/en/3.1/topics/class-based-views/intro/](https://docs.djangoproject.com/en/3.1/topics/class-based-views/intro/) 

Additional reading:
*  [https://docs.djangoproject.com/en/3.1/topics/class-based-views/generic-display/  
](https://docs.djangoproject.com/en/3.1/topics/class-based-views/generic-display/)
*  [https://docs.djangoproject.com/en/3.1/topics/class-based-views/generic-editing/  
](https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-editing/)
*  [https://www.codementor.io/jamesezechukwu/working-with-class-based-views-in-django-5zkjnrvwc](https://www.codementor.io/jamesezechukwu/working-with-class-based-views-in-django-5zkjnrvwc)

#### **Your Task**

 Identify 4 view functions (ideally including at least one form view) and convert them from function-based views to class-based views. Work in a new branch and submit a link to a PR back to your primary branch.

#### **Submission**

<span>Work in a dev branch and submit a link to a PR back to your main branch.</span>

<span>For example:</span>

```https://github.com/kenzie-se-q4/class-based-views-<github_username>/pull/2```