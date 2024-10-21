# 4.2. Headings

In this exercise, your task is to improve the accessibility of the **headings** on the page _before.html_.

- [https://ubax.github.io/.../before.html](https://ubax.github.io/a11y-kata/4-pitfalls/4.02-headings/before.html)
- [https://localhost:8000/.../before.html](http://localhost:8000/4-pitfalls/4.02-headings/before.html)
- [source code](./before.html)

You can refer to the [after.html](after.html) file to compare your solutions.

If you prefer not to solve the problems yourself, you can use the solution files to explore how each issue was fixed and look for any remaining problems:

- [Solution after problem 1](https://ubax.github.io/a11y-kata/4-pitfalls/4.02-headings/after-problem-1.html)

## Hints

<details>
<summary>Hint 1</summary>

Navigate using headings with a screen reader. Is anything missing?

- Mac: <kbd>Ctrl + Option + Cmd + H</kbd>
- Windows: <kbd>H</kbd>
- Android: <kbd>Swipe up + down</kbd> to select headings. Then <kbd>Swipe down</kbd>
- iOS: <kbd>Twist</kbd> to select headings. Then <kbd>Swipe down</kbd>

</details>

<details>
<summary>Hint 2</summary>

Is any element looking like a heading but not marked as one?

- You can use the [WAVE tool](https://wave.webaim.org/) to check the headings.
  - `WAVE` -> `Details` -> Uncheck everything except `Structural elements`

</details>

<details>
<summary>Hint 3</summary>

Are any levels of headings skipped?

</details>

## Problems & solutions

<details>
<summary>Problem 1</summary>

The article does not use proper heading tags. Instead, it applies styling to `<div>` elements with the classes `.h2` and `.h3`. As a result, users of screen readers will have difficulty navigating the content.

</details>
<details>
<summary>Solution for problem 1</summary>

Replace the `<div>` elements with the classes `.h2` and `.h3` with the appropriate heading tags. Change `.h2` to `<h2>` and `.h3` to `<h3>`.

```diff
- <div div class="h3">1. The Early Writing Machines</div>
+ <h3>1. The Early Writing Machines</h3>
```

</details>

<details>
<summary>Problem 2</summary>

Product titles are assigned `h5` tags, skipping several heading levels. _[Skipping heading ranks can be confusing and should be avoided where possible](https://www.w3.org/WAI/tutorials/page-structure/headings/#:~:text=Skipping%20heading%20ranks%20can%20be%20confusing%20and%20should%20be%20avoided%20where%20possible)_

</details>
<details>
<summary>Solution for problem 2</summary>

Change the `h5` tags used as product names to `h3` tags.

```diff
- <h5>Split Keyboard</h5>
+ <h3>Split Keyboard</h3>
```

</details>

## Resources

- [W3C tutorial on accessible headings](https://www.w3.org/WAI/tutorials/page-structure/headings/)
- [Success Criterion 1.3.1: Info and Relationships](https://www.w3.org/WAI/WCAG21/quickref/#info-and-relationships)
- [Success Criterion 2.4.6: Headings and Labels](https://www.w3.org/WAI/WCAG21/Understanding/headings-and-labels.html)
- [Success Criterion 2.4.10: Section Headings (AAA)](https://www.w3.org/WAI/WCAG21/Understanding/section-headings.html)
- [h tag definition](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements)
