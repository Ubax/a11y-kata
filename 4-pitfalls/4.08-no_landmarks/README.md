# 4.8. No landmarks

In this exercise, your goal is to improve the html structure of the page _before.html_.

- [https://ubax.github.io/.../before.html](https://ubax.github.io/a11y-kata/4-pitfalls/4.08-no_landmarks/before.html)
- [https://localhost:8000/.../before.html](http://localhost:8000/4-pitfalls/4.08-no_landmarks/before.html)
- [source code](./before.html)

You can refer to the [after.html](after.html) file to compare your solutions.

Support tools:

- Screen reader
- WAVE extension

## Hints

<details>
<summary>Hint 1</summary>

Using screen reader or WAVE extension, try to list all landmarks on the page.

</details>

<details>
<summary>Hint 2</summary>

List of landmarks:

- [`header`](https://www.w3.org/WAI/ARIA/apg/patterns/landmarks/examples/banner.html)
  - [`nav`](https://www.w3.org/WAI/ARIA/apg/patterns/landmarks/examples/navigation.html)
  - [`search`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/search)
- `main` - for the main content of the page
  - `aside` - for complementary content
  - `section` - for each section of content
- `footer` - for the footer of the page

  - `nav` - for the footer navigation

  TODO: links are missing to w3.

</details>

<details>
<summary>Hint 3</summary>

Using screen reader try to navigate between sections and navigation elements. Can you understand the purpose of each?

</details>

## Problems & Solutions

<details>
<summary>Problem 1</summary>

No HTML landmark elements are used. TODO:

</details>
<details>
<summary>Solution for problem 1</summary>

Use HTML landmarks to define the structure of the page.

- [`header`](https://www.w3.org/WAI/ARIA/apg/patterns/landmarks/examples/banner.html) - for the header of the page (logo, navigation, search)
  - [`nav`](https://www.w3.org/WAI/ARIA/apg/patterns/landmarks/examples/navigation.html) - for the navigation (top menu)
  - [`search`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/search) - for the search[^1]
- `main` - for the main content of the page (Our Pizzas, Our locations, Fun facts)
  - `aside` - for complementary content (Fun facts)
  - `section` - for each section of content (Our Pizzas, Our locations)
- `footer` - for the footer of the page (links, copyright)

  - `nav` - for the footer navigation

  TODO: links are missing to w3.

[^1]: The search tag is an element added in year 2023. It is supported in [all modern browsers](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/search#browser_compatibility). For older browsers, you can use a `role="search"` attribute on a form element.

</details>

<details>
<summary>Problem 2</summary>

HTML landmarks are missing labels

</details>
<details>
<summary>Solution for problem 2</summary>

When you use HTML landmarks, it is a good practice to provide a label for each landmark. This will help screen readers to announce the purpose of the landmark. However not all landmarks need a label.

- `nav` - There are two navigation elements on the page.
  - The top navigation can be labeled as `<nav aria-label="Primary">`. Note that there is no word navigation in the label. The screen reader will announce it as navigation.
  - The bottom navigation can be labeled as `<nav aria-label="Footer">`
- `section` and `aside` - There are multiple sections in the page. Each section can be labeled with a heading element.
  - `<section aria-labelledby="our-pizzas">`
  - `<section aria-labelledby="our-locations">`
  - `<aside aria-label="Fun facts">`

</details>

## Resources

- https://www.w3.org/WAI/ARIA/apg/patterns/landmarks/examples/general-principles.html
- [WCAG 2.0: 1.3.1 Info and Relationships](https://www.w3.org/WAI/WCAG21/quickref/?versions=2.0#info-and-relationships)
- https://developer.mozilla.org/en-US/blog/aria-accessibility-html-landmark-roles/
- https://developer.mozilla.org/en-US/docs/Web/HTML/Element/search
