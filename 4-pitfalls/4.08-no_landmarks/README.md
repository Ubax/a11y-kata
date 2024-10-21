# 4.8. No landmarks

In this exercise, your goal is to improve the **html structure** of the page _before.html_.

- [https://ubax.github.io/.../before.html](https://ubax.github.io/a11y-kata/4-pitfalls/4.08-no_landmarks/before.html)
- [https://localhost:8000/.../before.html](http://localhost:8000/4-pitfalls/4.08-no_landmarks/before.html)
- [source code](./before.html)

You can refer to the [after.html](after.html) file to compare your solutions.

If you prefer not to solve the problems yourself, you can use the solution files to explore how each issue was fixed and look for any remaining problems:

- [Solution after problem 1](https://ubax.github.io/a11y-kata/4-pitfalls/4.08-no_landmarks/after-problem-1.html)

## Hints

<details>
<summary>Hint 1</summary>

Using screen reader or WAVE extension, try to list all landmarks on the page.

- macOS Voice Over: <kbd>VO + Command + U</kbd> to open the rotor, then navigate with the <kbd>arrow keys</kbd> to find landmarks.
- Wave: `WAVE` -> `Structure`

</details>

<details>
<summary>Hint 2</summary>

List of landmarks:

- header - [aria docs](https://www.w3.org/WAI/ARIA/apg/patterns/landmarks/examples/banner.html), [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/header)
- nav - [aria docs](https://www.w3.org/WAI/ARIA/apg/patterns/landmarks/examples/navigation.html), [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav)
- search - [aria docs](https://www.w3.org/WAI/ARIA/apg/patterns/landmarks/examples/search.html), [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/search)
- main - [aria docs](https://www.w3.org/WAI/ARIA/apg/patterns/landmarks/examples/main.html), [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/main)
- aside - [aria docs](https://www.w3.org/WAI/ARIA/apg/patterns/landmarks/examples/complementary.html), [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/aside)
- section - [aria docs](https://www.w3.org/WAI/ARIA/apg/patterns/landmarks/examples/region.html), [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/section)
- footer - [aria docs](https://www.w3.org/WAI/ARIA/apg/patterns/landmarks/examples/contentinfo.html), [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/footer)

</details>

<details>
<summary>Hint 3</summary>

Using screen reader try to navigate between sections and navigation elements. Can you understand the purpose of each?

</details>

## Problems & Solutions

<details>
<summary>Problem 1</summary>

No HTML landmark elements are used. [WCAG 1.3.1 Info and Relationships](https://www.w3.org/WAI/WCAG21/Understanding/info-and-relationships) and [WCAG 1.3.6 Identify Purpose (AAA)](https://www.w3.org/WAI/WCAG21/Understanding/identify-purpose)

</details>
<details>
<summary>Solution for problem 1</summary>

Use HTML landmarks to define the structure of the page.

- header - [aria docs](https://www.w3.org/WAI/ARIA/apg/patterns/landmarks/examples/banner.html), [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/header)
- nav - [aria docs](https://www.w3.org/WAI/ARIA/apg/patterns/landmarks/examples/navigation.html), [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav)
- search[^1] - [aria docs](https://www.w3.org/WAI/ARIA/apg/patterns/landmarks/examples/search.html), [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/search)
- main - [aria docs](https://www.w3.org/WAI/ARIA/apg/patterns/landmarks/examples/main.html), [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/main)
- aside - [aria docs](https://www.w3.org/WAI/ARIA/apg/patterns/landmarks/examples/complementary.html), [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/aside)
- section - [aria docs](https://www.w3.org/WAI/ARIA/apg/patterns/landmarks/examples/region.html), [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/section)
- footer - [aria docs](https://www.w3.org/WAI/ARIA/apg/patterns/landmarks/examples/contentinfo.html), [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/footer)

[^1]: The search tag is an element added in year 2023. It is supported in [all modern browsers](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/search#browser_compatibility). For older browsers, you can use a `role="search"` attribute on a form element.

</details>

<details>
<summary>Problem 2</summary>

HTML landmarks are missing labels

</details>
<details>
<summary>Solution for problem 2</summary>

When you use multiple HTML landmarks of the same type, it is a good practice to provide a label for each landmark. This will help screen readers to announce the purpose of the landmark. However not all landmarks need a label.

- `nav` - There are two navigation elements on the page.
  - The top navigation can be labeled as `<nav aria-label="Primary">`. Note that there is no word navigation in the label. The screen reader will announce it as navigation.
  - The bottom navigation can be labeled as `<nav aria-label="Footer">`
- `section` and `aside` - There are multiple sections in the page. Each section can be labeled with a heading element.
  - `<section aria-labelledby="our-pizzas">`
  - `<section aria-labelledby="our-locations">`
  - `<aside aria-label="Fun facts">`

</details>

## Resources

- [General guideline on landmarks - W3C](https://www.w3.org/WAI/ARIA/apg/patterns/landmarks/examples/general-principles.html)
- [WCAG 1.3.1 Info and Relationships](https://www.w3.org/WAI/WCAG21/Understanding/info-and-relationships)
- [WCAG 1.3.6 Identify Purpose (AAA)](https://www.w3.org/WAI/WCAG21/Understanding/identify-purpose)
- [Using HTML landmark roles to improve accessibility - MDN](https://developer.mozilla.org/en-US/blog/aria-accessibility-html-landmark-roles/)
