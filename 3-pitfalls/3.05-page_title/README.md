# 3.5. Page Title

In this exercise, your goal is to improve the accessability of **page titles** for:

- [https://ubax.github.io/.../before.html](https://ubax.github.io/a11y-kata/3-pitfalls/3.05-page_title/before/index.html)
- [https://localhost:8000/.../before.html](http://localhost:8000/3-pitfalls/3.05-page_title/before/index.html)
- [source code](./before/index.html)

You can refer to the [after](./after/) to compare your solutions.

## Hints

<details>
<summary>Hint 1</summary>

Try opening all the articles in new tabs. Are you able to distinguish them by their titles?

</details>

## Problems & solutions

<details>
<summary>Problem 1</summary>

The homepage and subpages all have the same title, making it difficult for users to identify their location within the site. For screen reader users, this is especially confusing, as they hear the same title for every page. [WCAG 2.4.2: Page Titled](https://www.w3.org/WAI/WCAG21/Understanding/page-titled.html)

</details>
<details>
<summary>Solution for problem 1</summary>

Update the titles of the subpages to be more specific and descriptive.

```diff
- <title>Computer history</title>
+ <title>The Evolution of the Keyboard - Computer history</title>
```

</details>

<details>
<summary>Problem 2</summary>

On the page `The Personal Computers Revolution`, the title is back-loaded, meaning the most important information appears at the end. This makes it difficult for all users, especially when multiple tabs are open, as the critical part of the title is hidden. Moreover screen reader users will hear the important details last.

</details>
<details>
<summary>Solution for problem 2</summary>

Rearrange the title to be front-loaded.

```diff
- <title>Computer history - The Personal Computers Revolution</title>
+ <title>The Personal Computers Revolution - Computer history</title>
```

</details>

## Resources

- [WCAG 2.4.2 Page titled](https://www.w3.org/WAI/WCAG21/Understanding/page-titled.html)
- [Page Titles](https://www.w3.org/WAI/tutorials/page-structure/headings/)
