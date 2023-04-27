# mp5-django-blog

A walkthrough project for a blog, built using Django. GitHub features are used to document Agile methodologies.

## Design thinking

- Empathise
- Questions
- Examine

## Expected features

- Content is King - full access to blog posts
- Frictionless sign ups
- Engagement with content in a meaningful way

## Problem statement

"How do I develop a blog application that provides all this functionality to a user?"

We use this statement to populate our user stories.

## New view checklist

1. Create view code
2. Create template to render the view
3. Connect up URLs

## The Post detail view

Import `View` and `get_object_or_404` from `views` and `shortcuts` respectively.

This does not inherit from Django's generic views. As it is class based, if
statements are not used to check the method of the `request` object. We instead
simply create class methods, using HTTP vers.

When providing the url path with angled bracket syntax `<>`, the `slug` param
matches that of the `get` method we have made in the `PostDetail` view. The
first slug of `'<slug:slug'>/'` is a path converter. The second is the keyword
name. The path converter tells Django to convert the value to the given type, in
this instance, that of `slug`.

When we want to link to these views, for example using an anchor href, we give
the name in the template tag that we used in `urls.py`. We can also pass in an
argument, for which we will provide the slug:

```py
<a href="{% url 'post_detail' post.slug %}" class="post-link">
  <h2 class="card-title">{{ post.title }}</h2>
  <p class="card-text">{{ post.excerpt }}</p>
</a>
```

Sources:

- <https://youtu.be/9bFzeSlxPbs>
- <https://docs.djangoproject.com/en/3.2/topics/http/urls/#how-django-processes-a-request>
