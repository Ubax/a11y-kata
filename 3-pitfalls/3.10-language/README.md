# 3.10. Language

The goal of this exercise is to improve the **language** accessibility of the page _before.html_.

- [https://ubax.github.io/.../before.html](https://ubax.github.io/a11y-kata/3-pitfalls/3.10-language/before.html)
- [https://localhost:8000/.../before.html](http://localhost:8000/3-pitfalls/3.10-language/before.html)
- [source code](./before.html)

You can refer to the [after.html](after.html) file to compare your solutions.

If you prefer not to solve the problems yourself, you can use the solution files to explore how each issue was fixed and look for any remaining problems:

- [Solution after problem 1](https://ubax.github.io/a11y-kata/3-pitfalls/3.10-language/after-problem-1.html)
- [Solution after all problems](https://ubax.github.io/a11y-kata/3-pitfalls/3.10-language/after.html)

## Hints

<details>
<summary>Hint 1</summary>

Read the website content with a screen reader. Does the screen reader read the paragraphs in the correct language?

Experiment with different language settings in screen reader.

</details>

<details>
<summary>Hint 2</summary>

Read the `Author's note` or `In anderen Sprache` section with a screen reader.

Experiment with different language settings in screen reader. Does the screen reader read the content in the correct language?

</details>

<details>
<summary>Hint 3</summary>

繁體中文 corresponds to the `zh-hant` language code.

</details>

## Problems & Solutions

<details>
<summary>Problem 1</summary>

Missing `lang` attribute on website. [WCAG 3.1.1 Language of Page](https://www.w3.org/WAI/WCAG21/Understanding/language-of-page.html)

</details>
<details>
<summary>Solution for problem 1</summary>

Add the `lang` attribute to the `html` element. The value should be the language of the document.

```html
<html lang="de">
  ...
</html>
```

</details>

<details>
<summary>Problem 2</summary>

Some elements with text in a different language are missing a `lang` attribute. This makes it difficult for screen readers to switch languages correctly. [WCAG 3.1.2 Language of Parts](https://www.w3.org/WAI/WCAG21/Understanding/language-of-parts.html)

</details>
<details>
<summary>Solution for problem 2</summary>

Add the `lang` attribute to the elements with content in different language.

```html
<h2 lang="en">Author's note</h2>
<p lang="en">This article was generated using Chat GPT</p>
```

</details>

## Resources

- [Lang attribute - MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/lang)
- [WCAG 3.1.1 Language of Page](https://www.w3.org/WAI/WCAG21/quickref/#language-of-page)
- [WCAG 3.1.2 Language of Parts](https://www.w3.org/WAI/WCAG21/quickref/#language-of-parts)
