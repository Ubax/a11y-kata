# 4.2. Headings

In this exercise, your task is to enhance the accessibility of the headers on the webpage http://jakubtkacz.pl/a11y/4-2-headings/before.html. You can also open the local version of the page [before.html](./before.html) for reference.

Additionally, you can refer to the [after.html](after.html) file to compare your solutions.

<details>
<summary>Problem 1</summary>

The article does not use proper heading tags. Instead, it applies styling to `<div>` elements with the classes `.h2` and `.h3`. As a result, users of screen readers will have difficulty navigating the content.

</details>
<details>
<summary>Solution for problem 1</summary>

Replace the `<div>` elements with the classes `.h2` and `.h3` with the appropriate heading tags. Change `.h2` to `<h2>` and `.h3` to `<h3>`.

</details>

<details>
<summary>Problem 2</summary>

The heading levels are not used in a consistent order. The `h3` tag should not be used for the section title (**_"Buy Your Next Keyboard"_**). Moreover the product titles are assigned `h5` tags, skipping several heading levels.

</details>
<details>
<summary>Solution for problem 2</summary>

Change the `h3` tag for **_"Buy Your Next Keyboard"_** to an `h2` tag, and change the `h5` tags to `h3` tags.

</details>

## Resources

- [W3 tutorial on accessible headings](https://www.w3.org/WAI/tutorials/page-structure/headings/)
- [Success Criterion 1.3.1: Info and Relationships](https://www.w3.org/WAI/WCAG21/quickref/#info-and-relationships)
- [Success Criterion 2.4.6: Headings and Labels](https://www.w3.org/WAI/WCAG21/Understanding/headings-and-labels.html)
- [Success Criterion 2.4.10: Section Headings (AAA)](https://www.w3.org/WAI/WCAG21/Understanding/section-headings.html)
- [h tag definition](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements)
