# 4.1. Alternative Text

In this exercise, your task is to improve the accessibility of the images on the page _before.html_.

- [https://ubax.github.io/.../before.html](https://ubax.github.io/a11y-kata/4-pitfalls/4.01-alternative_text/before.html)
- [https://localhost:8000/.../before.html](http://localhost:8000/4-pitfalls/4.01-alternative_text/before.html)
- [Source code](./before.html)

You can refer to the [after.html](after.html) file to compare your solutions.

## Hints

<details>
<summary>Hint 1</summary>

Check the images on the website with screen reader. How are they described?

</details>

<details>
<summary>Hint 2</summary>

Use the `alt` attribute in HTML to provide alternative text for images.

- [`alt` property - MDN](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/alt)
- [Write helpful Alt Text - Harvard Accessibility](https://accessibility.huit.harvard.edu/describe-content-images)

</details>

<details>
<summary>Hint 3</summary>

Are there any [decorative images](https://www.w3.org/WAI/tutorials/images/decorative/) on the website?

Decorative images are images that do not convey any new information and do not require alternative text.

</details>

<details>
<summary>Hint 4</summary>

Did any of the descriptions seem too long?

- [Write helpful Alt Text - Harvard Accessibility](https://accessibility.huit.harvard.edu/describe-content-images)

</details>

## Problems & solutions

<details>
<summary>Problem 1</summary>

Missing alt text for important images.

</details>
<details>
<summary>Solution for problem 1</summary>

Add descriptive alt text to important images. For example:

```html
...
<img
  src="./assets/electric-typewriter.webp"
  alt="An electric typewriter with a cleaner design compared to mechanical ones"
/>
...
<img
  src="./assets/old-keyboard.webp"
  alt="A vintage computer keyboard connected to an early PC"
/>
...<b>test</b>
<img
  src="./assets/ergonomic-keyboard.webp"
  alt="A modern ergonomic split keyboard"
/>
...
```

</details>

<details>
<summary>Problem 2</summary>

The images in the `Buy Your Next Keyboard` section do not require alternative text. They can be considered as [decorative images](https://www.w3.org/WAI/tutorials/images/decorative/), because they illustrate the products mentioned in the adjacent headers.

</details>
<details>
<summary>Solution for problem 2</summary>

For decorative images, use `alt=""` so that screen readers will ignore them. For example:

```html
...
<img src="./assets/ergonomic-keyboard.webp" alt="" />
...
<img src="./assets/gaming-keyboard.webp" alt="" />
...
<img src="./assets/wireless.webp" alt="" />
...
```

</details>

<details>
<summary>Problem 3</summary>

The alternative text for the typewriter image is too long.

</details>
<details>
<summary>Solution for problem 3</summary>

Provide a more concise alternative text for the image. For instance:

```html
...
<img
  src="./assets/typewriter.webp"
  alt="An old mechanical typewriter with round keys and levers"
/>
...
```

</details>

## Resources

- [WCAG 2.1 - Success Criteria 1.1.1](https://www.w3.org/WAI/WCAG21/Understanding/non-text-content.html)
- [W3 tutorial on accessible images](https://www.w3.org/WAI/tutorials/images/)
- [Decorative images](https://www.w3.org/WAI/tutorials/images/decorative/)
- [Write helpful Alt Text - Harvard Accessibility](https://accessibility.huit.harvard.edu/describe-content-images)
- [alt property - MDN](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/alt)

## Image sources

- [Unsplash](https://unsplash.com/)
- [Electric Typewriter Image](<https://commons.wikimedia.org/wiki/File:IBM_Model_A_typewriter_(1).webp/>)
