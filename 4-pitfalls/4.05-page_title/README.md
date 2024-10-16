# 4.5. Page Title

In this exercise, your goal is to improve the accessability of page titles of:

- [https://ubax.github.io/.../before.html](https://ubax.github.io/a11y-kata/4-pitfalls/4.05-page_title/before/index.html)
- [https://localhost:8000/.../before.html](http://localhost:8000/4-pitfalls/4.05-page_title/before/index.html)
- [source code](./4.05-page_title/before/index.html)

You can refer to the [after](./after/) to compare your solutions.

## Hints

<details>
<summary>Hint 1</summary>

- Try to open all the articles in new tabs and see if you can identify the content of the page

</details>

## Problems & solutions

<details>
<summary>Problem 1</summary>

The home page and all the sub pages have the same title. This makes it hard for users to know where they are in the site. Moreover when screen reader users navigate through the page, they will hear the same title for all the pages.

</details>
<details>
<summary>Solution for problem 1</summary>

Change the titles in the sub pages to be more descriptive.

```html
<title>The Evolution of the Keyboard - Computer history</title>
```

</details>

<details>
<summary>Problem 2</summary>

On the page `The Personal Computers Revolution` the title is back-loaded. This means that the most important information is at the end of the title. This is a problem for all the users. When you have multiple tabs open, you can't see the title of the page. Moreover, screen reader users will hear the most important information at the end of the title.

</details>
<details>
<summary>Solution for problem 2</summary>

Change the title to be front-loaded.

```html
<title>The Personal Computers Revolution - Computer history</title>
```

</details>

## Resources

- [WCAG 2.4.2 Page titled](https://www.w3.org/WAI/WCAG21/Understanding/page-titled.html)
- [Page Titles](https://www.w3.org/WAI/tutorials/page-structure/headings/)
